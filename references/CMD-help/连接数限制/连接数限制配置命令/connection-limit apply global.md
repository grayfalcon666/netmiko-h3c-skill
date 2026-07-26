::: {#-316157085 .myid}
[]{#_Toc404793564}[]{#struct_0_37551_x7964_178678713}

**连接数限制 \-- 连接数限制配置命令 \-- connection-limit apply global**

------------------------------------------------------------------------

[**[connection-limit apply global]{lang="EN-US"}**]{#struct_0_37551_x7964_x171322146}[命令用来在全局应用连接数限制策略。]{style="font-family:
宋体"}

[**[undo connection-limit apply global]{lang="EN-US"}**]{#struct_0_37551_x7964_x685905064}[命令用来在全局取消应用的连接数限制策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x635597741}

[**[connection-limit apply global ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** } *policy-id*]{lang="EN-US"}]{#struct_0_37551_x7964_562005158}

[**[undo connection-limit apply global ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_37551_x7964_x1240426626}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1979615237}

[[全局没有应用任何连接数限制策略。]{style="font-family:宋体"}]{#struct_0_37551_x7964_x1161288430}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37551_x7964_624950178}

[[系统视图]{style="font-family:宋体"}]{#struct_0_37551_x7964_937335327}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1334261812}

[[network-admin]{lang="EN-US"}]{#struct_0_37551_x7964_x1419658048}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37551_x7964_x1330483189}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1651689578}

[**[ipv6-policy]{lang="EN-US"}**]{#struct_0_37551_x7964_x655469306}[：指定]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制策略。]{style="font-family:宋体;
color:black"}

[**[policy]{lang="EN-US"}**]{#struct_0_37551_x7964_1064313541}[：指定]{style="font-family:宋体;color:black"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制策略。]{style="font-family:宋体;
color:black"}

[*[policy-id]{lang="SV" style="color:black"}*]{#struct_0_37551_x7964_1841213884}[：]{style="font-family:宋体;
color:black"}[连接数限制策略编号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_37551_x7964_212193141}

[[全局最多只能应用一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_37551_x7964_623967138}[连接数限制策略和一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[连接数限制策略，后配置的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[连接数限制策略会覆盖已配置的对应类型的策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_37551_x7964_2123334093}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_1981371479}[在全局应用编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[连接数限制策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_37551_x7964_746908719}

[\[Sysname\] connection-limit apply global policy 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_70740618}[在全局应用编号为]{style="font-family:宋体"}[12]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[连接数限制策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_37551_x7964_80981993}

[\[Sysname\] connection-limit apply global ipv6-policy 12]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1112526779}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit]{lang="EN-US"}**]{#struct_0_37551_x7964_x872435710}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[limit]{lang="EN-US"}**]{#struct_0_37551_x7964_624032674}
:::

::: {#1120411418 .myid}
[]{#_Toc404793565}[]{#struct_0_37551_x7964_x593345277}[]{#_Toc364692741}

**连接数限制 \-- 连接数限制配置命令 \-- connection-limit amount**

------------------------------------------------------------------------

[**[connection-limit amount]{lang="EN-US"}**]{#struct_0_37551_x7964_x1202486355}[命令用来配置最大用户连接数。]{style="font-family:宋体"}

[**[undo connection-limit amount]{lang="EN-US"}**]{#struct_0_37551_x7964_2092868981}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x274422188}

[**[connection-limit amount]{lang="EN-US"}**[ *amount*]{lang="EN-US"}]{#struct_0_37551_x7964_x485364803}

[**[undo connection-limit amount]{lang="EN-US"}**]{#struct_0_37551_x7964_x451471627}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1878621680}

[[不限制最大用户连接数。]{style="font-family:宋体"}]{#struct_0_37551_x7964_x593279741}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1165620213}

[[user-profile]{lang="EN-US"}]{#struct_0_37551_x7964_1881374797}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1406973446}

[[network-admin]{lang="EN-US"}]{#struct_0_37551_x7964_668783080}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37551_x7964_405625588}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1301296831}

[*[amount]{lang="EN-US"}*]{#struct_0_37551_x7964_x1086021797}[：]{style="font-family:宋体;color:black"}[最大用户连接数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[。]{style="font-family:宋体;color:black"}[一个用户的连接数值超过此值时，将不能建立新的连接。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1498153851}

[[最大用户连接数可以多次配置，最后一次生效，修改后的配置立即生效。]{style="font-family:宋体"}]{#struct_0_37551_x7964_2073033410}

[[设备上的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_37551_x7964_x593869566}[被删除后，被下发该配置的用户也将不受此]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x776991437}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x1876324791}[创建名称为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[user-profile]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_37551_x7964_809694910}

[\[Sysname\] user-profile abc]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x937141782}[配置最大用户连接数为]{style="font-family:宋体"}[5]{lang="EN-US"}[，即]{style="font-family:宋体"}[一个用户的连接]{style="font-family:宋体"}[数超过]{style="font-family:宋体"}[5]{lang="EN-US"}[时，将不能建]{style="font-family:宋体"}[立新的连接]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\[Sysname-user-profile-abc\] connection-limit amount 5]{lang="EN-US"}]{#struct_0_37551_x7964_422931821}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1952498581}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display user-profile]{lang="EN-US"}**]{#struct_0_37551_x7964_x1598174867}[（安全命令参考]{style="font-family:宋体"}[/User Profile]{lang="EN-US"}[）]{style="font-family:宋体"}
:::

::::: {#-397803717 .myid}
[]{#_Toc404793566}[]{#struct_0_37551_x7964_746547728}[]{#_Toc312690465}[]{#_Toc312690466}[]{#_Toc312690467}[]{#_Toc312690468}[]{#_Toc312690469}[]{#_Toc312690470}[]{#_Toc312690471}[]{#_Toc312690472}[]{#_Toc312690473}[]{#_Toc312690474}[]{#_Toc312690475}[]{#_Toc312690476}[]{#_Toc312690477}[]{#_Toc312690478}[]{#_Toc312690479}[]{#_Toc312690480}[]{#_Toc312690481}[]{#_Toc312690482}[]{#_Toc312690483}[]{#_Toc312690487}[]{#_Toc312690488}[]{#_Toc312690489}

**连接数限制 \-- 连接数限制配置命令 \-- connection-limit apply**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](连接数限制命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_37551_x7964_x318143511}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_37551_x7964_x501582774}
:::

[ ]{lang="EN-US"}

[**[connection-limit apply]{lang="EN-US"}**]{#struct_0_37551_x7964_1949657495}[命令用来在接口上应用连接数限制策略。]{style="font-family:宋体"}

[**[undo connection-limit apply]{lang="EN-US"}**]{#struct_0_37551_x7964_x168035180}[命令用来在接口上取消应用的连接数限制策略。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1399625889}

[**[connection-limit apply ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** } *policy-id*]{lang="EN-US"}]{#struct_0_37551_x7964_832935434}

[**[undo connection-limit apply ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_37551_x7964_1021541218}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1235638311}

[[接口上没有应用任何连接数限制策略。]{style="font-family:宋体"}]{#struct_0_37551_x7964_1168597109}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37551_x7964_624491427}

[[接口视图]{style="font-family:宋体"}]{#struct_0_37551_x7964_868766861}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1674505215}

[[network-admin]{lang="EN-US"}]{#struct_0_37551_x7964_x767061453}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37551_x7964_1501795575}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1672571528}

[**[ipv6-policy]{lang="EN-US"}**]{#struct_0_37551_x7964_x1393377334}[：指定]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制策略。]{style="font-family:宋体;
color:black"}

[**[policy]{lang="EN-US"}**]{#struct_0_37551_x7964_x574819863}[：指定]{style="font-family:宋体;color:black"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制策略。]{style="font-family:宋体;
color:black"}

[*[policy-id]{lang="SV" style="color:black"}*]{#struct_0_37551_x7964_x373954163}[：]{style="font-family:宋体;
color:black"}[连接数限制策略编号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_37551_x7964_599840074}

[[同一个接口上同时只能应用一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_37551_x7964_624556963}[连接数限制策略和一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[连接数限制策略，后配置的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[连接数限制策略会覆盖已配置的对应类型的策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x3588356}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_37551_x7964_x724579127}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_181148333}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上应用编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[连接数限制策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_37551_x7964_505390801}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] connection-limit apply policy 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_1598732255}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[应用编号为]{style="font-family:宋体"}[12]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[连接数限制策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_37551_x7964_x1623560432}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] connection-limit apply ipv6-policy 12]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_37551_x7964_x2033869424}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x1384784960}[在接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上应用编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[连接数限制策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_37551_x7964_624622499}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] connection-limit apply policy 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x1964616788}[在接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上应用编号为]{style="font-family:宋体"}[12]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[连接数限制策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_37551_x7964_1961019107}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] connection-limit apply ipv6-policy 12]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x286383217}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit]{lang="EN-US"}**]{#struct_0_37551_x7964_305844207}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[limit]{lang="EN-US"}**]{#struct_0_37551_x7964_420688862}
:::::

::: {#-818296337 .myid}
[]{#_Toc404793567}[]{#struct_0_37551_x7964_1597944405}[]{#_Toc312690491}[]{#_Toc312690492}[]{#_Toc312690493}[]{#_Toc312690494}[]{#_Toc312690495}[]{#_Toc312690496}[]{#_Toc312690497}[]{#_Toc312690498}[]{#_Toc312690499}[]{#_Toc312690500}[]{#_Toc312690501}[]{#_Toc312690502}[]{#_Toc312690503}[]{#_Toc312690504}[]{#_Toc312690505}[]{#_Toc312690506}[]{#_Toc312690507}[]{#_Toc312690508}[]{#_Toc312690509}[]{#_Toc312690510}[]{#_Toc312690511}[]{#_Toc312690512}[]{#_Toc312690513}[]{#_Toc312690514}[]{#_Toc312690515}[]{#_Toc312690516}

**连接数限制 \-- 连接数限制配置命令 \-- connection-limit**

------------------------------------------------------------------------

[**[connection-limit]{lang="EN-US"}**]{#struct_0_37551_x7964_1679763953}[命令用来创建连接数限制策略，并进入连接数限制策略视图。]{style="font-family:宋体"}

[**[undo connection-limit]{lang="EN-US"}**]{#struct_0_37551_x7964_x693851845}[命令用来删除连接数限制策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_624688035}

[**[connection-limit ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** } *policy-id*]{lang="EN-US"}]{#struct_0_37551_x7964_x2043926698}

[**[undo connection-limit ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** } *policy-id*]{lang="EN-US"}]{#struct_0_37551_x7964_531706650}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_37551_x7964_53992791}

[[不存在任何连接数限制策略。]{style="font-family:宋体"}]{#struct_0_37551_x7964_x338678021}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1879213995}

[[系统视图]{style="font-family:宋体"}]{#struct_0_37551_x7964_223193563}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x21053369}

[[network-admin]{lang="EN-US"}]{#struct_0_37551_x7964_x124619594}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37551_x7964_1385372436}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37551_x7964_624753571}

[**[ipv6-policy]{lang="EN-US"}**]{#struct_0_37551_x7964_1550436282}[：指定]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制策略。]{style="font-family:宋体;
color:black"}

[**[policy]{lang="EN-US"}**]{#struct_0_37551_x7964_120678642}[：指定]{style="font-family:宋体;color:black"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制策略。]{style="font-family:宋体;
color:black"}

[*[policy-id]{lang="SV" style="color:black"}*]{#struct_0_37551_x7964_2022182081}[：]{style="font-family:宋体;
color:black"}[连接数限制策略编号（]{style="font-family:宋体;color:black"}[IPv4]{lang="SV" style="color:black"}[、]{style="font-family:宋体;color:black"}[IPv6]{lang="SV" style="color:black"}[连接数限制策略的编号空间各自独立），取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_37551_x7964_585437244}

[[\#]{lang="EN-US"}]{#struct_0_37551_x7964_819079934}[创建编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[连接数限制策略，并进入]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[连接数限制策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_37551_x7964_1951553724}

[\[Sysname\] connection-limit policy 1]{lang="EN-US"}

[\[Sysname-connlmt-policy-1\] ]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_37551_x7964_x1058945381}[创建编号为]{style="font-family:宋体"}[12]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[连接数限制策略，并进入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[连接数限制策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_37551_x7964_624819107}

[\[Sysname\] connection-limit ipv6-policy 12]{lang="EN-US"}

[\[Sysname-connlmt-ipv6-policy-12\] ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1435788660}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit apply]{lang="EN-US"}**]{#struct_0_37551_x7964_x1574783526}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit apply global]{lang="EN-US"}**]{#struct_0_37551_x7964_x2072568730}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display connection-limit]{lang="EN-US"}**]{#struct_0_37551_x7964_1893606011}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[limit]{lang="EN-US"}**]{#struct_0_37551_x7964_1727742368}
:::

::: {#-1685990313 .myid}
[]{#_Toc404793568}[]{#struct_0_37551_x7964_x593738494}[]{#_Toc364692744}

**连接数限制 \-- 连接数限制配置命令 \-- connection-limit rate**

------------------------------------------------------------------------

[**[connection-limit rate]{lang="EN-US"}**]{#struct_0_37551_x7964_x593672958}[命令用来配置最大用户新建连接速率。]{style="font-family:宋体"}

[**[undo connection-limit rate]{lang="EN-US"}**]{#struct_0_37551_x7964_x1155449547}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_2090381366}

[**[connection-limit rate]{lang="EN-US"}***[ rate]{lang="EN-US"}*]{#struct_0_37551_x7964_x1771972884}

[**[undo connection-limit rate]{lang="EN-US"}**]{#struct_0_37551_x7964_85841171}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x232798642}

[[不限制最大用户新建连接速率。]{style="font-family:宋体"}]{#struct_0_37551_x7964_555648906}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1891154733}

[[user-profile]{lang="EN-US"}]{#struct_0_37551_x7964_x593345278}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1203207251}

[[network-admin]{lang="EN-US"}]{#struct_0_37551_x7964_1131886671}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37551_x7964_x511956254}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1700021198}

[*[rate]{lang="EN-US"}*]{#struct_0_37551_x7964_1041776009}[：]{style="font-family:宋体;color:black"}[最大新建连接速率，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为每秒连接数]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}[一个用户的新建连接速率超过此值时，将不能建立新的连接。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_37551_x7964_466061267}

[[最大用户连接速率可以多次配置，最后一次生效，修改后的配置立即生效。]{style="font-family:宋体"}]{#struct_0_37551_x7964_x593279742}

[[设备上的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_37551_x7964_x1165685749}[被删除后，被下发该配置的用户也将不受此]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1718533614}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x2143735775}[创建名称为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[user-profile]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_37551_x7964_x1839525004}

[\[Sysname\] user-profile abc]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_529260566}[配置最大用户新建连接速率为]{style="font-family:宋体"}[100]{lang="EN-US"}[，即]{style="font-family:宋体"}[一个用户]{style="font-family:宋体"}[的每秒新建连接数超过]{style="font-family:宋体"}[100]{lang="EN-US"}[个时，将不能建]{style="font-family:宋体"}[立新的连接]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\[Sysname-user-profile-abc\] connection-limit rate 100]{lang="EN-US"}]{#struct_0_37551_x7964_x1645959614}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1890474059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display user-profile]{lang="EN-US"}**]{#struct_0_37551_x7964_x593869567}[（安全命令参考]{style="font-family:宋体"}[/User Profile]{lang="EN-US"}[）]{style="font-family:宋体"}
:::

::::: {#1614675773 .myid}
[]{#_Toc404793569}[]{#struct_0_37551_x7964_x1444733778}[]{#_Toc312690518}[]{#_Toc312690519}[]{#_Toc312690520}[]{#_Toc312690521}[]{#_Toc312690522}[]{#_Toc312690523}[]{#_Toc312690524}[]{#_Toc312690525}[]{#_Toc312690526}[]{#_Toc312690527}[]{#_Toc312690528}[]{#_Toc312690529}[]{#_Toc312690530}[]{#_Toc312690531}[]{#_Toc312690532}[]{#_Toc312690533}[]{#_Toc312690534}[]{#_Toc312690535}[]{#_Toc312690536}

**连接数限制 \-- 连接数限制配置命令 \-- display connection-limit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](连接数限制命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_37551_x7964_1416574449}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本]{style="font-family:KaiTi_GB2312"}]{#struct_0_37551_x7964_73520874}[命令的支持情况与设备的型号有关]{style="font-family:KaiTi_GB2312"}[，]{style="font-family:
KaiTi_GB2312"}[请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="SV"}

[**[display connection-limit]{lang="SV"}**]{#struct_0_37551_x7964_1655956561}[命令用来显示连接数限制策略的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_624884643}

[**[display connection-limit ]{lang="SV"}**]{#struct_0_37551_x7964_178678714}[{ **ipv6-policy** \| **policy** } { *policy-id* \| **all** }]{lang="SV"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x171322147}

[[任意视图]{style="font-family:宋体"}]{#struct_0_37551_x7964_x685839528}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x594406094}

[[network-admin]{lang="EN-US"}]{#struct_0_37551_x7964_220598115}

[[network-operator]{lang="EN-US"}]{#struct_0_37551_x7964_1001163446}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37551_x7964_1026862900}

[[mdc-operator]{lang="EN-US"}]{#struct_0_37551_x7964_1934695438}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37551_x7964_624950179}

[**[ipv6-policy]{lang="EN-US"}**]{#struct_0_37551_x7964_937335326}[：显示]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制策略。]{style="font-family:宋体;
color:black"}

[**[policy]{lang="EN-US"}**]{#struct_0_37551_x7964_x1334261813}[：显示]{style="font-family:宋体;color:black"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制策略。]{style="font-family:宋体;
color:black"}

[*[policy-id]{lang="EN-US" style="color:black"}*]{#struct_0_37551_x7964_1309225307}[：连接数限制策略编号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:
宋体;color:black"}*[ ]{style="color:blue"}*

[**[all]{lang="EN-US" style="color:black"}**]{#struct_0_37551_x7964_86010675}[：显示所有]{style="font-family:宋体;color:black"}[指定类型的连接数限制[策略。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_37551_x7964_611873479}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_1171437820}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[连接数限制策略的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit policy all]{lang="EN-US"}]{#struct_0_37551_x7964_623967139}

[3 policies in total:]{lang="EN-US"}

[ Policy  Rule     Stat Type  HiThres  LoThres  ACL]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[      0     1  Src-Dst-Port     2000     1800  3000]{lang="EN-US"}

[           12       Src-Dst      500       45  3001]{lang="EN-US"}

[          255            \--  1000000   980000  2001]{lang="EN-US"}

[ ]{lang="EN-US"}

[      1     2      Dst-Port      800      70   3010]{lang="EN-US"}

[            3       Src-Dst      100      90   3000 ]{lang="EN-US"}

[           10  Src-Dst-Port       50      45   3003]{lang="EN-US"}

[           11           Src      200     200   3004]{lang="EN-US"}

[          200           \--    500000  498000   2002]{lang="EN-US"}

[ ]{lang="EN-US"}

[     28     4          Port     1500    1400   3100]{lang="EN-US"}

[            5           Dst     3000     280   3101]{lang="EN-US"}

[           21       Src-Dst      200     180   3102]{lang="EN-US"}

[           25      Src-Port       50      35   3200]{lang="EN-US"}

[[#  ]{lang="EN-US"}]{#struct_0_37551_x7964_2123334094}[显示编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[连接数策略的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit policy 1]{lang="EN-US"}]{#struct_0_37551_x7964_624032675}

[IPv4 connection limit policy 1 has been applied 5 times, and has 5 limit rules.]{lang="EN-US"}

[Limit rule list:]{lang="EN-US"}

[ Policy  Rule     Stat Type  HiThres  LoThres  ACL]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[      1     2      Dst-Port      800      700  3010]{lang="EN-US"}

[            3       Src-Dst      100       90  3000]{lang="EN-US"}

[           10  Src-Dst-Port       50       45  3003]{lang="EN-US"}

[           11           Src      200      200  3004]{lang="EN-US"}

[          200            \--   500000   498000  2002]{lang="EN-US"}

[ Application list:]{lang="EN-US"}

[     GigabitEthernet1/0/1]{lang="EN-US"}

[     GigabitEthernet1/0/2]{lang="EN-US"}

[     Vlan-interface1]{lang="EN-US"}

[     Tunnel0]{lang="EN-US"}

[     Global]{lang="EN-US"}

[[#  ]{lang="EN-US"}]{#struct_0_37551_x7964_746547727}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[连接数限制策略的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-policy all]{lang="EN-US"}]{#struct_0_37551_x7964_1949657496}

[2 policies in total:]{lang="EN-US"}

[ Policy  Rule     Stat Type  HiThres  LoThres  ACL]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[      3     1       Src-Dst     1000      800  3010]{lang="EN-US"}

[            2           Dst      500      450  3001]{lang="EN-US"}

[      4     2  Src-Dst-Port      800      700  3010]{lang="EN-US"}

[            3           Src      100       90  3020]{lang="EN-US"}

[          200            \--   100000    89000  2005]{lang="EN-US"}

[[#  ]{lang="EN-US"}]{#struct_0_37551_x7964_x167838572}[显示编号为]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[连接数限制策略的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-policy 3]{lang="EN-US"}]{#struct_0_37551_x7964_624491424}

[IPv6 connection limit policy 3 has been applied 3 times, and has 2 limit rules.]{lang="EN-US"}

[Limit rule list:]{lang="EN-US"}

[Policy  Rule     Stat Type  HiThres  LoThres  ACL]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[     3     1       Src-Dst     1000      800  3010  ]{lang="EN-US"}

[           2           Dst      500      450  3001]{lang="EN-US"}

[Application list:]{lang="EN-US"}

[    GigabitEthernet1/0/1]{lang="EN-US"}

[    Vlan-interface1]{lang="EN-US"}

[    Tunnel0]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display connection-limit]{lang="EN-US"}]{#struct_0_37551_x7964_868766864}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x799332846}[[字段]{style="font-family:黑体"}]{#struct_0_37551_x7964_1674505212}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_37551_x7964_x766602701}

[[Limit rule list]{lang="EN-US"}]{#struct_0_37551_x7964_x873526597}

[[连接数限制策略信息列表]{style="font-family:宋体"}]{#struct_0_37551_x7964_x925778421}

[[Policy]{lang="EN-US"}]{#struct_0_37551_x7964_1898096213}

[[连接数限制策略编号]{style="font-family:宋体"}]{#struct_0_37551_x7964_624556960}

[[Rule]{lang="EN-US"}]{#struct_0_37551_x7964_x3588353}

[[连接数限制规则编号]{style="font-family:宋体"}]{#struct_0_37551_x7964_x1916220215}

[[Stat Type]{lang="EN-US"}]{#struct_0_37551_x7964_x1137723313}

[[统计方式，有如下取值：]{style="font-family:宋体"}]{#struct_0_37551_x7964_319288623}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Src-Dst-Port]{lang="EN-US"}]{#struct_0_37551_x7964_600455158}[：按源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[－目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[－服务的组合进行统计和限制]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Src-Dst]{lang="EN-US"}]{#struct_0_37551_x7964_624622496}[：按源]{style="font-family:宋体"}[IP]{lang="EN-US"}[－目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[的组合进行统计和限制]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Src-Port]{lang="EN-US"}]{#struct_0_37551_x7964_x1964616795}[：按源]{style="font-family:宋体"}[IP]{lang="EN-US"}[－服务的组合进行统计和限制]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dst-Port]{lang="EN-US"}]{#struct_0_37551_x7964_x1574367766}[：按目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[－服务的组合进行统计和限制]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Src]{lang="EN-US"}]{#struct_0_37551_x7964_x1857216478}[：按源]{style="font-family:宋体"}[IP]{lang="EN-US"}[进行统计和限制]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dst]{lang="EN-US"}]{#struct_0_37551_x7964_1462357592}[：按目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[进行统计和限制]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port]{lang="EN-US"}]{#struct_0_37551_x7964_2092925989}[：按服务进行统计和限制]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dslite]{lang="EN-US"}]{#struct_0_37551_x7964_x422074882}[：按]{style="font-family:宋体"}[DS-Lite]{lang="SV" style="color:black"}[隧道的]{lang="EN-US" style="font-family:
  宋体;color:black"}[B4]{lang="EN-US"}[设备]{lang="EN-US" style="font-family:宋体"}[进行统计和限制]{lang="EN-US" style="font-family:宋体;
  color:black"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\--]{lang="EN-US"}]{#struct_0_37551_x7964_624688032}[：不按照具体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、服务进行统计和限制，与本规则引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[相匹配的所有连接将整体受到指定的阈值限制]{style="font-family:宋体"}

[[HiThres]{lang="EN-US"}]{#struct_0_37551_x7964_x2043926693}

[[连接数上限]{style="font-family:宋体"}]{#struct_0_37551_x7964_578760817}

[[LoThres]{lang="EN-US"}]{#struct_0_37551_x7964_260096606}

[[连接数下限]{style="font-family:宋体"}]{#struct_0_37551_x7964_198967119}

[[ACL]{lang="EN-US"}]{#struct_0_37551_x7964_571796434}

[[规则引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_37551_x7964_624753568}[编号或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[Application list]{lang="EN-US"}]{#struct_0_37551_x7964_x405878861}

[[连接数限制策略应用列表，包括接口名称和]{style="font-family:宋体"}[Global]{lang="EN-US"}]{#struct_0_37551_x7964_x682125636}[，其中]{style="font-family:宋体"}[Global]{lang="EN-US"}[表示该连接数限制策略应用在全局]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x2065527954}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit]{lang="EN-US"}**]{#struct_0_37551_x7964_163983542}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit apply]{lang="EN-US"}**]{#struct_0_37551_x7964_712559885}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit apply global]{lang="EN-US"}**]{#struct_0_37551_x7964_x913719660}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[limit]{lang="EN-US"}**]{#struct_0_37551_x7964_624819104}

::::: {#216860153 .myid}
[]{#_Toc404793570}[]{#struct_0_37551_x7964_x1435788657}

**连接数限制 \-- 连接数限制配置命令 \-- display connection-limit ipv6-stat-nodes**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](连接数限制命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_37551_x7964_x815203103}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本]{style="font-family:KaiTi_GB2312"}]{#struct_0_37551_x7964_637957162}[命令的支持情况与设备的型号有关]{style="font-family:KaiTi_GB2312"}[，]{style="font-family:
KaiTi_GB2312"}[请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="SV"}

[**[display connection-limit ipv6-stat-nodes]{lang="SV"}**]{#struct_0_37551_x7964_x1367760352}[命令用来显示连接数限制在全局或接口的]{style="font-family:宋体"}[IPv6]{lang="SV"}[统计节点列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1551118713}

[[集中式设备]{style="font-family:宋体"}]{#struct_0_37551_x7964_x1888433720}[：]{style="font-family:宋体"}

[**[display connection-limit ipv6-stat-nodes]{lang="SV"}**]{#struct_0_37551_x7964_x1297551615}[ { **global** \| **interface** *interface-type interface-number* } \[ **destination** *destination-ip* \| **service-port** *port-number* \| **source** *source-ip* \] \* \[ **count** \]]{lang="SV"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_37551_x7964_1792368232}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display connection-limit ipv6-stat-nodes]{lang="EN-US"}**[ { **global** \| **interface** *interface-type interface-number* } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **destination** *destination-ip* \| **service-port** *port-number* \| **source** *source-ip* \] \* \[ **count** \]]{lang="EN-US"}]{#struct_0_37551_x7964_624884640}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_37551_x7964_178678711}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display connection-limit ipv6-stat-nodes]{lang="EN-US"}**[ { **global** \| **interface** *interface-type interface-number* } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **destination** *destination-ip* \| **service-port** *port-number* \| **source** *source-ip* \] \* \[ **count** \]]{lang="EN-US"}]{#struct_0_37551_x7964_x171322144}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x686036136}

[[任意视图]{style="font-family:宋体"}]{#struct_0_37551_x7964_1593060670}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x30385997}

[[network-admin]{lang="EN-US"}]{#struct_0_37551_x7964_x625734826}

[[network-operator]{lang="EN-US"}]{#struct_0_37551_x7964_506277644}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37551_x7964_1585118989}

[[mdc-operator]{lang="EN-US"}]{#struct_0_37551_x7964_624950176}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37551_x7964_937335329}

[**[global]{lang="EN-US" style="color:black"}**]{#struct_0_37551_x7964_x1334261802}[：显示全局的]{style="font-family:
宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[统计节点列表[。]{style="color:black"}]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_37551_x7964_x1419723584}[：显示指定接口的]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号[。]{style="color:black"}]{style="font-family:
宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_37551_x7964_375511551}[：显示指定单板上全局或全局接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_37551_x7964_x1463364249}[：显示指定成员设备上全局或全局接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_37551_x7964_578713364}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上全局或全局接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_37551_x7964_734534092}[：显示指定成员设备的指定单板上全局或全局接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_37551_x7964_x927403601}[：显示指定单板上全局或全局接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_37551_x7964_x1262484084}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上全局或全局接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[统计节点列表，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[destination]{lang="EN-US"}**[ *destination-ip*]{lang="EN-US"}]{#struct_0_37551_x7964_289417709}[：显示指定目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[统计节点列表。]{style="font-family:宋体"}

[**[service-port]{lang="EN-US"}***[ port-number]{lang="EN-US"}*]{#struct_0_37551_x7964_x1524973459}[：显示指定服务端口号的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[统计节点列表。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *source-ip*]{lang="EN-US"}]{#struct_0_37551_x7964_623967136}[：显示指定源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[统计节点列表。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_37551_x7964_2123334095}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[统计节点的个数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1981764695}

[[一个统计节点标识了连接数限制进行统计和限制的一个对象（一个连接或一类连接），包括该连接的报文特征（源]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_37551_x7964_722749814}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、服务端口号、传输层协议类型等）、对该连接所应用的连接限制策略、当前连接数目以及当前是否允许创建新的连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[source]{lang="EN-US"}**]{#struct_0_37551_x7964_x1383874998}[、]{lang="EN-US" style="font-family:宋体"}**[destination]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[service-port]{lang="EN-US"}**[中的一个或多个]{lang="EN-US" style="font-family:宋体"}[参数]{style="font-family:宋体"}[，则表示将按照]{lang="EN-US" style="font-family:宋体"}[多个]{style="font-family:宋体"}[条件来显示统计节点列表，比如指定了]{lang="EN-US" style="font-family:宋体"}**[source]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[destination]{lang="EN-US"}**[，则显示]{lang="EN-US" style="font-family:宋体"}[同时]{style="font-family:宋体"}[符合指定源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址和目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址的统计节点列表。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}**[source]{lang="EN-US"}**]{#struct_0_37551_x7964_2123983155}[、]{lang="EN-US" style="font-family:宋体"}**[destination]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[service-port]{lang="EN-US"}**[中]{lang="EN-US" style="font-family:宋体"}[任何一个参数，则表示显示所有的统计节点列表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1550287842}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_518190361}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_37551_x7964_624032672}

[ Src IP address          : Any]{lang="EN-US"}

[     VPN instance        : vpn5]{lang="EN-US"}

[ Dst IP address          : fe80::5ed9:98ff:feb1:69b6]{lang="EN-US"}

[     VPN instance        : abcdefghijklmnopqrstuvwxyzabcde]{lang="EN-US"}

[ Tunnel ID               : 9876543210]{lang="EN-US"}

[ Service                 : tcp/12345]{lang="EN-US"}

[ Limit rule ID           : 12345(ACL: 3184)]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 1000000/90000]{lang="EN-US"}

[ Sessions count          : 150000]{lang="EN-US"}

[ New session flag        : Permit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_746547726}[显示接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes interface vlan-interface 2]{lang="EN-US"}]{#struct_0_37551_x7964_1949657497}

[ Src IP address          : Any]{lang="EN-US"}

[     VPN instance        : vpn5]{lang="EN-US"}

[ Dst IP address          : fe80::5ed9:98ff:feb1:69b6]{lang="EN-US"}

[     VPN instance        : abcdefghijklmnopqrstuvwxyzabcde]{lang="EN-US"}

[ Tunnel ID               : 9876543210 ]{lang="EN-US"}

[ Service                 : tcp/12345 ]{lang="EN-US"}

[ Limit rule ID           : 12345(ACL: 3184)]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 1000000/90000]{lang="EN-US"}

[ Sessions count          : 150000]{lang="EN-US"}

[ New session flag        : Permit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x167904108}[显示全局接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[在]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上的所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes interface vlan-interface 10 slot 2]{lang="EN-US"}]{#struct_0_37551_x7964_624491425}

[Slot 2:]{lang="EN-US"}

[ Src IP address          : 112::2]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Dst IP address          : Any]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Tunnel ID               : \--]{lang="EN-US"}

[ Service                 : udp/300]{lang="EN-US"}

[ Limit rule ID           : 0(ACL: 3571)]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 3000/2900]{lang="EN-US"}

[ Sessions count          : 2002]{lang="EN-US"}

[ New session flag        : Permit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_868766863}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备上全局的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes global slot 2]{lang="EN-US"}]{#struct_0_37551_x7964_1674505213}

[Slot 2:]{lang="EN-US"}

[ Src IP address          : Any]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Dst IP address          : Any]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Tunnel ID               : \--]{lang="EN-US"}

[ Service                 : icmp/0]{lang="EN-US"}

[ Limit rule ID           : 22(ACL: 3666)]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 3500/3000]{lang="EN-US"}

[ Sessions count          : 3100]{lang="EN-US"}

[ New session flag        : Permit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x766668237}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/1/0/2]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes interface gigabitethernet 1/1/0/2]{lang="EN-US"}]{#struct_0_37551_x7964_624556961}

[Slot 1 in chassis 1:]{lang="EN-US"}

[ Src IP address          : 5::1]{lang="EN-US"}

[     VPN instance        : Vpn1]{lang="EN-US"}

[ Dst IP address          : Any]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Tunnel ID               : \--]{lang="EN-US"}

[ Service                 : All]{lang="EN-US"}

[ Limit rule ID           : 21(ACL: 2988)]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 2000/1500]{lang="EN-US"}

[ Sessions count          : 1988]{lang="EN-US"}

[ New session flag        : Deny]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x3588354}[显示全局源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2::1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes global source 2::1 count]{lang="EN-US"}]{#struct_0_37551_x7964_x342242103}

[       Current limit statistic nodes count is 16.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x10147978}[显示全局接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[在]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上的]{style="font-family:
宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes interface vlan-interface 10 slot 2 count]{lang="EN-US"}]{#struct_0_37551_x7964_624622497}

[Slot 2:]{lang="EN-US"}

[       Current limit statistic nodes count is 1.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x1964616794}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes global slot 2 count]{lang="EN-US"}]{#struct_0_37551_x7964_x8283825}

[Slot 2:]{lang="EN-US"}

[       Current limit statistic nodes count is 0.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x1371272240}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes global chassis 1 slot 2 count]{lang="EN-US"}]{#struct_0_37551_x7964_1795242185}

[Slot 2 in chassis 1:]{lang="EN-US"}

[       Current limit statistic nodes count is 0.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_304386294}[显示全局接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[在]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板的]{style="font-family:
宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes interface vlan-interface 10 slot 2 cpu 0]{lang="EN-US"}]{#struct_0_37551_x7964_304320758}

[CPU 0 on slot 2:]{lang="EN-US"}

[ Src IP address          : 112::2]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Dst IP address          : Any]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Tunnel ID               : \--]{lang="EN-US"}

[ Service                 : udp/300]{lang="EN-US"}

[ Limit rule ID           : 0(ACL: 3571)]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 3000/2900]{lang="EN-US"}

[ Sessions count          : 2002]{lang="EN-US"}

[ New session flag        : Permit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_1900016659}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上全局的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes global slot 2 cpu 0]{lang="EN-US"}]{#struct_0_37551_x7964_304255222}

[CPU 0 on slot 2:]{lang="EN-US"}

[ Src IP address          : Any]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Dst IP address          : Any]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Tunnel ID               : \--]{lang="EN-US"}

[ Service                 : icmp/0]{lang="EN-US"}

[ Limit rule ID           : 22(ACL: 3666)]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 3500/3000]{lang="EN-US"}

[ Sessions count          : 3100]{lang="EN-US"}

[ New session flag        : Permit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x1632415099}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/1/0/2]{lang="EN-US"}[在]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:
宋体"}[1]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes interface gigabitethernet 1/1/0/2 chassis 1 slot 1 cpu 0]{lang="EN-US"}]{#struct_0_37551_x7964_303665398}

[CPU 0 on slot 1 in chassis 1:]{lang="EN-US"}

[ Src IP address          : 5::1]{lang="EN-US"}

[     VPN instance        : Vpn1]{lang="EN-US"}

[ Dst IP address          : Any]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Tunnel ID               : \--]{lang="EN-US"}

[ Service                 : All]{lang="EN-US"}

[ Limit rule ID           : 21(ACL: 2988)]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 2000/1500]{lang="EN-US"}

[ Sessions count          : 1988]{lang="EN-US"}

[ New session flag        : Deny]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_513114478}[显示全局接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[在]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板的]{style="font-family:
宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes interface vlan-interface 10 slot 2 cpu 0 count]{lang="EN-US"}]{#struct_0_37551_x7964_286994836}

[CPU 0 on slot 2:]{lang="EN-US"}

[       Current limit statistic nodes count is 1.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_303599862}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes global slot 2 cpu 0 count]{lang="EN-US"}]{#struct_0_37551_x7964_x1014255540}

[CPU 0 on slot 2:]{lang="EN-US"}

[       Current limit statistic nodes count is 0.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x1755976387}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit ipv6-stat-nodes global chassis 1 slot 2 cpu 0 count]{lang="EN-US"}]{#struct_0_37551_x7964_304189685}

[CPU 0 on slot 2 in chassis 1:]{lang="EN-US"}

[       Current limit statistic nodes count is 0.]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display connection-limit stat-nodes]{lang="EN-US"}]{#struct_0_37551_x7964_484536240}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x798463758}[[字段]{style="font-family:黑体"}]{#struct_0_37551_x7964_296961406}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_37551_x7964_624688033}

[[Src IP address]{lang="EN-US"}]{#struct_0_37551_x7964_x2043926692}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_37551_x7964_x987323124}[地址]{style="font-family:宋体"}

[[Dst IP address]{lang="EN-US"}]{#struct_0_37551_x7964_x1181691920}

[[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_37551_x7964_425985345}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_37551_x7964_1865527506}

[[该地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_37551_x7964_767001446}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，"]{style="font-family:宋体"}[\--]{lang="EN-US"}["表示属于公网]{style="font-family:宋体"}

[[Tunnel ID]{lang="EN-US"}]{#struct_0_37551_x7964_624753569}

[[DS Lite]{lang="EN-US"}]{#struct_0_37551_x7964_x405878862}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[，"]{style="font-family:宋体"}[\--]{lang="EN-US"}["表示不属于任何]{style="font-family:宋体"}[DS Lite Tunnel]{lang="EN-US"}

[[Service]{lang="EN-US"}]{#struct_0_37551_x7964_x682322244}

[[协议名及服务端口号。如果不是知名协议则显示为"]{style="font-family:宋体"}[unknown(xx)]{lang="EN-US"}]{#struct_0_37551_x7964_1071930222}["，]{style="font-family:宋体"}[xx]{lang="EN-US"}[为协议编号，此时不显示服务端口号。其中，对于]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[协议，括弧内的数字为]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[的]{style="font-family:宋体"}[type]{lang="EN-US"}[和]{style="font-family:宋体"}[code]{lang="EN-US"}[字段组合表示的十六进制数所对应的十进制数]{style="font-family:宋体"}

[[Limit rule ID]{lang="EN-US"}]{#struct_0_37551_x7964_1071395806}

[[匹配的规则编号，括号里为匹配的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_37551_x7964_x1256549637}[编号]{style="font-family:宋体"}

[[Sessions threshold Hi/Lo]{lang="EN-US"}]{#struct_0_37551_x7964_624819105}

[[连接数限制的上限值及下限值]{style="font-family:宋体"}]{#struct_0_37551_x7964_x1435788658}

[[Sessions count]{lang="EN-US"}]{#struct_0_37551_x7964_x1218487630}

[[当前连接计数]{style="font-family:宋体"}]{#struct_0_37551_x7964_x1741689437}

[[New session flag]{lang="EN-US"}]{#struct_0_37551_x7964_1641815638}

[[是否允许创建新连接，]{style="font-family:宋体"}[Permit]{lang="EN-US"}]{#struct_0_37551_x7964_624884641}[表示允许创建，]{style="font-family:宋体"}[Deny]{lang="EN-US"}[表示不允许创建]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_178678712}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit apply global ipv6-policy]{lang="EN-US"}**]{#struct_0_37551_x7964_x171322145}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit apply ipv6-policy]{lang="EN-US"}**]{#struct_0_37551_x7964_x685970600}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit ipv6-policy]{lang="EN-US"}**]{#struct_0_37551_x7964_x236894898}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[limit]{lang="EN-US"}**]{#struct_0_37551_x7964_1557991602}

::::: {#-1415026309 .myid}
[]{#_Toc404793571}[]{#struct_0_37551_x7964_1683599182}[]{#_Toc312690585}[]{#_Toc312690586}[]{#_Toc312690587}[]{#_Toc312690588}[]{#_Toc312690589}[]{#_Toc312690590}[]{#_Toc312690591}[]{#_Toc312690592}[]{#_Toc312690593}[]{#_Toc312690594}[]{#_Toc312690595}[]{#_Toc312690596}[]{#_Toc312690597}[]{#_Toc312690598}[]{#_Toc312690599}[]{#_Toc312690600}[]{#_Toc312690601}[]{#_Toc312690602}[]{#_Toc312690603}[]{#_Toc312690633}[]{#_Toc312690634}[]{#_Toc312690635}[]{#_Toc312690636}[]{#_Toc312690637}[]{#_Toc312690638}

**连接数限制 \-- 连接数限制配置命令 \-- display connection-limit statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](连接数限制命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_37551_x7964_x1645984103}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本]{style="font-family:KaiTi_GB2312"}]{#struct_0_37551_x7964_624950177}[命令的支持情况与设备的型号有关]{style="font-family:KaiTi_GB2312"}[，]{style="font-family:
KaiTi_GB2312"}[请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="SV"}

[**[display connection-limit statistics]{lang="SV"}**]{#struct_0_37551_x7964_937335328}[命令用来显示连接数限制在全局或接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1334261803}

[[集中式设备]{style="font-family:宋体"}]{#struct_0_37551_x7964_1309159771}[：]{style="font-family:宋体"}

[**[display connection-limit statistics ]{lang="EN-US"}**[{ **global** \| **interface** *interface-type interface-number* } ]{lang="EN-US"}]{#struct_0_37551_x7964_1653816641}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_37551_x7964_2004379754}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display connection-limit statistics ]{lang="EN-US"}**[{ **global** \| **interface** *interface-type interface-number* } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_37551_x7964_1485975604}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_37551_x7964_656981330}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display connection-limit statistics ]{lang="EN-US"}**[{ **global** \| **interface** *interface-type interface-number* } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_37551_x7964_x2067163873}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37551_x7964_2066252064}

[[任意视图]{style="font-family:宋体"}]{#struct_0_37551_x7964_623967137}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37551_x7964_2123334096}

[[network-admin]{lang="EN-US"}]{#struct_0_37551_x7964_1981699159}

[[network-operator]{lang="EN-US"}]{#struct_0_37551_x7964_x1163770130}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37551_x7964_1572227620}

[[mdc-operator]{lang="EN-US"}]{#struct_0_37551_x7964_65567821}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1755065138}

[**[global]{lang="EN-US" style="color:black"}**]{#struct_0_37551_x7964_2052447756}[：显示全局的]{style="font-family:
宋体;color:black"}[连接数限制统计信息[。]{style="color:black"}]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_37551_x7964_486598868}[：显示指定接口的]{style="font-family:宋体;color:black"}[连接数限制统计信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号[。]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_37551_x7964_1233819808}[：显示指定单板上全局或全局接口的连接数限制统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定显示[全局的]{style="color:black"}连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_37551_x7964_1775649872}[：显示指定成员设备上全局或全局接口的连接数限制统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。该参数仅在指定显示[全局的]{style="color:black"}连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_37551_x7964_x1794005167}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上全局或全局接口的连接数限制统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。该参数仅在指定显示[全局的]{style="color:black"}连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_37551_x7964_624032673}[：显示指定成员设备的指定单板上全局或全局接口的连接数限制统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定显示[全局的]{style="color:black"}连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_37551_x7964_578647828}[：显示指定单板上全局或全局接口的连接数限制统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。该参数仅在指定显示[全局的]{style="color:black"}连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_37551_x7964_304386293}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上全局或全局接口的连接数限制统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_37551_x7964_746547725}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_1949657498}[显示全局[的]{style="color:black"}连接数限制统计信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit statistics global]{lang="EN-US"}]{#struct_0_37551_x7964_x168231788}

[Connection limit statistics (Global, slot 0):]{lang="EN-US"}

[    Dropped IPv4 packets:   54781]{lang="EN-US"}

[    Dropped IPv6 packets:   11457]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x577792715}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上的全局的连接数限制统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit statistics global slot 2]{lang="EN-US"}]{#struct_0_37551_x7964_x1341133866}

[Connection limit statistics (Global, slot 2):]{lang="EN-US"}

[    Dropped IPv4 packets:   74213]{lang="EN-US"}

[    Dropped IPv6 packets:   58174]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_1496948662}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备上全局的连接数限制统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit statistics global slot 2]{lang="EN-US"}]{#struct_0_37551_x7964_x2104391927}

[Connection limit statistics (Global, slot 2):]{lang="EN-US"}

[    Dropped IPv4 packets:   74213]{lang="EN-US"}

[    Dropped IPv6 packets:   58174]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_1900652545}[显示全局接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[在]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:
宋体"}[1]{lang="EN-US"}[号单板上的连接数限制统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit statistics interface vlan-interface 10 chassis 2 slot 1]{lang="EN-US"}]{#struct_0_37551_x7964_146553454}

[Connection limit statistics (Vlan-interface10, slot 1 in chassis 2):]{lang="EN-US"}

[    Dropped IPv4 packets:   12345]{lang="EN-US"}

[    Dropped IPv6 packets:   55239]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_304255221}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的全局的连接数限制统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit statistics global slot 2 cpu 0]{lang="EN-US"}]{#struct_0_37551_x7964_x1632415100}

[Connection limit statistics (Global, CPU 0 on slot 2):]{lang="EN-US"}

[    Dropped IPv4 packets:   74213]{lang="EN-US"}

[    Dropped IPv6 packets:   58174]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_303665397}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上全局的连接数限制统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit statistics global slot 2 cpu 0]{lang="EN-US"}]{#struct_0_37551_x7964_513114491}

[Connection limit statistics (Global, CPU 0 on slot 2):]{lang="EN-US"}

[    Dropped IPv4 packets:   74213]{lang="EN-US"}

[    Dropped IPv6 packets:   58174]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x860016243}[显示全局接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[在]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:
宋体"}[1]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的连接数限制统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit statistics interface vlan-interface 10 chassis 2 slot 1 cpu 0]{lang="EN-US"}]{#struct_0_37551_x7964_303599861}

[Connection limit statistics (Vlan-interface10, CPU 0 on slot 1 in chassis 2):]{lang="EN-US"}

[    Dropped IPv4 packets:   12345]{lang="EN-US"}

[    Dropped IPv6 packets:   55239]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display connection-limit statistics]{lang="EN-US"}]{#struct_0_37551_x7964_387982737}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x801621646}[[字段]{style="font-family:黑体"}]{#struct_0_37551_x7964_1394438685}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_37551_x7964_x784092327}

[[Dropped IPv4 packet]{lang="EN-US"}]{#struct_0_37551_x7964_x1584112943}

[[匹配全局或接口]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_37551_x7964_x1064609791}[连接数限制策略，因连接数超过指定上限而被丢弃的报文个数]{style="font-family:宋体"}

[[Dropped IPv6 packet]{lang="EN-US"}]{#struct_0_37551_x7964_x2104326391}

[[匹配全局或接口]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_37551_x7964_x711455788}[连接数限制策略，因连接数超过指定上限而被丢弃的报文个数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_2061774965}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit ]{lang="EN-US"}**]{#struct_0_37551_x7964_2128943518}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit apply]{lang="EN-US"}**]{#struct_0_37551_x7964_1526432742}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit apply global]{lang="EN-US"}**]{#struct_0_37551_x7964_x168354675}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[limit]{lang="EN-US"}**]{#struct_0_37551_x7964_962458454}

::::: {#1725398437 .myid}
[]{#_Toc404793572}[]{#struct_0_37551_x7964_36863732}[]{#_Toc312690640}[]{#_Toc312690641}

**连接数限制 \-- 连接数限制配置命令 \-- display connection-limit stat-nodes**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](连接数限制命令.files/image001.png){#图片 6 width="62" height="25"}]{lang="EN-US"}]{#struct_0_37551_x7964_x2104260855}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本]{style="font-family:KaiTi_GB2312"}]{#struct_0_37551_x7964_248839731}[命令的支持情况与设备的型号有关]{style="font-family:KaiTi_GB2312"}[，]{style="font-family:
KaiTi_GB2312"}[请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="SV"}

[**[display connection-limit stat-nodes]{lang="SV"}**]{#struct_0_37551_x7964_364496926}[命令用来显示连接数限制在全局或接口的]{style="font-family:宋体"}[IPv4]{lang="SV"}[统计节点列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1709855673}

[[集中式设备]{style="font-family:宋体"}]{#struct_0_37551_x7964_1366059503}[：]{style="font-family:宋体"}

[**[display connection-limit stat-nodes ]{lang="SV"}**]{#struct_0_37551_x7964_241509263}[{ **global** \| **interface** *interface-type interface-number* } \[ **destination** *destination-ip* \| **service-port** *port-number* \| **source** *source-ip* \] \* \[ **count** \]]{lang="SV"}

[**[display connection-limit stat-nodes ]{lang="SV"}**]{#struct_0_37551_x7964_1918739962}[{ **global** \| **interface** *interface-type interface-number* } **dslite-peer** *b4-address* \[ **count** \]]{lang="SV"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_37551_x7964_1758531441}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display connection-limit stat-nodes ]{lang="EN-US"}**[{ **global** \| **interface** *interface-type interface-number* } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **destination** *destination-ip* \| **service-port** *port-number* \| **source** *source-ip* \] \* \[ **count** \]]{lang="EN-US"}]{#struct_0_37551_x7964_1747955662}

[**[display connection-limit stat-nodes ]{lang="SV"}**]{#struct_0_37551_x7964_1918739963}[{ **global** \| **interface** *interface-type interface-number* } ]{lang="SV"}[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] ]{lang="EN-US"}**[dslite-peer]{lang="SV"}***[ b4-address]{lang="SV"}*[ \[ **count** \]]{lang="SV"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_37551_x7964_x917510941}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display connection-limit stat-nodes ]{lang="EN-US"}**[{ **global** \| **interface** *interface-type interface-number* } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **destination** *destination-ip* \| **service-port** *port-number* \| **source** *source-ip* \] \* \[ **count** \]]{lang="EN-US"}]{#struct_0_37551_x7964_x2104195319}

[**[display connection-limit stat-nodes ]{lang="SV"}**]{#struct_0_37551_x7964_1918739964}[{ **global** \| **interface** *interface-type interface-number* } ]{lang="SV"}[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] ]{lang="EN-US"}**[dslite-peer]{lang="SV"}***[ b4-address]{lang="SV"}*[ \[ **count** \]]{lang="SV"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1056576423}

[[任意视图]{style="font-family:宋体"}]{#struct_0_37551_x7964_x1308965184}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1603523589}

[[network-admin]{lang="EN-US"}]{#struct_0_37551_x7964_75017907}

[[network-operator]{lang="EN-US"}]{#struct_0_37551_x7964_1394479970}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37551_x7964_1217937075}

[[mdc-operator]{lang="EN-US"}]{#struct_0_37551_x7964_639137948}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x106553062}

[**[global]{lang="EN-US" style="color:black"}**]{#struct_0_37551_x7964_x2104129783}[：显示全局的]{style="font-family:
宋体;color:black"}[IPv4]{lang="EN-US" style="color:black"}[统计节点列表[。]{style="color:black"}]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_37551_x7964_580842766}[：显示指定接口的]{style="font-family:宋体;color:black"}[IPv4]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号[。]{style="color:black"}]{style="font-family:
宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_37551_x7964_x200052415}[：显示指定单板上全局或全局接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_37551_x7964_1668417351}[：显示指定成员设备上全局或全局接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_37551_x7964_x1746951000}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上全局或全局接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_37551_x7964_x837516415}[：显示指定成员设备的指定单板上全局或全局接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_37551_x7964_282137155}[：显示指定单板上全局或全局接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_37551_x7964_303993076}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上全局或全局接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[destination]{lang="EN-US"}**[ *destination-ip*]{lang="EN-US"}]{#struct_0_37551_x7964_637663551}[：显示指定目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[统计节点列表。]{style="font-family:宋体"}

[**[service-port]{lang="EN-US"}***[ port-number]{lang="EN-US"}*]{#struct_0_37551_x7964_x1242205138}[：显示指定服务端口号的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[统计节点列表。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *source-ip*]{lang="EN-US"}]{#struct_0_37551_x7964_x922857090}[：显示指定源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[统计节点列表。]{style="font-family:宋体"}

[**[dslite-peer]{lang="SV"}**]{#struct_0_37551_x7964_1918739967}*[ b4-address]{lang="SV"}*[：显示指定]{style="font-family:宋体"}[DS-Lite B4]{lang="EN-US"}[设备的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[统计节点列表，]{style="font-family:宋体"}*[b4-address]{lang="SV"}*[表示]{style="font-family:宋体"}[B4]{lang="EN-US"}[设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_37551_x7964_1287228744}[：显示]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[统计节点的个数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x383921440}

[[一个统计节点标识了连接数限制进行统计和限制的一个对象（一个连接或一类连接），包括该连接的报文特征（源]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_37551_x7964_x2104064247}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、服务端口号、传输层协议类型等）、对该连接所应用的连接限制策略、当前连接数目的统计值，以及当前是否允许创建新的连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[source]{lang="EN-US"}**]{#struct_0_37551_x7964_1942939491}[、]{lang="EN-US" style="font-family:宋体"}**[destination]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[service-port]{lang="EN-US"}**[中的一个或多个]{lang="EN-US" style="font-family:宋体"}[参数]{style="font-family:宋体"}[，则表示将按照]{lang="EN-US" style="font-family:宋体"}[多个]{style="font-family:宋体"}[条件来显示统计节点列表，比如指定了]{lang="EN-US" style="font-family:宋体"}**[source ]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[destination]{lang="EN-US"}**[，则显示]{lang="EN-US" style="font-family:宋体"}[同时]{style="font-family:宋体"}[符合指定源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址和目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址的统计节点列表。]{lang="EN-US" style="font-family:宋体"}[.]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}**[source]{lang="EN-US"}**]{#struct_0_37551_x7964_1770085419}[、]{lang="EN-US" style="font-family:宋体"}**[destination]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[service-port]{lang="EN-US"}**[中]{lang="EN-US" style="font-family:宋体"}[任何一个参数，则表示显示所有的统计节点列表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1877568808}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x876629137}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[连接数限制统计节点列表。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_37551_x7964_459860299}

[ Src IP address          : 100.100.100.100]{lang="EN-US"}

[     VPN instance        : 0123456789012345678901234567890]{lang="EN-US"}

[ Dst IP address          : 200.200.200.200]{lang="EN-US"}

[     VPN instance        : abcdefghijklmnopqrstuvwxyzabcde]{lang="EN-US"}

[ Tunnel ID               : 1234567890]{lang="EN-US"}

[ Service                 : tcp/12345 ]{lang="EN-US"}

[ Limit rule ID           : 12345(ACL: 3001) ]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 1100000/980000 ]{lang="EN-US"}

[ Sessions count          : 1050000]{lang="EN-US"}

[ New session flag        : Permit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x1668981968}[显示接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[连接数限制统计节点列表。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes interface vlan-interface 2]{lang="EN-US"}]{#struct_0_37551_x7964_x2103998711}

[ Src IP address          : 100.100.100.100]{lang="EN-US"}

[     VPN instance        : 0123456789012345678901234567890]{lang="EN-US"}

[ Dst IP address          : 200.200.200.200]{lang="EN-US"}

[     VPN instance        : abcdefghijklmnopqrstuvwxyzabcde]{lang="EN-US"}

[ Tunnel ID               : 1234567890]{lang="EN-US"}

[ Service                 : tcp/12345 ]{lang="EN-US"}

[ Limit rule ID           : 12345(ACL: 3001) ]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 1100000/980000 ]{lang="EN-US"}

[ Sessions count          : 1050000]{lang="EN-US"}

[ New session flag        : Permit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x48197418}[显示所有单板上全局的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes global]{lang="EN-US"}]{#struct_0_37551_x7964_x2103933175}

[Slot 0:]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[ Src IP address          : Any]{lang="EN-US"}

[     VPN instance        : Vpn1]{lang="EN-US"}

[ Dst IP address          : Any]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Tunnel ID               : \--]{lang="EN-US"}

[ Service                 : All]{lang="EN-US"}

[ Limit rule ID           : 21(ACL: 2002) ]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 2000/1500]{lang="EN-US"}

[ Sessions count          : 1988]{lang="EN-US"}

[ New session flag        : Deny]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x1543040146}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备上全局的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes global slot 2]{lang="EN-US"}]{#struct_0_37551_x7964_111601836}

[Slot 2:]{lang="EN-US"}

[ Src IP address          : Any]{lang="EN-US"}

[     VPN instance        : Vpn1]{lang="EN-US"}

[ Dst IP address          : 202.113.16.117]{lang="EN-US"}

[     VPN instance        : Vpn2]{lang="EN-US"}

[ Tunnel ID               : \--]{lang="EN-US"}

[ Service                 : icmp/0]{lang="EN-US"}

[ Limit rule ID           : 7(ACL: 3102) ]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 4000/3800 ]{lang="EN-US"}

[ Sessions count          : 1001]{lang="EN-US"}

[ New session flag        : Permit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_129018371}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/1/0/2]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes interface gigabitethernet 1/1/0/2]{lang="EN-US"}]{#struct_0_37551_x7964_x2104916215}

[Slot 1 in chassis 1:]{lang="EN-US"}

[ Src IP address          : Any]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Dst IP address          : 110.23.1.44]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Tunnel ID               : \--]{lang="EN-US"}

[ Service                 : udp/333]{lang="EN-US"}

[ Limit rule ID           : 19(ACL: 3307)]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 10000/9900 ]{lang="EN-US"}

[ Sessions count          : 1001]{lang="EN-US"}

[ New session flag        : Permit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x1512276242}[显示全局的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes global count]{lang="EN-US"}]{#struct_0_37551_x7964_1295960483}

[       Current limit statistic nodes count is 5.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_954750862}[显示全局接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[在]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上的]{style="font-family:
宋体"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes interface vlan-interface 10 slot 2 count]{lang="EN-US"}]{#struct_0_37551_x7964_x811923916}

[Slot 2:]{lang="EN-US"}

[       Current limit statistic nodes count is 1.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x1430686414}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备上源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes global slot 2 source 1.1.1.1 count]{lang="EN-US"}]{#struct_0_37551_x7964_x581269637}

[Slot 2:]{lang="EN-US"}

[       Current limit statistic nodes count is 0.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_5772297}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes global chassis 1 slot 2 count]{lang="EN-US"}]{#struct_0_37551_x7964_x2104850679}

[Slot 2 in chassis 1:]{lang="EN-US"}

[       Current limit statistic nodes count is 0.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_303599860}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上全局的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes global slot 1 cpu 0]{lang="EN-US"}]{#struct_0_37551_x7964_304189683}

[CPU 0 on slot 1:]{lang="EN-US"}

[ Src IP address          : Any]{lang="EN-US"}

[     VPN instance        : Vpn1]{lang="EN-US"}

[ Dst IP address          : Any]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Tunnel ID               : \--]{lang="EN-US"}

[ Service                 : All]{lang="EN-US"}

[ Limit rule ID           : 21(ACL: 2002) ]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 2000/1500]{lang="EN-US"}

[ Sessions count          : 1988]{lang="EN-US"}

[ New session flag        : Deny]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_304124147}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上全局的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes global slot 2 cpu 0]{lang="EN-US"}]{#struct_0_37551_x7964_1626320810}

[CPU 0 on slot 2:]{lang="EN-US"}

[ Src IP address          : Any]{lang="EN-US"}

[     VPN instance        : Vpn1]{lang="EN-US"}

[ Dst IP address          : 202.113.16.117]{lang="EN-US"}

[     VPN instance        : Vpn2]{lang="EN-US"}

[ Tunnel ID               : \--]{lang="EN-US"}

[ Service                 : icmp/0]{lang="EN-US"}

[ Limit rule ID           : 7(ACL: 3102) ]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 4000/3800 ]{lang="EN-US"}

[ Sessions count          : 1001]{lang="EN-US"}

[ New session flag        : Permit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_304058611}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/1/0/2]{lang="EN-US"}[在]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:
宋体"}[1]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制统计节点列表。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes interface gigabitethernet 1/1/0/2 chassis 1 slot 1 cpu 0]{lang="EN-US"}]{#struct_0_37551_x7964_303993075}

[CPU 0 on slot 1 in chassis 1:]{lang="EN-US"}

[ Src IP address          : Any]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Dst IP address          : 110.23.1.44]{lang="EN-US"}

[     VPN instance        : \--]{lang="EN-US"}

[ Tunnel ID               : \--]{lang="EN-US"}

[ Service                 : udp/333]{lang="EN-US"}

[ Limit rule ID           : 19(ACL: 3307)]{lang="EN-US"}

[ Sessions threshold Hi/Lo: 10000/9900 ]{lang="EN-US"}

[ Sessions count          : 1001]{lang="EN-US"}

[ New session flag        : Permit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x64681097}[显示全局接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[在]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板的]{style="font-family:
宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes interface vlan-interface 10 slot 2 cpu 0 count]{lang="EN-US"}]{#struct_0_37551_x7964_304451827}

[CPU 0 on slot 2:]{lang="EN-US"}

[       Current limit statistic nodes count is 1.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x601628528}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes global slot 2 cpu 0 source 1.1.1.1 count]{lang="EN-US"}]{#struct_0_37551_x7964_1363056249}

[CPU 0 on slot 2:]{lang="EN-US"}

[       Current limit statistic nodes count is 0.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_304386291}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US" style="color:black"}[连接数限制统计节点个数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display connection-limit stat-nodes global chassis 1 slot 2 cpu 0 count]{lang="EN-US"}]{#struct_0_37551_x7964_x810266443}

[CPU 0 on slot 2 in chassis 1:]{lang="EN-US"}

[       Current limit statistic nodes count is 0.]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display connection-limit stat-nodes]{lang="EN-US"}]{#struct_0_37551_x7964_x908604302}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x802482574}[[字段]{style="font-family:黑体"}]{#struct_0_37551_x7964_1128449040}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_37551_x7964_x854635317}

[[Src IP address]{lang="EN-US"}]{#struct_0_37551_x7964_x1871074365}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_37551_x7964_1289637108}[地址]{style="font-family:宋体"}

[[Dst IP address]{lang="EN-US"}]{#struct_0_37551_x7964_1311298817}

[[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_37551_x7964_x2104391926}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_37551_x7964_334568604}

[[该地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_37551_x7964_643071992}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，"]{style="font-family:宋体"}[\--]{lang="EN-US"}["表示不属于任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}

[[Tunnel ID]{lang="EN-US"}]{#struct_0_37551_x7964_x1373624626}

[[DS Lite]{lang="EN-US"}]{#struct_0_37551_x7964_x338091184}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[，"]{style="font-family:宋体"}[\--]{lang="EN-US"}["表示不属于任何]{style="font-family:宋体"}[DS Lite Tunnel]{lang="EN-US"}

[[Service]{lang="EN-US"}]{#struct_0_37551_x7964_1113025804}

[[协议名及服务端口号。如果不是知名协议则显示为"]{style="font-family:宋体"}[unknown(xx)]{lang="EN-US"}]{#struct_0_37551_x7964_x328047882}["，]{style="font-family:宋体"}[xx]{lang="EN-US"}[为协议编号，此时不显示服务端口号。其中，对于]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[协议，括弧内的数字为]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[的]{style="font-family:宋体"}[type]{lang="EN-US"}[和]{style="font-family:宋体"}[code]{lang="EN-US"}[字段组合表示的十六进制数所对应的十进制数]{style="font-family:宋体"}

[[Limit rule ID]{lang="EN-US"}]{#struct_0_37551_x7964_x2104326390}

[[匹配的规则编号，括号里为匹配的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_37551_x7964_854628153}[编号]{style="font-family:宋体"}

[[Sessions threshold Hi/Lo]{lang="EN-US"}]{#struct_0_37551_x7964_714789432}

[[连接数限制的上限值及下限值]{style="font-family:宋体"}]{#struct_0_37551_x7964_x506767126}

[[Sessions count]{lang="EN-US"}]{#struct_0_37551_x7964_1710837587}

[[当前连接计数]{style="font-family:宋体"}]{#struct_0_37551_x7964_118061247}

[[New session flag]{lang="EN-US"}]{#struct_0_37551_x7964_x2104260854}

[[是否允许创建新连接，]{style="font-family:宋体"}[Permit]{lang="EN-US"}]{#struct_0_37551_x7964_1814923672}[表示允许创建，]{style="font-family:宋体"}[Deny]{lang="EN-US"}[表示不允许创建]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1724013008}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit policy]{lang="EN-US"}**]{#struct_0_37551_x7964_x373443}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit apply global policy]{lang="EN-US"}**]{#struct_0_37551_x7964_2043058269}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit apply policy]{lang="EN-US"}**]{#struct_0_37551_x7964_x95560653}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[limit]{lang="EN-US"}**]{#struct_0_37551_x7964_1034827558}

::: {#1180161543 .myid}
[]{#_Toc404793573}[]{#struct_0_37551_x7964_218543685}

**连接数限制 \-- 连接数限制配置命令 \-- limit**

------------------------------------------------------------------------

[**[limit]{lang="EN-US"}**]{#struct_0_37551_x7964_x1543940952}[命令用来配置连接数限制规则。]{style="font-family:宋体"}

[**[undo limit]{lang="EN-US"}**]{#struct_0_37551_x7964_x2104195318}[命令用来删除指定的连接数限制规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_1672306932}

[[IPv4]{lang="EN-US"}]{#struct_0_37551_x7964_x1615878660}[连接数限制策略视图：]{style="font-family:宋体"}

[**[limit]{lang="EN-US"}**[ *limit-id* **acl** \[ **ipv6** \] { *acl-number* \| **name** *acl-name* } \[ **per-destination** \| **per-service** \| **per-source** \] \* **amount** *max-amount* *min-amount*]{lang="EN-US"}]{#struct_0_37551_x7964_x246026040}

[**[limit]{lang="EN-US"}**[ *limit-id* **acl**]{lang="EN-US"}]{#struct_0_37551_x7964_x968190507}**[ ]{lang="EN-US" style="font-size:9.0pt"}[ipv6]{lang="EN-US"}**[ { *acl-number* \| **name** *acl-name* } **per-ds-lite-b4 amount** *max-amount* *min-amount*]{lang="EN-US"}

[**[undo limit ]{lang="EN-US"}***[limit-id]{lang="EN-US"}*]{#struct_0_37551_x7964_361387204}

[[IPv6]{lang="EN-US"}]{#struct_0_37551_x7964_x1615878659}[连接数限制策略视图：]{style="font-family:宋体"}

[**[limit]{lang="EN-US"}**[ *limit-id* **acl** **ipv6** { *acl-number* \| **name** *acl-name* } \[ **per-destination** \| **per-service** \| **per-source** \] \* **amount** *max-amount* *min-amount*]{lang="EN-US"}]{#struct_0_37551_x7964_x1615878658}

[**[undo limit ]{lang="EN-US"}***[limit-id]{lang="EN-US"}*]{#struct_0_37551_x7964_x611763539}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_37551_x7964_231281152}

[[连接数策略中不存在任何规则。]{style="font-family:宋体"}]{#struct_0_37551_x7964_x486440189}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37551_x7964_578372850}

[[IPv4]{lang="EN-US"}]{#struct_0_37551_x7964_484885052}[连接数限制策略视图]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[连接数限制策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1937560215}

[[network-admin]{lang="EN-US"}]{#struct_0_37551_x7964_1751247256}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37551_x7964_x1208355558}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x2104129782}

[*[limit-id]{lang="SV"}*]{#struct_0_37551_x7964_2146926707}[：]{style="font-family:宋体"}[连接数限制规则编号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[acl]{lang="SV"}**]{#struct_0_37551_x7964_x515016086}[：指定用于匹配用户范围的]{style="font-family:宋体"}[ACL]{lang="SV"}[。该连接限制规则仅对]{style="font-family:宋体"}[匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的用户连接数进行统计和限制]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="SV"}**]{#struct_0_37551_x7964_x1555842330}[：表示引用]{style="font-family:宋体"}[I[Pv6 ACL]{style="color:black"}]{lang="SV"}[。若不指定该参数，则表示]{style="font-family:宋体;color:black"}[引用]{style="font-family:宋体"}[IPv4 ACL]{lang="SV" style="color:black"}[。]{style="font-family:宋体;color:black"}

[*[acl-number]{lang="SV"}*]{#struct_0_37551_x7964_1850939689}[：引用的]{style="font-family:宋体"}[ACL]{lang="SV"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="SV"}[～]{style="font-family:宋体"}[3999]{lang="SV"}[。]{style="font-family:
宋体"}

[**[name]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_37551_x7964_1467241519}*[acl-name]{lang="SV"}*[：引用的]{style="font-family:宋体"}[ACL]{lang="SV"}[名称。]{style="font-family:宋体"}

[**[per-destination]{lang="SV"}**]{#struct_0_37551_x7964_x456931160}[：]{style="font-family:宋体"}[表示按目的地址进行统计和限制。]{style="font-family:宋体"}

[**[per-service]{lang="SV"}**]{#struct_0_37551_x7964_315129421}[：]{style="font-family:宋体"}[表示按服务]{style="font-family:宋体"}[（]{style="font-family:宋体"}[即按传输层协议和服务端口]{style="font-family:宋体"}[）]{style="font-family:宋体"}[进行统计和限制。]{style="font-family:宋体"}

[**[per-source]{lang="SV"}**]{#struct_0_37551_x7964_x1197782560}[：]{style="font-family:宋体"}[表示按源地址进行统计和限制。]{style="font-family:宋体"}

[**[per-ds-lite-b4]{lang="SV"}**]{#struct_0_37551_x7964_x41900550}[：[表示按照]{style="color:black"}]{style="font-family:宋体"}[DS-Lite]{lang="SV" style="color:black"}[隧道的]{style="font-family:宋体;
color:black"}[B4]{lang="SV"}[设备]{style="font-family:宋体"}[IPv6]{lang="SV"}[地址]{style="font-family:宋体"}[来进行统计和限制。该参数仅在]{style="font-family:宋体;color:black"}[IPv4]{lang="SV" style="color:black"}[连接数限制策略视图下存在]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[*[max-amount]{lang="SV"}*]{#struct_0_37551_x7964_1691608870}[：指定的连接数上限，取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[1000000]{lang="SV"}[。某范围或某种类型的连接数值超过此值时，用户将不能建立新的连接。]{style="font-family:宋体"}

[*[min-amount]{lang="SV"}*]{#struct_0_37551_x7964_x2104064246}[：指定的连接数下限，取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[1000000]{lang="SV"}[，不能大于]{style="font-family:宋体"}*[max-amount]{lang="SV"}*[的取值。连接数的统计值降到此值之下时，允许用户建立新的连接]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x785943864}

[[每个连接数限制策略中可以定义多个规则，每个规则中需要指定引用的]{style="font-family:宋体"}]{#struct_0_37551_x7964_x1576283983}[ACL]{lang="SV"}[、规则的类型以及统计的上下门限值。对于]{style="font-family:宋体"}**[per-destination]{lang="SV"}**[、]{style="font-family:宋体"}**[per-source]{lang="SV"}**[、]{style="font-family:宋体"}**[per-service]{lang="SV"}**[类型，可以在一条规则中单独指定其中之一或指定它们的组合。例如，同时指定]{style="font-family:宋体"}**[per-destination]{lang="SV"}**[和]{style="font-family:宋体"}**[per-source]{lang="SV"}**[，就表示同时按照连接的报文源地址和目的地址进行统计和限制，具有相同源和目的的连接属于同一类连接，该类连接的数目将受到指定的阈值的限制。对于]{style="font-family:宋体"}**[per-ds-lite-b4]{lang="SV"}**[类型，只能在一条规则中单独指定]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_37551_x7964_1477498277}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个连接数限制策略中的不同规则必须引用不同的]{style="font-family:宋体"}]{#struct_0_37551_x7964_455970728}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}**[per-destination]{lang="EN-US"}**]{#struct_0_37551_x7964_340910125}[、]{lang="EN-US" style="font-family:
宋体"}**[per-service]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[per-source]{lang="EN-US"}**[三个参数都不指定，则表示与本规则引用的]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[相匹配的所有连接将整体受到指定的阈值限制。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}**[per-ds-lite-b4]{lang="SV"}**]{#struct_0_37551_x7964_x41900547}[参数]{lang="EN-US" style="font-family:宋体"}[用于限制]{style="font-family:宋体"}[DS-Lite]{lang="SV" style="color:black"}[隧道每个]{lang="EN-US" style="font-family:
宋体;color:black"}[B4]{lang="SV"}[设备连接]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4]{lang="SV"}[用户连接数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[每个规则限制的]{style="font-family:宋体"}[B4]{lang="SV"}[设备由规则中]{lang="EN-US" style="font-family:宋体"}[指定的]{style="font-family:宋体"}[IPv6 ACL]{lang="SV"}[来匹配。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体;color:black"}]{#struct_0_37551_x7964_1487351687}[DS-Lite]{lang="SV" style="color:black"}[隧道组网环境中，若]{lang="EN-US" style="font-family:
宋体;color:black"}[AFTR]{lang="SV" style="color:black"}[设备上采用了]{lang="EN-US" style="font-family:宋体;color:black"}[Endpoint-Independent Mapping]{lang="SV"}[模式的]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="SV"}[配置]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[则要基于]{style="font-family:宋体"}[B4]{lang="SV"}[设备来限制从]{style="font-family:宋体"}[IPv4]{lang="SV"}[外网主动访问]{style="font-family:宋体"}[IPv4]{lang="SV"}[内网的连接]{style="font-family:宋体"}[，]{style="font-family:宋体"}[配置了]{style="font-family:宋体"}**[per-ds-lite-b4]{lang="SV"}**[类型]{lang="EN-US" style="font-family:宋体"}[规则的连接数限制策略必须应用在]{style="font-family:宋体"}[DS-Lite]{lang="SV" style="color:black"}[隧道接口上或者应用在全局。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对设备上建立的连接与某连接数限制策略进行匹配时，将按照规则编号从小到大的顺序依次遍历该策略中的所有规则，直到找到一条匹配的规则为止。]{style="font-family:宋体"}]{#struct_0_37551_x7964_167612393}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当引用的]{style="font-family:宋体"}]{#struct_0_37551_x7964_x468932221}[ACL]{lang="EN-US"}[内容发生改变时，设备将按照新的连接数限制策略重新对已有连接进行统计和限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_37551_x7964_497683165}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x2103998710}[在]{style="font-family:宋体"}[lPv4]{lang="EN-US"}[连接数限制策略]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建一条规则，规则编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，引用]{style="font-family:宋体"}[ACL 3000]{lang="EN-US"}[，对匹配]{style="font-family:宋体"}[ACL 3000]{lang="EN-US"}[的连接]{style="font-family:宋体"}[同时按照报文的源地址和目的地址进行统计和限制]{style="font-family:宋体;color:black"}[，连接数的上限值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[、下限值为]{style="font-family:宋体"}[1800]{lang="EN-US"}[。该规则用于限制]{style="font-family:宋体"}[192.168.0.0/24]{lang="EN-US"}[网段的每台主机最多只能同时向外网的同一个目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发起]{style="font-family:宋体"}[2000]{lang="EN-US"}[条连接，超过]{style="font-family:宋体"}[2000]{lang="EN-US"}[条时，需要等待连接数下降到]{style="font-family:宋体"}[1800]{lang="EN-US"}[以下之后，才允许新建连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_37551_x7964_x1614281359}

[[\[Sysname\] acl number 3000]{lang="EN-US"}]{#struct_0_37551_x7964_730708763}

[[\[Sysname-acl-adv-3000\] rule permit ip source 192.168.0.0 0.0.0.255]{lang="EN-US"}]{#struct_0_37551_x7964_x881366990}

[[\[Sysname-acl-adv-3000\] quit]{lang="EN-US"}]{#struct_0_37551_x7964_572141000}

[[\[Sysname\] connection-limit policy 1]{lang="EN-US"}]{#struct_0_37551_x7964_x687070369}

[\[Sysname-connlmt-policy-1\] limit 1 acl 3000 per-destination per-source amount 2000 1800]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_457393155}[在]{style="font-family:宋体"}[lPv6]{lang="EN-US"}[连接数限制策略]{style="font-family:宋体"}[12]{lang="EN-US"}[中创建一条规则，规则编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[，引用]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[，对匹配]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[的连接]{style="font-family:宋体"}[按照报文的目的地址进行统计和限制]{style="font-family:宋体;color:black"}[，连接数的上限值为]{style="font-family:宋体"}[200]{lang="EN-US"}[、下限值为]{style="font-family:宋体"}[100]{lang="EN-US"}[。该规则用于限制]{style="font-family:宋体"}[2:1::/96]{lang="EN-US"}[网段的主机最多只能同时向外网的同一个目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发起]{style="font-family:宋体"}[200]{lang="EN-US"}[条连接，超过]{style="font-family:宋体"}[200]{lang="EN-US"}[条时，需要等待连接数下降到]{style="font-family:宋体"}[100]{lang="EN-US"}[以下之后，才允许新建连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_37551_x7964_459188764}

[[\[Sysname\] acl ipv6 number 2001]{lang="EN-US"}]{#struct_0_37551_x7964_1632614104}

[[\[Sysname-acl6-basic-2001\] rule permit source 2:1::/96]{lang="EN-US"}]{#struct_0_37551_x7964_x2103933174}

[[\[Sysname-acl6-basic-2001\] quit]{lang="EN-US"}]{#struct_0_37551_x7964_1185843209}

[[\[Sysname\] connection-limit ipv6-policy 12]{lang="EN-US"}]{#struct_0_37551_x7964_763953615}

[[\[Sysname-connlmt-ipv6-policy-12\] limit 2 acl ipv6 2001 per-destination amount 200 100]{lang="EN-US"}]{#struct_0_37551_x7964_x1264709162}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_155519769}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection-limit]{lang="EN-US"}**]{#struct_0_37551_x7964_220263595}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display connection-limit]{lang="EN-US"}**]{#struct_0_37551_x7964_1151753911}
:::

::: {#-881516081 .myid}
[]{#_Toc404793574}[]{#struct_0_37551_x7964_1583269600}[]{#_Toc312690542}[]{#_Toc312690543}[]{#_Toc312690544}[]{#_Toc312690545}[]{#_Toc312690546}[]{#_Toc312690547}[]{#_Toc312690548}[]{#_Toc312690549}[]{#_Toc312690550}[]{#_Toc312690551}[]{#_Toc312690552}[]{#_Toc312690553}[]{#_Toc312690554}[]{#_Toc312690555}[]{#_Toc312690556}[]{#_Toc312690557}[]{#_Toc312690558}[]{#_Toc312690559}[]{#_Toc312690560}[]{#_Toc312690561}[]{#_Toc312690562}[]{#_Toc312690563}[]{#_Toc312690564}[]{#_Toc312690565}[]{#_Toc312690566}[]{#_Toc312690567}[]{#_Toc312690568}[]{#_Toc312690569}[]{#_Toc312690570}[]{#_Toc312690571}[]{#_Toc312690572}[]{#_Toc312690573}[]{#_Toc312690574}[]{#_Toc312690575}[]{#_Toc312690576}[]{#_Toc312690577}[]{#_Toc312690578}[]{#_Toc312690579}[]{#_Toc312690580}[]{#_Toc312690581}[]{#_Toc312690582}[]{#_Toc312690583}

**连接数限制 \-- 连接数限制配置命令 \-- reset connection-limit statistics**

------------------------------------------------------------------------

[**[reset connection-limit statistics]{lang="EN-US"}**]{#struct_0_37551_x7964_1038305142}[命令用来清除连接数限制在全局或接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x2104916214}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_37551_x7964_1216607113}

[**[reset connection-limit statistics ]{lang="EN-US"}**[{ **global** \| **interface** *interface-type interface-number  *}]{lang="EN-US"}]{#struct_0_37551_x7964_x2103215747}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_37551_x7964_x727291960}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[reset connection-limit statistics ]{lang="EN-US"}**[{ **global** \| **interface** *interface-type interface-number* } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_37551_x7964_2052093258}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_37551_x7964_1228454596}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[reset connection-limit statistics ]{lang="EN-US"}**[{ **global** \| **interface** *interface-type interface-number* } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_37551_x7964_x331783945}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x248424627}

[[用户视图]{style="font-family:宋体"}]{#struct_0_37551_x7964_975322852}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x617551952}

[[network-admin]{lang="EN-US"}]{#struct_0_37551_x7964_x2104850678}

[[network-operator]{lang="EN-US"}]{#struct_0_37551_x7964_1820279053}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37551_x7964_x1546760808}

[[mdc-operator]{lang="EN-US"}]{#struct_0_37551_x7964_x67356198}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1756983860}

[**[global]{lang="EN-US" style="color:black"}**]{#struct_0_37551_x7964_1816791133}[：清除全局的]{style="font-family:
宋体;color:black"}[连接数限制统计信息[。]{style="color:black"}]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_37551_x7964_1690931244}[：清除指定接口上的]{style="font-family:宋体;color:black"}[连接数限制统计信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号[。]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_37551_x7964_x224140562}[：清除指定单板上全局或全局接口应用的连接数限制统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定[清除全局的]{style="color:black"}连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_37551_x7964_x1635122993}[：清除指定成员设备上全局或全局接口应用的连接数限制统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。该参数仅在指定[清除全局的]{style="color:black"}连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_37551_x7964_x897109322}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上全局或全局接口应用的连接数限制统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。该参数仅在指定[清除全局的]{style="color:black"}连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_37551_x7964_x2104391929}[：清除指定成员设备的指定单板上全局或全局接口应用的连接数限制统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定[清除全局的]{style="color:black"}连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_37551_x7964_x410710995}[：清除指定单板上全局或全局接口应用的连接数限制统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。该参数仅在指定[清除全局的]{style="color:black"}连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_37551_x7964_303993073}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上全局或全局接口的连接数限制统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1587745697}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_1740332488}[清除接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的连接数限制统计信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> reset connection-limit statistics interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_37551_x7964_609245882}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_1685296590}[清除接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上的连接数限制统计信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> reset connection-limit statistics interface vlan-interface 2]{lang="EN-US"}]{#struct_0_37551_x7964_x1823252254}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_x388080369}[清除]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上全局应用的连接数限制统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> reset connection-limit statistics global slot 2]{lang="EN-US"}]{#struct_0_37551_x7964_702301188}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_1422561021}[清除]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备上全局应用的连接数限制统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> reset connection-limit statistics global slot 2]{lang="EN-US"}]{#struct_0_37551_x7964_x2104326393}

[[\# ]{lang="EN-US"}]{#struct_0_37551_x7964_451343626}[清除]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备上]{style="font-family:宋体"}[3]{lang="EN-US"}[号单板上全局应用的连接数限制统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> reset connection-limit statistics global chassis 1 slot 2]{lang="EN-US"}]{#struct_0_37551_x7964_2094520801}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_37551_x7964_x1980412849}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display connection-limit statistics]{lang="EN-US"}**]{#struct_0_37551_x7964_127130812}

[ ]{lang="EN-US"}
:::
