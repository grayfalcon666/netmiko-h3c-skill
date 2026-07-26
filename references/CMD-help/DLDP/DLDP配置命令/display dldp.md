::: {#673058815 .myid}
[]{#_Toc404795542}[]{#struct_0_x1288_x1726_90002508}[]{#_Toc107481926}

**DLDP \-- DLDP配置命令 \-- display dldp**

------------------------------------------------------------------------

[**[display dldp]{lang="EN-US"}**]{#struct_0_x1288_x1726_1817515287}[命令用来显示]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[的全局配置信息和接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_2061984347}

[**[display dldp ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1288_x1726_x256370582}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x343412176}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1288_x1726_375924765}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1811081961}

[[network-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_920610878}

[[network-operator]{lang="EN-US"}]{#struct_0_x1288_x1726_x341055821}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_x1802456421}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1288_x1726_826605303}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1144730843}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1288_x1726_x435595212}[：显示指定接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果未指定本参数，将显示]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[的全局配置信息和所有接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_1113889646}

[[\# ]{lang="EN-US"}]{#struct_0_x1288_x1726_x406965154}[显示]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[的全局配置信息和所有接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display dldp]{lang="EN-US"}]{#struct_0_x1288_x1726_x1811016425}

[ DLDP global status: Enabled]{lang="EN-US"}

[ DLDP advertisement interval: 5s]{lang="EN-US"}

[ DLDP authentication-mode: Simple]{lang="EN-US"}

[ DLDP authentication-password: \*\*\*\*\*\*]{lang="EN-US"}

[ DLDP unidirectional-shutdown mode: Auto]{lang="EN-US"}

[ DLDP delaydown-timer value: 1s]{lang="EN-US"}

[ Number of enabled ports: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface GigabitEthernet1/0/1]{lang="EN-US"}

[ DLDP port state: Bidirectional]{lang="EN-US"}

[ Number of the port's neighbors: 1]{lang="EN-US"}

[  Neighbor MAC address: 0023-8956-3600]{lang="EN-US"}

[  Neighbor port index: 79]{lang="EN-US"}

[  Neighbor state: Confirmed]{lang="EN-US"}

[  Neighbor aged time: 13s]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface GigabitEthernet1/0/2]{lang="EN-US"}

[ DLDP port state: Inactive]{lang="EN-US"}

[ Number of the port's neighbors: 0 (Maximum number ever detected: 1)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1288_x1726_66101278}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display dldp interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1288_x1726_x1810426601}

[Interface GigabitEthernet1/0/1]{lang="EN-US"}

[ DLDP port state: Bidirectional]{lang="EN-US"}

[ Number of the port's neighbors: 1]{lang="EN-US"}

[  Neighbor MAC address: 0023-8956-3600]{lang="EN-US"}

[  Neighbor port index: 79]{lang="EN-US"}

[  Neighbor state: Confirmed]{lang="EN-US"}

[  Neighbor aged time: 13s]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display dldp]{lang="EN-US"}]{#struct_0_x1288_x1726_198744004}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1725807460}[[字段]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x418679062}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x496041186}

[[DLDP global status]{lang="EN-US"}]{#struct_0_x1288_x1726_x845827938}

[[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_368560844}[的全局状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1288_x1726_x989541795}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1288_x1726_x1810361065}[：表示已关闭]{lang="EN-US" style="font-family:宋体"}

[[DLDP advertisement interval]{lang="EN-US"}]{#struct_0_x1288_x1726_1476322630}

[[Advertisement]{lang="EN-US"}]{#struct_0_x1288_x1726_x1560076701}[报文的发送间隔，单位为秒]{style="font-family:宋体"}

[[DLDP authentication-mode]{lang="EN-US"}]{#struct_0_x1288_x1726_x1110598708}

[[当前设备与邻居设备间的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_x1930862580}[认证模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MD5]{lang="EN-US"}]{#struct_0_x1288_x1726_1257808259}[：表示]{lang="EN-US" style="font-family:宋体"}[MD5]{lang="EN-US"}[认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_x1288_x1726_1611778276}[：表示不认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Simple]{lang="EN-US"}]{#struct_0_x1288_x1726_x1810950888}[：表示明文认证]{lang="EN-US" style="font-family:宋体"}

[[DLDP authentication-password]{lang="EN-US"}]{#struct_0_x1288_x1726_2033659630}

[[当前设备与邻居设备间的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_x473024232}[认证密码：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\*\*\*\*\*\*]{lang="EN-US"}]{#struct_0_x1288_x1726_x1678060536}[：表示已配置密码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not configured]{lang="EN-US"}]{#struct_0_x1288_x1726_1305940743}[：表示已配置认证模式但尚未配置密码]{lang="EN-US" style="font-family:宋体"}

[[DLDP unidirectional-shutdown mode]{lang="EN-US"}]{#struct_0_x1288_x1726_x1810885352}

[[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_1035781558}[发现单向链路后接口的关闭模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auto]{lang="EN-US"}]{#struct_0_x1288_x1726_1771085860}[：表示自动模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Manual]{lang="EN-US"}]{#struct_0_x1288_x1726_x1857776931}[：表示手动模式]{lang="EN-US" style="font-family:宋体"}

[[DLDP delaydown-timer value]{lang="EN-US"}]{#struct_0_x1288_x1726_1662286648}

[[DelayDown]{lang="EN-US"}]{#struct_0_x1288_x1726_x1810819816}[定时器的超时时间，单位为秒]{style="font-family:宋体"}

[[Number of enabled ports]{lang="EN-US"}]{#struct_0_x1288_x1726_1389511144}

[[使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_x69670042}[的接口数]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1288_x1726_154412613}

[[使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_2076608533}[的接口名称]{style="font-family:宋体"}

[[DLDP port state]{lang="EN-US"}]{#struct_0_x1288_x1726_x1810754280}

[[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_x2069001696}[接口的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bidirectional]{lang="EN-US"}]{#struct_0_x1288_x1726_x467511317}[：表示双通状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x1288_x1726_x84240959}[：表示非活动状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initial]{lang="EN-US"}]{#struct_0_x1288_x1726_20392648}[：表示初始状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unidirectional]{lang="EN-US"}]{#struct_0_x1288_x1726_x1811213032}[：表示单通状态]{lang="EN-US" style="font-family:宋体"}

[[Number of the port's neighbors]{lang="EN-US"}]{#struct_0_x1288_x1726_x1896999747}

[[接口的邻居数]{style="font-family:宋体"}]{#struct_0_x1288_x1726_2101573594}

[[Maximum number ever detected]{lang="EN-US"}]{#struct_0_x1288_x1726_x1519410456}

[[接口曾收到的最大邻居数（只有在接口的当前邻居数与其曾收到的最大邻居数不一致时，才会显示本字段）]{style="font-family:宋体"}]{#struct_0_x1288_x1726_x1811147496}

[[Neighbor MAC address]{lang="EN-US"}]{#struct_0_x1288_x1726_x15244062}

[[邻居的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1288_x1726_x142282101}[地址]{style="font-family:宋体"}

[[Neighbor port index]{lang="EN-US"}]{#struct_0_x1288_x1726_106506102}

[[邻居的接口索引]{style="font-family:宋体"}]{#struct_0_x1288_x1726_x1811081960}

[[Neighbor state]{lang="EN-US"}]{#struct_0_x1288_x1726_x645473063}

[[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_1358470328}[邻居的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Confirmed]{lang="EN-US"}]{#struct_0_x1288_x1726_x1098439537}[：表示确定状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unconfirmed]{lang="EN-US"}]{#struct_0_x1288_x1726_x1811016424}[：表示未确定状态]{lang="EN-US" style="font-family:宋体"}

[[Neighbor aged time]{lang="EN-US"}]{#struct_0_x1288_x1726_1632185219}

[[邻居的老化时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x1288_x1726_x85602829}

[ ]{lang="EN-US"}

::: {#-1173018129 .myid}
[]{#_Toc404795543}[]{#struct_0_x1288_x1726_x2064935308}

**DLDP \-- DLDP配置命令 \-- display dldp statistics**

------------------------------------------------------------------------

[**[display dldp statistics]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1810426600}[命令用来显示接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1367339937}

[**[display dldp statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1288_x1726_1388033847}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_1847263963}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1288_x1726_1718669183}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_1468609831}

[[network-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_x669506742}

[[network-operator]{lang="EN-US"}]{#struct_0_x1288_x1726_1132321994}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_x1381326692}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1288_x1726_x1810361064}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x89761311}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1288_x1726_x829503339}[：显示指定接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[报文统计信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果未指定本参数，将显示所有接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x506044663}

[[\# ]{lang="EN-US"}]{#struct_0_x1288_x1726_x1051147545}[显示所有接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[]{#_Toc148329745}[[\<Sysname\> display dldp statistics]{lang="EN-US"}]{#struct_0_x1288_x1726_x1810950891}

[Interface GigabitEthernet1/0/1]{lang="EN-US"}

[ Packets sent: 6]{lang="EN-US"}

[ Packets received: 5]{lang="EN-US"}

[ Invalid packets received: 2]{lang="EN-US"}

[ Loopback packets received: 0]{lang="EN-US"}

[ Authentication-failed packets received: 0]{lang="EN-US"}

[ Valid packets received: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface GigabitEthernet1/0/2]{lang="EN-US"}

[ Packets sent: 7]{lang="EN-US"}

[ Packets received: 7]{lang="EN-US"}

[ Invalid packets received: 3]{lang="EN-US"}

[ Loopback packets received: 0]{lang="EN-US"}

[ Authentication-failed packets received: 0]{lang="EN-US"}

[ Valid packets received: 4]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display dldp statistics]{lang="EN-US"}]{#struct_0_x1288_x1726_111279793}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1695785470}[[字段]{style="font-family:黑体"}]{#struct_0_x1288_x1726_37124450}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1288_x1726_200954619}

[[Interface]{lang="EN-US"}]{#struct_0_x1288_x1726_452329657}

[[使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_1264334305}[的接口名称]{style="font-family:宋体"}

[[Packets sent]{lang="EN-US"}]{#struct_0_x1288_x1726_x1010555301}

[[发送的报文总数]{style="font-family:宋体"}]{#struct_0_x1288_x1726_x1810885355}

[[Packets received]{lang="EN-US"}]{#struct_0_x1288_x1726_x886532743}

[[收到的报文总数]{style="font-family:宋体"}]{#struct_0_x1288_x1726_1337416601}

[[Invalid packets received]{lang="EN-US"}]{#struct_0_x1288_x1726_x605213855}

[[收到的错误报文数]{style="font-family:宋体"}]{#struct_0_x1288_x1726_380402721}

[[Loopback packets received]{lang="EN-US"}]{#struct_0_x1288_x1726_x301237960}

[[收到的自环报文数]{style="font-family:宋体"}]{#struct_0_x1288_x1726_x100970869}

[[Authentication-failed packets received]{lang="EN-US"}]{#struct_0_x1288_x1726_x1810819819}

[[收到的认证失败报文数]{style="font-family:宋体"}]{#struct_0_x1288_x1726_x1339372211}

[[Valid packets received]{lang="EN-US"}]{#struct_0_x1288_x1726_132665467}

[[收到的合法报文数]{style="font-family:宋体"}]{#struct_0_x1288_x1726_x1552195285}

[[ ]{lang="EN-US"}]{#_Toc107481928}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1935783211}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}[ dldp statistics]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1626776968}

::: {#-273564874 .myid}
[]{#_Toc404795544}[]{#struct_0_x1288_x1726_x1264829677}

**DLDP \-- DLDP配置命令 \-- dldp authentication-mode**

------------------------------------------------------------------------

[**[dldp authentication-mode]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1810754283}[命令用来配置当前设备与邻居设备间的]{style="font-family:
宋体"}[DLDP]{lang="EN-US"}[认证模式。]{style="font-family:
宋体"}

[**[undo dldp authentication-mode]{lang="EN-US"}**]{#struct_0_x1288_x1726_x502917755}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_773410706}

[**[dldp authentication-mode]{lang="EN-US"}**[ { **md5** \| **none** \| **simple** }]{lang="EN-US"}]{#struct_0_x1288_x1726_773889446}

[**[undo dldp authentication-mode]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1838667214}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x113091765}

[[当前设备与邻居设备间的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_1186815260}[认证模式为不认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x557138569}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1288_x1726_x1462724901}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1811213035}

[[network-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_x330915806}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_2123013105}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_1561101616}

[**[md5]{lang="EN-US"}**]{#struct_0_x1288_x1726_1242482758}[：表示认证模式为]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_x1288_x1726_x208315881}[：表示认证模式为不认证。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1294845936}[：表示认证模式为明文认证。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_376469146}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请确保两台设备间通过光纤]{style="font-family:宋体"}]{#struct_0_x1288_x1726_2010693676}[/]{lang="EN-US"}[网线连接的接口上配置的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[认证模式和认证密码都相同，否则]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[将无法正常工作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置认证模式为明文认证或]{style="font-family:宋体"}]{#struct_0_x1288_x1726_x1811147499}[MD5]{lang="EN-US"}[认证后若未配置认证密码，则认证模式将仍为不认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1581328003}

[[\# ]{lang="EN-US"}]{#struct_0_x1288_x1726_349639154}[配置]{style="font-family:宋体"}[Device A]{lang="EN-US"}[和]{style="font-family:宋体"}[Device B]{lang="EN-US"}[通过光纤]{style="font-family:宋体"}[/]{lang="EN-US"}[网线连接的接口间的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[认证模式均为明文认证，认证密码均为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[Device A]{lang="FR"}]{#struct_0_x1288_x1726_x108209365}[上的配置]{lang="EN-US" style="font-family:宋体"}[：]{lang="EN-US" style="font-family:宋体"}

[[\<DeviceA\> system-view]{lang="EN-US"}]{#struct_0_x1288_x1726_1392970285}

[\[DeviceA\] dldp authentication-mode simple]{lang="EN-US"}

[\[DeviceA\] dldp authentication-password simple abc]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[Device B]{lang="FR"}]{#struct_0_x1288_x1726_x686467186}[上的配置]{lang="EN-US" style="font-family:宋体"}[：]{lang="EN-US" style="font-family:宋体"}

[[\<DeviceB\> system-view]{lang="EN-US"}]{#struct_0_x1288_x1726_37397186}

[\[DeviceB\] dldp authentication-mode simple]{lang="EN-US"}

[\[DeviceB\] dldp authentication-password simple abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x2081314313}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dldp]{lang="EN-US"}**]{#struct_0_x1288_x1726_x793946065}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dldp authentication-password]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1811081963}
:::

::: {#205826797 .myid}
[]{#_Toc404795545}[]{#struct_0_x1288_x1726_2083410292}

**DLDP \-- DLDP配置命令 \-- dldp authentication-password**

------------------------------------------------------------------------

[**[dldp authentication-password]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1618646162}[命令用来配置当前设备与邻居设备间的]{style="font-family:
宋体"}[DLDP]{lang="EN-US"}[认证密码。]{style="font-family:
宋体"}

[**[undo dldp authentication-password]{lang="EN-US"}**]{#struct_0_x1288_x1726_372441582}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x2061578738}

[**[dldp authentication-password]{lang="EN-US"}**[ { **cipher** *cipher* \| **simple** *simple* }]{lang="EN-US"}]{#struct_0_x1288_x1726_1990896767}

[**[undo dldp authentication-password]{lang="EN-US"}**]{#struct_0_x1288_x1726_1677541601}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_1498333128}

[[没有配置当前设备与邻居设备间的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_x1425147135}[认证密码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1811016427}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1288_x1726_x1096698136}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_34427333}

[[network-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_x1261387969}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_x936954683}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_382144660}

[**[cipher]{lang="EN-US"}**[ *cipher*]{lang="EN-US"}]{#struct_0_x1288_x1726_x1098956116}[：表示以密文方式输入的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[认证密码。]{style="font-family:宋体"}*[cipher]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[53]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**[ *simple*]{lang="EN-US"}]{#struct_0_x1288_x1726_x2020354317}[：表示以明文方式输入的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[认证密码。]{style="font-family:宋体"}*[simple]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[16]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x2083435992}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的]{style="font-family:宋体"}]{#struct_0_x1288_x1726_x1810426603}[DLDP]{lang="EN-US"}[认证密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请确保两台设备间通过光纤]{style="font-family:宋体"}]{#struct_0_x1288_x1726_x964055410}[/]{lang="EN-US"}[网线连接的接口上配置的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[认证模式和认证密码都相同，否则]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[将无法正常工作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置认证模式为明文认证或]{style="font-family:宋体"}]{#struct_0_x1288_x1726_948463462}[MD5]{lang="EN-US"}[认证后若未配置认证密码，则认证模式将仍为不认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_666527554}

[[\# ]{lang="EN-US"}]{#struct_0_x1288_x1726_x1303544561}[配置]{style="font-family:宋体"}[Device A]{lang="EN-US"}[和]{style="font-family:宋体"}[Device B]{lang="EN-US"}[通过光纤]{style="font-family:宋体"}[/]{lang="EN-US"}[网线连接的接口间的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[认证模式均为明文认证，认证密码均为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[Device A]{lang="FR"}]{#struct_0_x1288_x1726_x1507718601}[上的配置]{lang="EN-US" style="font-family:宋体"}[：]{lang="EN-US" style="font-family:宋体"}

[[\<DeviceA\> system-view]{lang="EN-US"}]{#struct_0_x1288_x1726_x430936347}

[\[DeviceA\] dldp authentication-mode simple]{lang="EN-US"}

[\[DeviceA\] dldp authentication-password simple abc]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[Device B]{lang="FR"}]{#struct_0_x1288_x1726_977533374}[上的配置]{lang="EN-US" style="font-family:宋体"}[：]{lang="EN-US" style="font-family:宋体"}

[[\<DeviceB\> system-view]{lang="FR"}]{#struct_0_x1288_x1726_x1810361067}

[\[DeviceB\] dldp authentication-mode simple]{lang="FR"}

[\[DeviceB\] dldp authentication-password ]{lang="FR"}[simple]{lang="EN-US"}[ ]{lang="EN-US"}[abc]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_313523216}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dldp]{lang="EN-US"}**]{#struct_0_x1288_x1726_409138571}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dldp authentication-mode]{lang="EN-US"}**]{#struct_0_x1288_x1726_952017243}
:::

::: {#-268472010 .myid}
[]{#_Toc404795546}[]{#struct_0_x1288_x1726_x917226753}

**DLDP \-- DLDP配置命令 \-- dldp delaydown-timer**

------------------------------------------------------------------------

[**[dldp delaydown-timer]{lang="EN-US"}**]{#struct_0_x1288_x1726_313178924}[命令用来配置]{style="font-family:宋体"}[DelayDown]{lang="EN-US"}[定时器的超时时间。]{style="font-family:宋体"}

[**[undo dldp delaydown-timer]{lang="EN-US"}**]{#struct_0_x1288_x1726_x960348931}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x660177906}

[**[dldp delaydown-timer]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x1288_x1726_921784573}

[**[undo dldp delaydown-timer]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1697611385}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1810950890}

[[DelayDown]{lang="EN-US"}]{#struct_0_x1288_x1726_1677363734}[定时器的超时时间为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_327133633}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1288_x1726_2088232901}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_1814135161}

[[network-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_x567975207}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_83519663}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x584885630}

[*[time]{lang="EN-US"}*]{#struct_0_x1288_x1726_x1127641993}[：表示]{style="font-family:宋体"}[DelayDown]{lang="EN-US"}[定时器的超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[5]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1810885354}

[[本配置将应用于所有使能了]{style="font-family:宋体"}[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_1842350612}[功能的接口上。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x731364358}

[[\# ]{lang="EN-US"}]{#struct_0_x1288_x1726_615452640}[配置]{style="font-family:宋体"}[DelayDown]{lang="EN-US"}[定时器的超时时间为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1288_x1726_2092059429}

[\[Sysname\] dldp delaydown-timer 2]{lang="EN-US"}

[]{#_Toc107481927}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x280415557}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dldp]{lang="EN-US"}**]{#struct_0_x1288_x1726_x97285132}
:::

::: {#-928954876 .myid}
[]{#_Toc107481929}[]{#_Toc404795547}[]{#struct_0_x1288_x1726_449416810}

**DLDP \-- DLDP配置命令 \-- dldp enable**

------------------------------------------------------------------------

[**[dldp enable]{lang="EN-US"}**]{#struct_0_x1288_x1726_1251450481}[命令用来在接口上使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo dldp enable]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1810819818}[命令用来在接口上关闭]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_226711730}

[**[dldp enable]{lang="EN-US"}**]{#struct_0_x1288_x1726_x747473113}

[**[undo dldp enable]{lang="EN-US"}**]{#struct_0_x1288_x1726_x950494029}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1827332065}

[[接口上的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_x44527406}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_1896693306}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1288_x1726_x830604646}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_1794117741}

[[network-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_x1810754282}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_1063166186}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_796004167}

[[要启用]{style="font-family:宋体"}[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_469610210}[功能，必须在全局和接口上都使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_565598738}

[[\# ]{lang="EN-US"}]{#struct_0_x1288_x1726_1481106112}[全局使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能，并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1288_x1726_1331323018}

[\[Sysname\] dldp global enable]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dldp enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x662205990}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dldp]{lang="EN-US"}**]{#struct_0_x1288_x1726_15951777}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dldp global enable]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1811213034}
:::

::: {#1081430494 .myid}
[]{#_Toc404795548}[]{#struct_0_x1288_x1726_1235168135}

**DLDP \-- DLDP配置命令 \-- dldp global enable**

------------------------------------------------------------------------

[**[dldp global enable]{lang="EN-US"}**]{#struct_0_x1288_x1726_x334054957}[命令用来全局使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo dldp global enable]{lang="EN-US"}**]{#struct_0_x1288_x1726_x854716610}[命令用来全局关闭]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1874839797}

[**[dldp global enable]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1698822833}

[**[undo dldp global enable]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1295233070}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_293661659}

[[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_x788258913}[功能处于全局关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1811147498}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1288_x1726_1147555352}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x2065111713}

[[network-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_1836508156}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_175028557}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_384491086}

[[要启用]{style="font-family:宋体"}[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_x1603126733}[功能，必须在全局和接口上都使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_682249964}

[[\# ]{lang="EN-US"}]{#struct_0_x1288_x1726_x1634128050}[全局使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1288_x1726_x1811081962}

[\[Sysname\] dldp global enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_517326351}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dldp]{lang="EN-US"}**]{#struct_0_x1288_x1726_1900976351}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dldp enable]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1435890690}
:::

::: {#-846709120 .myid}
[]{#_Toc404795549}[]{#struct_0_x1288_x1726_x1347578091}

**DLDP \-- DLDP配置命令 \-- dldp interval**

------------------------------------------------------------------------

[**[dldp interval]{lang="EN-US"}**]{#struct_0_x1288_x1726_1067929659}[命令用来配置]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文的发送间隔。]{style="font-family:宋体"}

[**[undo dldp interval]{lang="EN-US"}**]{#struct_0_x1288_x1726_1415651949}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x503148476}

[**[dldp interval ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_x1288_x1726_1140757939}

[**[undo dldp interval]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1811016426}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_469385805}

[[Advertisement]{lang="EN-US"}]{#struct_0_x1288_x1726_x707224220}[报文的发送间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1952136407}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1288_x1726_x275192193}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x106894549}

[[network-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_1158857806}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_977400780}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x963864171}

[*[time]{lang="EN-US"}*]{#struct_0_x1288_x1726_x72289231}[：表示]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文的发送间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1810426602}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本配置将应用于所有使能了]{style="font-family:宋体"}]{#struct_0_x1288_x1726_1764827945}[DLDP]{lang="EN-US"}[功能的接口上。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请确保通过光纤]{style="font-family:宋体"}]{#struct_0_x1288_x1726_1232765700}[/]{lang="EN-US"}[网线连接的两台设备上]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文的发送间隔相同，否则]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[将无法正常工作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_1793707443}

[[\# ]{lang="EN-US"}]{#struct_0_x1288_x1726_x1369649950}[配置]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文的发送间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1288_x1726_x354481407}

[\[Sysname\] dldp interval 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1604157970}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dldp]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1178827261}
:::

::: {#1890490380 .myid}
[]{#_Toc404795550}[]{#struct_0_x1288_x1726_1745328062}

**DLDP \-- DLDP配置命令 \-- dldp unidirectional-shutdown**

------------------------------------------------------------------------

[**[dldp unidirectional-shutdown]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1810361066}[命令用来配置]{style="font-family:
宋体"}[DLDP]{lang="EN-US"}[发现单向链路后接口的关闭模式。]{style="font-family:宋体"}

[**[undo dldp unidirectional-shutdown]{lang="EN-US"}**]{#struct_0_x1288_x1726_x1252560725}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1407077516}

[**[dldp unidirectional-shutdown]{lang="EN-US"}**[ { **auto** \| **manual** }]{lang="EN-US"}]{#struct_0_x1288_x1726_1227805122}

[**[undo]{lang="EN-US"}**[ **dldp unidirectional-shutdown**]{lang="EN-US"}]{#struct_0_x1288_x1726_x1318398711}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x722427801}

[[DLDP]{lang="EN-US"}]{#struct_0_x1288_x1726_x1165521732}[发现单向链路后接口的关闭模式为自动模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_170718445}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1288_x1726_1978988089}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1810950893}

[[network-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_x1051519621}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_x181089083}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_643306433}

[**[auto]{lang="EN-US"}**]{#struct_0_x1288_x1726_492053805}[：表示自动模式。在此模式下，当]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[检测到单向链路时会自动关闭单通接口。]{style="font-family:宋体"}

[**[manual]{lang="EN-US"}**]{#struct_0_x1288_x1726_x180567077}[：表示手动模式。在此模式下，当]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[检测到单向链路时不会直接关闭单通接口，而是需要用户手工将其关闭；当单向链路恢复为双向链路后，还需要用户手工将其打开。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_1391829663}

[[\# ]{lang="EN-US"}]{#struct_0_x1288_x1726_272383544}[配置]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[发现单向链路后接口的关闭模式为手动模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1288_x1726_744343585}

[\[Sysname\] dldp unidirectional-shutdown manual]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x1810885357}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dldp]{lang="EN-US"}**]{#struct_0_x1288_x1726_276266671}
:::

::: {#-1672584776 .myid}
[]{#_Toc404795551}[]{#struct_0_x1288_x1726_x629013715}

**DLDP \-- DLDP配置命令 \-- reset dldp statistics**

------------------------------------------------------------------------

[**[reset dldp statistics]{lang="EN-US"}**]{#struct_0_x1288_x1726_2097897029}[命令用来清除接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x979714111}

[**[reset dldp statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1288_x1726_x1923427057}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_290103524}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1288_x1726_1671388788}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_1460965449}

[[network-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_x1679320656}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1288_x1726_x1810819821}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_x983338459}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1288_x1726_x533487690}[：清除指定接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[报文统计信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果未指定本参数，将清除所有接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_1794737354}

[[\# ]{lang="EN-US"}]{#struct_0_x1288_x1726_x704852767}[清除所有接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<]{lang="EN-US"}]{#struct_0_x1288_x1726_896927917}[Sysname]{lang="FR"}[\> reset dldp statistics]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1288_x1726_1109343577}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dldp statistics]{lang="EN-US"}**]{#struct_0_x1288_x1726_x116019343}
:::
