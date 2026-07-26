::: {#1693794782 .myid}
[]{#_Toc404792569}[]{#struct_0_77048_16369_222679818}[]{#_Toc257814917}

**MAC地址认证 \-- MAC地址认证配置命令 \-- display mac-authentication**

------------------------------------------------------------------------

[**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_x440307652}[命令用来显示]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址认证的相关信息，主要包括全局及端口的配置信息、认证报文统计信息以及认证用户信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_992725483}

[**[display mac-authentication]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **ap** *ap-name* \[ **radio** *radio-id* \] \| **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_77048_16369_241336123}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1585216665}

[[任意视图]{style="font-family:宋体"}]{#struct_0_77048_16369_644038931}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_x669565152}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_x1201510354}

[[network-operator]{lang="EN-US"}]{#struct_0_77048_16369_x383799828}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_x765717294}

[[mdc-operator]{lang="EN-US"}]{#struct_0_77048_16369_1587696042}

[[【参数】]{style="font-family:黑体"}]{#struct_0_77048_16369_x52731807}

[**[ap]{lang="EN-US"}**[ *ap-name*]{lang="EN-US"}]{#struct_0_77048_16369_1754639909}[：显示指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的详细信息，]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[radio]{lang="EN-US"}**[ *radio-id*]{lang="EN-US"}]{#struct_0_77048_16369_x1482140405}[：显示指定]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的所有的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的详细信息，]{style="font-family:宋体"}*[radio-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Radio]{lang="EN-US"}[编号，取值范围与设备型号有关。如果不指定该参数，则显示指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_77048_16369_x439848900}[：显示全局及指定端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证相关信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。若指定的端口上未使能]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证，则不显示该端口任何信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_77048_16369_1931708399}

[[如果不指定任何参数，则显示所有在线]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x53626485}[地址认证的详细信息，先显示有线]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的信息，再显示无线]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_1234112385}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x308543958}[显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证信息。]{style="font-family:宋体"}

[[\<Sysname\> display mac-authentication]{lang="EN-US"}]{#struct_0_77048_16369_x439914436}

[Global MAC authentication parameters:]{lang="EN-US"}

[   MAC authentication     : Enabled]{lang="EN-US"}

[   Username format        : MAC address in lowercase(xxxxxxxxxxxx)]{lang="EN-US"}

[           Username       : mac]{lang="EN-US"}

[           Password       : Not configured]{lang="EN-US"}

[   Offline detect period  : 300 s]{lang="EN-US"}

[   Quiet period           : 60 s]{lang="EN-US"}

[   Server timeout         : 100 s]{lang="EN-US"}

[   Authentication domain  : Not configured, use default domain]{lang="EN-US"}

[ Max MAC-auth users       : 1024 per slot]{lang="EN-US"}

[Online MAC-auth wired users    : 1]{lang="EN-US"}

[ Online MAC-auth wireless users : 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Silent MAC users:]{lang="EN-US"}

[          MAC address       VLAN ID  From port               Port index]{lang="EN-US"}

[          0001-0000-0001    100      GigabitEthernet1/0/2    21]{lang="EN-US"}

[          0001-0000-0002    2        GigabitEthernet1/0/3    20]{lang="EN-US"}

[          0001-0000-0002    12       GigabitEthernet1/0/4    301]{lang="EN-US"}

[ ]{lang="EN-US"}

[ GigabitEthernet1/0/1  is link-up]{lang="EN-US"}

[   MAC authentication         : Enabled]{lang="EN-US"}

[   Authentication domain      : Not configured]{lang="EN-US"}

[   Auth-delay timer           : Enabled]{lang="EN-US"}

[       Auth-delay period      : 60 s]{lang="EN-US"}

[   Re-auth server-unreachable : Logoff]{lang="EN-US"}

[   Guest VLAN                 : 100]{lang="EN-US"}

[   Critical VLAN              : Not configured]{lang="EN-US"}

[   Host mode                  : Multiple VLAN]{lang="EN-US"}

[   Max online users           : 256]{lang="EN-US"}

[   Authentication attempts    : successful 2, failed 3]{lang="EN-US"}

[   Current online users       : 1]{lang="EN-US"}

[          MAC address       Auth state]{lang="EN-US"}

[          0001-0000-0001    Unauthenticated]{lang="EN-US"}

[ ]{lang="EN-US"}

[AP name: AP1  Radio ID: 1  SSID: wlan_maca_ssid]{lang="EN-US"}

[   BSSID                      : 1111-1111-1111]{lang="EN-US"}

[MAC authentication         : Enabled]{lang="EN-US"}

[   Authentication domain      : Not configured]{lang="EN-US"}

[   Max online users           : 256]{lang="EN-US"}

[   Authentication attempts    : successful 1, failed 0]{lang="EN-US"}

[   Current online users       : 2]{lang="EN-US"}

[          MAC address       Auth state]{lang="EN-US"}

[          0001-0000-0002    Authenticated]{lang="EN-US"}

[          0001-0000-0003    Unauthenticated]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display mac-authentication]{lang="EN-US"}]{#struct_0_77048_16369_x715779957}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1639592029}[[字段]{style="font-family:黑体"}]{#struct_0_77048_16369_x523042049}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_77048_16369_899738021}

[[Global MAC authentication parameters]{lang="EN-US"}]{#struct_0_77048_16369_566944952}

[[全局]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_567010488}[地址认证参数]{style="font-family:宋体"}

[[MAC authentication]{lang="EN-US"}]{#struct_0_77048_16369_528904854}

[[MAC]{lang="EN-US"}]{#struct_0_77048_16369_580108690}[地址认证的开启状态]{style="font-family:宋体"}

[[该功能的生效情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_77048_16369_x1950745572}

[[Username format]{lang="EN-US"}]{#struct_0_77048_16369_1125710756}

[[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x915590268}[地址认证使用的用户名格式，有以下两种情况：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若采用]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x1530080640}[地址形式，则显示具体的用户名格式以及是否带连字符、字母是否大小写，例如本例中"]{lang="EN-US" style="font-family:宋体"}[MAC address in lowercase]{lang="EN-US"}[(]{lang="EN-US"}[xxxxxxxxxxxx]{lang="EN-US"}[)]{lang="EN-US"}["，它表示用户名格式为不带连字符的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，其中字母为小写]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若采用固定用户名格式，则显示"]{lang="EN-US" style="font-family:宋体"}[Fixed account]{lang="EN-US"}]{#struct_0_77048_16369_1741471148}["]{lang="EN-US" style="font-family:宋体"}

[[Username:]{lang="EN-US"}]{#struct_0_77048_16369_x591611928}

[[用户名]{style="font-family:宋体"}]{#struct_0_77048_16369_1293726153}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用]{style="font-family:宋体"}]{#struct_0_77048_16369_1125645220}[MAC]{lang="EN-US"}[地址格式时，该值显示为"]{style="font-family:宋体"}[mac]{lang="EN-US"}["，无实际意义，仅表示采用]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为用户名和密码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用固定用户名格式时，该值为配置的用户名（缺省为]{style="font-family:宋体"}]{#struct_0_77048_16369_1058985419}[mac]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Password:]{lang="EN-US"}]{#struct_0_77048_16369_54254820}

[[用户名的密码]{style="font-family:宋体"}]{#struct_0_77048_16369_1242959065}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_2089180196}[地址格式时，该值显示为"]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[ot configured]{lang="EN-US"}["]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用固定用户名格式时，配置的值将显示为]{style="font-family:宋体"}]{#struct_0_77048_16369_1838377623}[\*\*\*\*\*\*]{lang="EN-US"}

[[Offline detect period]{lang="EN-US"}]{#struct_0_77048_16369_1624749935}

[[下线检测定时器的值]{style="font-family:宋体"}]{#struct_0_77048_16369_1125579684}

[[Quiet period]{lang="EN-US"}]{#struct_0_77048_16369_208227512}

[[静默定时器的值]{style="font-family:宋体"}]{#struct_0_77048_16369_1065791924}

[[Server timeout]{lang="EN-US"}]{#struct_0_77048_16369_x1231566840}

[[服务器连接超时定时器的值]{style="font-family:宋体"}]{#struct_0_77048_16369_x759259960}

[[Authentication domain]{lang="EN-US"}]{#struct_0_77048_16369_567403704}

[[系统视图下指定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_781740805}[地址认证用户使用的认证域]{style="font-family:宋体"}

[[Max MAC-auth users]{lang="EN-US"}]{#struct_0_77048_16369_x1453579747}

[[每单板能够支持的最大]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_1125514148}[地址认证用户数]{style="font-family:宋体"}

[[Online MAC-auth wired users]{lang="EN-US"}]{#struct_0_77048_16369_x94150451}

[[在线有线用户数]{style="font-family:宋体"}]{#struct_0_77048_16369_x1171243324}

[[Online MAC-auth wireless users]{lang="EN-US"}]{#struct_0_77048_16369_188555968}

[[在线无线用户数]{style="font-family:宋体"}]{#struct_0_77048_16369_x1249818982}

[[Silent MAC users]{lang="EN-US"}]{#struct_0_77048_16369_1125972900}

[[静默用户信息]{style="font-family:宋体"}]{#struct_0_77048_16369_1861098479}

[[MAC address]{lang="EN-US"}]{#struct_0_77048_16369_x1210667271}

[[静默用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_1240868822}[地址]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_77048_16369_163594892}

[[静默用户所在的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_77048_16369_x2138720051}

[[From port]{lang="EN-US"}]{#struct_0_77048_16369_1125907364}

[[静默用户接入的端口名称]{style="font-family:宋体"}]{#struct_0_77048_16369_x107954656}

[[Port index]{lang="EN-US"}]{#struct_0_77048_16369_1995555888}

[[静默用户接入的端口索引号]{style="font-family:宋体"}]{#struct_0_77048_16369_x1314671133}

[[GigabitEthernet1/0/1 is link-up]{lang="EN-US"}]{#struct_0_77048_16369_912734541}

[[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_77048_16369_1125841828}[的链路状态]{style="font-family:宋体"}

[[MAC authentication]{lang="EN-US"}]{#struct_0_77048_16369_1473423221}

[[当前端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x1274959584}[地址认证开启状态]{style="font-family:宋体"}

[[Authentication domain]{lang="EN-US"}]{#struct_0_77048_16369_163463820}

[[端口上指定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_560773552}[地址认证用户使用的认证域]{style="font-family:宋体"}

[[Auth-delay timer]{lang="EN-US"}]{#struct_0_77048_16369_x1726784879}

[[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x1789612747}[地址认证延迟功能的开启状态]{style="font-family:宋体"}

[[Auth-delay period]{lang="EN-US"}]{#struct_0_77048_16369_163791500}

[[配置的认证延迟时间]{style="font-family:宋体"}]{#struct_0_77048_16369_874826988}

[[Re-auth server-unreachable]{lang="EN-US"}]{#struct_0_77048_16369_x43288805}

[[重认证时服务器不可达对]{style="font-family:宋体"}[MACA]{lang="EN-US"}]{#struct_0_77048_16369_794265578}[地址认证的在线用户采取的动作]{style="font-family:宋体"}

[[Guest VLAN]{lang="EN-US"}]{#struct_0_77048_16369_163857036}

[[端口配置的]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}]{#struct_0_77048_16369_x877259659}

[[Critical VLAN]{lang="EN-US"}]{#struct_0_77048_16369_2055465061}

[[端口配置的]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}]{#struct_0_77048_16369_740872715}

[[Host mode]{lang="EN-US"}]{#struct_0_77048_16369_1339382730}

[[相同]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_733609591}[地址用户的工作模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Single VLAN]{lang="EN-US"}]{#struct_0_77048_16369_954184845}[：不允许相同]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址用户在属于不同]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的相同接口再次接入]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Multiple VLAN]{lang="EN-US"}]{#struct_0_77048_16369_x1224276158}[：允许相同]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址用户在属于不同]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的相同接口再次接入]{lang="EN-US" style="font-family:宋体"}

[[Max online users]{lang="EN-US"}]{#struct_0_77048_16369_x1843634614}

[[本端口最多可容纳的接入用户数]{style="font-family:宋体"}]{#struct_0_77048_16369_1125776292}

[[Authentication attempts: successful 1, failed 0]{lang="EN-US"}]{#struct_0_77048_16369_x891935608}

[[端口上]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x485850021}[地址认证的统计信息，包括认证通过的次数和认证失败的次数]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_77048_16369_1125710757}

[[接入用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x915655804}[地址]{style="font-family:宋体"}

[[Auth state]{lang="EN-US"}]{#struct_0_77048_16369_426324144}

[[接入用户的状态，包括以下两种：]{style="font-family:宋体"}]{#struct_0_77048_16369_x1296583766}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}[uthenticated]{lang="EN-US"}]{#struct_0_77048_16369_1125645221}[：认证]{lang="EN-US" style="font-family:宋体"}[成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}[nauthenticated]{lang="EN-US"}]{#struct_0_77048_16369_1059050955}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[AP name]{lang="EN-US"}]{#struct_0_77048_16369_1398409549}

[[AP]{lang="EN-US"}]{#struct_0_77048_16369_x1444921678}[名称]{style="font-family:宋体"}

[[Radio ID]{lang="EN-US"}]{#struct_0_77048_16369_x974308982}

[[Radio]{lang="EN-US"}]{#struct_0_77048_16369_1185701198}[编号]{style="font-family:宋体"}

[[SSID]{lang="EN-US"}]{#struct_0_77048_16369_x786699355}

[[服务集标识符]{style="font-family:宋体"}]{#struct_0_77048_16369_1754574373}

[[BSSID]{lang="EN-US"}]{#struct_0_77048_16369_x295022082}

[[基本服务集标识符]{style="font-family:宋体"}]{#struct_0_77048_16369_x964019197}

[ ]{lang="EN-US"}

::: {#1339195102 .myid}
[]{#_Toc404792570}[]{#struct_0_77048_16369_164119180}[]{#_Toc351708670}[]{#_Toc350159602}

**MAC地址认证 \-- MAC地址认证配置命令 \-- display mac-authentication connection**

------------------------------------------------------------------------

[**[display mac-authentication connection]{lang="EN-US"}**]{#struct_0_77048_16369_426948689}[命令用来显示当前]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证在线用户的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_1352596200}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_77048_16369_1276471500}

[**[display mac-authentication connection ]{lang="EN-US"}**[\[ **ap** *ap-name* \[ **radio** *radio-id* \] \| **interface** *interface-type* *interface-number* \| **user-mac** *mac-addr* \| **user-name** *user-name* \]]{lang="EN-US"}]{#struct_0_77048_16369_163529357}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_77048_16369_x1790801414}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display mac-authentication connection ]{lang="EN-US"}**[\[ **ap** *ap-name* \[ **radio** *radio-id* \] \| **interface** *interface-type* *interface-number* \| **slot** *slot-number* \| **user-mac** *mac-addr* \| **user-name** *user-name* \]]{lang="EN-US"}]{#struct_0_77048_16369_x1289551876}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_77048_16369_x144059569}[模式：]{style="font-family:宋体"}

[**[display mac-authentication connection ]{lang="EN-US"}**[\[ **ap** *ap-name* \[ **radio** *radio-id* \] \| **chassis** *chassis-number* **slot** *slot-number* \| **interface** ** ***interface-type* *interface-number* \| **user-mac** *mac-addr* \| **user-name** *user-name* \]]{lang="EN-US"}]{#struct_0_77048_16369_1094592987}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_x819564836}

[[任意视图]{style="font-family:宋体"}]{#struct_0_77048_16369_163594893}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_x2138720052}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_1555464434}

[[network-operator]{lang="EN-US"}]{#struct_0_77048_16369_x530034141}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_x8122562}

[[mdc-operator]{lang="EN-US"}]{#struct_0_77048_16369_x2110989036}

[[【参数】]{style="font-family:黑体"}]{#struct_0_77048_16369_163398285}

[**[ap]{lang="EN-US"}**[ *ap-name*]{lang="EN-US"}]{#struct_0_77048_16369_449021974}[：显示接入指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户的信息，]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[radio]{lang="EN-US"}**[ *radio-id*]{lang="EN-US"}]{#struct_0_77048_16369_449021973}[：显示接入指定]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的所有的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户的信息，]{style="font-family:宋体"}*[radio-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Radio]{lang="EN-US"}[编号，取值范围与设备型号有关。如果不指定该参数，则显示]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_77048_16369_712768812}[：显示指定端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户信息。其中]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示绑定的端口类型和端口编号。]{style="font-family:
宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_77048_16369_x1453081074}[：显示指定单板上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_77048_16369_x1494418275}[：显示指定成员设备上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_77048_16369_591774959}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_77048_16369_x341757501}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_77048_16369_1445012734}[：显示指定单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[user-mac]{lang="EN-US"}**[ *mac-addr*]{lang="EN-US"}]{#struct_0_77048_16369_163463821}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户信息。其中]{style="font-family:宋体"}*[mac-addr]{lang="EN-US"}*[表示用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-name ]{lang="EN-US"}***[user-name]{lang="EN-US"}*]{#struct_0_77048_16369_560773553}[：显示指定用户名的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户信息。其中]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*[表示用户名（可包含域名），为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1726784880}

[[若不指定任何参数，则显示所有端口上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x578776126}[地址认证在线用户信息。（集中式设备）]{style="font-family:宋体"}

[[若不指定任何参数，则显示所有单板上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x1938440639}[地址认证在线用户信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[若不指定任何参数，则显示所有成员设备上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x494089129}[地址认证在线用户信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[若不指定任何参数，则显示所有成员设备的所有单板上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_163791501}[地址认证在线用户信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_874826987}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x43288812}[显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证在线用户信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display mac-authentication connection]{lang="EN-US"}]{#struct_0_77048_16369_x1162049551}

[User MAC address: 0015-e9a6-7cfe]{lang="EN-US"}

[Access interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Username: ias]{lang="EN-US"}

[Authentication domain: h3c]{lang="EN-US"}

[Initial VLAN: 1]{lang="EN-US"}

[Authorization ]{lang="EN-US"}[untagged ]{lang="EN-US"}[VLAN: 100]{lang="EN-US"}

[Authorization ACL ID: 3001]{lang="EN-US"}

[Authorization user profile: N/A]{lang="EN-US"}

[Termination]{lang="EN-US"}[ action: Radius-request]{lang="EN-US"}

[Session timeout period: 2 s]{lang="EN-US"}

[Online from: 2013/03/02  13:14:15]{lang="EN-US"}

[Online duration: 0h 2m 15s]{lang="EN-US"}

[ ]{lang="EN-US"}

[User MAC address              : 0015-e9a6-7cfe]{lang="EN-US"}

[AP name                           : ap1]{lang="EN-US"}

[Radio ID                         : 1]{lang="EN-US"}

[SSID                             : wlan_dot1x_ssid]{lang="EN-US"}

[BSSID                         : 0015-e9a6-7cf0]{lang="EN-US"}

[User name                     : ias]{lang="EN-US"}

[Authentication domain         : 1]{lang="EN-US"}

[Initial VLAN                  : 1]{lang="EN-US"}

[Authorization untagged VLAN   : 100]{lang="EN-US"}

[Authorization ACL number      : 3001]{lang="EN-US"}

[Authorization user profile    : N/A]{lang="EN-US"}

[Termination action            : Radius-request]{lang="EN-US"}

[Session timeout period        : 2 sec]{lang="EN-US"}

[Online from                   : 2014/06/02 13:14:15]{lang="EN-US"}

[Online duration               : 0h 2m 15s]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total 1 connection(s) matched]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_813418099}[显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证在线用户信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display mac-authentication connection]{lang="EN-US"}]{#struct_0_77048_16369_163857037}

[Slot ID: 0]{lang="EN-US"}

[User MAC address: 0015-e9a6-7cfe]{lang="EN-US"}

[Access interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Username: ias]{lang="EN-US"}

[Authentication domain: h3c]{lang="EN-US"}

[Initial VLAN: 1]{lang="EN-US"}

[Authorization ]{lang="EN-US"}[untagged ]{lang="EN-US"}[VLAN: 100]{lang="EN-US"}

[Authorization ACL ID: 3001]{lang="EN-US"}

[Authorization user profile: N/A]{lang="EN-US"}

[Termination]{lang="EN-US"}[ action: Radius-request]{lang="EN-US"}

[Session timeout period: 2 s]{lang="EN-US"}

[Online from: 2013/03/02  13:14:15]{lang="EN-US"}

[Online duration: 0h 2m 15s]{lang="EN-US"}

[ ]{lang="EN-US"}

[User MAC address              : 0015-e9a6-7cfe]{lang="EN-US"}

[AP name                           : ap1]{lang="EN-US"}

[Radio ID                         : 1]{lang="EN-US"}

[SSID                             : wlan_dot1x_ssid]{lang="EN-US"}

[BSSID                         : 0015-e9a6-7cf0]{lang="EN-US"}

[User name                     : ias]{lang="EN-US"}

[Authentication domain         : 1]{lang="EN-US"}

[Initial VLAN                  : 1]{lang="EN-US"}

[Authorization untagged VLAN   : 100]{lang="EN-US"}

[Authorization ACL number      : 3001]{lang="EN-US"}

[Authorization user profile    : N/A]{lang="EN-US"}

[Termination action            : Radius-request]{lang="EN-US"}

[Session timeout period        : 2 sec]{lang="EN-US"}

[Online from                   : 2014/06/02 13:14:15]{lang="EN-US"}

[Online duration               : 0h 2m 15s]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total 1 connections matched.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x877259660}[显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证在线用户信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display mac-authentication connection]{lang="EN-US"}]{#struct_0_77048_16369_2054875236}

[Chassis ID: 1]{lang="EN-US"}

[Slot ID: 0]{lang="EN-US"}

[User MAC address: 0015-e9a6-7cfe]{lang="EN-US"}

[Access interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Username: ias]{lang="EN-US"}

[Authentication domain: h3c]{lang="EN-US"}

[Initial VLAN: 1]{lang="EN-US"}

[Authorization ]{lang="EN-US"}[untagged ]{lang="EN-US"}[VLAN: 100]{lang="EN-US"}

[Authorization ACL ID: 3001]{lang="EN-US"}

[Authorization user profile: N/A]{lang="EN-US"}

[Termination]{lang="EN-US"}[ action: Radius-request]{lang="EN-US"}

[Session timeout period: 2 s]{lang="EN-US"}

[Online from: 2013/03/02  13:14:15]{lang="EN-US"}

[Online duration: 0h 2m 15s]{lang="EN-US"}

[ ]{lang="EN-US"}

[User MAC address              : 0015-e9a6-7cfe]{lang="EN-US"}

[AP name                           : ap1]{lang="EN-US"}

[Radio ID                         : 1]{lang="EN-US"}

[SSID                             : wlan_dot1x_ssid]{lang="EN-US"}

[BSSID                         : 0015-e9a6-7cf0]{lang="EN-US"}

[User name                     : ias]{lang="EN-US"}

[Authentication domain         : 1]{lang="EN-US"}

[Initial VLAN                  : 1]{lang="EN-US"}

[Authorization untagged VLAN   : 100]{lang="EN-US"}

[Authorization ACL number      : 3001]{lang="EN-US"}

[Authorization user profile    : N/A]{lang="EN-US"}

[Termination action            : Radius-request]{lang="EN-US"}

[Session timeout period        : 2 sec]{lang="EN-US"}

[Online from                   : 2014/06/02 13:14:15]{lang="EN-US"}

[Online duration               : 0h 2m 15s]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total 1 connections matched.]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display mac-authentication connection ]{lang="EN-US"}]{#struct_0_77048_16369_163660429}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2111098631}[[字段]{style="font-family:黑体"}]{#struct_0_77048_16369_x1095089547}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_77048_16369_1355710592}

[[Chassis ID]{lang="EN-US"}]{#struct_0_77048_16369_x419552087}

[[当前设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_77048_16369_163725965}[中的成员编号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot ID]{lang="EN-US"}]{#struct_0_77048_16369_x1876671074}

[[[单板所在的槽位号]{style="font-family:宋体"}]{.TableTextChar}]{#struct_0_77048_16369_x682114475}[（]{style="font-family:宋体"}[[分布式设备－独立运行模式]{style="font-family:宋体"}]{.TableTextChar}[[/]{lang="EN-US"}]{.TableTextChar}[[分布式设备－]{style="font-family:
  宋体"}]{.TableTextChar}[IRF]{lang="EN-US"}[[模式]{style="font-family:宋体"}]{.TableTextChar}[）]{style="font-family:宋体"}

[[Slot ID]{lang="EN-US"}]{#struct_0_77048_16369_65589844}

[[当前设备]{style="font-family:宋体"}]{#struct_0_77048_16369_x1912978934}[[在]{style="font-family:宋体"}]{.TableTextChar}[IRF]{lang="EN-US"}[[中的成员编号]{style="font-family:宋体"}]{.TableTextChar}[（]{style="font-family:宋体"}[[集中式]{style="font-family:宋体"}]{.TableTextChar}[IRF]{lang="EN-US"}[[设备]{style="font-family:宋体"}]{.TableTextChar}[）]{style="font-family:宋体"}

[[User MAC address]{lang="EN-US"}]{#struct_0_77048_16369_164053645}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x1493071989}[地址]{style="font-family:宋体"}

[[Access interface]{lang="EN-US"}]{#struct_0_77048_16369_x250686477}

[[用户的接入接口名称]{style="font-family:宋体"}]{#struct_0_77048_16369_164119181}

[[AP name]{lang="EN-US"}]{#struct_0_77048_16369_x1909094308}

[[AP]{lang="EN-US"}]{#struct_0_77048_16369_1677220991}[的名称]{style="font-family:宋体"}

[[Radio ID]{lang="EN-US"}]{#struct_0_77048_16369_x1909094306}

[[Radio]{lang="EN-US"}]{#struct_0_77048_16369_x1909094305}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[SSID]{lang="EN-US"}]{#struct_0_77048_16369_561475744}

[[服务集标识符]{style="font-family:宋体"}]{#struct_0_77048_16369_x1909094304}

[[BSSID]{lang="EN-US"}]{#struct_0_77048_16369_x1909094303}

[[用户所属的基本服务集标识符]{style="font-family:宋体"}]{#struct_0_77048_16369_429557848}

[[Username]{lang="EN-US"}]{#struct_0_77048_16369_426948688}

[[用户名]{style="font-family:宋体"}]{#struct_0_77048_16369_1352596199}

[[Authentication domain]{lang="EN-US"}]{#struct_0_77048_16369_x1062770475}

[[认证时所用的]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_77048_16369_163529358}[域的名称]{style="font-family:宋体"}

[[Initial VLAN]{lang="EN-US"}]{#struct_0_77048_16369_x1790801425}

[[初始的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_77048_16369_1439134871}

[[Authorization untagged VLAN]{lang="EN-US"}]{#struct_0_77048_16369_163594894}

[[授权的]{style="font-family:宋体"}[untagged VLAN]{lang="EN-US"}]{#struct_0_77048_16369_x2138720049}

[[Authorization ACL ID]{lang="EN-US"}]{#struct_0_77048_16369_x817254097}

[[授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_77048_16369_163398286}[编号]{style="font-family:宋体"}

[[Authorization user profile]{lang="EN-US"}]{#struct_0_77048_16369_712768815}

[[授权用户的]{style="font-family:宋体"}[User profile]{lang="EN-US"}]{#struct_0_77048_16369_x1453081081}[名称]{style="font-family:宋体"}

[[Terminate action]{lang="EN-US"}]{#struct_0_77048_16369_163463822}

[[服务器下发的终止动作类型：]{style="font-family:宋体"}]{#struct_0_77048_16369_560773550}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Default]{lang="EN-US"}]{#struct_0_77048_16369_x1726784877}[：会话超时时间到达后，强制用户下线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Radius-Request]{lang="EN-US"}]{#struct_0_77048_16369_986324775}[：会话超时时间到达后，请求]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户进行重认证]{style="font-family:宋体"}

[[用户采用本地认证时，该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_77048_16369_163791502}

[[Session timeout period]{lang="EN-US"}]{#struct_0_77048_16369_874826990}

[[服务器下发的会话超时时间，该时间到达之后，用户所在的会话将会被删除，之后，对该用户所采取的动作，由]{style="font-family:宋体"}[Terminate action]{lang="EN-US"}]{#struct_0_77048_16369_x1999603949}[字段的取值决定]{style="font-family:宋体"}

[[用户采用本地认证时，该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_77048_16369_x227159393}

[[Online from]{lang="EN-US"}]{#struct_0_77048_16369_163857038}

[[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x877259649}[认证用户的上线时间]{style="font-family:宋体"}

[[Online duration]{lang="EN-US"}]{#struct_0_77048_16369_2055465062}

[[MAC]{lang="EN-US"}]{#struct_0_77048_16369_163660430}[认证用户的在线时长]{style="font-family:宋体"}

[[Total 1 connection(s) matched]{lang="EN-US"}]{#struct_0_77048_16369_1243562604}

[[在线]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x986097155}[地址认证用户个数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1462532001 .myid}
[]{#_Toc404792571}[]{#struct_0_77048_16369_1559635220}[]{#_Toc257814918}[]{#_Toc144718096}[]{#_Toc144718117}[]{#_Toc144718310}[]{#_Toc144718097}[]{#_Toc144718118}[]{#_Toc144718311}[]{#_Toc144718098}[]{#_Toc144718119}[]{#_Toc144718312}

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication**

------------------------------------------------------------------------

[**[mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_1504828869}[命令用来开启指定端口上或全局的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证。]{style="font-family:宋体"}

[**[undo mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_x1674393665}[命令用来关闭指定端口上或全局的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_193652530}

[**[mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_1125579685}

[**[undo mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_208161976}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1851507976}

[[所有端口及全局的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_1435620778}[地址认证都处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_314840274}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_77048_16369_107238054}[以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_1732850982}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_902239258}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_x2136458423}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_77048_16369_2039241408}

[[只有全局和端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x840068163}[地址认证均开启后，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证配置才能在端口上生效。该配置的生效情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_1125514149}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x94215987}[开启全局的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_77048_16369_991439417}

[\[Sysname\] mac-authentication]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_1967322555}[开启端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_77048_16369_x1455801054}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mac-authentication]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_x362085657}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_x1116838046}
:::

::: {#695242141 .myid}
[]{#_Toc404792572}[]{#struct_0_77048_16369_163725966}[]{#_Toc286753029}[]{#_Toc286753698}[]{#_Toc286853653}[]{#_Toc293333808}[]{#_Toc286753030}[]{#_Toc286753699}[]{#_Toc286853654}[]{#_Toc293333809}[]{#_Toc286753031}[]{#_Toc286753700}[]{#_Toc286853655}[]{#_Toc293333810}[]{#_Toc286753032}[]{#_Toc286753701}[]{#_Toc286853656}[]{#_Toc293333811}[]{#_Toc286753033}[]{#_Toc286753702}[]{#_Toc286853657}[]{#_Toc293333812}[]{#_Toc286753034}[]{#_Toc286753703}[]{#_Toc286853658}[]{#_Toc293333813}[]{#_Toc286753035}[]{#_Toc286753704}[]{#_Toc286853659}[]{#_Toc293333814}[]{#_Toc286753036}[]{#_Toc286753705}[]{#_Toc286853660}[]{#_Toc293333815}[]{#_Toc286753037}[]{#_Toc286753706}[]{#_Toc286853661}[]{#_Toc293333816}[]{#_Toc286753038}[]{#_Toc286753707}[]{#_Toc286853662}[]{#_Toc293333817}[]{#_Toc286753039}[]{#_Toc286753708}[]{#_Toc286853663}[]{#_Toc293333818}[]{#_Toc286753040}[]{#_Toc286753709}[]{#_Toc286853664}[]{#_Toc293333819}[]{#_Toc286753041}[]{#_Toc286753710}[]{#_Toc286853665}[]{#_Toc293333820}[]{#_Toc286753042}[]{#_Toc286753711}[]{#_Toc286853666}[]{#_Toc293333821}[]{#_Toc286753043}[]{#_Toc286753712}[]{#_Toc286853667}[]{#_Toc293333822}[]{#_Toc286753044}[]{#_Toc286753713}[]{#_Toc286853668}[]{#_Toc293333823}[]{#_Toc286753045}[]{#_Toc286753714}[]{#_Toc286853669}[]{#_Toc293333824}[]{#_Toc286753046}[]{#_Toc286753715}[]{#_Toc286853670}[]{#_Toc293333825}[]{#_Toc286753047}[]{#_Toc286753716}[]{#_Toc286853671}[]{#_Toc293333826}[]{#_Toc286753048}[]{#_Toc286753717}[]{#_Toc286853672}[]{#_Toc293333827}[]{#_Toc286753049}[]{#_Toc286753718}[]{#_Toc286853673}[]{#_Toc293333828}[]{#_Toc286753050}[]{#_Toc286753719}[]{#_Toc286853674}[]{#_Toc293333829}[]{#_Toc286753051}[]{#_Toc286753720}[]{#_Toc286853675}[]{#_Toc293333830}[]{#_Toc286753052}[]{#_Toc286753721}[]{#_Toc286853676}[]{#_Toc293333831}[]{#_Toc286753053}[]{#_Toc286753722}[]{#_Toc286853677}[]{#_Toc293333832}

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication critical vlan**

------------------------------------------------------------------------

[**[mac-authentication critical vlan]{lang="EN-US"}**]{#struct_0_77048_16369_x1876671077}[命令用来配置指定端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}[，即当]{style="font-family:宋体"}[MAC]{lang="EN-US"}[用户认证时对应的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域下所有认证服务器都不可达的情况下被授权访问]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}[内的资源。]{style="font-family:宋体"}

[**[undo mac-authentication critical vlan]{lang="EN-US"}**]{#struct_0_77048_16369_164053646}[命令用来恢复缺省情况**。**]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1493071986}

[**[mac-authentication critical vlan]{lang="EN-US"}***[ critical-vlan-id]{lang="EN-US"}*]{#struct_0_77048_16369_x203632310}

[**[undo mac-authentication critical vlan]{lang="EN-US"}**]{#struct_0_77048_16369_777062509}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1137215452}

[[端口上未配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x489377976}[地址认证的]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_164119182}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_77048_16369_426948691}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_x986055952}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_367233800}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_x601782453}

[[【参数】]{style="font-family:黑体"}]{#struct_0_77048_16369_163529359}

[*[critical-vlan-id]{lang="EN-US"}*]{#struct_0_77048_16369_x1790801424}[：端口上指定的]{style="font-family:宋体"}[Critical VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[（取值范围与设备型号有关，请以设备的实际情况为准）。该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[必须已经创建。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_77048_16369_65327701}

[[如果某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_77048_16369_x1629485966}[被指定为]{style="font-family:宋体"}[Super VLAN]{lang="EN-US"}[，则该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不能被指定为某个端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}[；同样，如果某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[被指定为某个端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}[，则该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不能被指定为]{style="font-family:宋体"}[Super VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[禁止删除已被配置为]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}]{#struct_0_77048_16369_370177153}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，若要删除该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，请先使用命令]{style="font-family:宋体"}**[undo mac-authentication ]{lang="EN-US"}[critica vlan]{lang="EN-US"}**[取消]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1289748484}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x296525782}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 100 ]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_77048_16369_x1530035233}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mac-authentication critical vlan 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_1870623926}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_163594895}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset mac-authentication critical-vlan]{lang="EN-US"}**]{#struct_0_77048_16369_x2138720050}
:::

::: {#1131898116 .myid}
[]{#_Toc404792573}[]{#struct_0_77048_16369_997760885}[]{#_Toc257814919}

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication domain**

------------------------------------------------------------------------

[**[mac-authentication domain]{lang="EN-US"}**]{#struct_0_77048_16369_x1334137456}[命令用来指定]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址认证用户使用的认证域。]{style="font-family:宋体"}

[**[undo mac-authentication domain]{lang="EN-US"}**]{#struct_0_77048_16369_1125972901}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_1861032943}

[**[mac-authentication]{lang="EN-US"}***[ ]{lang="EN-US"}***[domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_77048_16369_1478769926}

[**[undo mac-authentication]{lang="EN-US"}***[ ]{lang="EN-US"}***[domain]{lang="EN-US"}**]{#struct_0_77048_16369_1815092021}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_77048_16369_1434459121}

[[未指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_698959062}[地址认证用户使用的认证域，使用系统缺省的认证域。缺省认证域的介绍请参见"安全命令参考]{style="font-family:宋体"}[/AAA]{lang="EN-US"}["中的命令]{style="font-family:宋体"}**[domain default]{lang="EN-US"}***[ ]{lang="EN-US"}***[enable]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_x179152602}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_77048_16369_x1642206414}[以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_x5530501}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_1125907365}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_x107889120}

[[【参数】]{style="font-family:黑体"}]{#struct_0_77048_16369_1561267035}

[*[domain-name]{lang="EN-US"}*]{#struct_0_77048_16369_831423561}[：]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_77048_16369_910982338}

[[不同视图下指定的认证域的生效范围不同：]{style="font-family:宋体"}]{#struct_0_77048_16369_1041157591}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统视图下指定的认证域对所有开启了]{style="font-family:宋体"}]{#struct_0_77048_16369_95419561}[MAC]{lang="EN-US"}[地址认证的端口生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以太网接口视图下指定的认证域仅对本端口有效。不同的端口可以指定不同的认证域。]{style="font-family:宋体"}]{#struct_0_77048_16369_2019522920}

[[端口上接入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_967511951}[地址认证用户将按照如下先后顺序选择认证域：端口上指定的认证域]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[系统视图下指定的认证域]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[系统缺省的认证域。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_437795195}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_1906485787}[在系统视图下指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户使用的认证域为]{style="font-family:宋体"}[domain1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_77048_16369_1125841829}

[\[Sysname\] mac-authentication domain domain1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_1473488757}[指定端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上接入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户使用的认证域为]{style="font-family:宋体"}[aabbcc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_77048_16369_x1658744922}

[\[Sysname-GigabitEthernet1/0/1\] mac-authentication domain aabbcc]{lang="EN-US"}[]{#_Toc189478481}[]{#_Toc185754782}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_795149085}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_x247526750}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain default]{lang="EN-US"}***[ ]{lang="EN-US"}***[enable]{lang="EN-US"}**]{#struct_0_77048_16369_1954698642}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#1477500263 .myid}
[]{#_Toc404792574}[]{#struct_0_77048_16369_163398287}[]{#_Toc351708667}

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication guest-vlan**

------------------------------------------------------------------------

[**[mac-authentication guest-vlan]{lang="EN-US"}**]{#struct_0_77048_16369_712768814}[命令用来配置指定端口的]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址认证的]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[，即]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证失败的用户被授权访问的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo mac-authentication guest-vlan]{lang="EN-US"}**]{#struct_0_77048_16369_x1453081080}[命令用来恢复缺省情况**。**]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_163463823}

[**[mac-authentication guest-vlan ]{lang="EN-US"}***[guest-vlan-id]{lang="EN-US"}*]{#struct_0_77048_16369_560773551}

[**[undo mac-authentication guest-vlan]{lang="EN-US"}**]{#struct_0_77048_16369_x1726784878}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_77048_16369_x223528806}

[[端口上未配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x1087396335}[地址认证的]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_1405071227}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_77048_16369_163791503}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_874826989}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_x43288806}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_794265581}

[[【参数】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1690383528}

[*[guest-vlan-id]{lang="EN-US"}*]{#struct_0_77048_16369_163857039}[：端口上指定的]{style="font-family:宋体"}[Guest VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[（取值范围与设备型号有关，请以设备的实际情况为准）。该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[必须已经创建。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_77048_16369_65589845}

[ ]{lang="EN-US"}

[[如果某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_77048_16369_425673226}[被指定为]{style="font-family:宋体"}[Super VLAN]{lang="EN-US"}[，则该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不能被指定为某个端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[；同样，如果某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[被指定为某个端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[，则该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不能被指定为]{style="font-family:宋体"}[Super VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[禁止删除已被配置为]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}]{#struct_0_77048_16369_65524309}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，若要删除该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，请先使用命令]{style="font-family:宋体"}**[undo mac-authentication ]{lang="EN-US"}[guest-vlan]{lang="EN-US"}**[取消]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_x877259650}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_2054875237}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 100 ]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_77048_16369_x427765628}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mac-authentication guest-vlan 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_x265837652}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_x1438821888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset mac-authentication guest-vlan]{lang="EN-US"}**]{#struct_0_77048_16369_163660431}
:::

::: {#-204041230 .myid}
[]{#_Toc404792575}[]{#struct_0_77048_16369_1339448273}[]{#_Toc372381261}[]{#_Toc361662985}

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication host-mode**

------------------------------------------------------------------------

[**[mac-authentication host-mode multi-vlan]{lang="EN-US"}**]{#struct_0_77048_16369_x1238451860}[命令用来指定端口工作在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的多]{style="font-family:宋体"}[VLAN ]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[undo mac-authentication host-mode]{lang="EN-US"}**]{#struct_0_77048_16369_1339513809}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_x2028500717}

[**[mac-authentication host-mode multi-vlan]{lang="EN-US"}**]{#struct_0_77048_16369_325534019}

[**[undo mac-authentication host-mode]{lang="EN-US"}**]{#struct_0_77048_16369_x1389959375}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_77048_16369_x100396302}

[[端口工作在]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x1954620873}[地址认证的单]{style="font-family:宋体"}[VLAN ]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_107151134}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_77048_16369_x1389893839}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_1163656059}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_x1371533529}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_x1389828303}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1829088861}

[[端口工作在多]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_77048_16369_2002217269}[模式下时，如果相同]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的用户在属于不同]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的相同端口再次接入，设备将能够允许用户的流量在新的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内通过，且允许该用户的报文无需重新认证而在多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中转发。]{style="font-family:宋体"}

[[端口工作在单]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_77048_16369_x1389762767}[模式下时，在用户已上线，且没有被下发授权]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[情况下，如果此用户在属于不同]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的相同端口再次接入，则，设备将让原用户下线，使得该用户能够在新的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内重新开始认证。如果已上线用户被下发了授权]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则此用户在属于不同]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的相同端口再次接入时不会被强制下线。]{style="font-family:宋体"}

[[对于接入]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_77048_16369_2050056007}[电话类用户的端口，指定端口工作在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的多]{style="font-family:宋体"}[VLAN ]{lang="EN-US"}[模式，可避免]{style="font-family:宋体"}[IP]{lang="EN-US"}[电话终端的报文所携带的]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[发生变化后，因用户流量需要重新认证带来语音报文传输质量受干扰的问题。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_990207214}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x1389697231}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[工作在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的多]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_77048_16369_2068684873}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mac-authentication host-mode multi-vlan]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_x448521732}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_x1389631695}
:::

::::: {#273853227 .myid}
[]{#_Toc404792576}[]{#struct_0_77048_16369_1773128099}[]{#_Toc257814921}

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication max-user**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址认证命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_77048_16369_x34631674}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_77048_16369_x667331249}
:::

[ ]{lang="EN-US"}

[**[mac-authentication]{lang="EN-US"}**[ **max-user**]{lang="EN-US"}]{#struct_0_77048_16369_1125776293}[命令用来配置端口上最多允许同时接入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户数。当接入此端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户数超过最大值后，新接入的用户将被拒绝。]{style="font-family:宋体"}

[**[undo mac-authentication]{lang="EN-US"}**[ **max-user**]{lang="EN-US"}]{#struct_0_77048_16369_x509326782}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_x409019826}

[**[mac-authentication]{lang="EN-US"}**[ **max-user** *user-number*]{lang="EN-US"}]{#struct_0_77048_16369_1672350195}

[**[undo mac-authentication max-user]{lang="EN-US"}**]{#struct_0_77048_16369_2096706848}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_77048_16369_x545966777}

[[端口上最多允许同时接入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x657959411}[地址认证用户数与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1777654999}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_77048_16369_1413811419}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_x441872511}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_1126235045}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_167237205}

[[【参数】]{style="font-family:黑体"}]{#struct_0_77048_16369_925900386}

[*[user-number]{lang="EN-US"}*]{#struct_0_77048_16369_x128916274}[：端口允许同时接入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户数的最大值，不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1187374974}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x380959831}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[最多允许同时接入]{style="font-family:宋体"}[32]{lang="EN-US"}[个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_77048_16369_x1793190639}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mac-authentication max-user 32]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1634213345}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_1305582496}
:::::

::: {#2092943494 .myid}
[]{#_Toc404792577}[]{#struct_0_77048_16369_163725967}[]{#_Toc351708669}[]{#_Toc350159601}

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication re-authenticate server-unreachable keep-online**

------------------------------------------------------------------------

[**[mac-authentication re-authenticate server-unreachable keep-online]{lang="EN-US"}**]{#struct_0_77048_16369_x1876671076}[命令用来配置重认证服务器不可达时端口上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户保持在线状态。]{style="font-family:宋体"}

[**[undo mac-authentication re-authenticate server-unreachable]{lang="EN-US"}**]{#struct_0_77048_16369_480684939}[命令用来恢复缺省情况**。**]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_x2035996949}

[**[mac-authentication re-authenticate server-unreachable keep-online]{lang="EN-US"}**]{#struct_0_77048_16369_164053647}

[**[undo mac-authentication re-authenticate server-unreachable]{lang="EN-US"}**]{#struct_0_77048_16369_x1493071987}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1769716251}

[[端口上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_1599593390}[地址认证在线用户重认证时，若认证服务器不可达，则会被强制下线。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_x866649537}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_77048_16369_1080357190}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_164119183}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_426948690}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_x986055953}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_163529352}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x1790801419}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证在线用户进行重认证时，若服务器不可达，则保持在线状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_77048_16369_x886267349}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mac-authentication re-authenticate server-unreachable keep-online]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_1318822421}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_x124314903}
:::

::: {#1306595024 .myid}
[]{#_Toc404792578}[]{#struct_0_77048_16369_6568474}[]{#_Toc257814922}

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication timer**

------------------------------------------------------------------------

[**[mac-authentication]{lang="EN-US"}**[ **timer**]{lang="EN-US"}]{#struct_0_77048_16369_1126169509}[命令用来配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的定时器参数。]{style="font-family:宋体"}

[**[undo mac-authentication]{lang="EN-US"}**[ **timer**]{lang="EN-US"}]{#struct_0_77048_16369_1654476084}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_1118464242}

[**[mac-authentication]{lang="EN-US"}**[ **timer** { **offline-detect** *offline-detect-value* \| **quiet** *quiet-value* \| **server-timeout** *server-timeout-value* }]{lang="EN-US"}]{#struct_0_77048_16369_x405743863}

[**[undo mac-authentication]{lang="EN-US"}**[ **timer** { **offline-detect** \| **quiet** \| **server-timeout** }]{lang="EN-US"}]{#struct_0_77048_16369_533822696}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_77048_16369_x72148195}

[[下线检测定时器的值为]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_77048_16369_x1806731785}[秒，静默定时器的值为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒，服务器超时定时器的值为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_x165703438}

[[系统视图]{style="font-family:宋体"}]{#struct_0_77048_16369_78217019}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_1125710754}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_x915721340}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_1977835041}

[[【参数】]{style="font-family:黑体"}]{#struct_0_77048_16369_1387565524}

[**[offline-detect]{lang="EN-US"}***[ offline-detect-value]{lang="EN-US"}*]{#struct_0_77048_16369_904379860}[：表示下线检测定时器。其中，]{style="font-family:宋体"}*[offline-detect-value]{lang="EN-US"}*[表示下线检测定时器的值，取值范围]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[quiet]{lang="EN-US"}**[ *quiet-value*]{lang="EN-US"}]{#struct_0_77048_16369_661980757}[：表示静默定时器。其中]{style="font-family:宋体"}*[quiet-value]{lang="EN-US"}*[表示静默定时器的值，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[server-timeout]{lang="EN-US"}***[ server-timeout-value]{lang="EN-US"}*]{#struct_0_77048_16369_2138135875}[：表示服务器超时定时器。其中，]{style="font-family:宋体"}*[server-timeout-value]{lang="EN-US"}*[表示服务器超时定时器的值，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1859141333}

[[MAC]{lang="EN-US"}]{#struct_0_77048_16369_1017817643}[地址认证过程受以下定时器的控制：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下线检测定时器（]{style="font-family:宋体"}]{#struct_0_77048_16369_x369067844}**[offline-detect]{lang="EN-US"}**[）：用来设置在线用户空闲超时的时间间隔。若设备在一个下线检测定时器间隔之内，没有收到某在线用户的报文，将切断该用户的连接，同时通知]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器停止对其计费。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[静默定时器（]{style="font-family:宋体"}]{#struct_0_77048_16369_1125645218}**[quiet]{lang="EN-US"}**[）：用来设置用户认证失败以后，设备需要等待的时间间隔。在静默期间，设备不对来自认证失败用户的报文进行认证处理，直接丢弃。静默期后，如果设备再次收到该用户的报文，则依然可以对其进行认证处理。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[服务器超时定时器（]{style="font-family:宋体"}]{#struct_0_77048_16369_1059509708}**[server-timeout]{lang="EN-US"}**[）：用来设置设备同]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的连接超时时间。在用户的认证过程中，如果到服务器超时定时器超时时设备一直没有收到]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的应答，则设备将在相应的端口上禁止此用户访问网络。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_1580094635}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x1624749600}[设置服务器超时定时器时长为]{style="font-family:宋体"}[150]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_77048_16369_x1952650585}

[\[Sysname\] mac-authentication timer server-timeout 150]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_1746157218}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_x1335362386}
:::

::: {#-1679078414 .myid}
[]{#_Toc404792579}[]{#struct_0_77048_16369_676653612}[]{#_Toc334532754}[]{#_Toc331088879}

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication timer auth-delay**

------------------------------------------------------------------------

[**[mac-authentication timer auth-delay]{lang="EN-US"}**]{#struct_0_77048_16369_295366945}[命令用来开启]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证延迟功能，并配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的延时时间。]{style="font-family:宋体"}

[**[undo mac-authentication timer auth-delay]{lang="EN-US"}**]{#struct_0_77048_16369_x77838060}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_1125579682}

[**[mac-authentication timer auth-delay ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_77048_16369_208358584}

[**[undo mac-authentication timer auth-delay]{lang="EN-US"}**]{#struct_0_77048_16369_x2024689121}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_77048_16369_1302424015}

[[MAC]{lang="EN-US"}]{#struct_0_77048_16369_1690891729}[地址认证延迟功能处于关闭状态，如果用户报文触发]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证，认证将会立刻开始。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_1329586955}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_77048_16369_x983938556}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_1422499956}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_x1264956214}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_x1812767159}

[[【参数】]{style="font-family:黑体"}]{#struct_0_77048_16369_1125514146}

[*[time]{lang="EN-US"}*]{#struct_0_77048_16369_x93232947}[：延迟]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[180]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_77048_16369_x2100227466}

[[端口同时开启了]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x439440102}[地址认证和]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证的情况下，某些组网环境中希望设备对用户报文先进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证。例如，有些客户端在发送]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证请求报文之前，就已经向设备发送了其它报文，比如]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文，因而触发了并不期望的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证。这种情况下，就可以开启端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证延时功能。]{style="font-family:宋体"}

[[开启端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_45998739}[地址认证延时功能之后，端口就不会在收到用户报文时立即触发]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证，而是在等待一定的延迟时间之后，再会对之前收到的用户报文进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证。在此认证延迟期间，端口对用户报文的其它认证过程并不受影响。]{style="font-family:宋体"}

[[开启了]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_380037748}[地址认证延迟功能的接口上不建议同时配置端口安全的模式为]{style="font-family:宋体"}**[mac-else-userlogin-secure]{lang="EN-US"}**[或]{style="font-family:宋体"}**[mac-else-userlogin-secure-ext]{lang="EN-US"}**[，否则]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证延迟功能不生效。端口安全模式的具体配置请参见"安全命令参考"中的"端口安全"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1225623328}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x1905387449}[开启]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址延迟认证功能，并指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的延时时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_77048_16369_x1343029418}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mac-authentication timer auth-delay 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_x234348379}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_1125972898}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port-security port-mode]{lang="EN-US"}**]{#struct_0_77048_16369_x94692360}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[端口安全]{style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::::: {#-474750202 .myid}
[]{#_Toc404792580}[]{#struct_0_77048_16369_x1595499240}[]{#_Toc257814923}[]{#_Toc151190786}

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication user-name-format**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址认证命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_77048_16369_1136824246}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_77048_16369_x869318229}
:::

**[ ]{lang="EN-US"}**

[**[mac-authentication user-name-format]{lang="EN-US"}**]{#struct_0_77048_16369_1321499661}[命令用来配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的用户名格式。]{style="font-family:宋体"}

[**[undo mac-authentication user-name-format]{lang="EN-US"}**]{#struct_0_77048_16369_x2010100531}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_1352476943}

[**[mac-authentication user-name-format]{lang="EN-US"}**[ { **fixed** \[ **account** *name* \] \[ **password** { **cipher** \| **simple** } *password* \] \| **mac-address** \[ { **with-hyphen** \| **without-hyphen** } \[ **lowercase** \| **uppercase** \] \] }]{lang="EN-US"}]{#struct_0_77048_16369_1723033831}

[**[undo mac-authentication user-name-format]{lang="EN-US"}**]{#struct_0_77048_16369_1937609139}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_77048_16369_1125907362}

[[使用用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x108347872}[地址作为用户名和密码，其中字母为小写，且不带连字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_1763462873}

[[系统视图]{style="font-family:宋体"}]{#struct_0_77048_16369_x1364509572}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_232461240}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_1277432023}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_x1773527621}

[[【参数】]{style="font-family:黑体"}]{#struct_0_77048_16369_x997399829}

[**[fixed]{lang="EN-US"}**]{#struct_0_77048_16369_x646247341}[：表示采用固定用户名格式。]{style="font-family:宋体"}

[**[account]{lang="EN-US"}**[ *name*]{lang="EN-US"}]{#struct_0_77048_16369_1125841826}[：指定发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器进行认证或者在本地进行认证的用户名。其中]{style="font-family:宋体"}*[name]{lang="EN-US"}*[为用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[55]{lang="EN-US"}[个字符的字符串，区分大小写，不能包括字符]{style="font-family:宋体"}[@]{lang="EN-US"}[，缺省为]{style="font-family:宋体"}[mac]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[password]{lang="EN-US"}**]{#struct_0_77048_16369_1472505717}[：指定固定用户名的密码。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_77048_16369_1446416950}[：表示以密文方式设置密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_77048_16369_1021609899}[：表示以明文方式设置密码。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_77048_16369_1511410968}[：设置的明文密码或密文密码，区分大小写。明文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串；密文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}**]{#struct_0_77048_16369_1468400798}[：表示使用用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为用户名和密码。]{style="font-family:宋体"}

[**[with-hyphen]{lang="EN-US"}**]{#struct_0_77048_16369_915690319}[：带连字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址格式，例如]{style="font-family:宋体"}[xx-xx-xx-xx-xx-xx]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[without-hyphen]{lang="EN-US"}**]{#struct_0_77048_16369_x768743894}[：不带连字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址格式，例如]{style="font-family:宋体"}[xxxxxxxxxxxx]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[lowercase]{lang="EN-US"}**]{#struct_0_77048_16369_488668990}[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址中的字母为小写。]{style="font-family:宋体"}

[**[uppercase]{lang="EN-US"}**]{#struct_0_77048_16369_x2079968520}[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址中的字母为大写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_77048_16369_1125776290}

[[若指定用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x509130174}[地址为用户名，则用户密码也为用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。这种情况下，每一个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户都使用唯一的用户名进行认证，安全性高，但要求认证服务器端配置多个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[形式的用户帐户。]{style="font-family:宋体"}

[[若指定一个固定的用户名，则表示不论用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_x1196232485}[地址为何值，所有用户均使用设备上指定的一个固定用户名和密码作为身份信息进行认证。由于同一个端口下可以有多个用户进行认证，因此这种情况下端口上的所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户均使用同一个固定用户名进行认证，服务器端仅需要配置一个用户帐户即可满足所有认证用户的认证需求，适用于接入客户端比较可信的网络环境。]{style="font-family:宋体"}

[[以明文或密文方式设置的密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_77048_16369_1410864148}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_846124685}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_1070672182}[配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的用户名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[，密码是明文]{style="font-family:宋体"}[xyz]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_77048_16369_x897114621}

[\[Sysname\] mac-authentication user-name-format fixed account abc password simple xyz]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x2009401332}[配置用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为用户名和密码，使用带连字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址格式，其中字母大写。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_77048_16369_706381869}

[\[Sysname\] mac-authentication user-name-format mac-address with-hyphen uppercase]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_1126235042}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_166909525}
:::::

::: {#156453265 .myid}
[]{#_Toc404792581}[]{#struct_0_77048_16369_163791496}

**MAC地址认证 \-- MAC地址认证配置命令 \-- reset mac-authentication critical-vlan**

------------------------------------------------------------------------

[**[reset mac-authentication critical-vlan]{lang="EN-US"}**]{#struct_0_77048_16369_x1500561011}[命令用来清除]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_1673398383}

[**[reset mac-authentication critical-vlan]{lang="EN-US"}**[ **interface** *interface-type interface-number* \[ **mac-address** *mac-address* \]]{lang="EN-US"}]{#struct_0_77048_16369_163857032}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_x877259655}

[[用户视图]{style="font-family:宋体"}]{#struct_0_77048_16369_2055202917}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_777662233}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_x341769325}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_454830822}

[[【参数】]{style="font-family:黑体"}]{#struct_0_77048_16369_163660424}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_77048_16369_x1095089560}[：表示使指定端口上的用户退出]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。]{style="font-family:
宋体"}

[**[mac-address]{lang="EN-US"}**[ *mac-address*]{lang="EN-US"}]{#struct_0_77048_16369_952294993}[：表示使指定]{style="font-family:宋体"} [MAC]{lang="EN-US"}[地址的用户退出]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1450283964}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x1758200815}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使得]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1-1-1]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户退出]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset mac-authentication critical-vlan interface gigabitethernet 1/0/1 mac-address 1-1-1]{lang="EN-US"}]{#struct_0_77048_16369_163725960}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1876671079}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_x1085399002}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-authentication critical vlan]{lang="EN-US"}**]{#struct_0_77048_16369_2125800401}
:::

::: {#2097023217 .myid}
[]{#_Toc404792582}[]{#struct_0_77048_16369_1046750807}

**MAC地址认证 \-- MAC地址认证配置命令 \-- reset mac-authentication guest-vlan**

------------------------------------------------------------------------

[**[reset mac-authentication guest-vlan]{lang="EN-US"}**]{#struct_0_77048_16369_164053640}[命令用来清除]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1493071984}

[**[reset mac-authentication guest-vlan]{lang="EN-US"}**[ **interface** *interface-type interface-number* \[ **mac-address** *mac-address* \]]{lang="EN-US"}]{#struct_0_77048_16369_x1366431724}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1255724055}

[[用户视图]{style="font-family:宋体"}]{#struct_0_77048_16369_x2147190590}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_164119176}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_x764692393}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_1634994884}

[[【参数】]{style="font-family:黑体"}]{#struct_0_77048_16369_1006059919}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_77048_16369_163529353}[：表示使指定端口上的用户退出]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。]{style="font-family:
宋体"}

[**[mac-address]{lang="EN-US"}**[ *mac-address*]{lang="EN-US"}]{#struct_0_77048_16369_x1790801418}[：表示使指定]{style="font-family:宋体"} [MAC]{lang="EN-US"}[地址的用户退出]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_679816592}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x1065183083}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使得]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1-1-1]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户退出]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset mac-authentication guest-vlan interface gigabitethernet 1/0/1 mac-address 1-1-1]{lang="EN-US"}]{#struct_0_77048_16369_163594889}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_199932114}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_723772465}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-authentication guest-vlan]{lang="EN-US"}**]{#struct_0_77048_16369_x1550636959}
:::

::: {#975205799 .myid}
[]{#_Toc404792583}[]{#struct_0_77048_16369_1488362199}

**MAC地址认证 \-- MAC地址认证配置命令 \-- reset mac-authentication statistics**

------------------------------------------------------------------------

[**[reset mac-authentication]{lang="EN-US"}***[ ]{lang="EN-US"}***[statistics]{lang="EN-US"}**]{#struct_0_77048_16369_9342552}[命令用来清除]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_1290750920}

[**[reset mac-authentication statistics]{lang="EN-US"}**[ \[ **ap** *ap-name* \[ **radio** *radio-id* \] \| **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_77048_16369_x326346674}

[[【视图】]{style="font-family:黑体"}]{#struct_0_77048_16369_x384362552}

[[用户视图]{style="font-family:宋体"}]{#struct_0_77048_16369_x158442664}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_77048_16369_x933230247}

[[network-admin]{lang="EN-US"}]{#struct_0_77048_16369_1437721069}

[[mdc-admin]{lang="EN-US"}]{#struct_0_77048_16369_1126169506}

[[【参数】]{style="font-family:黑体"}]{#struct_0_77048_16369_1655328052}

[**[ap]{lang="EN-US"}**[ *ap-name*]{lang="EN-US"}]{#struct_0_77048_16369_1754377765}[：清除指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证统计信息，]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[radio]{lang="EN-US"}**[ *radio-id*]{lang="EN-US"}]{#struct_0_77048_16369_872543480}[：清除指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证统计信息，]{style="font-family:宋体"}*[radio-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Radio]{lang="EN-US"}[编号，取值范围与设备型号有关。如果不指定该参数，则清除指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有射频天线下的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_77048_16369_1445644814}[：清除指定端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证统计信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_77048_16369_372928807}

[[如果不指定任何参数，则清除所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_77048_16369_1090047986}[地址认证统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_77048_16369_x1748054720}

[[\# ]{lang="EN-US"}]{#struct_0_77048_16369_x96005502}[清除以太网端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[认证统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset mac-authentication statistics interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_77048_16369_x354916503}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_77048_16369_x14731444}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-authentication]{lang="EN-US"}**]{#struct_0_77048_16369_1466842757}
:::
