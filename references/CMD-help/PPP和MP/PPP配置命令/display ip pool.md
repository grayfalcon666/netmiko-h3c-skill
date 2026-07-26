::: {#-723135731 .myid}
[]{#_Toc31795057}[]{#_Toc505401497}[]{#_Toc31795061}[]{#_Toc505401499}[]{#_Toc136938064}[]{#_Toc96758138}[]{#_Toc332278967}[]{#_Toc259009501}[]{#_Toc404785029}[]{#struct_0_x2041_67218_x1532467605}[]{#_Toc349654524}[]{#_Toc334604322}[]{#_Toc334028087}

**PPP和MP \-- PPP配置命令 \-- display ip pool**

------------------------------------------------------------------------

[**[display ip pool]{lang="EN-US"}**]{#struct_0_x2041_67218_x296536513}[命令用来显示]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x347992259}

[**[display ip pool]{lang="EN-US"}**[ \[ *pool-name \|* **group** *group-name* \]]{lang="EN-US"}]{#struct_0_x2041_67218_x1442568070}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x617736938}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x2022065166}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_859173444}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_866469018}

[[network-operator]{lang="EN-US"}]{#struct_0_x2041_67218_1035300138}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x543419071}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x1769854265}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x2097726810}

[*[pool-name]{lang="EN-US"}*]{#struct_0_x2041_67218_x665415992}[：显示指定]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池的信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_x2041_67218_683239507}[：显示指定组内的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池信息。]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*[表示组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x617409258}

[[如果不指定任何参数，则显示所有]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x836828450}[地址池的简要信息；如果指定]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池的名称，将显示指定]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1403418646}

[[\# ]{lang="SV"}]{#struct_0_x2041_67218_x1195846763}[显示所有]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip pool]{lang="SV"}]{#struct_0_x2041_67218_56840803}

[Group name: a]{lang="SV"}

[  Pool name           Start IP address    End IP address      Free   In use]{lang="SV"}

[  aaa1                1.1.1.1             1.1.1.5             5      0]{lang="SV"}

[  aaa2                1.1.1.6             1.1.1.10            5      0]{lang="SV"}

[Group name: b]{lang="SV"}

[  Pool name           Start IP address    End IP address      Free   In use]{lang="SV"}

[  bbb                 1.1.2.1             1.1.2.5             4      1]{lang="SV"}

[                      2.2.2.1             2.2.2.5             5      0]{lang="SV"}

[[\# ]{lang="SV"}]{#struct_0_x2041_67218_x210278607}[显示组]{style="font-family:宋体"}[a]{lang="SV"}[的]{style="font-family:
宋体"}[PPP]{lang="EN-US"}[地址池的]{style="font-family:宋体"}[简要]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip pool group a]{lang="SV"}]{#struct_0_x2041_67218_x617343722}

[Group name: a]{lang="SV"}

[  Pool name           Start IP address    End IP address      Free   In use]{lang="SV"}

[  aaa1                1.1.1.1             1.1.1.5             5      0]{lang="SV"}

[  aaa2                1.1.1.6             1.1.1.10            5      0]{lang="SV"}

[[\# ]{lang="SV"}]{#struct_0_x2041_67218_x1155959672}[显示]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[bbb]{lang="SV"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip pool bbb]{lang="SV"}]{#struct_0_x2041_67218_1175286055}

[Group name: b]{lang="SV"}

[  Pool name           Start IP address    End IP address      Free   In use]{lang="SV"}

[  bbb                 1.1.2.1             1.1.2.5             4      1]{lang="SV"}

[                      2.2.2.1             2.2.2.5             5      0]{lang="SV"}

[In use IP addresses:]{lang="SV"}

[  IP address      Interface]{lang="SV"}

[  1.1.2.1         POS2/2/0]{lang="SV"}

[[表1-1 ]{lang="EN-US"}[display ip pool]{lang="EN-US"}]{#struct_0_x2041_67218_197783790}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_702626295}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_1740077830}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_x617540330}

[[Group name]{lang="EN-US"}]{#struct_0_x2041_67218_x794701186}

[[组的名称]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1475038796}

[[Pool ]{lang="SV"}[name]{lang="EN-US"}]{#struct_0_x2041_67218_x1444934939}

[[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x831411570}[地址池的名称]{style="font-family:宋体"}

[[Start IP address]{lang="SV"}]{#struct_0_x2041_67218_224751101}

[[IP]{lang="EN-US"}]{#struct_0_x2041_67218_x1232557038}[地址范围的起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[End IP address]{lang="SV"}]{#struct_0_x2041_67218_x617474794}

[[IP]{lang="EN-US"}]{#struct_0_x2041_67218_768255249}[地址范围的结束]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Free]{lang="EN-US"}]{#struct_0_x2041_67218_x71470039}

[[空闲]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_x1685728570}[地址个数]{style="font-family:宋体"}

[[In use]{lang="EN-US"}]{#struct_0_x2041_67218_x628696431}

[[已经分配出去的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_x1799219102}[地址个数]{style="font-family:宋体"}

[[In use IP addresses]{lang="EN-US"}]{#struct_0_x2041_67218_x617147114}

[[已经分配出去的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_x1978186061}[地址信息]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_x2041_67218_839378562}

[[已经分配出去的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_x324349950}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x2041_67218_x1036641681}

[[本端设备上为对端接口申请分配该]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_1098730024}[地址的接口]{style="font-family:宋体"}

[ ]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x617081578}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip pool]{lang="EN-US"}**]{#struct_0_x2041_67218_356277532}

::: {#1494867593 .myid}
[]{#_Toc404785030}[]{#struct_0_x2041_67218_1601252921}[]{#_Toc375915616}

**PPP和MP \-- PPP配置命令 \-- display ppp access-user**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}[ ppp access-user]{lang="EN-US"}**]{#struct_0_x2041_67218_x918799629}[命令用来显示]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接入用户的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1601318457}

[**[display ppp access-user]{lang="EN-US"}**[ { **interface** *interface-type interface-number* \[ **count** \] \| **ip-address** *ip-address* \| **ipv6-address** *ipv6-address* \| **username** *user-name* \| **[user-type]{style="color:black"}** { **[lac ]{style="color:black"}**\| **[lns]{style="color:black"}** \| **[pppoa]{style="color:black"}** \| **[pppoe]{style="color:black"}** } }]{lang="EN-US"}]{#struct_0_x2041_67218_x600454937}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x2126920752}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1440055473}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1750145526}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1601646137}

[[network-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x1356526372}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_34558334}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x2024753351}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_103113174}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2041_67218_1601711673}[：显示通过指定接口上线的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接入用户的简要信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示用户接入接口的类型及接口号。]{style="font-family:
宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x2041_67218_x2140170212}[：显示通过指定接口上线的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接入用户总数。]{style="font-family:宋体"}

[**[ip-address ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_x2041_67218_1804659665}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接入用户的详细信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[表示用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6-address ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_x2041_67218_x343917291}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接入用户的详细信息。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[表示用户的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[username ]{lang="EN-US"}***[user-name]{lang="EN-US"}*]{#struct_0_x2041_67218_x1559115083}[：显示指定用户名的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接入用户的详细信息。]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*[表示用户的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[user-type]{lang="EN-US" style="color:black"}**]{#struct_0_x2041_67218_x422689957}[：显示指定类型的在线用户的简要信息。]{style="font-family:
宋体"}

[**[lac]{lang="EN-US" style="color:black"}**]{#struct_0_x2041_67218_x1270080752}[：显示设备作为]{style="font-family:宋体"}[LAC]{lang="EN-US"}[的在线用户的简要信息。]{style="font-family:宋体"}

[**[lns]{lang="EN-US" style="color:black"}**]{#struct_0_x2041_67218_x1817377749}[：显示设备作为]{style="font-family:宋体"}[LNS]{lang="EN-US"}[的在线用户的简要信息。]{style="font-family:宋体"}

[**[pppoa]{lang="EN-US" style="color:black"}**]{#struct_0_x2041_67218_1172935841}[：显示用户类型为]{style="font-family:
宋体"}[PPPoA]{lang="EN-US"}[的在线用户的简要信息。]{style="font-family:宋体"}

[**[pppoe]{lang="EN-US" style="color:black"}**]{#struct_0_x2041_67218_x1965190731}[：显示用户类型为]{style="font-family:
宋体"}[PPPoE]{lang="EN-US"}[的在线用户的简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1601515065}

[[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_567634507}[接入用户的简要信息包括：用户对应的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口简名、用户的用户名、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x111115793}[接入用户的详细信息包括：用户对应的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口简名、用户]{style="font-family:宋体"}[User ID]{lang="EN-US"}[、用户的用户名、认证信息、用户上下行流量数、用户接入设备的时间等。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1797836828}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x772776610}[查看通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上线的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接入用户的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ppp access-user interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x2041_67218_1601580601}

[Interface     Username        MAC address     IP address       IPv6 address]{lang="EN-US"}

[VA0           user1@h3c       0001-0101-9101  192.168.100.173  -]{lang="EN-US"}

[VA1           h3cajerizerfsss 0001-0101-9101  192.168.80.173   2000::1]{lang="EN-US"}

[              Sserercerws]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x595647674}[查看通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上线的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接入用户总数。]{style="font-family:宋体"}

[[\<Sysname\> display ppp access-user interface gigabitethernet 1/0/1 count]{lang="EN-US"}]{#struct_0_x2041_67218_x568091900}

[Total users: 2]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ppp access-user]{lang="EN-US"}]{#struct_0_x2041_67218_1794086138}[命令显示信息描述表（简要信息）]{style="font-family:黑体"}

[]{#table_struct_0_140189710}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_1601908281}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_548849570}

[[Interface]{lang="EN-US"}]{#struct_0_x2041_67218_762621433}

[[用户对应的]{style="font-family:宋体"}[VA]{lang="EN-US"}]{#struct_0_x2041_67218_1601973817}[接口简名]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_x2041_67218_x142037466}

[[用户名（"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x2041_67218_1716767073}["表示用户不需要认证）]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x2041_67218_1601383992}

[[用户]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2041_67218_1779937128}[地址（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示用户为非]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[用户）]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_x2041_67218_x130319640}

[[用户]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_1601449528}[地址（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示用户未分配到]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址）]{style="font-family:宋体"}

[[IPv6 address]{lang="EN-US"}]{#struct_0_x2041_67218_x199738150}

[[用户]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x2041_67218_x1703509651}[地址（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示用户未分配到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址）]{style="font-family:宋体"}

[[Total users]{lang="EN-US"}]{#struct_0_x2041_67218_1601252920}

[[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x918865165}[接入用户总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_81998064}[查看]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[50.50.50.3]{lang="EN-US"}[的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接入用户的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ppp access-user ip-address 50.50.50.3]{lang="EN-US"}]{#struct_0_x2041_67218_1601318456}

[Basic:]{lang="EN-US"}

[  Interface: VA0]{lang="EN-US"}

[  User ID: 0x28000002]{lang="EN-US"}

[  Username: user1@hrss]{lang="EN-US"}

[  Domain: hrss]{lang="EN-US"}

[  Access interface: RAGG22]{lang="EN-US"}

[  Service-VLAN/Customer-VLAN: -/-]{lang="EN-US"}

[  MAC address: 0000-0000-0001]{lang="EN-US"}

[  IP address: 50.50.50.3]{lang="EN-US"}

[  IPv6 address: -]{lang="EN-US"}

[  IPv6 PD prefix: -]{lang="EN-US"}

[  VPN instance: 123]{lang="EN-US"}

[  Access type: PPPoE]{lang="EN-US"}

[  Authentication type: CHAP]{lang="EN-US"}

[ ]{lang="EN-US"}

[AAA:]{lang="EN-US"}

[  Authentication state: Authenticated]{lang="EN-US"}

[  Authorization state: Authorized]{lang="EN-US"}

[  Realtime accounting switch: Open]{lang="EN-US"}

[  Realtime accounting interval: 60s]{lang="EN-US"}

[  Login time: 2013-1-19  2:42:3:358]{lang="EN-US"}

[  Accounting start time: 2013-1-19  2:42:3:382]{lang="EN-US"}

[  Online time(hh:mm:ss): 0:7:34]{lang="EN-US"}

[  Accounting state: Accounting]{lang="EN-US"}

[  Idle cut: 0 sec  0 byte]{lang="EN-US"}

[  Session timeout: 12000 s]{lang="EN-US"}

[  Time remained: 8000 s]{lang="EN-US"}

[  Byte remained: 20971520 bytes]{lang="EN-US"}

[  Redirect WebURL: http://6.6.6.6]{lang="EN-US"}

[ ]{lang="EN-US"}

[ACL&QoS:]{lang="EN-US"}

[  User profile: profile123 (active)]{lang="EN-US"}

[  User group profile: -]{lang="EN-US"}

[  Inbound CAR: CIR 64000bps PIR 640000bps]{lang="EN-US"}

[  Outbound CAR: CIR 64000bps PIR 640000bps]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT:]{lang="EN-US"}

[  Global IP address: 111.8.0.200]{lang="EN-US"}

[  Port block: 28744-28748]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flow Statistic:]{lang="EN-US"}

[  IPv4 uplink   packets/bytes: 7/546]{lang="EN-US"}

[  IPv4 downlink packets/bytes: 0/0]{lang="EN-US"}

[  IPv6 uplink   packets/bytes: 0/0]{lang="EN-US"}

[  IPv6 downlink packets/bytes: 0/0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ITA:]{lang="EN-US"}

[  Level-1 uplink   packets/bytes: 100/128000]{lang="EN-US"}

[          downlink packets/bytes: 200/256000]{lang="EN-US"}

[  Level-2 uplink   packets/bytes: 100/128000]{lang="EN-US"}

[          downlink packets/bytes: 200/256000]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ppp access-user]{lang="EN-US"}]{#struct_0_x2041_67218_567568971}[命令显示信息描述表（详细信息）]{style="font-family:黑体"}

[]{#table_struct_0_159464824}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_800656214}

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_1601580600}

[[Basic]{lang="EN-US"}]{#struct_0_x2041_67218_x422100133}

[[基础信息]{style="font-family:宋体"}]{#struct_0_x2041_67218_x422165669}

[[Interface]{lang="EN-US"}]{#struct_0_x2041_67218_x595582138}

[[用户对应的]{style="font-family:宋体"}[VA]{lang="EN-US"}]{#struct_0_x2041_67218_611466448}[接口简名]{style="font-family:宋体"}

[[User ID]{lang="EN-US"}]{#struct_0_x2041_67218_1601908280}

[[用户]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2041_67218_548915106}

[[Username]{lang="EN-US"}]{#struct_0_x2041_67218_1601973816}

[[用户名（"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x2041_67218_x142103002}["表示用户不需要认证）]{style="font-family:宋体"}

[[Domain]{lang="EN-US"}]{#struct_0_x2041_67218_x422624424}

[[认证使用的]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_x2041_67218_354627372}[域名（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示未指定认证]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名）]{style="font-family:宋体"}

[[Access interface]{lang="EN-US"}]{#struct_0_x2041_67218_513842224}

[[用户接入的接口名]{style="font-family:宋体"}]{#struct_0_x2041_67218_1601383991}

[[Service-VLAN/Customer-VLAN]{lang="EN-US"}]{#struct_0_x2041_67218_x37566856}

[[服务提供商]{style="font-family:宋体"}[VLAN/]{lang="EN-US"}]{#struct_0_x2041_67218_x422689960}[用户]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示没有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[信息）]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x2041_67218_x1269622001}

[[用户]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2041_67218_241018586}[地址]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_x2041_67218_1779740520}

[[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_x1653001053}[地址（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示用户没有分配到]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址）]{style="font-family:宋体"}

[[IPv6 address]{lang="EN-US"}]{#struct_0_x2041_67218_1601449527}

[[用户的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x2041_67218_x198886182}[地址（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示用户没有分配到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址）]{style="font-family:宋体"}

[[IPv6 PD prefix]{lang="EN-US"}]{#struct_0_x2041_67218_x601550873}

[[用户的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x2041_67218_1601252919}[代理前缀（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示用户没有分配到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[代理前缀）]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_x2041_67218_x2140039140}

[[用户所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x2041_67218_1601515063}[（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示未绑定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例）]{style="font-family:宋体"}

[[Access type]{lang="EN-US"}]{#struct_0_x2041_67218_567765579}

[[用户的接入类型，目前支持]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_1484358290}[、]{style="font-family:宋体"}[PPPoA]{lang="EN-US"}[和]{style="font-family:宋体"}[L2TP]{lang="EN-US"}

[[Authentication type]{lang="EN-US"}]{#struct_0_x2041_67218_1601580599}

[[用户接入采用的认证类型，包括：]{style="font-family:宋体"}[PAP]{lang="EN-US"}]{#struct_0_x2041_67218_977806157}[、]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[、]{style="font-family:宋体"}[MS-CHAP]{lang="EN-US"}[、]{style="font-family:宋体"}[MS-CHAP-V2]{lang="EN-US"}

[[AAA]{lang="EN-US"}]{#struct_0_x2041_67218_x422886568}

[[AAA]{lang="EN-US"}]{#struct_0_x2041_67218_x458418012}[信息]{style="font-family:宋体"}

[[Authentication state]{lang="EN-US"}]{#struct_0_x2041_67218_x496050694}

[[用户的认证状态，包括：]{style="font-family:宋体"}]{#struct_0_x2041_67218_1601908279}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x2041_67218_549373855}[：表示未认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Authenticating]{lang="EN-US"}]{#struct_0_x2041_67218_1601973815}[：表示正在认证中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Authenticated]{lang="EN-US"}]{#struct_0_x2041_67218_x142168538}[：表示已认证]{lang="EN-US" style="font-family:宋体"}

[[Authorization state]{lang="EN-US"}]{#struct_0_x2041_67218_873248162}

[[用户的授权状态，包括：]{style="font-family:宋体"}]{#struct_0_x2041_67218_1601383990}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x2041_67218_1779806056}[：表示未授权]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Authorizing]{lang="EN-US"}]{#struct_0_x2041_67218_1601449526}[：表示正在授权中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Authorized]{lang="EN-US"}]{#struct_0_x2041_67218_x198820646}[：表示已授权]{lang="EN-US" style="font-family:宋体"}

[[Realtime accounting switch]{lang="EN-US"}]{#struct_0_x2041_67218_x933419355}

[[实时计费开关，取值包括：]{style="font-family:宋体"}]{#struct_0_x2041_67218_1601252918}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Open]{lang="EN-US"}]{#struct_0_x2041_67218_x919389450}[：表示开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Closed]{lang="EN-US"}]{#struct_0_x2041_67218_109576830}[：表示关闭]{lang="EN-US" style="font-family:宋体"}

[[Realtime accounting interval]{lang="EN-US"}]{#struct_0_x2041_67218_1601318454}

[[实时计费时间间隔，单位为秒（"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x2041_67218_x600389401}["表示未授权实时计费时间间隔）]{style="font-family:宋体"}

[[Login time]{lang="EN-US"}]{#struct_0_x2041_67218_1601646134}

[[用户接入时间]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1356591908}

[[Accounting start time]{lang="EN-US"}]{#struct_0_x2041_67218_x1084843299}

[[开始对用户计费的时间（"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x2041_67218_1601711670}["表示未对用户计费）]{style="font-family:宋体"}

[[Online time(hh:mm:ss)]{lang="EN-US"}]{#struct_0_x2041_67218_x172067672}

[[用户本次上线的在线时长]{style="font-family:宋体"}]{#struct_0_x2041_67218_342509727}

[[Accounting state]{lang="EN-US"}]{#struct_0_x2041_67218_x2140104676}

[[用户的计费状态，包括：]{style="font-family:宋体"}]{#struct_0_x2041_67218_1601515062}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Accounting]{lang="EN-US"}]{#struct_0_x2041_67218_567700043}[：表示正在计费]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stop]{lang="EN-US"}]{#struct_0_x2041_67218_302851077}[：表示停止计费]{lang="EN-US" style="font-family:宋体"}

[[Idle cut]{lang="EN-US"}]{#struct_0_x2041_67218_x423017640}

[[用户的闲置切断参数（在指定时间范围内流量没超过指定字节数，则认为该用户下线并强制将该用户下线）]{style="font-family:宋体"}]{#struct_0_x2041_67218_1884916693}

[[Session timeout]{lang="EN-US"}]{#struct_0_x2041_67218_x423083176}

[[用户的授权时间，单位为秒（"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x2041_67218_1467571778}["表示未对用户指定授权时间）]{style="font-family:宋体"}

[[Time remained]{lang="EN-US"}]{#struct_0_x2041_67218_x845559873}

[[用户的剩余时间，单位为秒（"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x2041_67218_x422100136}["表示未对用户指定授权时间）]{style="font-family:宋体"}

[[Byte remained]{lang="EN-US"}]{#struct_0_x2041_67218_1492779220}

[[用户的剩余流量，单位为字节（"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x2041_67218_594558683}["表示未对用户指定授权流量）]{style="font-family:宋体"}

[[Redirect WebURL]{lang="EN-US"}]{#struct_0_x2041_67218_x422165672}

[[用户的上线推送页面地址（"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x2041_67218_x820075777}["表示未对用户指定上线推送页面地址]{style="font-family:宋体"}

[[ACL&QoS]{lang="EN-US"}]{#struct_0_x2041_67218_x422624423}

[[ACL]{lang="EN-US"}]{#struct_0_x2041_67218_354955052}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[User profile]{lang="EN-US"}]{#struct_0_x2041_67218_1601580598}

[[授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_x2041_67218_977871693}[名称（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示未授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[）]{style="font-family:宋体"}

[[括号中的]{style="font-family:宋体"}[active]{lang="EN-US"}]{#struct_0_x2041_67218_1601908278}[表示授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发成功，]{style="font-family:宋体"}[inactive]{lang="EN-US"}[表示授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发失败]{style="font-family:宋体"}

[[User group profile]{lang="EN-US"}]{#struct_0_x2041_67218_549439391}

[[授权的]{style="font-family:宋体"}[User Group Profile]{lang="EN-US"}]{#struct_0_x2041_67218_462154236}[（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示未授权]{style="font-family:宋体"}[User Group Profile]{lang="EN-US"}[）]{style="font-family:宋体"}

[[括号中的]{style="font-family:宋体"}[active]{lang="EN-US"}]{#struct_0_x2041_67218_1601973814}[表示授权]{style="font-family:宋体"}[User Group Profile]{lang="EN-US"}[下发成功，]{style="font-family:宋体"}[inactive]{lang="EN-US"}[表示授权]{style="font-family:宋体"}[User Group Profile]{lang="EN-US"}[下发失败]{style="font-family:宋体"}

[[Inbound CAR]{lang="EN-US"}]{#struct_0_x2041_67218_x142234074}

[[授权的入方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_x2041_67218_1601383997}[：]{style="font-family:宋体"}[CIR]{lang="EN-US"}[承诺信息速率和]{style="font-family:宋体"}[PIR]{lang="EN-US"}[峰值速度]{style="font-family:宋体"}

[[Outbound CAR]{lang="EN-US"}]{#struct_0_x2041_67218_1779609448}

[[授权的出方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_x2041_67218_1601252925}[：]{style="font-family:宋体"}[CIR]{lang="EN-US"}[承诺信息速率和]{style="font-family:宋体"}[PIR]{lang="EN-US"}[峰值速度]{style="font-family:宋体"}

[[NAT]{lang="EN-US"}]{#struct_0_x2041_67218_x422689959}

[[NAT]{lang="EN-US"}]{#struct_0_x2041_67218_x422755495}[信息]{style="font-family:宋体"}

[[Global IP address]{lang="EN-US"}]{#struct_0_x2041_67218_x1200446541}

[[用户的公网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_1817384921}[地址（进行]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[地址转换后显示此字段，关于]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[地址转换的详细介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[业务配置指导"中的"]{style="font-family:宋体"}[NAT]{lang="EN-US"}["）]{style="font-family:宋体"}

[[Port block]{lang="EN-US"}]{#struct_0_x2041_67218_x422821031}

[[用户的端口块：起始端口]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x2041_67218_1879012984}[结束端口（进行]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[地址转换后显示此字段）]{style="font-family:宋体"}

[[Flow Statistic]{lang="EN-US"}]{#struct_0_x2041_67218_x422886567}

[[流量统计信息]{style="font-family:宋体"}]{#struct_0_x2041_67218_x458352476}

[[IPv4 uplink   packets/bytes]{lang="EN-US"}]{#struct_0_x2041_67218_x611186439}

[[用户的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x2041_67218_x422952103}[上行计费流量的报文数和字节数]{style="font-family:宋体"}

[[IPv4 downlink packets/bytes ]{lang="EN-US"}]{#struct_0_x2041_67218_x1632179469}

[[用户的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x2041_67218_x423017639}[下行计费流量的报文数和字节数]{style="font-family:宋体"}

[[IPv6 uplink   packets/bytes]{lang="EN-US"}]{#struct_0_x2041_67218_1884457946}

[[用户的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x2041_67218_x851061573}[上行计费流量的报文数和字节数]{style="font-family:宋体"}

[[IPv6 downlink packets/bytes]{lang="EN-US"}]{#struct_0_x2041_67218_x423083175}

[[用户的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x2041_67218_1467637314}[下行计费流量的报文数和字节数]{style="font-family:宋体"}

[[ITA]{lang="EN-US"}]{#struct_0_x2041_67218_x422100135}

[[ITA]{lang="EN-US"}]{#struct_0_x2041_67218_1492844756}[统计信息（使能]{style="font-family:宋体"}[ITA]{lang="EN-US"}[后才会显示]{style="font-family:宋体"}[ITA]{lang="EN-US"}[统计信息；如果配置了]{style="font-family:宋体"}**[traffic-separate enable]{lang="EN-US"}**[命令，]{style="font-family:宋体"}[Flow Statistic]{lang="EN-US"}[统计信息中将不包含]{style="font-family:宋体"}[ITA]{lang="EN-US"}[统计信息。关于]{style="font-family:宋体"}[ITA]{lang="EN-US"}[和]{style="font-family:宋体"}**[traffic-separate enable]{lang="EN-US"}**[命令的详细介绍请参见"安全配置指导"中的"]{style="font-family:宋体"}[AAA]{lang="EN-US"}["）]{style="font-family:宋体"}

[[Level-n uplink   packets/bytes]{lang="EN-US"}]{#struct_0_x2041_67218_x1004197356}

[[             downlink packets/bytes]{lang="EN-US"}]{#struct_0_x2041_67218_x422165671}

[[计费等级为]{style="font-family:宋体"}[n]{lang="EN-US"}]{#struct_0_x2041_67218_x820272385}[的上行和下行流量的报文数和字节数，]{style="font-family:宋体"}[n]{lang="EN-US"}[的取值由]{style="font-family:宋体"}**[traffic level]{lang="EN-US"}**[命令决定，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[ ]{lang="SV"}

::: {#-1934014052 .myid}
[]{#_Toc404785031}[]{#struct_0_x2041_67218_x600127258}[]{#_Toc371343251}

**PPP和MP \-- PPP配置命令 \-- display ppp compression iphc**

------------------------------------------------------------------------

[**[display ppp compression iphc]{lang="EN-US"}**]{#struct_0_x2041_67218_x1754444118}[命令用来显示]{style="font-family:
宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1601646140}

[**[display ppp compression iphc]{lang="EN-US"}**[ { **rtp** \| **tcp** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2041_67218_x1356854055}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1409665993}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1309108918}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1601711676}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x2140497892}

[[network-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x1419579883}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1684203242}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2041_67218_1601515068}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_568355403}

[**[rtp]{lang="EN-US"}**]{#struct_0_x2041_67218_670644543}[：显示]{style="font-family:宋体"}[IPHC RTP]{lang="EN-US"}[头压缩的统计信息。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_x2041_67218_1132285060}[：显示]{style="font-family:宋体"}[IPHC TCP]{lang="EN-US"}[头压缩的统计信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x242626984}[：显示指定接口的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。不指定本参数时，将显示所有接口的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1601580604}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x2041_67218_x595844282}[MP]{lang="EN-US"}[链路使用]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[时，如果采用虚拟模板接口、]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口，压缩在]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口上进行，这时在]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口下可以看到压缩信息；如果采用]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口，在]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口下可以看到压缩信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当普通]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1736443620}[PPP]{lang="EN-US"}[链路使用]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[时，压缩在物理链路上进行，在物理接口下可以看到压缩信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1971957152}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1601908284}[显示]{style="font-family:宋体"}[IPHC RTP]{lang="EN-US"}[头压缩的统计信息。]{style="font-family:宋体"}

[[\<Sysname\>display ppp compression iphc rtp]{lang="EN-US"}]{#struct_0_x2041_67218_548652962}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--Slot1\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Interface: Virtual-Access0]{lang="EN-US"}

[  Received:]{lang="EN-US"}

[    Compressed/Error/Total: 0/0/0 packets]{lang="EN-US"}

[  Sent:]{lang="EN-US"}

[    Compressed/Total: 0/0 packets]{lang="EN-US"}

[    Sent/Saved/Total: 0/0/0 bytes]{lang="EN-US"}

[    Packet-based compression ratio: 0%]{lang="EN-US"}

[    Byte-based compression ratio: 0%]{lang="EN-US"}

[  Connections:]{lang="EN-US"}

[    Rx/Tx: 16/16]{lang="EN-US"}

[    Five-Minute-Miss: 0 (Misses/5Mins)]{lang="EN-US"}

[    Max-Miss: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--Slot3\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Interface: Virtual-Access0]{lang="EN-US"}

[  Received:]{lang="EN-US"}

[    Compressed/Error/Total: 20/5/40 packets]{lang="EN-US"}

[  Sent:]{lang="EN-US"}

[    Compressed/Total: 34/40 packets]{lang="EN-US"}

[    Sent/Saved/Total: 1131/1210/2341 bytes]{lang="EN-US"}

[    Packet-based compression ratio: 85%]{lang="EN-US"}

[    Byte-based compression ratio: 51%]{lang="EN-US"}

[  Connections:]{lang="EN-US"}

[    Rx/Tx: 16/16]{lang="EN-US"}

[    Five-Minute-Miss: 0 (Misses/5Mins)]{lang="EN-US"}

[    Max-Miss: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--Slot4\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Interface: Virtual-Access0]{lang="EN-US"}

[  Received:]{lang="EN-US"}

[    Compressed/Error/Total: 102/13/181 packets]{lang="EN-US"}

[  Sent:]{lang="EN-US"}

[    Compressed/Total: 161/176 packets]{lang="EN-US"}

[    Sent/Saved/Total: 5582/5771/11353 bytes]{lang="EN-US"}

[    Packet-based compression ratio: 91%]{lang="EN-US"}

[    Byte-based compression ratio: 50%]{lang="EN-US"}

[  Connections:]{lang="EN-US"}

[    Rx/Tx: 16/16]{lang="EN-US"}

[    Five-Minute-Miss: 0 (Misses/5Mins)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1601973820}[显示]{style="font-family:宋体"}[IPHC TCP]{lang="EN-US"}[头压缩的统计信息。]{style="font-family:宋体"}

[[\<Sysname\>display ppp compression iphc tcp]{lang="EN-US"}]{#struct_0_x2041_67218_x141971927}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--Slot1\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Interface: Virtual-Access0]{lang="EN-US"}

[  Received:]{lang="EN-US"}

[    Compressed/Error/Total: 0/0/0 packets]{lang="EN-US"}

[  Sent:]{lang="EN-US"}

[    Compressed/Total: 0/0 packets]{lang="EN-US"}

[    Sent/Saved/Total: 0/0/0 bytes]{lang="EN-US"}

[    Packet-based compression ratio: 0%]{lang="EN-US"}

[    Byte-based compression ratio: 0%]{lang="EN-US"}

[  Connections:]{lang="EN-US"}

[    Rx/Tx: 16/16]{lang="EN-US"}

[    Five-Minute-Miss: 0 (Misses/5Mins)]{lang="EN-US"}

[    Max-Miss: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--Slot3\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Interface: Virtual-Access0]{lang="EN-US"}

[  Received:]{lang="EN-US"}

[    Compressed/Error/Total: 20/5/40 packets]{lang="EN-US"}

[  Sent:]{lang="EN-US"}

[    Compressed/Total: 34/40 packets]{lang="EN-US"}

[    Sent/Saved/Total: 1131/1210/2341 bytes]{lang="EN-US"}

[    Packet-based compression ratio: 85%]{lang="EN-US"}

[    Byte-based compression ratio: 51%]{lang="EN-US"}

[  Connections:]{lang="EN-US"}

[    Rx/Tx: 16/16]{lang="EN-US"}

[    Five-Minute-Miss: 0 (Misses/5Mins)]{lang="EN-US"}

[    Max-Miss: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--Slot4\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Interface: Virtual-Access0]{lang="EN-US"}

[  Received:]{lang="EN-US"}

[    Compressed/Error/Total: 102/13/181 packets]{lang="EN-US"}

[  Sent:]{lang="EN-US"}

[    Compressed/Total: 161/176 packets]{lang="EN-US"}

[    Sent/Saved/Total: 5582/5771/11353 bytes]{lang="EN-US"}

[    Packet-based compression ratio: 91%]{lang="EN-US"}

[    Byte-based compression ratio: 50%]{lang="EN-US"}

[  Connections:]{lang="EN-US"}

[    Rx/Tx: 16/16]{lang="EN-US"}

[    Five-Minute-Miss: 0 (Misses/5Mins)]{lang="EN-US"}

[    Max-Miss: 0]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ppp compression iphc]{lang="EN-US"}]{#struct_0_x2041_67218_x1686141364}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_208556649}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1127499362}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_x395383001}

[[Received::]{lang="EN-US"}]{#struct_0_x2041_67218_1246726280}

[[  Compressed/Error/Total:]{lang="EN-US"}]{#struct_0_x2041_67218_743737291}

[[收到报文的统计信息：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1127564898}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Compressed]{lang="EN-US"}]{#struct_0_x2041_67218_x170651017}[：被压缩的报文数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error]{lang="EN-US"}]{#struct_0_x2041_67218_x1127237218}[：错误报文数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Total]{lang="EN-US"}]{#struct_0_x2041_67218_x580232454}[：总的报文数]{lang="EN-US" style="font-family:宋体"}

[[Sent::]{lang="EN-US"}]{#struct_0_x2041_67218_x1127171682}

[[  Compressed/Total:]{lang="EN-US"}]{#struct_0_x2041_67218_1352002772}

[[  Sent/Saved/Total:]{lang="EN-US"}]{#struct_0_x2041_67218_902773728}

[[  Packet-based compression ratio:]{lang="EN-US"}]{#struct_0_x2041_67218_x1127368290}

[[  Byte-based compression ratio:]{lang="EN-US"}]{#struct_0_x2041_67218_733067081}

[[发送报文的统计信息：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1127302754}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Compressed]{lang="EN-US"}]{#struct_0_x2041_67218_1646646500}[：被压缩的报文数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Total]{lang="EN-US"}]{#struct_0_x2041_67218_x1126975074}[：总的报文数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sent]{lang="EN-US"}]{#struct_0_x2041_67218_708314047}[：实际发送的字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Saved]{lang="EN-US"}]{#struct_0_x2041_67218_x1126909538}[：节省的字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Total]{lang="EN-US"}]{#struct_0_x2041_67218_1216760907}[：在不压缩的情况下，需要发送的字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Packet-based compression ratio]{lang="EN-US"}]{#struct_0_x2041_67218_x1127499363}[：基于报文的压缩率，表示压缩的报文在总发送报文中的比率，即（]{lang="EN-US" style="font-family:宋体"}[Compressed]{lang="EN-US"}[÷]{lang="EN-US" style="font-family:宋体"}[Total]{lang="EN-US"}[）×]{lang="EN-US" style="font-family:宋体"}[100%]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Byte-based compression ratio]{lang="EN-US"}]{#struct_0_x2041_67218_1170700940}[：基于字节的压缩率，表示压缩后带宽节省的百分比，即（]{lang="EN-US" style="font-family:宋体"}[Saved]{lang="EN-US"}[÷]{lang="EN-US" style="font-family:宋体"}[Total]{lang="EN-US"}[）×]{lang="EN-US" style="font-family:宋体"}[100%]{lang="EN-US"}

[[Connections:]{lang="EN-US"}]{#struct_0_x2041_67218_x1127433827}

[[  Rx/Tx:]{lang="EN-US"}]{#struct_0_x2041_67218_1243687619}

[[  Five-Minute-Miss:]{lang="EN-US"}]{#struct_0_x2041_67218_x1127630435}

[[  Max-Miss:]{lang="EN-US"}]{#struct_0_x2041_67218_x1482157075}

[[连接信息：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1127564899}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Rx]{lang="EN-US"}]{#struct_0_x2041_67218_x1736734958}[：作为接收方，可解压缩的连接数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tx]{lang="EN-US"}]{#struct_0_x2041_67218_x1127237219}[：作为发送方，可压缩的连接数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Five-Minute-Miss]{lang="EN-US"}]{#struct_0_x2041_67218_985851487}[：最后]{style="font-family:宋体"}[5]{lang="EN-US"}[分钟内，查找表项失败的次数（系统每]{style="font-family:宋体"}[5]{lang="EN-US"}[分钟统计一次查找表项失败的次数，本字段显示的是最新一次统计的结果）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Max-Miss]{lang="EN-US"}]{#struct_0_x2041_67218_x1127171683}[：查找表项失败的最大次数（将每次统计的查找表项失败的次数进行比较，得到最大值在这个字段显示）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1376880583}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp compression iphc enable]{lang="EN-US"}**]{#struct_0_x2041_67218_x187328169}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}**[reset ppp compression iphc]{lang="EN-US"}**]{#struct_0_x2041_67218_695312311}

::: {#1670910300 .myid}
[]{#_Toc404785032}[]{#struct_0_x2041_67218_1868272245}

**PPP和MP \-- PPP配置命令 \-- ip address ppp-negotiate**

------------------------------------------------------------------------

[**[ip address ppp-negotiate]{lang="EN-US"}**]{#struct_0_x2041_67218_1280195912}[命令用来为接口配置]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址可协商属性，使接口接受]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协商产生的由]{style="font-family:宋体"}[Server]{lang="EN-US"}[端分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ip address ppp-negotiate]{lang="EN-US"}**]{#struct_0_x2041_67218_x879575461}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1419993139}

[**[ip address ppp-negotiate]{lang="EN-US"}**]{#struct_0_x2041_67218_704357932}

[**[undo ip address ppp-negotiate]{lang="EN-US"}**]{#struct_0_x2041_67218_291848994}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x617671405}

[[接口没有配置]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_x1565172157}[地址可协商属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1743998113}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x710650868}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1422273824}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x754915390}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1281862637}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1100123445}

[**[ip address ppp-negotiate]{lang="EN-US"}**]{#struct_0_x2041_67218_50310964}[命令和]{style="font-family:宋体"}**[ip address]{lang="EN-US"}**[命令互斥，二者不能同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x617605869}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1250807631}[为接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址可协商属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x35744359}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ip address ppp-negotiate]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1265855297}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip address]{lang="EN-US"}**]{#struct_0_x2041_67218_1057018561}[（]{lang="EN-US" style="font-family:宋体"}[三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[业务]{style="font-family:宋体"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remote address]{lang="EN-US"}**]{#struct_0_x2041_67218_x967849489}
:::

::: {#-245081024 .myid}
[]{#_Toc332278968}[]{#_Toc259009502}[]{#_Toc404785033}[]{#struct_0_x2041_67218_2081550739}[]{#_Toc349654526}

**PPP和MP \-- PPP配置命令 \-- ip pool**

------------------------------------------------------------------------

[**[ip pool]{lang="EN-US"}**]{#struct_0_x2041_67218_x617802477}[命令]{style="font-family:宋体"}[用来配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池。]{style="font-family:宋体"}

[**[undo ip pool]{lang="EN-US"}**]{#struct_0_x2041_67218_x10032663}[命令]{style="font-family:宋体"}[用来删除指定的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池或删除指定]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池下的指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围，该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围必须与配置的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围相同]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x738272710}

[**[ip pool]{lang="EN-US"}**[ *pool-name* *start-ip-address* \[ *end-ip-address* \] \[ **group** *group-name* \]]{lang="EN-US"}]{#struct_0_x2041_67218_x718157017}

[**[undo ip pool ]{lang="EN-US"}***[pool-name]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ *start-ip-address* \[ *end-ip-address* \] \]]{lang="EN-US"}]{#struct_0_x2041_67218_x57522509}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_333733798}

[[没有配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_1295363695}[地址池。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1740241656}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x174475081}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x617736941}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x2021475335}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x783146041}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x718197352}

[*[pool-name]{lang="EN-US"}*]{#struct_0_x2041_67218_1922975407}[：]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[start-ip-address]{lang="EN-US"}*[ \[ *end-ip-address* \]]{lang="EN-US"}]{#struct_0_x2041_67218_x636365592}[：定义一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}*[start-ip-address]{lang="EN-US"}*[为起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[end-ip-address]{lang="EN-US"}*[为结束]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。一个起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和结束]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的地址为一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}[如果不指定结束]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围]{style="font-family:宋体"}[中只有一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，即起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}**[ *group-name*]{lang="EN-US"}]{#struct_0_x2041_67218_x1087005887}[：指定]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池所在的组。]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*[表示组]{style="font-family:宋体"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。不指定本参数时，组名称为]{style="font-family:宋体"}[default]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x574275347}

[[系统支持多个地址空间，以此来实现对]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x2041_67218_1511546793}[的支持，每个地址空间可以对应一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，不同地址空间中可以存在相同的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[系统用组来划分地址空间，每个组表示一个地址空间。设备上可以存在多个组。一个组下可以包含多个]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x617409261}[地址池，一个]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池下可以包含多个]{style="font-family:宋体"}[IP]{lang="SV"}[地址范围]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x837418273}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1755543696}[PPP]{lang="EN-US"}[地址池只能属于一个组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x2041_67218_x695214724}[PPP]{lang="EN-US"}[地址池下可以包含多个]{style="font-family:宋体"}[IP]{lang="SV"}[地址范围，]{style="font-family:宋体"}[一次只能配置一个]{style="font-family:宋体"}[IP]{lang="SV"}[地址范围，]{style="font-family:宋体"}[可以通过多次配置本命令来配置多个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同组内的]{style="font-family:宋体"}]{#struct_0_x2041_67218_1040775148}[IP]{lang="NO-BOK"}[地址范围]{style="font-family:宋体"}[可以重叠，同一个组内的]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[地址范围]{style="font-family:宋体"}[不可以重叠。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x2041_67218_1617356200}[IP]{lang="EN-US"}[地址范围中包含的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址数最多为]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1590235523}[PPP]{lang="EN-US"}[地址池中包含的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址数最多]{style="font-family:宋体"}[为]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对]{style="font-family:宋体"}]{#struct_0_x2041_67218_1701737647}[PPP]{lang="EN-US"}[地址池配置的修改不会影响到已经分配出去的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的使用。比如，从]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[a]{lang="EN-US"}[中分配出去一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[后，删除]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[a]{lang="EN-US"}[，已经分配出去的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[仍可以正常使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1195409067}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x617343725}[配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[aaa]{lang="EN-US"}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围为]{style="font-family:宋体"}[129.102.0.1]{lang="EN-US"}[到]{style="font-family:宋体"}[129.102.0.10]{lang="EN-US"}[，]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池所在的组为]{style="font-family:宋体"}[a]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1155894136}

[\[Sysname\] ip pool aaa 129.102.0.1 129.102.0.10 group a]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_845397670}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip pool]{lang="EN-US"}**]{#struct_0_x2041_67218_x186219489}
:::

::: {#-1199070574 .myid}
[]{#_Toc404785034}[]{#struct_0_x2041_67218_1116143670}[]{#_Toc372732484}[]{#_Toc372654224}

**PPP和MP \-- PPP配置命令 \-- ip pool gateway**

------------------------------------------------------------------------

[**[ip pool gateway]{lang="EN-US"}**]{#struct_0_x2041_67218_x1401247944}[命令用来配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池的网关地址。]{style="font-family:宋体"}

[**[undo ip pool gateway]{lang="EN-US"}**]{#struct_0_x2041_67218_1372965149}[命令用来删除指定]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池的网关地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1766035893}

[**[ip pool ]{lang="EN-US"}***[pool-name]{lang="EN-US"}***[ gateway ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x2041_67218_x2007524661}

[**[undo ip pool ]{lang="EN-US"}***[pool-name]{lang="EN-US"}[ ]{lang="EN-US"}***[gateway]{lang="EN-US"}**]{#struct_0_x2041_67218_2058951203}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1116340278}

[[没有为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_1726285127}[地址池配置网关地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2096748110}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1794877236}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1244515394}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1640555883}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1637148009}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1999616467}

[*[pool-name]{lang="EN-US"}*]{#struct_0_x2041_67218_1116274742}[：]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。该]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池必须已经存在。]{style="font-family:宋体"}

[*[ip-address]{lang="SV"}*]{#struct_0_x2041_67218_x1437411369}[：]{style="font-family:宋体"}[PPP]{lang="SV"}[地址池的网关地址。]{style="font-family:
宋体"}

[**[vpn-instance]{lang="SV"}**]{#struct_0_x2041_67218_x574113117}[ *vpn-instance-name*]{lang="SV"}[：]{style="font-family:宋体"}[网关地址]{style="font-family:宋体"}[所在的]{style="font-family:宋体"}[VPN]{lang="SV"}[实例。]{style="font-family:宋体"}[指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。]{style="font-family:宋体"}*[vpn-instance-name]{lang="SV"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="SV"}[的]{style="font-family:宋体"}[VPN]{lang="SV"}[实例名称，为]{style="font-family:
宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[31]{lang="SV"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[不指定本参数时，表示指定的是公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_717846165}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1263780638}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当同时配置了]{style="font-family:宋体"}]{#struct_0_x2041_67218_1557381209}[PPP]{lang="EN-US"}[地址池的网关地址和接入接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址时，会使用接入接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_1116995638}[地址池只能配置一个网关地址，不同]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池配置的网关地址不能相同，即为不同]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池配置网关地址时，]{lang="EN-US" style="font-family:宋体"}[ip-address]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[vpn-instance-name]{lang="EN-US"}[不能完全相同。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_2072666574}[地址池的网关地址可以配置为任意一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，只要不同]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池的网关地址不冲突即可。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_933487725}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_679204317}[为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[aaa]{lang="EN-US"}[配置网关地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，所在]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例为]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1377688919}

[\[Sysname\] ip pool aaa gateway 1.1.1.1 vpn-instance test]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x35876884}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip pool]{lang="EN-US"}**]{#struct_0_x2041_67218_x1165453440}
:::

::: {#-826229410 .myid}
[]{#_Toc404785035}[]{#struct_0_x2041_67218_1437733891}

**PPP和MP \-- PPP配置命令 \-- link-protocol ppp**

------------------------------------------------------------------------

[**[link-protocol]{lang="EN-US"}**[ **ppp**]{lang="EN-US"}]{#struct_0_x2041_67218_1735035214}[命令用来配置接口封装的链路层协议为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_770166292}

[**[link-protocol ppp]{lang="EN-US"}**]{#struct_0_x2041_67218_x1151393783}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2021393731}

[[除以太网接口、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2041_67218_x617540333}[接口、]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口外，其它接口封装的链路层协议均为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x794635650}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1116306372}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1094468041}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1072547346}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_415898539}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1733113931}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1473544926}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[封装的链路层协议为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x617474797}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol ppp]{lang="EN-US"}
:::

::: {#-1665071920 .myid}
[]{#_Toc404785036}[]{#struct_0_x2041_67218_x1127171684}[]{#_Toc376765042}[]{#_Toc372640635}[]{#_Toc185927308}[]{#_Toc123026768}

**PPP和MP \-- PPP配置命令 \-- nas-port-type**

------------------------------------------------------------------------

[**[nas-port-type]{lang="EN-US"}**]{#struct_0_x2041_67218_x1127368292}[命令用来配置接口的]{style="font-family:宋体"}[nas-port-type]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[**[undo nas-port-type]{lang="EN-US"}**]{#struct_0_x2041_67218_1895866495}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1127302756}

[**[nas-port-type]{lang="EN-US"}**[ { **802.11** *\|* **adsl-cap** *\|* **adsl-dmt** *\|* **async** *\|* **cable** *\|* **ethernet** *\|* **g.3-fax** *\|* **hdlc** *\|* **idsl** *\|* **isdn-async-v110** *\|* **isdn-async-v120** *\|* **isdn-sync** *\|* **piafs** *\|* **sdsl** *\|* **sync** *\|* **virtual** *\|* **wireless-other** *\|* **x.25** *\|* **x.75** *\|* **xdsl** }]{lang="EN-US"}]{#struct_0_x2041_67218_483847086}

[**[undo nas-port-type]{lang="EN-US"}**]{#struct_0_x2041_67218_x400228194}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1126975076}

[[nas-port-type]{lang="EN-US"}]{#struct_0_x2041_67218_x454485367}[属性由]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户的业务类型和承载链路类型决定：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_x1126909540}[是]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[业务，当]{style="font-family:宋体"}[承载链路类型为]{lang="EN-US" style="font-family:宋体"}[三层虚拟以太网接口时]{style="font-family:宋体"}[，]{lang="EN-US" style="font-family:
宋体"}[nas-port-type]{lang="EN-US"}[属性为]{lang="EN-US" style="font-family:宋体"}**[xdsl]{lang="EN-US"}**[，否则]{lang="EN-US" style="font-family:宋体"}[nas-port-type]{lang="EN-US"}[属性为]{lang="EN-US" style="font-family:宋体"}**[ethernet]{lang="EN-US"}**[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_x1127499365}[是]{style="font-family:宋体"}[PPP]{lang="EN-US"}[o]{lang="EN-US"}[A]{lang="EN-US"}[业务]{style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[nas-port-type]{lang="EN-US"}[属性为]{lang="EN-US" style="font-family:宋体"}**[xdsl]{lang="EN-US"}**[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_1977269994}[是]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[业务]{style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[nas-port-type]{lang="EN-US"}[属性为]{lang="EN-US" style="font-family:宋体"}**[virtual]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x2113922099}

[[虚拟模板接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1127433829}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_437118565}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x463045265}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1127630437}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1650010807}

[**[802.11]{lang="EN-US"}**]{#struct_0_x2041_67218_x1766054640}[：符合]{style="font-family:宋体"}[Wireless-IEEE 802.11]{lang="EN-US"}[标准的接口类型，对应的编码值为]{style="font-family:宋体"}[19]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[adsl-cap]{lang="EN-US"}**]{#struct_0_x2041_67218_x1127564901}[：]{style="font-family:宋体"}[ADSL-CAP]{lang="EN-US"}[（]{style="font-family:宋体"}[Asymmetric DSL]{lang="EN-US"}[，]{style="font-family:宋体"}[Carrierless Amplitude Phase Modulation]{lang="EN-US"}[）接口类型，]{style="font-family:
宋体"}

[[对应的编码值为]{style="font-family:宋体"}[12]{lang="EN-US"}]{#struct_0_x2041_67218_x1380963349}[。]{style="font-family:宋体"}

[**[adsl-dmt]{lang="EN-US"}**]{#struct_0_x2041_67218_1453506174}[：]{style="font-family:宋体"}[ADSL-DMT]{lang="EN-US"}[（]{style="font-family:宋体"}[Asymmetric DSL]{lang="EN-US"}[，]{style="font-family:宋体"}[Discrete Multi-Tone]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[13]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[async]{lang="EN-US"}**]{#struct_0_x2041_67218_x1127237221}[：]{style="font-family:宋体"}[Async]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cable]{lang="EN-US"}**]{#struct_0_x2041_67218_629686663}[：]{style="font-family:宋体"}[Cable]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[17]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ethernet]{lang="EN-US"}**]{#struct_0_x2041_67218_1980704105}[：]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g.3-fax]{lang="EN-US"}**]{#struct_0_x2041_67218_x1127171685}[：]{style="font-family:宋体"}[G.3 Fax]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[hdlc]{lang="EN-US"}**]{#struct_0_x2041_67218_1755287299}[：]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[idsl]{lang="EN-US"}**]{#struct_0_x2041_67218_x647695090}[：]{style="font-family:宋体"}[IDSL]{lang="EN-US"}[（]{style="font-family:宋体"}[ISDN Digital Subscriber Line]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[14]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[isdn-async-v110]{lang="EN-US"}**]{#struct_0_x2041_67218_x1127368293}[：]{style="font-family:宋体"}[ISDN Async V.110]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[isdn-async-v120]{lang="EN-US"}**]{#struct_0_x2041_67218_329782554}[：]{style="font-family:宋体"}[ISDN Async V.120]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[isdn-sync]{lang="EN-US"}**]{#struct_0_x2041_67218_1251912848}[：]{style="font-family:宋体"}[ISDN Sync]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[piafs]{lang="EN-US"}**]{#struct_0_x2041_67218_x1127302757}[：符合]{style="font-family:宋体"}[PIAFS]{lang="EN-US"}[（]{style="font-family:宋体"}[PHS]{lang="EN-US"}[（]{style="font-family:宋体"}[Personal Handyphone System]{lang="EN-US"}[）]{style="font-family:宋体"}[Internet Access Forum Standard]{lang="EN-US"}[）标准的接口类型，对应的编码值为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sdsl]{lang="EN-US"}**]{#struct_0_x2041_67218_x1082236855}[：]{style="font-family:宋体"}[SDSL]{lang="EN-US"}[（]{style="font-family:宋体"}[Symmetric DSL]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[11]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sync]{lang="EN-US"}**]{#struct_0_x2041_67218_x1471914275}[：]{style="font-family:宋体"}[Sync]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[virtual]{lang="EN-US"}**]{#struct_0_x2041_67218_x1126975077}[：]{style="font-family:宋体"}[Virtual]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[wireless-other]{lang="EN-US"}**]{#struct_0_x2041_67218_1111598574}[：]{style="font-family:宋体"}[Wireless-other]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[18]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[x.25]{lang="EN-US"}**]{#struct_0_x2041_67218_x1126909541}[：]{style="font-family:宋体"}[X.25]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[x.75]{lang="EN-US"}**]{#struct_0_x2041_67218_x705356786}[：]{style="font-family:宋体"}[X.75]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[9]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[xdsl]{lang="EN-US"}**]{#struct_0_x2041_67218_x1127499358}[：]{style="font-family:宋体"}[XDSL]{lang="EN-US"}[（]{style="font-family:宋体"}[Digital Subscriber Line of unknown type]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1127433822}

[[本命令配置的]{style="font-family:宋体"}[nas-port-type]{lang="EN-US"}]{#struct_0_x2041_67218_1646972146}[属性主要应用于]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证计费时所携带的]{style="font-family:宋体"}[nas-port-type]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[关于]{style="font-family:宋体"}[nas-port-type]{lang="EN-US"}]{#struct_0_x2041_67218_x1127630430}[属性的详细介绍请参见]{style="font-family:宋体"}[RFC 2865]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1078872548}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1216654726}[配置虚拟模板接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[nas-port-type]{lang="EN-US"}[属性为]{style="font-family:宋体"}**[sync]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1127564894}

[\[Sysname\] interface virtual-template 1]{lang="EN-US"}

[\[Sysname-Virtual-Template1\] nas-port-type sync]{lang="EN-US"}
:::

::::: {#-513225710 .myid}
[]{#_Toc404785037}[]{#struct_0_x2041_67218_x1760634919}[]{#_Toc346386966}

**PPP和MP \-- PPP配置命令 \-- ppp accm**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2041_67218_1235567996}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_x1816414544}
:::

[ ]{lang="EN-US"}

[**[ppp accm]{lang="EN-US"}**]{#struct_0_x2041_67218_1891183695}[命令用来配置]{style="font-family:宋体"}[ACCM]{lang="EN-US"}[字段的值。]{style="font-family:宋体"}

[**[undo ppp accm]{lang="EN-US"}**]{#struct_0_x2041_67218_335674038}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x923788118}

[**[ppp accm ]{lang="EN-US"}***[hex-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1455970732}

[**[undo ppp accm]{lang="EN-US"}**]{#struct_0_x2041_67218_1890261133}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x887823279}

[[ACCM]{lang="EN-US"}]{#struct_0_x2041_67218_976474320}[字段的值为]{style="font-family:宋体"}[0x000A0000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2002702179}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_897592857}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1760700455}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_218497020}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1942579624}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2145672356}

[*[hex-number]{lang="EN-US"}*]{#struct_0_x2041_67218_1164463718}[：十六进制表示的]{style="font-family:宋体"}[ACCM]{lang="EN-US"}[字段的值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFFFFFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1246212376}

[[ACCM]{lang="EN-US"}]{#struct_0_x2041_67218_1106795235}[协商选项只有在异步链路上才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1166502547}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x827507621}[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上配置]{style="font-family:宋体"}[ACCM]{lang="EN-US"}[字段的值为]{style="font-family:宋体"}[0x01010101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1674022044}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp accm 01010101]{lang="EN-US"}
:::::

::: {#-971348811 .myid}
[]{#_Toc404785038}[]{#struct_0_x2041_67218_1185750592}[]{#_Toc346386967}[]{#_Toc259009505}

**PPP和MP \-- PPP配置命令 \-- ppp account-statistics enable**

------------------------------------------------------------------------

[**[ppp account-statistics enable]{lang="EN-US"}**]{#struct_0_x2041_67218_1529706250}[命令用来开启]{style="font-family:
宋体"}[PPP]{lang="EN-US"}[计费统计功能。]{style="font-family:宋体"}

[**[undo ppp account-statistics enable]{lang="EN-US"}**]{#struct_0_x2041_67218_81939011}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1111829211}

[**[ppp account-statistics enable]{lang="EN-US"}**[ \[ **acl** { *acl-number* \| **name** *acl-name* } \]]{lang="EN-US"}]{#struct_0_x2041_67218_x1760241703}

[**[undo ppp account-statistics enable]{lang="EN-US"}**]{#struct_0_x2041_67218_x1291479637}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x717519746}

[[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_138281662}[计费统计功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1595777118}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1936349239}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x432126594}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_865073363}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x974724924}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x423242480}

[**[acl]{lang="EN-US"}**]{#struct_0_x2041_67218_1874651620}[：对符合]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的流量进行计费统计。如果不配置]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，则对所有流量都进行计费统计。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1406287832}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，取值范围]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。对于同一个]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，如果同时存在对应的]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[，则会同时生效。]{style="font-family:宋体"}

[**[name ]{lang="EN-US"}***[acl-name]{lang="EN-US"}*]{#struct_0_x2041_67218_x1147297929}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。为避免混淆，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称不允许使用英文单词]{style="font-family:宋体"}[all]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1426920316}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x522587994}[在]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上开启]{style="font-family:宋体"}[PPP]{lang="EN-US"}[计费统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1760307239}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp account-statistics enable]{lang="EN-US"}
:::

::::: {#952290210 .myid}
[]{#_Toc404785039}[]{#struct_0_x2041_67218_1259416982}[]{#_Toc346386968}

**PPP和MP \-- PPP配置命令 \-- ppp acfc local-request**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2041_67218_x2063308557}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_x825898037}
:::

**[ ]{lang="EN-US"}**

[**[ppp acfc local-request]{lang="EN-US"}**]{#struct_0_x2041_67218_1367058101}[命令用来配置本地发送]{style="font-family:宋体"}[ACFC]{lang="EN-US"}[协商请求，即]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商时本地发送的协商请求携带]{style="font-family:宋体"}[ACFC]{lang="EN-US"}[协商选项。]{style="font-family:宋体"}

[**[undo ppp acfc local-request]{lang="EN-US"}**]{#struct_0_x2041_67218_1444720372}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1092109180}

[**[ppp acfc local-request]{lang="EN-US"}**]{#struct_0_x2041_67218_x1460912365}

[**[undo ppp acfc local-request]{lang="EN-US"}**]{#struct_0_x2041_67218_x645874621}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1386332313}

[[LCP]{lang="EN-US"}]{#struct_0_x2041_67218_x616146567}[协商时本地发送的协商请求不携带]{style="font-family:宋体"}[ACFC]{lang="EN-US"}[协商选项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1113766733}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_802876925}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x194682055}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1836237516}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1367997041}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_352676474}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_650205464}[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上配置本地发送]{style="font-family:宋体"}[ACFC]{lang="EN-US"}[协商请求。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1173674196}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp acfc local-request]{lang="EN-US"}
:::::

::::: {#-840231868 .myid}
[]{#_Toc404785040}[]{#struct_0_x2041_67218_729417528}[]{#_Toc346386969}

**PPP和MP \-- PPP配置命令 \-- ppp acfc remote-reject**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2041_67218_x1380344607}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_639836279}
:::

**[ ]{lang="EN-US"}**

[**[ppp acfc remote-reject]{lang="EN-US"}**]{#struct_0_x2041_67218_96686422}[命令用来拒绝对端的]{style="font-family:宋体"}[ACFC]{lang="EN-US"}[协商请求，即]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商时拒绝对端携带的]{style="font-family:宋体"}[ACFC]{lang="EN-US"}[协商选项。]{style="font-family:宋体"}

[**[undo ppp acfc remote-reject]{lang="EN-US"}**]{#struct_0_x2041_67218_374287915}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x369798309}

[**[ppp acfc remote-reject]{lang="EN-US"}**]{#struct_0_x2041_67218_x1894220657}

[**[undo ppp acfc remote-reject]{lang="EN-US"}**]{#struct_0_x2041_67218_108823014}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1448572856}

[[接受对端的]{style="font-family:宋体"}[ACFC]{lang="EN-US"}]{#struct_0_x2041_67218_x194747591}[协商请求，即]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商时接受对端携带的]{style="font-family:宋体"}[ACFC]{lang="EN-US"}[协商选项，并且发送的报文进行地址控制字段压缩。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_872192748}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_112187884}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1436297292}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1671278140}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1878364276}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x554301547}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_608271784}[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上配置拒绝对端的]{style="font-family:宋体"}[ACFC]{lang="EN-US"}[协商请求。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_342931123}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp acfc remote-reject]{lang="EN-US"}
:::::

::: {#-859190717 .myid}
[]{#_Toc404785041}[]{#struct_0_x2041_67218_768451857}[]{#_Toc332278969}[]{#_Toc259009508}[]{#_Toc136938065}[]{#_Toc96758140}[]{#_Toc31795062}[]{#_Toc505401500}

**PPP和MP \-- PPP配置命令 \-- ppp authentication-mode**

------------------------------------------------------------------------

[**[ppp authentication-mode]{lang="EN-US"}**]{#struct_0_x2041_67218_567261321}[命令用来配置本地认证对端的认证方式。]{style="font-family:宋体"}

[**[undo ppp authentication-mode]{lang="EN-US"}**]{#struct_0_x2041_67218_x1433626268}[命令用来取消配置的认证方式，即不进行认证。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1118482302}

[**[ppp authentication-mode]{lang="EN-US"}**[ { **chap** **\|** **ms-chap** \| **ms-chap-v2** \| **pap** } \* \[ \[ **call-in** \] **domain** *isp-name* \]]{lang="EN-US"}]{#struct_0_x2041_67218_1528954453}

[**[undo ppp authentication-mode]{lang="EN-US"}**]{#struct_0_x2041_67218_1285447759}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1582486714}

[[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_581591076}[协议不进行认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x617147117}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1978120525}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1158169587}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_582964519}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x87767608}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1180089963}

[**[chap]{lang="EN-US"}**]{#struct_0_x2041_67218_668616507}[：采用]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证方式。]{style="font-family:宋体"}

[**[ms-chap]{lang="EN-US"}**]{#struct_0_x2041_67218_x194813127}[：采用]{style="font-family:宋体"}[MS-CHAP]{lang="EN-US"}[认证方式。]{style="font-family:宋体"}

[**[ms-chap-v2]{lang="EN-US"}**]{#struct_0_x2041_67218_2079443162}[：采用]{style="font-family:宋体"}[MS-CHAP-V2]{lang="EN-US"}[认证方式。]{style="font-family:宋体"}

[**[pap]{lang="EN-US"}**]{#struct_0_x2041_67218_x1141727083}[：采用]{style="font-family:宋体"}[PAP]{lang="EN-US"}[认证方式。]{style="font-family:宋体"}

[**[call-in]{lang="EN-US"}**]{#struct_0_x2041_67218_x339086202}[：表示只在远端用户呼入时才认证对方。当本端作为]{style="font-family:宋体"}[DDR]{lang="EN-US"}[呼叫的接收端时可以配置本参数。关于]{style="font-family:宋体"}[DDR]{lang="EN-US"}[的详细介绍请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[广域网接入配置指导"中的"]{style="font-family:宋体"}[DDR]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[domain ]{lang="EN-US"}***[isp-name]{lang="EN-US"}*]{#struct_0_x2041_67218_x617081581}[：表示用户认证采用的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_356736277}

[[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_1681601563}[有以下几种认证方式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PAP]{lang="EN-US"}]{#struct_0_x2041_67218_1990192068}[为两次握手认证，口令为明文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CHAP]{lang="EN-US"}]{#struct_0_x2041_67218_x1840550054}[为三次握手认证，口令为密文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MS-CHAP]{lang="EN-US"}]{#struct_0_x2041_67218_x1816552029}[为微软]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证，是三次握手认证，口令为密文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MS-CHAP-V2]{lang="EN-US"}]{#struct_0_x2041_67218_208053431}[为微软]{style="font-family:
宋体"}[CHAP V2]{lang="EN-US"}[认证，是三次握手认证，口令为密文。]{style="font-family:宋体"}

[[用户可以同时配置上面的多种认证方式。]{style="font-family:宋体"}]{#struct_0_x2041_67218_107043978}

[[上述任何一种认证方式，只是一种认证过程，最终能否通过认证，还需要]{style="font-family:宋体"}[AAA]{lang="EN-US"}]{#struct_0_x2041_67218_x1987241192}[来作决定，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[可以利用本地认证数据库认证或由]{style="font-family:宋体"}[AAA]{lang="EN-US"}[服务器进行认证。关于]{style="font-family:宋体"}[AAA]{lang="EN-US"}[认证的详细介绍请参见"安全配置指导"中的"]{style="font-family:宋体"}[AAA]{lang="EN-US"}["。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1915303600}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置时指定了]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1963645511}**[domain]{lang="EN-US"}**[，则使用指定]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域对对端设备进行认证，如果要进行]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址分配，则必须在该]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域下关联]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池（通过]{style="font-family:宋体"}**[display domain]{lang="EN-US"}**[命令可以查看该]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的配置）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置时没有指定]{lang="EN-US" style="font-family:宋体"}**[domain]{lang="EN-US"}**]{#struct_0_x2041_67218_x617671404}[，则判断用户名中是否带有]{lang="EN-US" style="font-family:宋体"}[domain]{lang="EN-US"}[信息。如果用户名中带有]{lang="EN-US" style="font-family:宋体"}[domain]{lang="EN-US"}[信息，则以用户名中的]{lang="EN-US" style="font-family:宋体"}[domain]{lang="EN-US"}[为准（若本地不存在该]{lang="EN-US" style="font-family:宋体"}[domain]{lang="EN-US"}[，则认证失败）；如果用户名中不带]{lang="EN-US" style="font-family:宋体"}[domain]{lang="EN-US"}[，则使用系统缺省的]{lang="EN-US" style="font-family:宋体"}[ISP]{lang="EN-US"}[域（缺省]{lang="EN-US" style="font-family:宋体"}[ISP]{lang="EN-US"}[域可以通过命令]{lang="EN-US" style="font-family:宋体"}**[domain default]{lang="EN-US"}**[配置，若不配置，则缺省]{lang="EN-US" style="font-family:宋体"}[ISP]{lang="EN-US"}[域为]{lang="EN-US" style="font-family:宋体"}[system]{lang="EN-US"}[）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于拨号接口的认证，建议在物理接口和]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1565237693}[Dialer]{lang="EN-US"}[接口上都配置。因为当物理接口接收到]{style="font-family:宋体"}[DDR]{lang="EN-US"}[呼叫请求时，首先进行]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协商并认证拨入用户的合法性，然后再将呼叫转交给上层协议进行处理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x642472520}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x848418791}[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上，采用]{style="font-family:宋体"}[PAP]{lang="EN-US"}[方法认证对端设备。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1953909203}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp authentication-mode pap]{lang="EN-US"}[]{#_Toc31795064}[]{#_Toc505401502}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1315554239}[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上，采用]{style="font-family:宋体"}[PAP]{lang="EN-US"}[、]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[、]{style="font-family:宋体"}[MS-CHAP]{lang="EN-US"}[三种方法认证对端设备。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_779347161}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp authentication-mode pap chap ms-chap]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1361693096}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain default]{lang="EN-US"}**]{#struct_0_x2041_67218_x617605868}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_x2041_67218_x1250742095}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp chap password]{lang="EN-US"}**]{#struct_0_x2041_67218_x1387879613}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp chap user]{lang="EN-US"}**]{#struct_0_x2041_67218_x1539425937}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp pap local-user]{lang="EN-US"}**]{#struct_0_x2041_67218_389997903}
:::

::: {#825351393 .myid}
[]{#_Toc404785042}[]{#struct_0_x2041_67218_x1394133612}[]{#_Toc332278970}[]{#_Toc259009509}[]{#_Toc136938066}[]{#_Toc96758141}

**PPP和MP \-- PPP配置命令 \-- ppp chap password**

------------------------------------------------------------------------

[**[ppp chap password]{lang="EN-US"}**]{#struct_0_x2041_67218_1809173979}[命令用来配置进行]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证时采用的密码。]{style="font-family:宋体"}

[**[undo ppp chap password]{lang="EN-US"}**]{#struct_0_x2041_67218_x1407733965}[命令用来取消配置的密码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2038768119}

[**[ppp chap password]{lang="EN-US"}**[ { **cipher** \| **simple** } *password*]{lang="EN-US"}]{#struct_0_x2041_67218_x617802476}

[**[undo ppp chap password]{lang="EN-US"}**]{#struct_0_x2041_67218_x9967127}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1750294069}

[[没有配置进行]{style="font-family:宋体"}[CHAP]{lang="EN-US"}]{#struct_0_x2041_67218_1535595240}[认证时采用的密码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_901762412}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1969621771}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1045162432}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1071004360}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x568520022}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x617736940}

[**[cipher]{lang="EN-US"}**]{#struct_0_x2041_67218_x2021540871}[：表示以密文方式设置密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x2041_67218_923289945}[：表示以明文方式设置密码。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_x2041_67218_1740596203}[：]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证时采用的密码，区分大小写，以明文方式设置密码时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[48]{lang="EN-US"}[个字符的字符串，以密文方式设置密码时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[97]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1313110128}

[[需要注意的是，以明文或密文方式设置的密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1878230751}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_422047489}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x535802642}[配置本地设备以]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[方式被对端设备认证时，密码为]{style="font-family:宋体"}[sysname]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x617409260}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp chap password simple sysname]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x837352737}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp authentication-mode chap]{lang="EN-US"}**]{#struct_0_x2041_67218_234277739}
:::

::: {#-1389117867 .myid}
[]{#_Toc31795065}[]{#_Toc505401503}[]{#_Toc404785043}[]{#struct_0_x2041_67218_765653030}[]{#_Toc332278971}[]{#_Toc259009510}[]{#_Toc136938067}[]{#_Toc96758142}[]{#_Toc31795063}[]{#_Toc505401501}

**PPP和MP \-- PPP配置命令 \-- ppp chap user**

------------------------------------------------------------------------

[**[ppp chap user]{lang="EN-US"}**]{#struct_0_x2041_67218_x1001649401}[命令用来配置采用]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证时的用户名。]{style="font-family:宋体"}

[**[undo ppp chap user]{lang="EN-US"}**]{#struct_0_x2041_67218_1553353053}[命令用来删除已有的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1156040549}

[**[ppp chap user]{lang="EN-US"}**[ *username*]{lang="EN-US"}]{#struct_0_x2041_67218_x412277483}

[**[undo ppp chap user]{lang="EN-US"}**]{#struct_0_x2041_67218_x1587722610}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x617343724}

[[CHAP]{lang="EN-US"}]{#struct_0_x2041_67218_x1155828600}[认证的用户名为空。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_66194358}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x640200112}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_800460972}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1498109606}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_196165403}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1995187699}

[*[username]{lang="EN-US"}*]{#struct_0_x2041_67218_220777762}[：]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。该用户名是发送到对端设备进行]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证时使用的用户名。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x617540332}

[[配置]{style="font-family:宋体"}[CHAP]{lang="EN-US"}]{#struct_0_x2041_67218_x794570114}[认证时，要将各自的]{style="font-family:宋体"}*[username]{lang="EN-US"}*[配置为对端的]{style="font-family:宋体"}*[local-user]{lang="EN-US"}*[，而且对应的]{style="font-family:宋体"}*[password]{lang="EN-US"}*[要一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1236477444}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1996310846}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[进行]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证时的用户名为]{style="font-family:宋体"}[Root]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1891241519}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp chap user Root]{lang="EN-US"}[]{#_Toc31795066}[]{#_Toc505401504}[]{#_Toc31795058}[]{#_Toc136938068}[]{#_Toc96758143}[]{#_Toc37576001}[]{#_Toc29028046}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1247157165}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp authentication-mode chap]{lang="EN-US"}**]{#struct_0_x2041_67218_x1640145301}
:::

::: {#1316938429 .myid}
[]{#_Toc404785044}[]{#struct_0_x2041_67218_x1127302751}[]{#_Toc371343252}

**PPP和MP \-- PPP配置命令 \-- ppp compression iphc enable**

------------------------------------------------------------------------

[**[ppp compression iphc enable]{lang="EN-US"}**]{#struct_0_x2041_67218_x1126975071}[命令用来开启]{style="font-family:
宋体"}[IPHC]{lang="EN-US"}[压缩功能。]{style="font-family:宋体"}

[**[undo ppp compression iphc enable]{lang="EN-US"}**]{#struct_0_x2041_67218_305029520}[命令用来关闭]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x966273722}

[**[ppp compression iphc enable]{lang="EN-US"}**[ \[ **nonstandard** \]]{lang="EN-US"}]{#struct_0_x2041_67218_x1126909535}

[**[undo ppp compression iphc enable]{lang="EN-US"}**]{#struct_0_x2041_67218_1263815074}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1251510625}

[[IPHC]{lang="EN-US"}]{#struct_0_x2041_67218_451093612}[压缩功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x531245040}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1251445089}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_67427726}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1485261303}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1251379553}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x352037522}

[**[nonstandard]{lang="EN-US"}**]{#struct_0_x2041_67218_1251314017}[：非标准的兼容的封装格式。不指定本参数时，则按照标准格式进行报文封装。与友商设备互通时需要配置本参数。配置本参数后，仅支持]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩，不支持]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1492299063}

[[IPHC]{lang="EN-US"}]{#struct_0_x2041_67218_x1942347275}[压缩分为如下两种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RTP]{lang="EN-US"}]{#struct_0_x2041_67218_1251772769}[头压缩：对报文中的]{style="font-family:宋体"}[RTP/UDP/IP]{lang="EN-US"}[头进行压缩。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TCP]{lang="EN-US"}]{#struct_0_x2041_67218_1239497600}[头压缩：对报文中的]{style="font-family:宋体"}[TCP/IP]{lang="EN-US"}[头进行压缩。]{style="font-family:宋体"}

[[开启]{style="font-family:宋体"}[IPHC]{lang="EN-US"}]{#struct_0_x2041_67218_1251707233}[压缩功能后，上述两种压缩功能都将启动；关闭]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能后，上述两种压缩功能都将被禁止。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x704777098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户必须在链路的两端同时开启]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1068937380}[IPHC]{lang="EN-US"}[压缩功能，该功能才生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在虚拟模板接口]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_1251641697}[、]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口、]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口上]{style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:宋体"}[本功能]{style="font-family:宋体"}[时，]{lang="EN-US" style="font-family:宋体"}[配置]{style="font-family:宋体"}[不]{lang="EN-US" style="font-family:宋体"}[会]{style="font-family:宋体"}[立]{lang="EN-US" style="font-family:宋体"}[即]{style="font-family:宋体"}[生效，只有对此接口或]{lang="EN-US" style="font-family:宋体"}[者]{style="font-family:宋体"}[其绑定的物理接口进行]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[/]{lang="EN-US"}**[undo shutdown]{lang="EN-US"}**[操作后，配置才能生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2010034235}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1599223021}[开启]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1251576161}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp compression iphc enable]{lang="EN-US"}[]{#_Toc371343253}[]{#_Toc371343254}[]{#_Toc371343255}
:::

::: {#-520875354 .myid}
[]{#_Toc404785045}[]{#struct_0_x2041_67218_x703239994}[]{#_Toc371343256}

**PPP和MP \-- PPP配置命令 \-- ppp compression iphc rtp-connections**

------------------------------------------------------------------------

[**[ppp compression iphc rtp-connections]{lang="EN-US"}**]{#struct_0_x2041_67218_1252034913}[命令用来配置接口上允许进行]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩的最大连接数。]{style="font-family:宋体"}

[**[undo ppp compression iphc rtp-connections]{lang="EN-US"}**]{#struct_0_x2041_67218_x1194896732}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2079715078}

[**[ppp compression iphc rtp-connections ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_1251969377}

[**[undo ppp compression iphc rtp-connections]{lang="EN-US"}**]{#struct_0_x2041_67218_796349482}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_759565260}

[[接口上允许进行]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x2041_67218_1251510624}[头压缩的最大连接数为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_451028076}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1251445088}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_67493262}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1842313103}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1251379552}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x352103058}

[*[number]{lang="EN-US"}*]{#struct_0_x2041_67218_511874098}[：接口上允许进行]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩的最大连接数，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[。当]{style="font-family:宋体"}*[number]{lang="EN-US"}*[≤]{style="font-family:宋体"}[256]{lang="EN-US"}[时，报文将被压缩成]{style="font-family:宋体"}[COMPRESSED_RTP_8]{lang="EN-US"}[格式，当]{style="font-family:宋体"}*[number]{lang="EN-US"}*[＞]{style="font-family:宋体"}[256]{lang="EN-US"}[时，报文将被压缩成]{style="font-family:宋体"}[COMPRESSED_RTP_16]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1251314016}

[[RTP]{lang="EN-US"}]{#struct_0_x2041_67218_x1492364599}[（]{style="font-family:宋体"}[Real-time Transport Protocol]{lang="EN-US"}[，实时传输协议）是面向连接的协议，一条链路上所能承载的]{style="font-family:宋体"}[RTP]{lang="EN-US"}[连接的数目是比较多的，但压缩算法压缩时需对每个连接维护一定的信息，从而占用一定的内存，因此可以用]{style="font-family:宋体"}**[ppp compression iphc rtp-connections]{lang="EN-US"}**[命令来配置]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩的最大连接数。例如最大连接数配置为]{style="font-family:宋体"}[3]{lang="EN-US"}[时，第]{style="font-family:宋体"}[4]{lang="EN-US"}[条]{style="font-family:宋体"}[RTP]{lang="EN-US"}[连接上的报文就不会被压缩了。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2041_67218_572373939}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_1251772768}[本功能后，需要对接口进行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[/**undo shutdown**]{lang="EN-US"}[操作后，配置才能生效。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在开启]{style="font-family:宋体"}]{#struct_0_x2041_67218_1239432064}[IPHC]{lang="EN-US"}[压缩功能后，才能配置本命令。在关闭]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能后，本配置将被清除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x611254837}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1251707232}[配置]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口上允许进行]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩的最大连接数为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x704711562}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp compression iphc enable]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp compression iphc rtp-connections 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1251641696}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp compression iphc enable]{lang="EN-US"}**]{#struct_0_x2041_67218_2010099771}[]{#_Toc371343257}
:::

::: {#2048348778 .myid}
[]{#_Toc404785046}[]{#struct_0_x2041_67218_x441767704}[]{#_Toc371343258}

**PPP和MP \-- PPP配置命令 \-- ppp compression iphc tcp-connections**

------------------------------------------------------------------------

[**[ppp compression iphc tcp-connections]{lang="EN-US"}**]{#struct_0_x2041_67218_1251576160}[命令用来配置接口上允许进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩的最大连接数。]{style="font-family:宋体"}

[**[undo ppp compression iphc tcp-connections]{lang="EN-US"}**]{#struct_0_x2041_67218_x703305530}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x946128860}

[**[ppp compression iphc tcp-connections ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_1252034912}

[**[undo ppp compression iphc tcp-connections]{lang="EN-US"}**]{#struct_0_x2041_67218_x1194962268}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x2124803506}

[[接口上允许进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x2041_67218_1251969376}[头压缩的最大连接数为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_796415018}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1759787567}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1251510623}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_450700396}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1300273737}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1251445087}

[*[number]{lang="EN-US"}*]{#struct_0_x2041_67218_66772366}[：接口上允许进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩的最大连接数，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x869933051}

[[TCP]{lang="EN-US"}]{#struct_0_x2041_67218_887258999}[是面向连接的协议，一条链路上所能承载的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的数目是比较多的，但压缩算法压缩时需对每个连接维护一定的信息，从而占用一定的内存，因此可以用]{style="font-family:宋体"}**[ppp compression iphc tcp-connections]{lang="EN-US"}**[命令来配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩的最大连接数。例如最大连接数配置为]{style="font-family:宋体"}[3]{lang="EN-US"}[时，第]{style="font-family:宋体"}[4]{lang="EN-US"}[条]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接上的报文就不会被压缩了。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2041_67218_1251379551}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_x352168594}[本功能后，需要对接口进行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[/**undo shutdown**]{lang="EN-US"}[操作后，配置才能生效。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在开启]{style="font-family:宋体"}]{#struct_0_x2041_67218_2043909847}[IPHC]{lang="EN-US"}[压缩功能，且不指定]{style="font-family:宋体"}**[nonstandard]{lang="EN-US"}**[参数时，才能配置本命令。在关闭]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能]{style="font-family:宋体"}[或者更改配置为]{lang="EN-US" style="font-family:宋体"}**[nonstandard]{lang="EN-US"}**[模式]{lang="EN-US" style="font-family:宋体"}[后，本配置将被清除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1251314015}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1492167991}[配置]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口上允许进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩的最大连接数为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_77928151}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp compression iphc enable]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp compression iphc tcp-connections 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1251772767}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp compression iphc enable]{lang="EN-US"}**]{#struct_0_x2041_67218_1240415104}[]{#_Toc371343259}
:::

::: {#-377694282 .myid}
[]{#_Toc404785047}[]{#struct_0_x2041_67218_x1742113501}[]{#_Toc332278972}[]{#_Toc259009512}

**PPP和MP \-- PPP配置命令 \-- ppp ipcp dns**

------------------------------------------------------------------------

[**[ppp ipcp dns]{lang="EN-US"}**]{#struct_0_x2041_67218_x1597014829}[命令用来配置设备为对端设备指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ppp ipcp dns]{lang="EN-US"}**]{#struct_0_x2041_67218_x617474796}[命令用来禁止设备为对端设备指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_768386321}

[**[ppp ipcp dns]{lang="EN-US"}**[ *primary-dns-address* \[ *secondary-dns-address* \]]{lang="EN-US"}]{#struct_0_x2041_67218_x469046695}

[**[undo ppp ipcp dns]{lang="EN-US"}**[ *primary-dns-address* \[ *secondary-dns-address* \]]{lang="EN-US"}]{#struct_0_x2041_67218_x672539655}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_581232879}

[[设备不为对端设备指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x2041_67218_x461858539}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x52331279}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1070077373}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_693486999}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x617147116}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1978054989}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_563483200}

[*[primary-dns-address]{lang="EN-US"}*]{#struct_0_x2041_67218_1749674980}[：主]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[secondary-dns-address]{lang="EN-US"}*]{#struct_0_x2041_67218_1580167471}[：从]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_358602024}

[[当设备之间通过]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x1594593557}[协议相连时，通过协商，设备可以为对端设备指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址（但需要等待对端请求，不会主动给对端指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[的地址）。]{style="font-family:宋体"}

[[如果主机与设备通过]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x1601710367}[协议相连时，用户可以在主机上使用命令]{style="font-family:宋体"}**[winipcfg]{lang="EN-US"}**[或]{style="font-family:宋体"}**[ipconfig/all]{lang="EN-US"}**[来查看设备为其提供的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1702331473}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x617081580}[配置设备为对端设备分配的主]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[100.1.1.1]{lang="EN-US"}[，从]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[100.1.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_356801813}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp ipcp dns 100.1.1.1 100.1.1.2]{lang="EN-US"}
:::

::: {#-1080735711 .myid}
[]{#_Toc76529677}[]{#_Toc38855352}[]{#_Toc18143115}[]{#_Toc17793771}[]{#_Toc14777415}[]{#_Toc96758144}[]{#_Toc404785048}[]{#struct_0_x2041_67218_1490855536}[]{#_Toc332278973}[]{#_Toc259009513}[]{#_Toc136938069}

**PPP和MP \-- PPP配置命令 \-- ppp ipcp dns admit-any**

------------------------------------------------------------------------

[**[ppp ipcp dns admit-any]{lang="EN-US"}**]{#struct_0_x2041_67218_x90524297}[命令用来配置设备可以被动地接收对端设备指定的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，即设备不发送]{style="font-family:宋体"}[DNS]{lang="EN-US"}[请求，也能接收对端设备分配的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ppp ipcp dns admit-any]{lang="EN-US"}**]{#struct_0_x2041_67218_318441347}[命令用来禁止设备被动地接收对端设备指定的]{style="font-family:
宋体"}[DNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_365034202}

[**[ppp ipcp dns admit-any]{lang="EN-US"}**]{#struct_0_x2041_67218_x1391643911}

[**[undo ppp ipcp dns admit-any]{lang="EN-US"}**]{#struct_0_x2041_67218_1233390089}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1761600730}

[[设备不会被动地接收对端设备指定的]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x2041_67218_327570312}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1475453249}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x231954150}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_737480841}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_499873712}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1482733736}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1211761273}

[[当设备通过]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x951283664}[协议与其它设备相连时，通过协商，设备可以被动地接收对端设备指定的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址，这样设备就可以使用对端设备指定的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器来解析域名。]{style="font-family:宋体"}

[[正常情况下，]{style="font-family:宋体"}[Client]{lang="EN-US"}]{#struct_0_x2041_67218_1761535194}[端配置了]{style="font-family:宋体"}**[ppp ipcp dns request]{lang="EN-US"}**[，]{style="font-family:宋体"}[Server]{lang="EN-US"}[端才会为本端指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址。但是有一些特殊的设备，]{style="font-family:宋体"}[Client]{lang="EN-US"}[端并未请求，]{style="font-family:宋体"}[Server]{lang="EN-US"}[端却要强制为]{style="font-family:宋体"}[Client]{lang="EN-US"}[端指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址，从而导致协商不通过，为了适应这种情况，]{style="font-family:宋体"}[Client]{lang="EN-US"}[端可以配置]{style="font-family:宋体"}**[ppp ipcp dns admit-any]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1459001910}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1444368267}[配置本地设备的]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口可以被动地接收对端指定的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x990838598}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp ipcp dns admit-any]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_528056792}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp ipcp dns request]{lang="EN-US"}**]{#struct_0_x2041_67218_x2030386014}
:::

::: {#-194979007 .myid}
[]{#_Toc136938070}[]{#_Toc404785049}[]{#struct_0_x2041_67218_609946395}[]{#_Toc332278974}[]{#_Toc259009514}[]{#_Toc122244736}[]{#_Toc134850897}[]{#_Toc134850898}[]{#_Toc134850899}[]{#_Toc134850900}[]{#_Toc134850901}[]{#_Toc134850902}[]{#_Toc134850903}[]{#_Toc134850904}[]{#_Toc134850905}[]{#_Toc134850906}[]{#_Toc134850907}[]{#_Toc134850908}[]{#_Toc134850909}[]{#_Toc134850910}[]{#_Toc134850911}[]{#_Toc134850912}[]{#_Toc134850913}[]{#_Toc134850915}[]{#_Toc134850916}

**PPP和MP \-- PPP配置命令 \-- ppp ipcp dns request**

------------------------------------------------------------------------

[**[ppp ipcp dns request]{lang="EN-US"}**]{#struct_0_x2041_67218_781049048}[命令用来配置设备可以主动向对端请求]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[**[undo ppp ipcp dns request]{lang="EN-US"}**]{#struct_0_x2041_67218_511896243}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1761469658}

[**[ppp ipcp dns request]{lang="EN-US"}**]{#struct_0_x2041_67218_724116231}

[**[undo ppp ipcp dns request]{lang="EN-US"}**]{#struct_0_x2041_67218_699547900}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1829511473}

[[禁止设备主动向对端请求]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x2041_67218_x471095341}[服务器地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1968808088}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x2057701859}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1928998092}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1235015578}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1761404122}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1259330123}

[[当设备通过]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_749667114}[协议与其它设备相连时（通常为设备拨号连接运营商的接入服务器），在进行]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商时，设备可以主动请求对端设备为其指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址，这样设备就可以使用对端设备指定的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[来解析域名。]{style="font-family:宋体"}

[[如果协商到有效的]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x2041_67218_x851261086}[服务器地址，将在接口显示信息中打印出来。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1266582204}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1040126328}[配置]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口主动请求]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_477180562}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp ipcp dns request]{lang="EN-US"}
:::

::: {#-1483285082 .myid}
[]{#_Toc404785050}[]{#struct_0_x2041_67218_1926512222}

**PPP和MP \-- PPP配置命令 \-- ppp ipcp remote-address match**

------------------------------------------------------------------------

[**[ppp ipcp remote-address match]{lang="EN-US"}**]{#struct_0_x2041_67218_1808538737}[命令用来使能接口的]{style="font-family:
宋体"}[IP]{lang="EN-US"}[网段检查功能。]{style="font-family:宋体"}

[**[undo ppp ipcp remote-address match]{lang="EN-US"}**]{#struct_0_x2041_67218_x1393440738}[命令用来关闭接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[网段检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1009829258}

[**[ppp ipcp remote-address match]{lang="EN-US"}**]{#struct_0_x2041_67218_1177826264}

[**[undo ppp ipcp remote-address match]{lang="EN-US"}**]{#struct_0_x2041_67218_x802371133}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_985752991}

[[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_x906464556}[网段检查功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1673577425}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_2070051692}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_320058340}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_92776242}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1259472740}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_636502281}

[[使能接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_x799400066}[网段检查功能后，当]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商时，本端会检查对端接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址与本端接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是否在同一网段，如果不在同一网段，则]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_565061162}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1476173528}[在虚拟模板接口]{style="font-family:宋体"}[1]{lang="EN-US"}[上使能接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[网段检查功能]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1968417153}

[\[Sysname\] interface virtual-template 1]{lang="EN-US"}

[\[Sysname-Virtual-Template1\] ppp ipcp remote-address match]{lang="EN-US"}
:::

::: {#-1918744438 .myid}
[]{#_Toc404785051}[]{#struct_0_x2041_67218_1251969375}[]{#_Toc376765043}

**PPP和MP \-- PPP配置命令 \-- ppp ip-pool route**

------------------------------------------------------------------------

[**[ppp ip-pool route]{lang="EN-US"}**]{#struct_0_x2041_67218_796480554}[命令用来配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由。]{style="font-family:宋体"}

[**[undo ppp ip-pool route]{lang="EN-US"}**]{#struct_0_x2041_67218_x1000177063}[命令用来删除]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1251510622}

[**[ppp ip-pool route ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ { *mask-length* \| *mask* } \[ **vpn-instance** *vpn-instance-name* \] \[ **vsrp-instance** *vsrp-instance-name* \]]{lang="EN-US"}]{#struct_0_x2041_67218_450634860}

[**[undo ppp ip-pool route ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ { *mask-length* \| *mask* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x2041_67218_1271378847}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1251445086}

[[没有配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_66837902}[地址池路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x2032638263}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1251379550}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x352234130}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_111484792}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1251314014}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1492233527}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x2041_67218_2054031962}[：]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，为点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x2041_67218_1251772766}[：]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由的子网掩码长度，即掩码中连续"]{style="font-family:宋体"}[1]{lang="EN-US"}["的个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x2041_67218_1240349568}[：]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址相应的子网掩码，为点分十进制格式。]{style="font-family:宋体"}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x2041_67218_x896836246}[：]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。如果未指定本参数，则表示]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_x2041_67218_1251707230}[：]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称，则视为单机环境，添加]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由。如果指定]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称，则仅在]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例处于]{style="font-family:宋体"}[Master]{lang="EN-US"}[状态下会添加]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由，当]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例由]{style="font-family:宋体"}[Master]{lang="EN-US"}[状态变为]{style="font-family:宋体"}[Backup]{lang="EN-US"}[或]{style="font-family:宋体"}[Down]{lang="EN-US"}[状态时撤销]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x704842634}

[[BRAS]{lang="EN-US"}]{#struct_0_x2041_67218_x1436743502}[（]{style="font-family:宋体"}[Broadband Remote Access Server]{lang="EN-US"}[，宽带接入服务器）通过撤销和发布]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由来实现对下行流量转发的控制。]{style="font-family:宋体"}

[[BRAS]{lang="EN-US"}]{#struct_0_x2041_67218_1251641694}[设备配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由以后，将生成一条黑洞静态路由，所有到该网段的流量均被丢弃，只有当合法用户上线以后，在]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[设备上添加一条对应的主机路由，下行的用户流量才能被正确转发。动态路由协议通过引入静态路由把该路由发布到上游的核心路由器上，核心路由器上所有到该网段的流量都引到]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[设备上。]{style="font-family:宋体"}

[[图1-1 ]{lang="EN-US"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_2009968699}[地址池路由示意图]{style="font-family:黑体"}

[[![](PPP命令.files/image002.png){#图片 38 width="357" height="59"}]{lang="EN-US"}]{#struct_0_x2041_67218_1601354479}

[ ]{lang="EN-US"}

[[用户需要保证配置的]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_1251576158}[地址池路由网段覆盖]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池网段范围。当存在多个]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池网段时，可以配置多条对应的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由。]{style="font-family:宋体"}

[[在多机环境下，用户在]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_x2041_67218_x703829815}[主用设备和备用设备上需要配置相同的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由。配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由绑定]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例以后，仅]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例处于]{style="font-family:宋体"}[Master]{lang="EN-US"}[状态的设备会添加和发布]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由，当]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例由]{style="font-family:宋体"}[Master]{lang="EN-US"}[状态变为]{style="font-family:宋体"}[Backup]{lang="EN-US"}[或]{style="font-family:宋体"}[Down]{lang="EN-US"}[状态时撤销]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1420102489}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1252034910}[配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[添加的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池路由为]{style="font-family:宋体"}[2.2.2.2/24]{lang="EN-US"}[并绑定]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例]{style="font-family:宋体"}[vsrp1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1195093340}

[\[Sysname\] ppp ip-pool route 2.2.2.2 24 vsrp-instance vsrp1]{lang="EN-US"}
:::

::: {#165293185 .myid}
[]{#_Toc404785052}[]{#struct_0_x2041_67218_532874667}[]{#_Toc370742828}[]{#_Toc259009516}[]{#_Toc136938071}[]{#_Toc96758145}

**PPP和MP \-- PPP配置命令 \-- ppp lqm**

------------------------------------------------------------------------

[**[ppp lqm]{lang="EN-US"}**]{#struct_0_x2041_67218_1251969374}[命令用来开启]{style="font-family:宋体"}[PPP]{lang="EN-US"}[链路质量监测功能。]{style="font-family:宋体"}

[**[undo ppp lqm]{lang="EN-US"}**]{#struct_0_x2041_67218_796546090}[命令用来关闭]{style="font-family:宋体"}[PPP]{lang="EN-US"}[链路质量监测功能。]{style="font-family:宋体"}

[]{#struct_0_x2041_67218_638597474}[[【命令】]{style="font-family:黑体"}]{#_Toc32639266}

[**[ppp lqm close-percentage ]{lang="EN-US"}***[close-percentage]{lang="EN-US"}*[ \[ **resume-percentage** *resume-percentage* \]]{lang="EN-US"}]{#struct_0_x2041_67218_1251510629}

[**[undo ppp lqm]{lang="EN-US"}**]{#struct_0_x2041_67218_450307180}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1218282369}

[[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_1251445093}[链路质量监测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_67034509}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_511185732}[]{#_Toc32639268}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1251379557}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x351775378}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1251314021}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1492430134}

[**[close-percentage ]{lang="EN-US"}***[close-percentage]{lang="EN-US"}*]{#struct_0_x2041_67218_x1716933491}[：禁用链路质量百分比，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[resume-percentage]{lang="EN-US"}***[ resume-percentage]{lang="EN-US"}*]{#struct_0_x2041_67218_1251772773}[：恢复链路质量百分比，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}*[resume-percentage]{lang="EN-US"}*[的值必须大于等于]{style="font-family:宋体"}*[close-percentage]{lang="EN-US"}*[的值。]{style="font-family:宋体"}*[resume-percentage]{lang="EN-US"}*[的缺省值等于]{style="font-family:宋体"}*[close-percentage]{lang="EN-US"}*[的值。]{style="font-family:宋体"}

[]{#struct_0_x2041_67218_1240152961}[[【使用指导】]{style="font-family:黑体"}]{#_Toc32639269}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当在]{style="font-family:宋体"}]{#struct_0_x2041_67218_1251707237}[PPP]{lang="EN-US"}[链路两端同时开启链路质量监测功能时，两端设备的参数必须相等。一般来说，不建议在链路两端同时开启链路质量监测功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不建议在拨号线路上开启]{style="font-family:宋体"}]{#struct_0_x2041_67218_x704514954}[PPP]{lang="EN-US"}[链路质量监测功能。当在拨号线路上开启链路质量监测功能后，由于拨号线路的特点，一旦链路被禁用，]{style="font-family:宋体"}[DDR]{lang="EN-US"}[模块就会把拨号线路挂断，因此链路质量监测就不能正常的运行。只有当有数据需要传输时，]{style="font-family:宋体"}[DDR]{lang="EN-US"}[模块把拨号线路重新呼起，链路质量监测功能才能恢复正常。]{style="font-family:宋体"}

[]{#struct_0_x2041_67218_x1814051919}[[【举例】]{style="font-family:黑体"}]{#_Toc32639270}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1251641701}[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上开启]{style="font-family:宋体"}[PPP]{lang="EN-US"}[链路质量监测功能，禁用链路质量百分比为]{style="font-family:宋体"}[90%]{lang="EN-US"}[，恢复链路质量百分比为]{style="font-family:宋体"}[95%]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x328486860}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp lqm close-percentage 90 resume-percentage 95]{lang="EN-US"}
:::

::: {#-2064348837 .myid}
[]{#_Toc31795068}[]{#_Toc505401505}[]{#_Toc404785053}[]{#struct_0_x2041_67218_x731218834}[]{#_Toc332278976}[]{#_Toc259009528}[]{#_Toc136938080}[]{#_Toc96758153}[]{#_Toc31795069}[]{#_Toc505401506}[]{#_Toc350266065}[]{#_Toc350266066}[]{#_Toc350266067}[]{#_Toc350266068}[]{#_Toc350266069}[]{#_Toc350266070}[]{#_Toc350266071}[]{#_Toc350266072}[]{#_Toc350266073}[]{#_Toc350266074}[]{#_Toc350266075}[]{#_Toc350266076}[]{#_Toc350266077}[]{#_Toc350266078}[]{#_Toc350266079}[]{#_Toc350266080}[]{#_Toc350266081}[]{#_Toc350266082}[]{#_Toc350266083}[]{#_Toc350266084}[]{#_Toc350266085}[]{#_Toc350266086}[]{#_Toc350266087}[]{#_Toc350266088}[]{#_Toc350266089}

**PPP和MP \-- PPP配置命令 \-- ppp pap local-user**

------------------------------------------------------------------------

[**[ppp pap local-user]{lang="EN-US"}**]{#struct_0_x2041_67218_1761338586}[命令用来配置本地设备被对端设备采用]{style="font-family:宋体"}[PAP]{lang="EN-US"}[方式认证时发送的用户名和密码。]{style="font-family:宋体"}

[**[undo ppp pap local-user]{lang="EN-US"}**]{#struct_0_x2041_67218_x421286130}[命令用来取消配置的用户名和密码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_440670077}

[**[ppp pap local-user]{lang="EN-US"}***[ username]{lang="EN-US"}*[ **password** { **cipher** \| **simple** } *password*]{lang="EN-US"}]{#struct_0_x2041_67218_x840036531}

[**[undo ppp pap local-user]{lang="EN-US"}**]{#struct_0_x2041_67218_1767986377}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_341577291}

[[被对端以]{style="font-family:宋体"}[PAP]{lang="EN-US"}]{#struct_0_x2041_67218_1060115345}[方式认证时，本地设备发送的用户名和密码均为空。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1321179832}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1157582131}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1761273050}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1666928157}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_913770624}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_305482128}

[*[username]{lang="EN-US"}*]{#struct_0_x2041_67218_1905698436}[：本地设备被对端设备采用]{style="font-family:宋体"}[PAP]{lang="EN-US"}[方式认证时发送的用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x2041_67218_x2094544771}[：表示以密文方式设置密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x2041_67218_316754409}[：表示以明文方式设置密码。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_x2041_67218_x1996022252}[：本地设备被对端设备采用]{style="font-family:宋体"}[PAP]{lang="EN-US"}[方式认证时发送的密码，区分大小写，以明文方式设置密码时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[48]{lang="EN-US"}[个字符的字符串，以密文方式设置密码时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[97]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1647771818}

[[当本地设备被对端以]{style="font-family:宋体"}[PAP]{lang="EN-US"}]{#struct_0_x2041_67218_x1419363595}[方式认证时，本地设备发送的用户名]{style="font-family:宋体"}*[username]{lang="EN-US"}*[和密码]{style="font-family:宋体"}*[password]{lang="EN-US"}*[应与对端设备的]{style="font-family:宋体"}*[username]{lang="EN-US"}*[（通过命令]{style="font-family:宋体"}**[local-user]{lang="EN-US"}**[ *username*]{lang="EN-US"}[配置）和]{style="font-family:宋体"}*[password]{lang="EN-US"}*[（通过命令]{style="font-family:宋体"}**[password ]{lang="EN-US"}**[{ **cipher** \| **simple** } *password*]{lang="EN-US"}[配置）一致。]{style="font-family:宋体"}

[[需要注意的是，以明文或密文方式设置的密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x2041_67218_1761207514}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1867285579}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1636721898}[配置本地设备被对端以]{style="font-family:宋体"}[PAP]{lang="EN-US"}[方式认证时发送的用户名为]{style="font-family:宋体"}[user1]{lang="EN-US"}[，密码为]{style="font-family:宋体"}[pass1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1567962653}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp pap local-user user1 password simple pass1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x271369251}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_x2041_67218_2140596400}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password]{lang="EN-US"}**]{#struct_0_x2041_67218_x1301644330}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::::: {#-1718286905 .myid}
[]{#_Toc404785054}[]{#struct_0_x2041_67218_x194157767}[]{#_Toc346386970}

**PPP和MP \-- PPP配置命令 \-- ppp pfc local-request**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2041_67218_483236407}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_x1096012410}
:::

**[ ]{lang="EN-US"}**

[**[ppp pfc local-request]{lang="EN-US"}**]{#struct_0_x2041_67218_1164692884}[命令用来配置本地发送]{style="font-family:宋体"}[PFC]{lang="EN-US"}[协商请求，即]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商时本地发送的协商请求携带]{style="font-family:宋体"}[PFC]{lang="EN-US"}[协商选项。]{style="font-family:宋体"}

[**[undo ppp pfc local-request]{lang="EN-US"}**]{#struct_0_x2041_67218_x1456587576}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_819008525}

[**[ppp pfc local-request]{lang="EN-US"}**]{#struct_0_x2041_67218_x194223303}

[**[undo ppp pfc local-request]{lang="EN-US"}**]{#struct_0_x2041_67218_1707657138}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1943503223}

[[LCP]{lang="EN-US"}]{#struct_0_x2041_67218_1411042966}[协商时本地发送的协商请求不携带]{style="font-family:宋体"}[PFC]{lang="EN-US"}[协商选项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_529996789}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1016249142}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1519072680}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_910171110}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_413709868}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1040360696}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_2024752114}[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上配置本地发送]{style="font-family:宋体"}[PFC]{lang="EN-US"}[协商请求。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x194682054}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp pfc local-request]{lang="EN-US"}
:::::

::::: {#222986750 .myid}
[]{#_Toc404785055}[]{#struct_0_x2041_67218_x1836303052}[]{#_Toc346386971}

**PPP和MP \-- PPP配置命令 \-- ppp pfc remote-reject**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2041_67218_x99350861}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_384467247}
:::

**[ ]{lang="EN-US"}**

[**[ppp pfc remote]{lang="EN-US"}[-reject]{lang="EN-US"}**]{#struct_0_x2041_67218_x484879771}[命令用来拒绝对端的]{style="font-family:宋体"}[PFC]{lang="EN-US"}[协商请求，即]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商时拒绝对端携带的]{style="font-family:宋体"}[PFC]{lang="EN-US"}[协商选项。]{style="font-family:宋体"}

[**[undo ppp pfc remote]{lang="EN-US"}[-reject]{lang="EN-US"}**]{#struct_0_x2041_67218_x1235086034}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x186312042}

[**[ppp pfc remote]{lang="EN-US"}[-reject]{lang="EN-US"}**]{#struct_0_x2041_67218_1433295703}

[**[undo ppp pfc remote]{lang="EN-US"}[-reject]{lang="EN-US"}**]{#struct_0_x2041_67218_x1492464042}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1775936069}

[[接受对端的]{style="font-family:宋体"}[PFC]{lang="EN-US"}]{#struct_0_x2041_67218_x223678585}[协商请求，即]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商时接受对端携带的]{style="font-family:宋体"}[PFC]{lang="EN-US"}[协商选项，并且发送的报文进行协议字段压缩。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1142512006}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x194747590}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_872127212}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1875888418}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1957689019}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x288926453}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x625267070}[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上配置拒绝对端的]{style="font-family:宋体"}[PFC]{lang="EN-US"}[协商请求。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1642630165}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp pfc remote-reject]{lang="EN-US"}
:::::

::: {#353863818 .myid}
[]{#_Toc42680335}[]{#_Toc404785056}[]{#struct_0_x2041_67218_69375348}[]{#_Toc332278977}[]{#_Toc259009531}[]{#_Toc136938081}[]{#_Toc96758154}

**PPP和MP \-- PPP配置命令 \-- ppp timer negotiate**

------------------------------------------------------------------------

[**[ppp timer negotiate]{lang="EN-US"}**]{#struct_0_x2041_67218_873738760}[命令用来配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协商超时时间间隔。]{style="font-family:宋体"}

[**[undo ppp timer negotiate]{lang="EN-US"}**]{#struct_0_x2041_67218_1761141978}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1901316172}

[**[ppp timer negotiate]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_x2041_67218_x649458366}

[**[undo ppp timer negotiate]{lang="EN-US"}**]{#struct_0_x2041_67218_x946227669}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_371313055}

[[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x411304834}[协商超时时间间隔为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2053022891}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1450889389}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_319243042}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1762125018}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1006921038}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_100086711}

[*[seconds]{lang="EN-US"}*]{#struct_0_x2041_67218_1373798578}[：协商超时时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1341485099}

[[在]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_725010636}[协商过程中，如果在超时时间间隔内没有收到对端的应答报文，则]{style="font-family:宋体"}[PPP]{lang="EN-US"}[将会重发前一次发送的报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1484107832}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1006328515}[配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协商超时时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1762059482}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp timer negotiate 5]{lang="EN-US"}
:::

::: {#-498566505 .myid}
[]{#_Toc96758155}[]{#_Toc404785057}[]{#struct_0_x2041_67218_x167697530}[]{#_Toc332278978}[]{#_Toc259009532}[]{#_Toc136938082}[]{#_Toc95362153}

**PPP和MP \-- PPP配置命令 \-- remote address**

------------------------------------------------------------------------

[**[remote address]{lang="EN-US"}**]{#struct_0_x2041_67218_x1219538496}[命令用来配置为]{style="font-family:宋体"}[Client]{lang="EN-US"}[端分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo remote address]{lang="EN-US"}**]{#struct_0_x2041_67218_x654584431}[命令用来取消为]{style="font-family:宋体"}[Client]{lang="EN-US"}[端分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1283383298}

[**[remote address]{lang="EN-US"}**[ { *ip-address \|* **pool** *pool-name* }]{lang="EN-US"}]{#struct_0_x2041_67218_835209194}

[**[undo remote address]{lang="EN-US"}**]{#struct_0_x2041_67218_x1833055741}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x20119741}

[[接口不为]{style="font-family:宋体"}[Client]{lang="EN-US"}]{#struct_0_x2041_67218_x1090433359}[端分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_362141160}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1761600731}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_327635848}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_970950484}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_558830550}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_950316439}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x2041_67218_x374467515}[：为]{style="font-family:宋体"}[Client]{lang="EN-US"}[端分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[pool]{lang="EN-US"}**[ *pool-name*]{lang="EN-US"}]{#struct_0_x2041_67218_x332904059}[：为]{style="font-family:宋体"}[Client]{lang="EN-US"}[端分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址使用的地址池，即将地址池]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[中的一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址分配给]{style="font-family:宋体"}[Client]{lang="EN-US"}[端。该地址池既可以是]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池，也可以是]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示地址池的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1934618487}

[[当对端接口还未配置]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_1474926926}[地址而本端接口已经有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址时，本端接口可以为对端接口分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。这时，需要在对端接口上配置]{style="font-family:宋体"}**[ip address ppp-negotiate]{lang="EN-US"}**[命令，使对端接口作为]{style="font-family:宋体"}[Client]{lang="EN-US"}[端，接受由]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协商产生的、]{style="font-family:宋体"}[Server]{lang="EN-US"}[端分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2041_67218_1761535195}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_1054199911}[可以使用两类地址池为对端接口分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址：]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池、]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池，优先采用]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池。如果用户配置了名称相同的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池和]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池，并采用该名称的地址池来分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则系统只会使用]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池来分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本端接口配置了]{style="font-family:宋体"}**[remote address]{lang="EN-US"}**]{#struct_0_x2041_67218_713252356}[命令]{lang="EN-US" style="font-family:宋体"}[后会强制为对端分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，如果]{style="font-family:宋体"}[对端接口没有配置]{lang="EN-US" style="font-family:宋体"}**[ip address ppp-negotiate]{lang="EN-US"}**[命令而是]{lang="EN-US" style="font-family:宋体"}[直接]{style="font-family:宋体"}[配置了]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}[，则]{style="font-family:宋体"}[对端接口]{lang="EN-US" style="font-family:宋体"}[不会]{style="font-family:宋体"}[接受本端分配的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{lang="EN-US" style="font-family:宋体"}[则会导致]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商]{lang="EN-US" style="font-family:宋体"}[失败]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Server]{lang="EN-US"}]{#struct_0_x2041_67218_1458936374}[端]{style="font-family:宋体"}[给]{lang="EN-US" style="font-family:宋体"}[Client]{lang="EN-US"}[端分配]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址后，]{lang="EN-US" style="font-family:宋体"}[可以]{style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:宋体"}**[remote address]{lang="EN-US"}**[/**undo remote address**]{lang="EN-US"}[命令，]{lang="EN-US" style="font-family:
宋体"}[但是配置不能立即生效，]{style="font-family:宋体"}[已经为]{lang="EN-US" style="font-family:宋体"}[Client]{lang="EN-US"}[端分配的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址仍然可以正常使用]{lang="EN-US" style="font-family:宋体"}[，需要等到下一次]{style="font-family:
宋体"}[IPCP]{lang="EN-US"}[协商时新的配置才生效]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remote address]{lang="EN-US"}**]{#struct_0_x2041_67218_x228890549}[命令的配置不能立即生效，需要等到下一次]{lang="EN-US" style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商时，才会根据此配置进行协商。建议在配置此应用时先配置]{lang="EN-US" style="font-family:宋体"}**[remote address]{lang="EN-US"}**[命令，然后再配置]{lang="EN-US" style="font-family:宋体"}**[ip address]{lang="EN-US"}**[命令，使得]{lang="EN-US" style="font-family:宋体"}**[remote address]{lang="EN-US"}**[命令的]{style="font-family:宋体"}[配置能够生效（因为配置]{lang="EN-US" style="font-family:宋体"}**[ip address]{lang="EN-US"}**[命令后，就开始进行]{lang="EN-US" style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商。因此，如果在]{lang="EN-US" style="font-family:宋体"}**[ip address]{lang="EN-US"}**[命令后配置]{lang="EN-US" style="font-family:宋体"}**[remote address]{lang="EN-US"}**[命令，需要等到下次]{lang="EN-US" style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商时，才能为]{lang="EN-US" style="font-family:宋体"}[Client]{lang="EN-US"}[端分配]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址。所以建议先配置]{lang="EN-US" style="font-family:宋体"}**[remote address]{lang="EN-US"}**[命令，再配置]{lang="EN-US" style="font-family:宋体"}**[ip address]{lang="EN-US"}**[命令）。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1986134488}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1899973047}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[为]{style="font-family:宋体"}[Client]{lang="EN-US"}[端分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.0.0.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_2097084857}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] remote address 10.0.0.1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_147857053}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[使用地址池]{style="font-family:宋体"}[aaa]{lang="EN-US"}[为]{style="font-family:宋体"}[Client]{lang="EN-US"}[端分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1761469659}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] remote address pool aaa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_724181767}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip address ppp-negotiate]{lang="EN-US"}**]{#struct_0_x2041_67218_x1611668398}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip pool]{lang="EN-US"}**]{#struct_0_x2041_67218_x1903535861}
:::

::: {#1526860545 .myid}
[]{#_Toc404785058}[]{#struct_0_x2041_67218_1251641700}[]{#_Toc371343260}

**PPP和MP \-- PPP配置命令 \-- reset ppp compression iphc**

------------------------------------------------------------------------

[**[reset ppp compression iphc]{lang="EN-US"}**]{#struct_0_x2041_67218_x328421324}[命令用来清除]{style="font-family:
宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1251576164}

[**[reset ppp compression iphc]{lang="EN-US"}**[ \[ **rtp** \| **tcp** \] \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2041_67218_x703043386}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1252034916}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1195224412}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1251969380}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_796808239}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x860740733}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1477372730}

[**[rtp]{lang="EN-US"}**]{#struct_0_x2041_67218_1263415189}[：清除]{style="font-family:宋体"}[IPHC RTP]{lang="EN-US"}[头压缩的统计信息。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_x2041_67218_x2064999849}[：清除]{style="font-family:宋体"}[IPHC TCP]{lang="EN-US"}[头压缩的统计信息。不指定]{style="font-family:宋体"}**[rtp]{lang="EN-US"}**[和]{style="font-family:宋体"}**[tcp]{lang="EN-US"}**[参数时，将同时清除]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩和]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩的统计信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x1477438266}[：清除指定接口的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。不指定本参数时，将清除所有接口的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1453520090}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1758142531}[清除所有接口的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ppp compression iphc]{lang="EN-US"}]{#struct_0_x2041_67218_x1477503802}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_961038223}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ppp compression iphc]{lang="EN-US"}**]{#struct_0_x2041_67218_x1477569338}
:::

::: {#1474946988 .myid}
[]{#_Toc404785059}[]{#struct_0_x2041_67218_1891070513}[]{#_Toc332278979}[]{#_Toc259009534}[]{#_Toc136938083}

**PPP和MP \-- PPP配置命令 \-- timer-hold**

------------------------------------------------------------------------

[**[timer-hold]{lang="EN-US"}**]{#struct_0_x2041_67218_1484282028}[命令用来配置接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期。]{style="font-family:宋体"}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_x2041_67218_1071943292}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x496981884}

[**[timer-hold]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x2041_67218_1761404123}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_x2041_67218_x1259264587}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1208208201}

[[接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x2041_67218_687065348}[报文的周期为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1927116049}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1374477771}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x721978489}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1108040036}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_298168532}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1761338587}

[*[seconds]{lang="EN-US"}*]{#struct_0_x2041_67218_x421351666}[：接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2023781784}

[[如果将接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x2041_67218_979540947}[报文的周期配置为]{style="font-family:宋体"}[0]{lang="EN-US"}[秒，则不发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[在速率非常低的链路上，参数]{style="font-family:宋体"}*[period]{lang="EN-US"}*]{#struct_0_x2041_67218_1670732892}[不能配置过小。因为在低速链路上，大报文可能会需要很长的时间才能传送完毕，这样就会延迟]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的发送与接收。而接口如果在]{style="font-family:宋体"}*[retry]{lang="EN-US"}*[个（可以通过]{style="font-family:宋体"}**[timer-hold retry]{lang="EN-US"}**[命令修改该个数）]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期之后仍然无法收到对端的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，它就会认为链路发生故障。如果]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文被延迟的时间超过接口的这个限制，链路就会被认为发生故障而被关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x880796190}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1734356556}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1993987062}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] timer-hold 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_47965278}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold retry]{lang="EN-US"}**]{#struct_0_x2041_67218_47965277}
:::

::: {#518520923 .myid}
[]{#_Toc404785060}[]{#struct_0_x2041_67218_1318763755}[]{#_Toc394763468}

**PPP和MP \-- PPP配置命令 \-- timer-hold retry**

------------------------------------------------------------------------

[**[timer-hold]{lang="EN-US"}**[ **retry**]{lang="EN-US"}]{#struct_0_x2041_67218_x1523850138}[命令用来配置接口在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路。]{style="font-family:宋体"}

[**[undo timer-hold retry]{lang="EN-US"}**]{#struct_0_x2041_67218_x1907136533}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1523850139}

[**[timer-hold]{lang="EN-US"}**[ **retry** *retry*]{lang="EN-US"}]{#struct_0_x2041_67218_x1523850140}

[**[undo timer-hold retry]{lang="EN-US"}**]{#struct_0_x2041_67218_x1523850141}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x696955272}

[[接口在]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x2041_67218_x1523850142}[个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1100239799}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1523850143}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1523850144}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x293670745}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1523850145}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1272413196}

[*[retry]{lang="EN-US"}*]{#struct_0_x2041_67218_x1523850146}[：]{style="font-family:宋体;color:black"}[接口在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1523850147}

[[在速率非常低的链路上，参数]{style="font-family:宋体"}*[retry]{lang="EN-US"}*]{#struct_0_x2041_67218_814802022}[不能配置过小。因为在低速链路上，大报文可能会需要很长的时间才能传送完毕，这样就会延迟]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的发送与接收。而接口如果在]{style="font-family:宋体"}*[retry]{lang="EN-US"}*[个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期之后仍然无法收到对端的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，它就会认为链路发生故障。如果]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文被延迟的时间超过接口的这个限制，链路就会被认为发生故障而被关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x299606691}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_814802021}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[在]{style="font-family:宋体"}[10]{lang="EN-US"}[个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_814802020}

[[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}]{#struct_0_x2041_67218_814802019}

[[\[Sysname-Serial2/1/0\] timer-hold retry 10]{lang="EN-US"}]{#struct_0_x2041_67218_50127965}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1530338202}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold]{lang="EN-US"}**]{#struct_0_x2041_67218_1775364433}
:::

::: {#2057184978 .myid}
[]{#_Toc404785061}[]{#struct_0_x2041_67218_x1071503468}

**PPP和MP \-- PPP配置命令 \-- reset ppp access-user**

------------------------------------------------------------------------

[**[reset ppp access-user]{lang="EN-US"}**]{#struct_0_x2041_67218_x361449601}[命令用来强制]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户下线。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1038086407}

[**[reset ppp access-user]{lang="EN-US"}**[ { **ip-address** *ip-address* \[ **vpn-instance** *vpn-instance-name* \] \| **ipv6-address** *ipv6-address* \[ **vpn-instance** *vpn-instance-name* \] \| **username** *user-name* }]{lang="EN-US"}]{#struct_0_x2041_67218_494580473}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1276009214}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x2130371693}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x930908366}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1220442166}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_589657518}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x2050710057}

[**[ip-address]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x2041_67218_x503639864}[：表示指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[表示用户的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6-address]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_x2041_67218_1564543768}[：表示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[表示用户的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x2041_67218_2060664414}[：表示指定]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示该用户属于公网。]{style="font-family:宋体"}

[**[username]{lang="EN-US"}**[ *user-name*]{lang="EN-US"}]{#struct_0_x2041_67218_155261434}[：表示指定用户名的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户。]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*[表示用户的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_356471390}

[[用户被强制下线后，可重新上线。]{style="font-family:宋体"}]{#struct_0_x2041_67218_x951408323}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x336619677}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x305458413}[强制]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.100.2]{lang="EN-US"}[的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户下线。]{style="font-family:宋体"}

[[\<Sysname\> reset ppp access-user ip-address 192.168.100.2]{lang="EN-US"}]{#struct_0_x2041_67218_1544590905}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x668218941}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ppp access-user]{lang="EN-US"}**]{#struct_0_x2041_67218_x1204388923}
:::

::: {#1742433432 .myid}
[]{#_Toc404785063}[]{#struct_0_x2041_67218_x1666993693}[]{#_Toc342919786}[]{#_Toc335656788}[]{#_Toc323804932}

**PPP和MP \-- MP配置命令 \-- bandwidth**

------------------------------------------------------------------------

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bandwidth]{lang="EN-US"}**]{#struct_0_x2041_67218_x1539988718}[命令用来配置接口的期望带宽。]{lang="EN-US" style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x2041_67218_x1150131254}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x194488502}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_x2041_67218_2073198925}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x2041_67218_1014530891}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x241564533}

[[接口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_x2041_67218_x1607319870}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1761207515}

[[虚拟模板接口视图]{style="font-family:宋体"}[/MP-group]{lang="EN-US"}]{#struct_0_x2041_67218_1867351115}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1078642827}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x298967559}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_280468258}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1848430995}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x2041_67218_463900986}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1386950738}

[[接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_x2041_67218_1652061770}[路由配置指导"中的"]{style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1761141979}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1901381708}[配置虚拟模板接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[1000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_548903080}

[\[Sysname\] interface virtual-template 10]{lang="EN-US"}

[\[Sysname-Virtual-Template10\] bandwidth 1000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1137796718}[配置接口]{style="font-family:宋体"}[MP-group3]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[1000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1477127045}

[\[Sysname\] interface mp-group 3]{lang="EN-US"}

[\[Sysname-MP-group3\] bandwidth 1000]{lang="EN-US"}
:::

::: {#1948332219 .myid}
[]{#_Toc323804930}[]{#_Toc404785064}[]{#struct_0_x2041_67218_1968274419}[]{#_Toc342919787}[]{#_Toc335656811}[]{#_Toc329007815}[]{#_Toc309912009}[]{#_Toc335126006}[]{#_Toc335656789}[]{#_Toc335126007}[]{#_Toc335656790}[]{#_Toc335126008}[]{#_Toc335656791}[]{#_Toc335126009}[]{#_Toc335656792}[]{#_Toc335126010}[]{#_Toc335656793}[]{#_Toc335126011}[]{#_Toc335656794}[]{#_Toc335126012}[]{#_Toc335656795}[]{#_Toc335126013}[]{#_Toc335656796}[]{#_Toc335126014}[]{#_Toc335656797}[]{#_Toc335126015}[]{#_Toc335656798}[]{#_Toc335126016}[]{#_Toc335656799}[]{#_Toc335126017}[]{#_Toc335656800}[]{#_Toc335126018}[]{#_Toc335656801}[]{#_Toc335126019}[]{#_Toc335656802}[]{#_Toc335126020}[]{#_Toc335656803}[]{#_Toc335126021}[]{#_Toc335656804}[]{#_Toc335126022}[]{#_Toc335656805}[]{#_Toc335126023}[]{#_Toc335656806}[]{#_Toc335126024}[]{#_Toc335656807}[]{#_Toc335126025}[]{#_Toc335656808}[]{#_Toc335126026}[]{#_Toc335656809}[]{#_Toc335126027}[]{#_Toc335656810}

**PPP和MP \-- MP配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x2041_67218_1854809721}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1573147720}

[**[default]{lang="EN-US"}**]{#struct_0_x2041_67218_1762125019}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1006855502}

[[虚拟模板接口视图]{style="font-family:宋体"}[/MP-group]{lang="EN-US"}]{#struct_0_x2041_67218_984613961}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_126843699}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1363931407}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_295483054}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x171239540}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1409750938}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x2041_67218_1784115220}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1762059483}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x167763066}[将虚拟模板接口]{style="font-family:宋体"}[10]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x422084810}

[\[Sysname\] interface virtual-template 10]{lang="EN-US"}

[\[Sysname-Virtual-Template10\] default]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x429052409}[将接口]{style="font-family:宋体"}[MP-group3]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1476454826}

[\[Sysname\] interface mp-group 3]{lang="EN-US"}

[\[Sysname-MP-group3\] default]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404785065}[]{#struct_0_x2041_67218_1232144113}[]{#_Toc342919788}[]{#_Toc335656812}

**PPP和MP \-- MP配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x2041_67218_605700753}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x2041_67218_1047385938}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1761600728}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x2041_67218_328094599}

[**[undo description]{lang="EN-US"}**]{#struct_0_x2041_67218_x871910183}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1141112084}

[[接口的描述信息为"*该接口的接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_x2041_67218_1120006916}["，比如：]{style="font-family:宋体"}[Virtual-Template1 Interface]{lang="EN-US"}[、]{style="font-family:宋体"}[MP-group3 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1390916951}

[[虚拟模板接口视图]{style="font-family:宋体"}[/MP-group]{lang="EN-US"}]{#struct_0_x2041_67218_x1415553247}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_632521638}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1309813995}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1761535192}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1458870838}

[*[text]{lang="EN-US"}*]{#struct_0_x2041_67218_x1454038006}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_450956033}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x801763572}[配置虚拟模板接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[virtual-interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x813990679}

[\[Sysname\] interface virtual-template 10]{lang="EN-US"}

[\[Sysname-Virtual-Template10\] description virtual-interface]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1583688963}[配置接口]{style="font-family:宋体"}[MP-group3]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[mpgroup-interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_885279135}

[\[Sysname\] interface mp-group 3]{lang="EN-US"}

[\[Sysname-MP-group3\] description mpgroup-interface]{lang="EN-US"}
:::

::: {#1664133814 .myid}
[]{#_Toc404785066}[]{#struct_0_x2041_67218_1761469656}[]{#_Toc342919789}[]{#_Toc335656813}[]{#_Toc323804934}

**PPP和MP \-- MP配置命令 \-- display interface mp-group**

------------------------------------------------------------------------

[**[display interface ]{lang="EN-US"}[mp-group]{lang="EN-US"}**]{#struct_0_x2041_67218_724247303}[命令用来显示]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_575714510}

[**[display interface ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_x2041_67218_x553042419}**[mp-group]{lang="EN-US"}**[ \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_360450159}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1095995486}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_679261535}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_959944653}

[[network-operator]{lang="EN-US"}]{#struct_0_x2041_67218_1761404120}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1259461195}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x1266371453}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1325130526}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1445514305}[：显示指定]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口的编号，取值范围为已创建的]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x2041_67218_1576677793}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x2041_67218_x1748479196}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x2041_67218_1826686351}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1144960324}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_x2041_67218_1761338584}**[mp-group]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}**[mp-group]{lang="EN-US"}**]{#struct_0_x2041_67218_x421417202}[参数，不指定]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1617267901}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x444827135}[显示接口]{style="font-family:宋体"}[MP-group12]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface mp-group 12]{lang="EN-US"}]{#struct_0_x2041_67218_1761273048}

[MP-group12]{lang="EN-US"}

[Current state: DOWN]{lang="EN-US"}

[Line protocol state: DOWN]{lang="EN-US"}

[Description: MP-group12 Interface]{lang="EN-US"}

[Bandwidth: 2048kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Hold timer: 10 seconds,retry times: 5]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Link layer protocol: PPP]{lang="EN-US"}

[LCP: initial]{lang="EN-US"}

[Physical: MP, baudrate: 2048000 bps]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[Last link flapping: Never]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate: 0 bytes/sec, 0 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0 bytes/sec, 0 packets/sec]{lang="EN-US"}

[Input: 0 packets, 0 bytes, 0 droped]{lang="EN-US"}

[Output: 0 packets, 0 bytes, 0 droped]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1667452446}[显示接口]{style="font-family:宋体"}[MP-group12]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface mp-group 12 brief]{lang="EN-US"}]{#struct_0_x2041_67218_543798872}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[MP12                 DOWN DOWN     \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1371822106}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface mp-group brief down]{lang="EN-US"}]{#struct_0_x2041_67218_x618978519}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[MP1                  ADM  Administratively]{lang="EN-US"}

[MP12                 DOWN Not connected]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display interface mp-group]{lang="EN-US"}]{#struct_0_x2041_67218_1761207512}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_699774213}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_1867678795}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_1138732729}

[[MP-group12 ]{lang="EN-US"}]{#struct_0_x2041_67218_x275317262}

[[Current state]{lang="EN-US"}]{#struct_0_x2041_67218_x2066921173}

[[接口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1413586614}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2041_67218_x303331320}[（]{lang="EN-US" style="font-family:宋体"}[Administratively]{lang="EN-US"}[）：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}[shutdown]{lang="EN-US"}[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2041_67218_1761141976}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2041_67218_1901185100}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x2041_67218_x1037604142}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_x2041_67218_591431661}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2041_67218_x1169105541}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2041_67218_x235034736}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x2041_67218_1762125016}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1007314254}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x2041_67218_535821063}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_x2041_67218_90444876}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x2041_67218_x1354699274}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_x2041_67218_1966786602}

[[Hold timer]{lang="EN-US"}]{#struct_0_x2041_67218_1762059480}

[[当前接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x2041_67218_x167566458}[报文的周期]{style="font-family:宋体"}

[[retry times]{lang="EN-US"}]{#struct_0_x2041_67218_428139619}

[[在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x2041_67218_428139616}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路]{style="font-family:宋体"}

[[Internet protocol processing ]{lang="EN-US"}]{#struct_0_x2041_67218_x1590960948}

[[网络层协议处理状况：（]{style="font-family:宋体"}[enabled/disabled]{lang="EN-US"}]{#struct_0_x2041_67218_x1468974941}[）]{style="font-family:宋体"}

[[Link layer protocol: PPP]{lang="EN-US"}]{#struct_0_x2041_67218_1902558051}

[[链路层封装的协议]{style="font-family:宋体"}]{#struct_0_x2041_67218_1761600729}

[[LCP: initial]{lang="EN-US"}]{#struct_0_x2041_67218_328160135}

[[LCP]{lang="EN-US"}]{#struct_0_x2041_67218_x875502640}[（链路控制协议）初始化完成]{style="font-family:宋体"}

[[Physical]{lang="EN-US"}]{#struct_0_x2041_67218_x258610278}

[[接口的物理类型]{style="font-family:宋体"}]{#struct_0_x2041_67218_1761535193}

[[baudrate]{lang="EN-US"}]{#struct_0_x2041_67218_x1477176123}

[[接口的波特率]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1477241659}

[[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}]{#struct_0_x2041_67218_x1197197099}

[[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}]{#struct_0_x2041_67218_x1476913979}

[[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}]{#struct_0_x2041_67218_x1477372732}

[[接口输出队列的类型：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x2023887749}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[紧急发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_x2041_67218_1761469657}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[协议发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_x2041_67218_724312839}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[先入先出发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_x2041_67218_1730334482}

[[Last link flapping]{lang="EN-US"}]{#struct_0_x2041_67218_45802598}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_x2041_67218_45802594}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters: Never]{lang="EN-US"}]{#struct_0_x2041_67218_1032340169}

[[最后一次清除接口统计信息的时间（]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_x2041_67218_1761404121}[表示未清除过接口的统计信息）]{style="font-family:宋体"}

[[Last 300 seconds input rate: 0 bytes/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_x2041_67218_x1259395659}

[[Last 300 seconds output rate: 0 bytes/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_x2041_67218_x404542029}

[[当前接口最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x2041_67218_x1450113013}[秒内输入（]{style="font-family:宋体"}[input]{lang="EN-US"}[）和输出（]{style="font-family:宋体"}[output]{lang="EN-US"}[）报文的平均速率]{style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 droped]{lang="EN-US"}]{#struct_0_x2041_67218_1761338585}

[[接口输入的报文总数（分别以包和字节为单位进行了统计），输入报文中丢弃的报文数]{style="font-family:宋体"}]{#struct_0_x2041_67218_x421482738}

[[Output: 0 packets, 0 bytes, 0 droped]{lang="EN-US"}]{#struct_0_x2041_67218_x1911559537}

[[接口输出的报文总数（分别以包和字节为单位进行了统计），输出报文中丢弃的报文数]{style="font-family:宋体"}]{#struct_0_x2041_67218_x281425368}

[[Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_x2041_67218_1761273049}

[[三层模式下（]{style="font-family:宋体"}[route]{lang="EN-US"}]{#struct_0_x2041_67218_x1667517982}[）的接口的概要信息，即三层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x2041_67218_x467249299}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x2041_67218_1907814492}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复端口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x2041_67218_1761207513}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_x2041_67218_1867744331}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x2041_67218_288368090}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x2041_67218_1761141977}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x2041_67218_1901250636}

[[Link]{lang="EN-US"}]{#struct_0_x2041_67218_137241641}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1749749724}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2041_67218_1762125017}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2041_67218_x616332122}[：表示]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[物理上不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x2041_67218_x1007248718}[：表示]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_x2041_67218_x1983059677}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x2041_67218_x226354743}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x2041_67218_1762059481}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2041_67218_1902941736}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2041_67218_x194878661}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_x2041_67218_x641105457}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_x2041_67218_1761600726}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_327439239}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x2041_67218_x889776797}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_x2041_67218_1761535190}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x2041_67218_1458739766}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x2041_67218_122049779}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1768931016}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x2041_67218_2089600830}**[ mp-group]{lang="EN-US"}**

::: {#-1527012141 .myid}
[]{#_Toc404785067}[]{#struct_0_x2041_67218_1761469654}[]{#_Toc342919790}[]{#_Toc335656814}

**PPP和MP \-- MP配置命令 \-- display interface virtual-access**

------------------------------------------------------------------------

[**[display interface ]{lang="EN-US"}[virtual-access]{lang="EN-US"}**]{#struct_0_x2041_67218_724378375}[命令用来显示]{style="font-family:宋体"}[VA]{lang="EN-US"}[（]{style="font-family:宋体"}[Virtual Access]{lang="EN-US"}[，虚拟访问）接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x611732243}

[**[display interface ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_x2041_67218_949227536}**[virtual-access]{lang="EN-US"}**[ \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x689812733}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x119907270}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1550403480}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x662780221}

[[network-operator]{lang="EN-US"}]{#struct_0_x2041_67218_1761404118}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1258936908}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x834683832}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1571072147}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1099582725}[：显示指定]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的编号，取值范围为已创建的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x2041_67218_949358608}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x2041_67218_934792899}[：用来显示用户配置的接口的全部描述信息。]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的描述信息]{style="font-family:宋体"}[不可配置，此参数无用。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x2041_67218_1826751886}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_847222724}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}**[virtual-access]{lang="EN-US"}**]{#struct_0_x2041_67218_1028232661}[参数，将显示设备支持的所有接口的相关信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}**[virtual-access]{lang="EN-US"}**]{#struct_0_x2041_67218_583146842}[参数，不指定]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1337370997}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1761338582}[显示接口]{style="font-family:宋体"}[VA1]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface virtual-access 1]{lang="EN-US"}]{#struct_0_x2041_67218_x421548274}

[Virtual-Access1]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP]{lang="EN-US"}

[Description: Virtual-Access1 Interface]{lang="EN-US"}

[Bandwidth: 1920kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Hold timer: 10 seconds,retry times: 5]{lang="EN-US"}

[Internet Address is 122.1.1.1/24 Primary]{lang="EN-US"}

[Link layer protocol: PPP]{lang="EN-US"}

[LCP: opened, MP: opened, IPCP: opened]{lang="EN-US"}

[Physical: MP, baudrate: 1920000 bps]{lang="EN-US"}

[Main interface: Virtual-Template1]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[Last link flapping: Never]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Input: 2 packets, 24 bytes, 0 drops]{lang="EN-US"}

[Output: 2 packets, 24 bytes, 0 drops]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_948899856}[显示]{style="font-family:宋体"}[VA1]{lang="EN-US"}[接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface virtual-access 1 brief]{lang="EN-US"}]{#struct_0_x2041_67218_948965392}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[VA1                  DOWN DOWN     \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_378216507}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface virtual-access brief down]{lang="EN-US"}]{#struct_0_x2041_67218_949030928}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[VA1                  DOWN Not connected]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display interface virtual-access]{lang="EN-US"}]{#struct_0_x2041_67218_418227732}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_688688479}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_79872132}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_1761273046}

[[Virtual-Access1]{lang="EN-US"}]{#struct_0_x2041_67218_x1667059230}

[[Current state]{lang="EN-US"}]{#struct_0_x2041_67218_x1730741572}

[[接口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1430350423}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2041_67218_x1727822587}[：表示该接口的管理状态为开启，但物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2041_67218_1761207510}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x2041_67218_1867547723}

[[接口的链路协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x879721628}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2041_67218_x522613239}[：该接口的协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2041_67218_x1082106007}[：该接口的协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x2041_67218_x178438112}

[[接口描述信息]{style="font-family:宋体"}]{#struct_0_x2041_67218_1761141974}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x2041_67218_x194550981}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_x2041_67218_x194616517}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x2041_67218_1901054028}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1450183080}

[[Hold timer]{lang="EN-US"}]{#struct_0_x2041_67218_x691335268}

[[当前接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x2041_67218_x645626962}[报文的周期]{style="font-family:宋体"}

[[retry times]{lang="EN-US"}]{#struct_0_x2041_67218_2008605789}

[[在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x2041_67218_52290660}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路]{style="font-family:宋体"}

[[Internet Address is 122.1.1.1/24 Primary]{lang="EN-US"}]{#struct_0_x2041_67218_200092078}

[[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_638719512}[地址。]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址使用的是]{style="font-family:宋体"}[VT]{lang="EN-US"}[接口配置的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，如果]{style="font-family:宋体"}[VT]{lang="EN-US"}[接口尚未配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，本字段将变为"]{style="font-family:宋体"}[Internet protocol processing: disabled]{lang="EN-US"}["]{style="font-family:宋体"}

[[Link layer protocol: PPP]{lang="EN-US"}]{#struct_0_x2041_67218_1641848977}

[[链路层封装的协议]{style="font-family:宋体"}]{#struct_0_x2041_67218_1762125014}

[[LCP: opened, MP: opened, IPCP: opened]{lang="EN-US"}]{#struct_0_x2041_67218_x1007183182}

[[表示]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x220477499}[连接建立成功]{style="font-family:宋体"}

[[Physical]{lang="EN-US"}]{#struct_0_x2041_67218_x175928124}

[[接口的物理类型]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1669505526}

[[baudrate]{lang="EN-US"}]{#struct_0_x2041_67218_1762059478}

[[接口的波特率]{style="font-family:宋体"}]{#struct_0_x2041_67218_x168090731}

[[Main interface]{lang="EN-US"}]{#struct_0_x2041_67218_1053872230}

[[VA]{lang="EN-US"}]{#struct_0_x2041_67218_1053937766}[接口关联的模板]{style="font-family:宋体"}

[[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}]{#struct_0_x2041_67218_x1368781551}

[[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}]{#struct_0_x2041_67218_x194682052}

[[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}]{#struct_0_x2041_67218_x1836696268}

[[接口输出队列的类型：]{style="font-family:宋体"}]{#struct_0_x2041_67218_1761600727}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[紧急发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_x2041_67218_327504775}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[协议发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_x2041_67218_644445063}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[先入先出发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_x2041_67218_x470014512}

[[Last link flapping]{lang="EN-US"}]{#struct_0_x2041_67218_819127398}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_x2041_67218_819127394}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters: Never]{lang="EN-US"}]{#struct_0_x2041_67218_1826817421}

[[最后一次清除接口统计信息的时间（]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_x2041_67218_1826882957}[表示未清除过接口的统计信息）]{style="font-family:宋体"}

[[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_x2041_67218_1458674230}

[[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_x2041_67218_x194813124}

[[当前接口最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x2041_67218_x1395830176}[秒内输入（]{style="font-family:宋体"}[input]{lang="EN-US"}[）和输出（]{style="font-family:宋体"}[output]{lang="EN-US"}[）报文的平均速率]{style="font-family:宋体"}

[[Input: 2 packets, 24 bytes, 0 drops]{lang="EN-US"}]{#struct_0_x2041_67218_x36986845}

[[接口输入的报文总数（分别以包和字节为单位进行了统计），输入报文中丢弃的报文数]{style="font-family:宋体"}]{#struct_0_x2041_67218_1761469655}

[[Output: 2 packets, 24 bytes, 0 drops]{lang="EN-US"}]{#struct_0_x2041_67218_724443911}

[[接口输出的报文总数（分别以包和字节为单位进行了统计），输出报文中丢弃的报文数]{style="font-family:宋体"}]{#struct_0_x2041_67218_414859998}

[[Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_x2041_67218_949161999}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_x2041_67218_949227535}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x2041_67218_1321129035}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x2041_67218_949293071}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复端口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x2041_67218_949358607}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_x2041_67218_926441315}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x2041_67218_948899855}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x2041_67218_29225360}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x2041_67218_948965391}

[[Link]{lang="EN-US"}]{#struct_0_x2041_67218_949030927}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x443327132}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2041_67218_949096463}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2041_67218_949686287}[：表示接口物理上]{lang="EN-US" style="font-family:宋体"}[不通]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x2041_67218_1139641868}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x2041_67218_949751823}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2041_67218_1152146584}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2041_67218_x194223300}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_x2041_67218_x194682051}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_x2041_67218_949227534}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_949293070}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x2041_67218_951089054}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_x2041_67218_949358606}[命令给接口配置的描述信息（]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的描述信息不可配置，此字段无需关注）]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x2041_67218_926441314}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x2041_67218_948899854}[的原因，取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1826620813}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x2041_67218_x1062587491}**[ virtual-access]{lang="EN-US"}**

::: {#1103668727 .myid}
[]{#_Toc404785068}[]{#struct_0_x2041_67218_x1577891743}[]{#_Toc342919791}[]{#_Toc335656815}

**PPP和MP \-- MP配置命令 \-- display interface virtual-template**

------------------------------------------------------------------------

[**[display interface ]{lang="EN-US"}[virtual-template]{lang="EN-US"}**]{#struct_0_x2041_67218_x357003271}[命令用来显示虚拟模板接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1449694161}

[**[display interface ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_x2041_67218_1761404119}**[virtual-template]{lang="EN-US"}**[ \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1258871372}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x132818952}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1693485034}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x785795588}

[[network-operator]{lang="EN-US"}]{#struct_0_x2041_67218_1886293019}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_601883416}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x1771062510}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1761338583}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x421613810}[：显示指定虚拟模板接口的信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[虚拟模板接口的编号，取值范围为已创建的虚拟模板接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x2041_67218_2031050602}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x2041_67218_x646116809}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x2041_67218_1826293133}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1459202776}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}**[virtual-template]{lang="EN-US"}**]{#struct_0_x2041_67218_x1905321424}[参数，将显示设备支持的所有接口的相关信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}**[virtual-template]{lang="EN-US"}**]{#struct_0_x2041_67218_185484121}[参数，不指定]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的]{style="font-family:宋体"}[虚拟模板接口]{lang="EN-US" style="font-family:
宋体"}[的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1891848339}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1761273047}[显示虚拟模板接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface virtual-template 1]{lang="EN-US"}]{#struct_0_x2041_67218_x1667124766}

[Virtual-Template1]{lang="EN-US"}

[Current state: DOWN]{lang="EN-US"}

[Line protocol state: DOWN]{lang="EN-US"}

[Description: Virtual-Template1 Interface]{lang="EN-US"}

[Bandwidth: 100000kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Hold timer: 10 seconds,retry times: 5]{lang="EN-US"}

[Internet Address: 6.1.1.2/8 Primary]{lang="EN-US"}

[Link layer protocol: PPP]{lang="EN-US"}

[LCP: initial]{lang="EN-US"}

[Physical: None, baudrate: 100000000 bps]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_890672070}[显示虚拟模板接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface virtual-template 1 brief]{lang="EN-US"}]{#struct_0_x2041_67218_1761207511}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP        Description]{lang="EN-US"}

[VT1                  DOWN DOWN     \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1867613259}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的虚拟模板接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface Virtual-Template brief down]{lang="EN-US"}]{#struct_0_x2041_67218_x88297130}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[VT0                  DOWN Not connected]{lang="EN-US"}

[VT12                 DOWN Not connected]{lang="EN-US"}

[VT1023               DOWN Not connected]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display interface virtual-template]{lang="EN-US"}]{#struct_0_x2041_67218_x375735830}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_718089446}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1064738698}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_1761141975}

[[Virtual-Template1 ]{lang="EN-US"}]{#struct_0_x2041_67218_1901119564}

[[Current state]{lang="EN-US"}]{#struct_0_x2041_67218_508312896}

[[接口当前的物理状态。虚拟模板接口的状态只能为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}]{#struct_0_x2041_67218_x1171144335}[，表示物理状态为关闭]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x2041_67218_x1007117646}

[[接口的链路层协议状态。虚拟模板接口的状态只能为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}]{#struct_0_x2041_67218_x497348147}[，表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x2041_67218_884522546}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x2041_67218_1762059479}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x2041_67218_x168156267}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1404904355}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x2041_67218_x1725752879}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_x2041_67218_1123809399}

[[Hold timer]{lang="EN-US"}]{#struct_0_x2041_67218_x967282625}

[[当前接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x2041_67218_514001366}[报文的周期]{style="font-family:宋体"}

[[retry times]{lang="EN-US"}]{#struct_0_x2041_67218_x1526012761}

[[在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x2041_67218_x1526012760}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路]{style="font-family:宋体"}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_x2041_67218_x906117579}

[[网络层协议处理状况。]{style="font-family:宋体"}[disabled]{lang="EN-US"}]{#struct_0_x2041_67218_x1048883541}[表示接口尚未配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，不能处理]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文。当接口配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之后，本字段将变为"]{style="font-family:宋体"}[Internet Address]{lang="EN-US"}["，后面显示接口配置的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Link layer protocol: PPP]{lang="EN-US"}]{#struct_0_x2041_67218_666266191}

[[链路层封装的协议]{style="font-family:宋体"}]{#struct_0_x2041_67218_x967348161}

[[LCP: initial]{lang="EN-US"}]{#struct_0_x2041_67218_2074180625}

[[LCP]{lang="EN-US"}]{#struct_0_x2041_67218_812328995}[协议初始化完成]{style="font-family:宋体"}

[[Physical]{lang="EN-US"}]{#struct_0_x2041_67218_x789092581}

[[接口的物理类型]{style="font-family:宋体"}]{#struct_0_x2041_67218_x699049273}

[[baudrate]{lang="EN-US"}]{#struct_0_x2041_67218_x967413697}

[[接口的波特率]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1067352292}

[[Output queue - Urgent queuing: Size/Length/Discards 0/100/0)]{lang="EN-US"}]{#struct_0_x2041_67218_x495814460}

[[Output queue - Protocol queuing: Size/Length/Discards 0/500/0)]{lang="EN-US"}]{#struct_0_x2041_67218_x1154877165}

[[Output queue - FIFO queuing: Size/Length/Discards 0/75/0)]{lang="EN-US"}]{#struct_0_x2041_67218_x967479233}

[[接口输出队列的类型：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1824460536}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[紧急发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1248890478}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[协议发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_x2041_67218_x120574508}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[先入先出发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_x2041_67218_x967544769}

[[Brief information on interface(s) under route mode:]{lang="EN-US"}]{#struct_0_x2041_67218_x1368045097}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_x2041_67218_x967741377}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x2041_67218_481596929}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x2041_67218_573382413}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x2041_67218_x966758337}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_x2041_67218_2056617106}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x2041_67218_1411377301}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x2041_67218_2031974883}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x2041_67218_x966823873}

[[Link]{lang="EN-US"}]{#struct_0_x2041_67218_2063433622}

[[接口物理连接状态。虚拟模板接口的取值只能为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}]{#struct_0_x2041_67218_x368073310}[，表示接口物理上不通]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x2041_67218_837789970}

[[接口数据链路层协议状态。虚拟模板接口的取值只能为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}]{#struct_0_x2041_67218_x967348160}[，表示接口的数据链路层不通]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_x2041_67218_x967413696}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2041_67218_x1067286756}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x2041_67218_1966380934}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_x2041_67218_x967479232}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x2041_67218_x1824395000}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x2041_67218_1068482206}[的原因，取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1764770663 .myid}
[]{#_Toc404785069}[]{#struct_0_x2041_67218_x967544768}[]{#_Toc342919801}[]{#_Toc341432204}[]{#_Toc370998626}[]{#_Toc370998627}

**PPP和MP \-- MP配置命令 \-- display ppp mp**

------------------------------------------------------------------------

[**[display ppp mp]{lang="EN-US"}**]{#struct_0_x2041_67218_x686558317}[命令用来显示]{style="font-family:宋体"}[MP]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_460496881}

[**[display ppp mp]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2041_67218_x1601392010}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1542306069}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x530413480}[]{#_Hlt24182605}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1938773813}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_2126154070}

[[network-operator]{lang="EN-US"}]{#struct_0_x2041_67218_1720145035}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1070803472}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x967610304}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2056855942}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2041_67218_1036439685}[：显示指定接口的]{style="font-family:宋体"}[MP]{lang="EN-US"}[信息。不指定本参数时，将显示所有接口的]{style="font-family:宋体"}[MP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_47858908}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1377658634}[显示]{style="font-family:宋体"}[MP]{lang="EN-US"}[的相关信息（通过]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[配置的]{style="font-family:宋体"}[MP]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> display ppp mp]{lang="EN-US"}]{#struct_0_x2041_67218_x967675840}

[Template: MP-group1]{lang="EN-US"}

[max-bind: 20, fragment: enabled, min-fragment: 128]{lang="EN-US"}

[Master link: MP-group1, Active members: 2, Bundle Multilink]{lang="EN-US"}

[Peer\'s endPoint descriptor: MP-group1]{lang="EN-US"}

[Sequence format: short (rcv)/long (sent)]{lang="EN-US"}

[Bundle Up Time: 2012/11/05  07:29:33:612]{lang="EN-US"}

[0 lost fragments, 0 reordered, 0 unassigned, 0 interleaved]{lang="EN-US"}

[Sequence: 0 (rcv)/0 (sent)]{lang="EN-US"}

[Active member channels: 2 members]{lang="EN-US"}

[      Serial2/1/0:15               Up-Time: 2012/11/05  07:29:33:613]{lang="EN-US"}

[      Serial2/1/0:16               Up-Time: 2012/11/05  07:30:10:945]{lang="EN-US"}

[Inactive member channels: 2 members]{lang="EN-US"}

[      Serial2/1/0:17]{lang="EN-US"}

[      Serial2/1/0:18]{lang="EN-US"}

[]{#struct_0_x2041_67218_x1525716847}[]{#_Toc37211916}[]{#_Ref126986659}[]{#_Ref126986655}[]{#_Toc95359205}[]{#_Toc85604316}[]{#_Toc81386695}[]{#_Toc74661818}[]{#_Toc72589781}[]{#_Toc72589508}[]{#_Toc72588993}[]{#_Toc65921163}[]{#_Toc65919111}[]{#_Toc65919086}[]{#_Toc65910720}[]{#_Toc65909965}[]{#_Toc60125175}[]{#_Toc60111174}[表1-8 ]{lang="EN-US"}[display ppp mp]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_709125432}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1794299313}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_215176301}

[[Template: MP-group1]{lang="EN-US"}]{#struct_0_x2041_67218_1163901599}

[[MP]{lang="EN-US"}]{#struct_0_x2041_67218_604030793}[接口为]{style="font-family:宋体"}[MP-group1]{lang="EN-US"}

[[max-bind]{lang="SV"}]{#struct_0_x2041_67218_x967741376}

[[MP]{lang="SV"}]{#struct_0_x2041_67218_481531393}[最大捆绑链路数]{style="font-family:宋体"}

[[fragment]{lang="EN-US"}]{#struct_0_x2041_67218_x885878225}

[[是否使能]{style="font-family:宋体"}[MP]{lang="EN-US"}]{#struct_0_x2041_67218_x449797992}[报文分片功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabled]{lang="EN-US"}]{#struct_0_x2041_67218_x798176653}[表示使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled]{lang="EN-US"}]{#struct_0_x2041_67218_x220197166}[表示未使能]{style="font-family:宋体"}

[[min-fragment]{lang="SV"}]{#struct_0_x2041_67218_x966758336}

[[MP]{lang="EN-US"}]{#struct_0_x2041_67218_2056682642}[报文分片的最小长度]{style="font-family:宋体"}

[[Master link]{lang="EN-US"}]{#struct_0_x2041_67218_963981216}

[[主通道]{style="font-family:宋体"}]{#struct_0_x2041_67218_1056578790}

[[Active members]{lang="EN-US"}]{#struct_0_x2041_67218_529123663}

[[绑定的生效通道数目]{style="font-family:宋体"}]{#struct_0_x2041_67218_442839326}

[[Bundle Multilink]{lang="EN-US"}]{#struct_0_x2041_67218_x966823872}

[[多链路捆绑]{style="font-family:宋体"}]{#struct_0_x2041_67218_2063368086}

[[Peer\'s endPoint descriptor]{lang="EN-US"}]{#struct_0_x2041_67218_x709975592}

[[MP]{lang="EN-US"}]{#struct_0_x2041_67218_x1358939948}[通道对端终端描述符]{style="font-family:宋体"}

[[Sequence format: short (rcv)/long (sent)]{lang="EN-US"}]{#struct_0_x2041_67218_1537324269}

[[MP]{lang="EN-US"}]{#struct_0_x2041_67218_x967282627}[序号格式，收方向短序，发方向长序]{style="font-family:宋体"}

[[Bundle Up Time]{lang="EN-US"}]{#struct_0_x2041_67218_513870294}

[[MP]{lang="EN-US"}]{#struct_0_x2041_67218_x1894453776}[通道]{style="font-family:宋体"}[Up]{lang="EN-US"}[的时间]{style="font-family:宋体"}

[[lost fragments]{lang="EN-US"}]{#struct_0_x2041_67218_1722774589}

[[丢弃分片数]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1967431398}

[[reordered]{lang="EN-US"}]{#struct_0_x2041_67218_x967348163}

[[重组报文数]{style="font-family:宋体"}]{#struct_0_x2041_67218_2074049553}

[[unassigned]{lang="EN-US"}]{#struct_0_x2041_67218_456462104}

[[等待重组分片数]{style="font-family:宋体"}]{#struct_0_x2041_67218_1377940525}

[[interleaved]{lang="EN-US"}]{#struct_0_x2041_67218_x967413699}

[[交叉存取分片数（]{style="font-family:宋体"}[LFI]{lang="EN-US"}]{#struct_0_x2041_67218_x1067221220}[是将]{style="font-family:宋体"}[MP]{lang="EN-US"}[报文分成小片穿插到其他报文中传输，交叉存取分片数指的是穿插到其他报文中传输的分片个数）]{style="font-family:宋体"}

[[Sequence: 0 (rcv)/0 (sent)]{lang="EN-US"}]{#struct_0_x2041_67218_x1053752483}

[[接收序列号]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_918356903}[发送序列号]{style="font-family:宋体"}

[[Active member channels]{lang="EN-US"}]{#struct_0_x2041_67218_x967479235}

[[生效的子通道]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1824591608}

[[Up-Time]{lang="EN-US"}]{#struct_0_x2041_67218_876176252}

[[子通道]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x2041_67218_1091917445}[的时间]{style="font-family:宋体"}

[[Inactive member channels]{lang="EN-US"}]{#struct_0_x2041_67218_x967544771}

[[不生效的子通道]{style="font-family:宋体"}]{#struct_0_x2041_67218_x685968492}

[]{#_Toc153166415}[]{#_Toc322966183}[]{#_Toc259009498}[]{#_Toc153166410}[]{#_Hlt24616813}[ ]{lang="EN-US"}

::: {#-534332413 .myid}
[]{#_Toc404785070}[]{#struct_0_x2041_67218_x973561731}[]{#_Toc342919792}[]{#_Toc335656816}[]{#_Toc322966184}

**PPP和MP \-- MP配置命令 \-- interface mp-group**

------------------------------------------------------------------------

[**[interface mp-group]{lang="EN-US"}**]{#struct_0_x2041_67218_854494660}[命令用来创建]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口并进入指定的]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口视图。如果指定的]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口已经创建，则该命令用来直接进入]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[**[undo interface mp-group]{lang="EN-US"}**]{#struct_0_x2041_67218_124625635}[命令用来删除指定的]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1226536839}

[**[interface mp-group]{lang="EN-US"}**[ *mp-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x967610307}

[**[undo interface mp-group]{lang="EN-US"}**[ *mp-number*]{lang="EN-US"}]{#struct_0_x2041_67218_2056921478}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x971857243}

[[未创建]{style="font-family:宋体"}[MP-group]{lang="EN-US"}]{#struct_0_x2041_67218_2118601222}[接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1161198519}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x121484893}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_169094899}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x951864652}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1448599396}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x967675843}

[*[mp-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1525913455}[：]{style="font-family:宋体"}[]{#_Hlt24806852}[MP-group]{lang="EN-US"}[接口的编号，取值范围为]{style="font-family:
宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_655900949}

[[该命令与]{style="font-family:宋体"}**[ppp mp mp-group]{lang="EN-US"}**]{#struct_0_x2041_67218_x1256441905}[命令配合使用，可以先创建]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口，也可以先配置接口加入]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x984636304}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1660759650}[创建接口]{style="font-family:宋体"}[MP-group3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x588373208}

[\[Sysname\] interface mp-group 3]{lang="EN-US"}

[\[Sysname-MP-group3\]]{lang="EN-US"}
:::

::: {#154791547 .myid}
[]{#_Toc404785071}[]{#struct_0_x2041_67218_x190197747}[]{#_Toc342919793}[]{#_Toc335656817}[]{#_Toc322966185}

**PPP和MP \-- MP配置命令 \-- interface virtual-template**

------------------------------------------------------------------------

[**[interface virtual-template]{lang="EN-US"}**]{#struct_0_x2041_67218_x967741379}[命令用来创建虚拟模板接口并进入指定的虚拟模板接口视图。如果指定的虚拟模板接口已经创建，则该命令用来直接进入虚拟模板接口视图。]{style="font-family:
宋体"}

[**[undo interface virtual-template]{lang="EN-US"}**]{#struct_0_x2041_67218_481465857}[命令用来删除指定虚拟模板接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_950769087}

[**[interface virtual-template]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x2041_67218_2053390666}

[**[undo interface virtual-template]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x2041_67218_1608521707}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_57186273}

[[未创建虚拟模板接口。]{style="font-family:宋体"}]{#struct_0_x2041_67218_2128243077}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x48397079}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_822101336}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x966758339}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_2056223890}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x133186938}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_565573849}

[*[number]{lang="EN-US"}*]{#struct_0_x2041_67218_x2085504638}[：虚拟模板接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x430619826}

[[在删除虚拟模板接口前，请确定相关的虚拟访问接口都已经删除，而且该虚拟模板接口不再被使用。]{style="font-family:宋体"}]{#struct_0_x2041_67218_582030096}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_480125701}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_327380219}[创建虚拟模板接口]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x966823875}

[\[Sysname\] interface virtual-template 10]{lang="EN-US"}

[\[Sysname-Virtual-Template10\]]{lang="EN-US"}[]{#_Hlt13991793}
:::

::: {#988247972 .myid}
[]{#_Toc404785072}[]{#struct_0_x2041_67218_2063040406}[]{#_Toc342919794}[]{#_Toc335656818}[]{#_Toc317856914}[]{#_Toc309228572}[]{#_Toc13287745}

**PPP和MP \-- MP配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_x2041_67218_414992203}[命令用来设置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x2041_67218_x296074155}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_41613224}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_x2041_67218_x618976093}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x2041_67218_x1389315010}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1366152462}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x2041_67218_988036325}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x967282626}

[[虚拟模板接口视图]{style="font-family:宋体"}[/MP-group]{lang="EN-US"}]{#struct_0_x2041_67218_513804758}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x661674418}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_534705138}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_135964533}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x683549243}

[*[size]{lang="EN-US"}*]{#struct_0_x2041_67218_336401553}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1646816690}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x2041_67218_356448692}[值影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[需要注意的是，配置了]{style="font-family:宋体"}**[mtu]{lang="EN-US"}**]{#struct_0_x2041_67218_x1369831571}[命令后需要执行命令]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[和]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[，这样该配置才能在接口上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x967348162}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_2073984017}[配置虚拟模板接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1400]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1023280728}

[\[Sysname\] interface virtual-template 10]{lang="EN-US"}

[\[Sysname-Virtual-Template10\] mtu 1400]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1615251143}[配置接口]{style="font-family:宋体"}[MP-group3]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1200]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x2005146705}

[\[Sysname\] interface mp-group 3]{lang="EN-US"}

[\[Sysname-MP-group3\] mtu 1200]{lang="EN-US"}
:::

::: {#1542253459 .myid}
[]{#_Toc404785073}[]{#struct_0_x2041_67218_x194419906}[]{#_Toc346386959}

**PPP和MP \-- MP配置命令 \-- ppp mp**

------------------------------------------------------------------------

[**[ppp mp]{lang="EN-US"}**]{#struct_0_x2041_67218_x194485442}[命令用来配置封装]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的接口工作在]{style="font-family:宋体"}[MP]{lang="EN-US"}[方式。]{style="font-family:宋体"}

[**[undo ppp mp]{lang="EN-US"}**]{#struct_0_x2041_67218_x312507398}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1828144930}

[**[ppp mp]{lang="EN-US"}**]{#struct_0_x2041_67218_x1690017452}

[**[undo ppp mp]{lang="EN-US"}**]{#struct_0_x2041_67218_x194550978}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_138356233}

[[封装]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x1174565480}[的接口工作在普通]{style="font-family:宋体"}[PPP]{lang="EN-US"}[方式下。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x650499133}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x194616514}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x691400804}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_2138908196}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_67873824}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1247378839}

[[为了增加带宽，可以将多个]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x194157762}[链路捆绑使用，形成一个逻辑]{style="font-family:宋体"}[MP]{lang="EN-US"}[接口使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_483564087}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_756351197}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[工作在]{style="font-family:宋体"}[MP]{lang="EN-US"}[方式下。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1980322218}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp mp]{lang="EN-US"}
:::

::: {#-1781579941 .myid}
[]{#_Toc404785074}[]{#struct_0_x2041_67218_x194223298}[]{#_Toc346386960}

**PPP和MP \-- MP配置命令 \-- ppp mp binding-mode**

------------------------------------------------------------------------

[**[ppp mp binding-mode]{lang="EN-US"}**]{#struct_0_x2041_67218_x631715927}[命令用来配置]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑的条件。]{style="font-family:宋体"}

[**[undo ppp mp binding-mode]{lang="EN-US"}**]{#struct_0_x2041_67218_497064876}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1027111920}

[**[ppp mp binding-mode]{lang="EN-US"}**[ { **authentication** \| **both** \| **descriptor** }]{lang="EN-US"}]{#struct_0_x2041_67218_1371401886}

[**[undo ppp mp binding-mode]{lang="EN-US"}**]{#struct_0_x2041_67218_380157936}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1855141182}

[[同时根据]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_1229631567}[的认证用户名和终端标识符进行]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_842704947}

[[虚拟模板接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_1371336350}[Dialer]{lang="SV"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1864429769}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_433398537}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1969469381}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1371270814}

[**[authentication]{lang="EN-US"}**]{#struct_0_x2041_67218_x1188088504}[：根据]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的认证用户名进行]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑。]{style="font-family:宋体"}

[**[both]{lang="EN-US"}**]{#struct_0_x2041_67218_x1528687335}[：同时根据]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的认证用户名和终端标识符进行]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑。]{style="font-family:宋体"}

[**[descriptor]{lang="EN-US"}**]{#struct_0_x2041_67218_x1766914530}[：根据]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的终端标识符进行]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1371205278}

[[用户名是指]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_321557275}[链路进行]{style="font-family:宋体"}[PAP]{lang="EN-US"}[、]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[、]{style="font-family:宋体"}[MS-CHAP]{lang="EN-US"}[或]{style="font-family:宋体"}[MS-CHAP-V2]{lang="EN-US"}[认证时所接收到的对端用户名；终端标识符是用来唯一标识一台设备的标志，是指进行]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商时所接收到的对端终端标识符。系统可以根据接口接收到的用户名或终端标识符找到指定的虚拟模板接口，从而利用模板上的配置，创建相应的]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x424406065}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当只选择]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1740826584}**[descriptor]{lang="EN-US"}**[的绑定模式时，]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑时无法区分不同的用户，如果不同用户需要绑定到不同的捆绑组下时，应该选用]{style="font-family:宋体"}**[both]{lang="EN-US"}**[的绑定模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当只选择]{style="font-family:宋体"}]{#struct_0_x2041_67218_1371664030}**[authentication]{lang="EN-US"}**[的绑定模式时，无法区分各个对端设备，因此]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑有多个对端设备时，应该选用]{style="font-family:宋体"}**[both]{lang="EN-US"}**[的绑定模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1622014162}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_2092622339}[仅根据]{style="font-family:宋体"}[PPP]{lang="EN-US"}[认证的用户名进行]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_838820663}

[\[Sysname\] interface virtual-template1]{lang="EN-US"}

[\[Sysname-Virtual-Template1\] ppp mp binding-mode authentication]{lang="EN-US"}
:::

::: {#-1360208838 .myid}
[]{#_Toc404785075}[]{#struct_0_x2041_67218_1371598494}[]{#_Toc346386961}

**PPP和MP \-- MP配置命令 \-- ppp mp endpoint**

------------------------------------------------------------------------

[**[ppp]{lang="EN-US"}**[ **mp** **endpoint**]{lang="EN-US"}]{#struct_0_x2041_67218_x799699051}[命令用来配置当前接口在]{style="font-family:宋体"}[MP]{lang="EN-US"}[应用时，]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商的]{style="font-family:宋体"}[Endpoint]{lang="EN-US"}[选项内容。]{style="font-family:宋体"}

[**[undo ppp mp endpoint]{lang="EN-US"}**]{#struct_0_x2041_67218_1785924856}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x812562247}

[**[ppp mp endpoint ]{lang="EN-US"}***[endpoint]{lang="EN-US"}*]{#struct_0_x2041_67218_730196300}

[**[undo ppp mp endpoint]{lang="EN-US"}**]{#struct_0_x2041_67218_1371532958}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1922637207}

[[接口发送报文中携带的]{style="font-family:宋体"}[Endpoint]{lang="EN-US"}]{#struct_0_x2041_67218_1680523011}[选项内容为设备名称。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1144061390}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1371467422}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_342064012}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1230908322}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1648838454}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1371926174}

[*[endpoint]{lang="EN-US"}*]{#struct_0_x2041_67218_1488187269}[：终端描述符（]{style="font-family:宋体"}[Endpoint]{lang="EN-US"}[选项内容），为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1980050138}

[[在]{style="font-family:宋体"}[MP]{lang="EN-US"}]{#struct_0_x2041_67218_1319970714}[的]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商过程会协商]{style="font-family:宋体"}[Endpoint]{lang="EN-US"}[选项（终端描述符）值：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在通过虚拟模板接口配置]{style="font-family:宋体"}]{#struct_0_x2041_67218_1371860638}[MP]{lang="EN-US"}[时，会根据]{style="font-family:宋体"}[Endpoint]{lang="EN-US"}[选项值来进行]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑。缺省情况下，接口发送报文中携带的]{style="font-family:宋体"}[Endpoint]{lang="EN-US"}[选项内容为设备名称。如果网络中存在相同的设备名称，导致无法区分]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑时，用户可以修改接口发送报文中携带的]{style="font-family:宋体"}[Endpoint]{lang="EN-US"}[选项的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在通过]{lang="EN-US" style="font-family:宋体"}[MP-group]{lang="EN-US"}]{#struct_0_x2041_67218_x35507200}[接口配置]{lang="EN-US" style="font-family:宋体"}[MP]{lang="EN-US"}[时，不需要根据]{lang="EN-US" style="font-family:宋体"}[Endpoint]{lang="EN-US"}[选项值进行]{lang="EN-US" style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑。当使用]{lang="EN-US" style="font-family:宋体"}**[ppp]{lang="EN-US"}**[ **mp** **mp-group**]{lang="EN-US"}[命令将接口加入指定]{lang="EN-US" style="font-family:宋体"}[MP-group]{lang="EN-US"}[后]{style="font-family:宋体"}[，接口发送报文中携带的]{lang="EN-US" style="font-family:宋体"}[Endpoint]{lang="EN-US"}[选项内容]{lang="EN-US" style="font-family:宋体"}[缺省]{style="font-family:宋体"}[为]{lang="EN-US" style="font-family:宋体"}[MP-group]{lang="EN-US"}[的接口名称，]{lang="EN-US" style="font-family:宋体"}[如果]{style="font-family:宋体"}[用户配置]{lang="EN-US" style="font-family:宋体"}[了]{style="font-family:宋体"}[Endpoint]{lang="EN-US"}[选项内容]{lang="EN-US" style="font-family:宋体"}[，则携带用户配置的值。]{style="font-family:宋体"}

[[由于]{style="font-family:宋体"}[Endpoint]{lang="EN-US"}]{#struct_0_x2041_67218_x2881425}[选项内容最长为]{style="font-family:宋体"}[20]{lang="EN-US"}[字节，如果内容超过]{style="font-family:宋体"}[20]{lang="EN-US"}[个字节，则截取前]{style="font-family:宋体"}[20]{lang="EN-US"}[个字节作为]{style="font-family:宋体"}[Endpoint]{lang="EN-US"}[选项内容。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x880640780}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x605665996}[配置]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口发送报文中的]{style="font-family:宋体"}[Endpoint]{lang="EN-US"}[选项内容。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1371401887}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp mp endpoint 123456]{lang="EN-US"}
:::

::: {#1411109209 .myid}
[]{#_Toc323804931}[]{#_Toc404785076}[]{#struct_0_x2041_67218_x480568268}[]{#_Toc342919802}[]{#_Toc341432205}[]{#_Toc259009520}

**PPP和MP \-- MP配置命令 \-- ppp mp fragment disable**

------------------------------------------------------------------------

[**[ppp mp fragment disable]{lang="FR"}**]{#struct_0_x2041_67218_988520437}[命令用来关闭]{style="font-family:宋体"}[MP]{lang="FR"}[报文分片功能。]{style="font-family:宋体"}

[**[undo ppp mp fragment disable]{lang="FR"}**]{#struct_0_x2041_67218_x967413698}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1067155684}

[**[ppp mp fragment disable]{lang="FR"}**]{#struct_0_x2041_67218_x1708313502}

[**[undo ppp mp fragment disable]{lang="FR"}**]{#struct_0_x2041_67218_x520222370}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1800399334}

[[MP]{lang="EN-US"}]{#struct_0_x2041_67218_719863171}[报文分片功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1328821915}

[[虚拟模板接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x453833364}[/Dialer]{lang="SV"}[接口视图]{style="font-family:宋体"}[/MP-group]{lang="SV"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1364159174}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x967479234}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1824526072}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1902650383}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}**[ppp mp fragment disable]{lang="EN-US"}**]{#struct_0_x2041_67218_x1570430032}[命令关闭]{lang="EN-US" style="font-family:宋体"}[MP]{lang="FR"}[报文分片功能后，发送的报文中仍然带有]{lang="EN-US" style="font-family:宋体"}[MP]{lang="EN-US"}[序号和分片标记，只不过每个报文都是以一个整片发送出去。当对端设备不支持分片重组功能时，需要在本端配置]{lang="EN-US" style="font-family:宋体"}**[ppp mp fragment disable]{lang="EN-US"}**[命令，以和对端进行互通。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}**[ppp mp fragment disable]{lang="EN-US"}**]{#struct_0_x2041_67218_1950691414}[命令后，接口的]{lang="EN-US" style="font-family:宋体"}**[ppp mp lfi enable]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ppp mp min-fragment]{lang="EN-US"}**[命令不再起作用。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1300541491}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1074960363}[关闭接口]{style="font-family:宋体"}[MP-group1]{lang="EN-US"}[的]{style="font-family:宋体"}[MP]{lang="EN-US"}[报文分片功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1904462878}

[\[Sysname\] interface mp-group 1]{lang="EN-US"}

[\[Sysname-MP-group1\] ppp mp fragment disable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1272596300}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp lfi enable]{lang="EN-US"}**]{#struct_0_x2041_67218_x967544770}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp min-fragment]{lang="EN-US"}**]{#struct_0_x2041_67218_x686034028}
:::

::: {#1856378633 .myid}
[]{#_Toc404785077}[]{#struct_0_x2041_67218_416290419}[]{#_Toc342919803}[]{#_Toc341432206}[]{#_Toc56569676}

**PPP和MP \-- MP配置命令 \-- ppp mp lfi delay-per-frag**

------------------------------------------------------------------------

[**[ppp mp lfi delay-per-frag]{lang="SV"}**]{#struct_0_x2041_67218_x968290333}[命令用来配置传输一个]{style="font-family:宋体"}[LFI]{lang="SV"}[分片的最大时延。]{style="font-family:宋体"}

[**[undo ppp mp lfi delay-per-frag]{lang="SV"}**]{#struct_0_x2041_67218_x2024595297}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1144309281}

[**[ppp mp lfi delay-per-frag]{lang="SV"}**]{#struct_0_x2041_67218_1918524772}[ *time*]{lang="SV"}

[**[undo ppp mp lfi delay-per-frag]{lang="SV"}**]{#struct_0_x2041_67218_1672337129}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x967610306}

[[传输一个]{style="font-family:宋体"}[LFI]{lang="EN-US"}]{#struct_0_x2041_67218_2056987014}[分片的最大时延为]{style="font-family:宋体"}[10ms]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x942151927}

[[虚拟模板接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1318156956}[/Dialer]{lang="SV"}[接口视图]{style="font-family:宋体"}[/MP-group]{lang="SV"}[接口]{style="font-family:宋体"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x239165826}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1010984185}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1654942081}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1678275081}

[*[time]{lang="EN-US"}*]{#struct_0_x2041_67218_x608463242}[：]{style="font-family:宋体"}[LFI]{lang="EN-US"}[分片的最大时延值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位是]{style="font-family:宋体"}[ms]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x967675842}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1525847919}[把接口]{style="font-family:宋体"}[MP-group 1]{lang="EN-US"}[的]{style="font-family:宋体"}[LFI]{lang="EN-US"}[分片的最大时延配置为]{style="font-family:宋体"}[20ms]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x2035237365}

[\[Sysname\] interface mp-group 1]{lang="EN-US"}

[\[Sysname-MP-group1\] ppp mp lfi delay-per-frag 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x994812057}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp lfi enable]{lang="EN-US"}**]{#struct_0_x2041_67218_x1321452178}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp lfi size-per-frag]{lang="SV"}**]{#struct_0_x2041_67218_x1439737581}
:::

::: {#77540858 .myid}
[]{#_Toc404785078}[]{#struct_0_x2041_67218_x204451903}[]{#_Toc342919804}[]{#_Toc341432207}[]{#_Toc23850173}

**PPP和MP \-- MP配置命令 \-- ppp mp lfi enable**

------------------------------------------------------------------------

[**[ppp mp lfi enable]{lang="EN-US"}**]{#struct_0_x2041_67218_x920164867}[命令用来在接口上使能]{style="font-family:宋体"}[LFI]{lang="EN-US"}[（]{style="font-family:宋体"}[Link Fragmentation and Interleaving]{lang="EN-US"}[，链路分片与交叉）功能。]{style="font-family:宋体"}

[**[undo ppp mp lfi]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2041_67218_x967741378}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_481400321}

[**[ppp mp lfi enable]{lang="EN-US"}**]{#struct_0_x2041_67218_1813615186}

[**[undo ppp mp lfi enable]{lang="EN-US"}**]{#struct_0_x2041_67218_x429956420}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x848684923}

[[LFI]{lang="EN-US"}]{#struct_0_x2041_67218_x1948696798}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1362713756}

[[虚拟模板接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_69120321}[/Dialer]{lang="SV"}[接口视图]{style="font-family:宋体"}[/]{lang="SV"}[MP-group]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1808599885}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x966758338}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_2056289426}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x627947383}

[[使能]{style="font-family:宋体"}[LFI]{lang="EN-US"}]{#struct_0_x2041_67218_x814838487}[功能后，]{style="font-family:宋体"}[LFI]{lang="EN-US"}[最大分片大小由]{style="font-family:宋体"}[LFI]{lang="EN-US"}[分片的最大时延（通过]{style="font-family:宋体"}**[ppp mp lfi delay-per-frag]{lang="EN-US"}**[命令配置）和]{style="font-family:宋体"}[LFI]{lang="SV"}[分片的最大字节数（通过]{style="font-family:宋体"}**[ppp mp lfi size-per-frag]{lang="EN-US"}**[命令配置）决定：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1382320127}[LFI]{lang="SV"}[分片的最大字节数，]{style="font-family:宋体"}[LFI]{lang="EN-US"}[最大分片大小就是该最大字节数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{style="font-family:宋体"}]{#struct_0_x2041_67218_1582768904}[LFI]{lang="EN-US"}[分片的最大时延，]{style="font-family:宋体"}[LFI]{lang="EN-US"}[最大分片大小通过接口的期望带宽和配置的最大时延计算得出：]{style="font-family:宋体"}[LFI]{lang="EN-US"}[最大分片大小＝（接口的期望带宽×最大时延）÷]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[关闭]{style="font-family:宋体"}[LFI]{lang="EN-US"}]{#struct_0_x2041_67218_x2047880648}[功能会同时删除用户配置的]{style="font-family:宋体"}[LFI]{lang="EN-US"}[分片的最大时延或]{style="font-family:宋体"}[LFI]{lang="EN-US"}[分片的最大字节数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1322894924}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x725663382}[在接口]{style="font-family:宋体"}[MP-group1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[LFI]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x966823874}

[\[Sysname\] interface mp-group 1]{lang="EN-US"}

[\[Sysname-MP-group1\] ppp mp lfi enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2062974870}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp lfi delay-per-frag]{lang="EN-US"}**]{#struct_0_x2041_67218_x343402393}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp lfi size-per-frag]{lang="EN-US"}**]{#struct_0_x2041_67218_534559}
:::

::: {#1524891893 .myid}
[]{#_Toc404785079}[]{#struct_0_x2041_67218_x2062361604}[]{#_Toc342919805}[]{#_Toc341432208}[]{#_Toc259009546}

**PPP和MP \-- MP配置命令 \-- ppp mp lfi size-per-frag**

------------------------------------------------------------------------

[**[ppp mp lfi size-per-frag]{lang="SV"}**]{#struct_0_x2041_67218_772076776}[命令用来配置]{style="font-family:宋体"}[LFI]{lang="SV"}[分片的最大字节数。]{style="font-family:宋体"}

[**[undo ppp mp lfi size-per-frag]{lang="SV"}**]{#struct_0_x2041_67218_1275831543}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1082965864}

[**[ppp mp lfi size-per-frag]{lang="SV"}**]{#struct_0_x2041_67218_x967282629}[ *size*]{lang="SV"}

[**[undo ppp mp lfi size-per-frag]{lang="SV"}**]{#struct_0_x2041_67218_513214934}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_870724657}

[[LFI]{lang="SV"}]{#struct_0_x2041_67218_x1548409109}[分片的大小由]{style="font-family:宋体"}**[ppp mp lfi delay-per-frag]{lang="SV"}**[的配置来决定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2041353440}

[[虚拟模板接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_464634387}[/Dialer]{lang="SV"}[接口视图]{style="font-family:宋体"}[/MP-group]{lang="SV"}[接口]{style="font-family:宋体"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x692733421}

[[network-admin]{lang="SV"}]{#struct_0_x2041_67218_x1501706124}

[[mdc-admin]{lang="SV"}]{#struct_0_x2041_67218_1364629124}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x967348165}

[*[size]{lang="SV"}*]{#struct_0_x2041_67218_2073918481}[：]{style="font-family:宋体"}[LFI]{lang="SV"}[分片的最大字节数]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:
宋体"}[40]{lang="SV"}[～]{style="font-family:宋体"}[1500]{lang="SV"}[，]{style="font-family:宋体"}[单位是字节。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1369801309}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1212598111}[把接口]{style="font-family:宋体"}[MP-group 1]{lang="EN-US"}[的]{style="font-family:宋体"}[LFI]{lang="EN-US"}[分片的最大字节数配置为]{style="font-family:宋体"}[80]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x735794853}

[\[Sysname\] interface mp-group 1]{lang="EN-US"}

[\[Sysname-MP-group1\] ppp mp lfi size-per-frag 80]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1608519756}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp lfi enable]{lang="EN-US"}**]{#struct_0_x2041_67218_407125172}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp lfi delay-per-frag]{lang="EN-US"}**]{#struct_0_x2041_67218_x468997203}
:::

::: {#501593530 .myid}
[]{#_Toc404785080}[]{#struct_0_x2041_67218_x967413701}[]{#_Toc342919806}[]{#_Toc341432209}[]{#_Toc259009521}

**PPP和MP \-- MP配置命令 \-- ppp mp max-bind**

------------------------------------------------------------------------

[**[ppp mp max-bind]{lang="SV"}**]{#struct_0_x2041_67218_888569621}[命令用来配置]{style="font-family:宋体"}[MP]{lang="SV"}[最大捆绑链路数。]{style="font-family:宋体"}

[**[undo ppp mp max-bind]{lang="SV"}**]{#struct_0_x2041_67218_1096579568}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x175161711}

[**[ppp mp]{lang="SV"}**]{#struct_0_x2041_67218_1391496546}[ **max-bind** *max-bind-num*]{lang="SV"}

[**[undo ppp mp max-bind]{lang="SV"}**]{#struct_0_x2041_67218_1781743963}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x155581841}

[[MP]{lang="SV"}]{#struct_0_x2041_67218_1323138515}[最大捆绑链路数为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x967479237}

[[虚拟模板接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1824722680}[/Dialer]{lang="SV"}[接口视图]{style="font-family:宋体"}[/MP-group]{lang="SV"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1760031413}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_834994467}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1979610081}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1656938678}

[*[max-bind-num]{lang="SV"}*]{#struct_0_x2041_67218_2074003654}[：表示可以被捆绑的最大链路数，取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[128]{lang="SV"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x736387802}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一般情况下用户不必配置此参数，当需要配置此参数时请在技术工程师的指导下进行。配置该参数可能影响]{style="font-family:宋体"}]{#struct_0_x2041_67218_x467106688}[PPP]{lang="EN-US"}[的性能。]{style="font-family:宋体"}[如果确实需要使用大于]{lang="EN-US" style="font-family:宋体"}[16]{lang="EN-US"}[个的]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[通道进行捆绑，可以改变]{lang="EN-US" style="font-family:宋体"}*[max-bind-num]{lang="EN-US"}*[参数。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x2041_67218_x967544773}[MP]{lang="EN-US"}[捆绑链路失败，那么很可能是由于用户想要捆绑的链路数大于最大捆绑链路数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令配置后立即生效。如果修改后的]{style="font-family:宋体"}]{#struct_0_x2041_67218_x686099564}[MP]{lang="EN-US"}[最大捆绑链路数小于实际已经加入]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑的链路数，那么已经加入]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑的链路不会因此而退出捆绑。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x747564090}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1789345481}[配置]{style="font-family:宋体"}[MP]{lang="EN-US"}[的最大捆绑链路数为]{style="font-family:宋体"}[12]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x752501101}

[\[Sysname\] interface mp-group 1]{lang="EN-US"}

[\[Sysname-MP-group1\] ppp mp max-bind 12]{lang="EN-US"}
:::

::: {#458732514 .myid}
[]{#_Toc404785081}[]{#struct_0_x2041_67218_1371598495}[]{#_Toc346386962}

**PPP和MP \-- MP配置命令 \-- ppp mp min-bind**

------------------------------------------------------------------------

[**[ppp mp min-bind]{lang="SV"}**]{#struct_0_x2041_67218_x799764587}[命令用来配置]{style="font-family:宋体"}[MP]{lang="SV"}[最少需要呼起的]{style="font-family:宋体"}[PPP]{lang="SV"}[通道数。]{style="font-family:宋体"}

[**[undo ppp mp min-bind]{lang="SV"}**]{#struct_0_x2041_67218_1371532959}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1922571671}

[**[ppp mp min-bind ]{lang="SV"}**]{#struct_0_x2041_67218_2071963603}*[min-bind-num]{lang="SV"}*

[**[undo ppp mp min-bind]{lang="SV"}**]{#struct_0_x2041_67218_x1265787944}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1371467423}

[[最小捆绑链路数为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x2041_67218_342129548}[，即]{style="font-family:宋体"}[MP]{lang="EN-US"}[拨号将依赖流量检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x708915885}

[[Dialer]{lang="SV"}]{#struct_0_x2041_67218_x1794295595}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1371926175}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1488252805}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x797274498}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1510275047}

[*[min-bind-num]{lang="SV"}*]{#struct_0_x2041_67218_1371860639}[：最小捆绑链路数，取值范围为]{style="font-family:宋体"}[0]{lang="SV"}[～]{style="font-family:宋体"}[128]{lang="SV"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x35441664}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在拨号使用中，有时需要能够同时使用多条通道来承载业务，因此需要一次报文触发能够呼起多条通道以保证最小需要的带宽。此时可以使用该命令来配置最小捆绑链路数。]{style="font-family:宋体"}]{#struct_0_x2041_67218_1560491755}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当配置的最小捆绑链路数不为]{style="font-family:宋体"}]{#struct_0_x2041_67218_2010957791}[0]{lang="SV"}[时，]{style="font-family:宋体"}[MP]{lang="EN-US"}[拨号将不依赖流量检测，但对于已经呼叫建立的链路会因为没有流量后空闲超时而主动拆除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp min-bind]{lang="EN-US"}**]{#struct_0_x2041_67218_1371401888}[命令配置的最小捆绑链路数应该小于等于]{lang="EN-US" style="font-family:宋体"}**[ppp mp]{lang="EN-US"}**[ **max-bind**]{lang="EN-US"}[命令配置的最大捆绑链路数]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_379240432}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x603970792}[配置]{style="font-family:宋体"}[MP]{lang="EN-US"}[最小捆绑链路数为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x2041_67218_x1867124275}

[\[Sysname\] interface dialer 0]{lang="NO-BOK"}

[\[Sysname-Dialer0\] ppp mp min-bind 4]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1371336352}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp max-bind]{lang="NO-BOK"}**]{#struct_0_x2041_67218_1864560841}
:::

::: {#-146039147 .myid}
[]{#_Toc404785082}[]{#struct_0_x2041_67218_x566526514}[]{#_Toc342919807}[]{#_Toc341432210}[]{#_Toc96758150}[]{#_Toc322966190}

**PPP和MP \-- MP配置命令 \-- ppp mp min-fragment**

------------------------------------------------------------------------

[**[ppp mp min-fragment]{lang="EN-US"}**]{#struct_0_x2041_67218_1216994501}[命令用来配置对]{style="font-family:宋体"}[MP]{lang="EN-US"}[报文进行分片的最小报文长度。]{style="font-family:宋体"}

[**[undo ppp mp min-fragment]{lang="EN-US"}**]{#struct_0_x2041_67218_x1761159574}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x967610309}

[**[ppp mp min-fragment]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_x2041_67218_2057052550}

[**[undo ppp mp min-fragment]{lang="EN-US"}**]{#struct_0_x2041_67218_1799368543}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1381282811}

[[MP]{lang="EN-US"}]{#struct_0_x2041_67218_x269119875}[报文进行分片的最小报文长度为]{style="font-family:宋体"}[128]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_255586431}

[[虚拟模板接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1041056954}[/Dialer]{lang="SV"}[接口视图]{style="font-family:宋体"}[/]{lang="SV"}[MP-group]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_897026103}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1762122298}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x967675845}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1526044527}

[*[size]{lang="EN-US"}*]{#struct_0_x2041_67218_x1166123540}[：对]{style="font-family:宋体"}[MP]{lang="EN-US"}[出报文进行分片的最小报文长度。当]{style="font-family:宋体"}[MP]{lang="EN-US"}[报文长度小于这个值则不进行分片，大于等于这个值则开始分片。取值范围为]{style="font-family:宋体"}[128]{lang="EN-US"}[～]{style="font-family:宋体"}[1500]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1251013608}

[[如果采用硬件芯片实现]{style="font-family:宋体"}[MP]{lang="EN-US"}]{#struct_0_x2041_67218_140749630}[捆绑功能（如]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[硬件芯片），则最小分片大小的配置需要参考具体芯片规格（如部分硬件芯片约定只能按]{style="font-family:宋体"}[128]{lang="EN-US"}[、]{style="font-family:宋体"}[256]{lang="EN-US"}[、]{style="font-family:宋体"}[512]{lang="EN-US"}[等字节分片），此时要求]{style="font-family:宋体"}**[ppp mp min-fragment]{lang="EN-US"}**[命令的配置参数符合芯片要求。如果不符合，则]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑无法产生，子通道]{style="font-family:宋体"}[LCP]{lang="EN-US"}[链路会拆断。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x820048740}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1208984904}[配置对]{style="font-family:宋体"}[MP]{lang="EN-US"}[报文进行分片的最小报文长度为]{style="font-family:宋体"}[500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1700137681}

[\[Sysname\] interface mp-group 1]{lang="EN-US"}

[\[Sysname-MP-group1\] ppp mp min-fragment 500]{lang="EN-US"}
:::

::: {#194451391 .myid}
[]{#_Toc404785083}[]{#struct_0_x2041_67218_x967741381}[]{#_Toc342919808}[]{#_Toc341432211}[]{#_Toc136938077}[]{#_Toc322966191}

**PPP和MP \-- MP配置命令 \-- ppp mp mp-group**

------------------------------------------------------------------------

[**[ppp mp mp-group]{lang="EN-US"}**]{#struct_0_x2041_67218_481990154}[命令用来将当前接口加入指定的]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[，使接口工作在]{style="font-family:宋体"}[MP]{lang="EN-US"}[方式。]{style="font-family:宋体"}

[**[undo ppp mp]{lang="EN-US"}**]{#struct_0_x2041_67218_1905293882}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1115991945}

[**[ppp mp mp-group]{lang="EN-US"}**[ *mp-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x457076889}

[**[undo ppp mp]{lang="EN-US"}**]{#struct_0_x2041_67218_x461490693}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1295376053}

[[接口工作在普通]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x1474996396}[方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x460393212}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x966758341}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2056748171}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x611599026}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1275985220}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1960385467}

[*[mp-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1094411532}[：]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_394781723}

[[本命令与]{style="font-family:宋体"}**[interface mp-group]{lang="EN-US"}**]{#struct_0_x2041_67218_x377949470}[命令配合使用，可以先创建]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口然后再将指定接口加入到该]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[中，也可以先配置接口加入]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[然后再创建该]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x966823877}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_2063171478}[将接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[加入]{style="font-family:宋体"}[MP-group1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1156531330}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp mp mp-group 1]{lang="EN-US"}

[]{#struct_0_x2041_67218_2122328791}[]{#_Toc136938078}[]{#_Toc322966195}[【相关命令】]{style="font-family:
黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface mp-group]{lang="EN-US"}**]{#struct_0_x2041_67218_1547160475}
:::

::: {#-383424767 .myid}
[]{#_Toc404785084}[]{#struct_0_x2041_67218_x769899589}[]{#_Toc342919809}[]{#_Toc341432212}[]{#_Toc322966192}[]{#_Toc259009522}[]{#_Toc136938075}[]{#_Toc322966193}[]{#_Toc259009523}[]{#_Toc136938076}

**PPP和MP \-- MP配置命令 \-- ppp mp short-sequence**

------------------------------------------------------------------------

[**[ppp mp short-sequence]{lang="EN-US"}**]{#struct_0_x2041_67218_x565317230}[命令用来触发]{style="font-family:宋体"}[MP]{lang="EN-US"}[短序协商，协商成功后本端接收方向将使用短序。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ppp mp short-sequence**]{lang="EN-US"}]{#struct_0_x2041_67218_1730171196}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x569401257}

[**[ppp mp short-sequence]{lang="SV"}**]{#struct_0_x2041_67218_x967282628}

[**[undo]{lang="EN-US"}**[ **ppp mp** **short-sequence**]{lang="EN-US"}]{#struct_0_x2041_67218_513149398}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x111314642}

[[不触发短序协商，使用长序。]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1025203028}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x175160500}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x556989956}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1085398235}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x469389516}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x967348164}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2073852945}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置该命令只能使接收方向更改为短序方式，如果发送方向想使用短序方式，则需要在对端配置该命令。]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1752231752}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MP]{lang="EN-US"}]{#struct_0_x2041_67218_x1766421305}[捆绑组使用的长短序方式由第一条加入该捆绑组中的子通道决定，后续加入捆绑组的子通道配置不能更改]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑组的长短序方式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果想使用]{style="font-family:宋体"}]{#struct_0_x2041_67218_x195358439}[MP]{lang="EN-US"}[短序协商，对于普通]{style="font-family:宋体"}[MP]{lang="EN-US"}[，建议在所有的]{style="font-family:宋体"}[MP]{lang="EN-US"}[子通道下配置该命令。配置该命令会导致]{style="font-family:宋体"}[PPP]{lang="EN-US"}[重协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_521437423}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1205680461}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[为]{style="font-family:宋体"}[MP]{lang="EN-US"}[短序协商。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x674924437}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp mp mp-group 1]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp mp short-sequence]{lang="EN-US"}
:::

::: {#1435943686 .myid}
[]{#_Toc404785085}[]{#struct_0_x2041_67218_165967057}[]{#_Toc387237200}

**PPP和MP \-- MP配置命令 \-- ppp mp soft-binding**

------------------------------------------------------------------------

[**[ppp mp soft-binding]{lang="EN-US"}**]{#struct_0_x2041_67218_x1140251447}[命令用来配置接口采用软件捆绑模式。]{style="font-family:宋体"}

[**[undo ppp mp soft-binding]{lang="EN-US"}**]{#struct_0_x2041_67218_x1045222402}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x495737524}

[**[ppp mp soft-binding]{lang="EN-US"}**]{#struct_0_x2041_67218_1200134885}

[**[undo ppp mp soft-binding]{lang="EN-US"}**]{#struct_0_x2041_67218_110163503}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_166032593}

[[同时支持两种捆绑模式的接口，缺省采用硬件捆绑模式。]{style="font-family:宋体"}]{#struct_0_x2041_67218_x250635534}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_867609537}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1708872603}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1218184116}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1925392525}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_2781218}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_165442762}

[[MP]{lang="EN-US"}]{#struct_0_x2041_67218_x1237584815}[捆绑有如下两种捆绑模式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[硬件捆绑模式：报文的分片和重组通过硬件实现，效率高。]{style="font-family:宋体"}]{#struct_0_x2041_67218_1096984133}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[软件捆绑模式：报文的分片和重组通过]{style="font-family:宋体"}]{#struct_0_x2041_67218_172894705}[CPU]{lang="EN-US"}[实现，效率较低。]{style="font-family:宋体"}

[[不同接口支持的]{style="font-family:宋体"}[MP]{lang="EN-US"}]{#struct_0_x2041_67218_1489944096}[捆绑模式不同，有的接口只支持硬件捆绑模式，有的接口只支持软件捆绑模式，有的接口同时支持两种捆绑模式。]{style="font-family:宋体"}

[[同时支持两种捆绑模式的接口，缺省采用硬件捆绑模式，在如下情况可以通过命令切换为软件捆绑模式：]{style="font-family:宋体"}]{#struct_0_x2041_67218_1948141760}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CPOS E1/T1]{lang="EN-US"}]{#struct_0_x2041_67218_195999828}[接口卡不支持跨]{style="font-family:
宋体"}[CPOS]{lang="EN-US"}[接口的硬件]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑，只能将同一个]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口通道化生成的多个同步串口进行硬件]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑，如果用户想将不同]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口通道化生成的多个同步串口进行]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑，必须先将这些同步串口的捆绑模式切换为软件捆绑模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[硬件捆绑模式的接口不能和软件捆绑模式的接口进行]{style="font-family:宋体"}]{#struct_0_x2041_67218_165508298}[MP]{lang="EN-US"}[捆绑。当用户想将支持两种捆绑模式的接口和只支持软件捆绑模式的接口进行]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑时，必须先将硬件捆绑模式的接口切换为软件捆绑模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_328940498}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1269645784}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[采用软件捆绑模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1320117607}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp mp soft-binding]{lang="EN-US"}
:::

::: {#-49163180 .myid}
[]{#_Toc404785086}[]{#struct_0_x2041_67218_x967413700}[]{#_Toc342919810}[]{#_Toc341432213}[]{#_Toc322966196}[]{#_Toc96758151}[]{#_Toc31795060}[]{#_Toc322966194}[]{#_Toc259009524}

**PPP和MP \-- MP配置命令 \-- ppp mp sort-buffer-size**

------------------------------------------------------------------------

[**[ppp mp sort-buffer-size]{lang="EN-US"}**]{#struct_0_x2041_67218_888635157}[命令用来配置]{style="font-family:宋体"}[MP]{lang="EN-US"}[排序窗口的大小。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ppp mp sort-buffer-size**]{lang="EN-US"}]{#struct_0_x2041_67218_546506232}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1150669824}

[**[ppp mp ]{lang="SV"}[sort-buffer-size]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_x2041_67218_1974140223}

[**[undo]{lang="EN-US"}**[ **ppp mp** **sort-buffer-size**]{lang="EN-US"}]{#struct_0_x2041_67218_343815398}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x393248499}

[[MP]{lang="EN-US"}]{#struct_0_x2041_67218_133660834}[排序窗口大小系数为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x293881427}

[[虚拟模板接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x967479236}[/Dialer]{lang="SV"}[接口视图]{style="font-family:宋体"}[/]{lang="SV"}[MP-group]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1824657144}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_5397869}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_165687025}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_963322893}

[*[size]{lang="EN-US"}*]{#struct_0_x2041_67218_1884149691}[：]{style="font-family:宋体"}[MP]{lang="EN-US"}[排序窗口大小系数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1493190415}

[[MP]{lang="EN-US"}]{#struct_0_x2041_67218_529750159}[排序窗口大小＝]{style="font-family:宋体"}[MP]{lang="EN-US"}[当前加入的子通道个数×]{style="font-family:宋体"}*[size]{lang="EN-US"}*[。其中，]{style="font-family:宋体"}[MP]{lang="EN-US"}[当前加入的子通道个数可以通过]{style="font-family:宋体"}**[display ppp mp]{lang="EN-US"}**[命令查询。如果计算出来的]{style="font-family:宋体"}[MP]{lang="EN-US"}[排序窗口大小为]{style="font-family:宋体"}[20]{lang="EN-US"}[，则表示可对]{style="font-family:宋体"}[20]{lang="EN-US"}[个报文进行排序。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[MP]{lang="EN-US"}]{#struct_0_x2041_67218_x1078013076}[情况下，接收端收到的报文很可能乱序。因此需要对接收到的报文进行排序。窗口越大排序结果越好，但会增大报文的延迟。对于语音报文，应避免出现延时过大的问题。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x967544772}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x686165100}[配置]{style="font-family:宋体"}[MP]{lang="EN-US"}[排序窗口的大小。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1200065389}

[\[Sysname\] interface mp-group 1]{lang="EN-US"}

[\[Sysname-MP-group1\] ppp mp sort-buffer-size 64]{lang="EN-US"}
:::

::: {#2092894719 .myid}
[]{#_Toc404785087}[]{#struct_0_x2041_67218_2023779049}[]{#_Toc342919811}[]{#_Toc341432214}[]{#_1.2.8__ppp}

**PPP和MP \-- MP配置命令 \-- ppp mp timer lost-fragment**

------------------------------------------------------------------------

[**[ppp mp timer lost-fragment]{lang="SV"}**]{#struct_0_x2041_67218_x1000259401}[命令用来配置]{style="font-family:宋体"}[MP]{lang="EN-US"}[等待期望分片报文的时间。]{style="font-family:宋体"}

[**[undo ]{lang="SV"}**]{#struct_0_x2041_67218_1138516205}**[ppp mp timer lost-fragment]{lang="SV"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_116534082}

[**[ppp mp timer lost-fragment]{lang="SV"}***[ seconds]{lang="EN-US"}*]{#struct_0_x2041_67218_x1823779855}

[**[undo ppp mp timer lost-fragment]{lang="SV"}**]{#struct_0_x2041_67218_x967610308}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2057118086}

[[MP]{lang="EN-US"}]{#struct_0_x2041_67218_2135276815}[等待期望分片报文的时间为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1117184221}

[[虚拟模板接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1931434950}[/Dialer]{lang="SV"}[接口视图]{style="font-family:宋体"}[/MP-group]{lang="SV"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x346406362}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1426565710}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x354186144}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x789891488}

[*[seconds]{lang="EN-US"}*]{#struct_0_x2041_67218_x967675844}[：表示]{style="font-family:宋体"}[MP]{lang="EN-US"}[等待期望分片报文的时间，取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[255]{lang="SV"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1525978991}

[[MP]{lang="EN-US"}]{#struct_0_x2041_67218_344697598}[报文被分片发送后，接收端会将这些分片重新组装成一个报文。当接收端收到分片报文后，会先将这些分片报文放到缓冲区中，待收到该报文的所有分片后，再将分片组装起来。用户可以配置]{style="font-family:宋体"}[MP]{lang="EN-US"}[等待期望分片报文的时间。当接收端收到某报文的第一个分片后，就开启等待期望分片报文的定时器，当这个定时器超时后，系统查看是否收到了该报文的所有分片，如果已经收到了所有分片，则将分片报文组装起来；如果收到的分片不完整，则认为分片报文丢失，将已经收到的该报文的所有分片都丢弃，以空出缓冲区。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_623696996}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x434034564}[配置]{style="font-family:宋体"}[MP]{lang="EN-US"}[等待期望分片报文的时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1497370433}

[\[Sysname\] interface mp-group 1]{lang="EN-US"}

[\[Sysname-MP-group1\] ppp mp timer lost-fragment 20]{lang="EN-US"}
:::

::: {#509651284 .myid}
[]{#_Toc404785088}[]{#struct_0_x2041_67218_1371532960}[]{#_Toc346386963}

**PPP和MP \-- MP配置命令 \-- ppp mp user**

------------------------------------------------------------------------

[**[ppp mp user]{lang="NO-BOK"}**]{#struct_0_x2041_67218_1922112916}[命令用来配置根据用户名进行]{style="font-family:宋体"}[MP]{lang="NO-BOK"}[捆绑。]{style="font-family:宋体"}

[**[undo]{lang="NO-BOK"}**]{#struct_0_x2041_67218_1700207864}[ **ppp mp user**]{lang="NO-BOK"}[命令用来取消已经配置的根据用户名进行]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1371467424}

[**[ppp mp user]{lang="EN-US"}***[ username]{lang="EN-US"}*[ **bind virtual-template** *number*]{lang="EN-US"}]{#struct_0_x2041_67218_342457228}

[**[undo ppp mp user]{lang="EN-US"}**[ *username*]{lang="EN-US"}]{#struct_0_x2041_67218_206116081}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2141079273}

[[不根据用户名进行]{style="font-family:宋体"}[MP]{lang="EN-US"}]{#struct_0_x2041_67218_1371926176}[捆绑。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1488056197}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1957207905}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x29863018}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1371860640}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x34982909}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x494523572}

[*[username]{lang="EN-US"}*]{#struct_0_x2041_67218_x1524709320}[：用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[bind virtual-template]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_x2041_67218_1371401889}[：绑定的虚拟模板接口。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[用来指定虚拟模板接口号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_379305968}

[[在]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_1009792703}[建立连接的过程中，当]{style="font-family:宋体"}[PPP]{lang="EN-US"}[认证通过后，如果该用户名指定的虚拟模板接口存在，则将按照虚拟模板接口的参数进行]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑，并创建一个]{style="font-family:宋体"}[VA]{lang="EN-US"}[口进行数据传输。]{style="font-family:宋体"}

[[在虚拟模板接口上可以配置的工作参数包括：]{style="font-family:宋体"}]{#struct_0_x2041_67218_2032024147}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地]{style="font-family:宋体"}]{#struct_0_x2041_67218_1371336353}[IP]{lang="EN-US"}[地址和为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[对端分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址（或地址池）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp]{lang="EN-US"}**]{#struct_0_x2041_67218_1864495305}[相关命令]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1917085105}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1371270817}[指定用户名]{style="font-family:宋体"}[user1]{lang="EN-US"}[对应的虚拟模板接口为]{style="font-family:宋体"}[1]{lang="EN-US"}[，并配置该虚拟模板接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}[202.38.60.1/24]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1188022968}

[\[Sysname\] ppp mp user user1 bind virtual-template 1]{lang="EN-US"}

[\[Sysname\] interface virtual-template 1]{lang="EN-US"}

[\[Sysname-Virtual-Template1\] ip address 202.38.60.1 255.255.255.0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x391168869}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp]{lang="EN-US"}**]{#struct_0_x2041_67218_1862500548}
:::

::: {#-1584468699 .myid}
[]{#_Toc404785089}[]{#struct_0_x2041_67218_1371205281}[]{#_Toc346386964}

**PPP和MP \-- MP配置命令 \-- ppp mp virtual-template**

------------------------------------------------------------------------

[**[ppp mp ]{lang="EN-US"}[virtual-template]{lang="EN-US"}**]{#struct_0_x2041_67218_322147090}[命令用来将当前接口加入指定的虚拟模板接口，使接口工作在]{style="font-family:宋体"}[MP]{lang="EN-US"}[方式。]{style="font-family:宋体"}

[**[undo ppp mp]{lang="EN-US"}**]{#struct_0_x2041_67218_235154402}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1694742971}

[**[ppp mp virtual-template]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x2041_67218_1371664033}

[**[undo ppp mp]{lang="EN-US"}**]{#struct_0_x2041_67218_x1622079698}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x584762846}

[[接口工作在普通]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x630236198}[方式下。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1371598497}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x799895659}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x210074506}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_214410277}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1371532961}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1922047380}

[*[number]{lang="EN-US"}*]{#struct_0_x2041_67218_x288768195}[：接口所要绑定的虚拟模板接口号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1371467425}

[[本命令实现了在接口上指定要绑定的虚拟模板接口号，将该接口绑定到指定的虚拟模板接口上。配置该命令的接口进行]{style="font-family:宋体"}[MP]{lang="EN-US"}]{#struct_0_x2041_67218_342522764}[绑定时，可以不用配置]{style="font-family:宋体"}[PAP]{lang="EN-US"}[、]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[、]{style="font-family:宋体"}[MS-CHAP]{lang="EN-US"}[或]{style="font-family:宋体"}[MS-CHAP-V2]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[两个或多个配置了相同虚拟模板接口号的接口直接绑定在一起。另外，在接口上该命令与]{style="font-family:宋体"}**[ppp mp]{lang="EN-US"}**]{#struct_0_x2041_67218_x1383025027}[命令互斥，即同一个接口只能配置这两条命令中的一条。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1986470730}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1371926177}[配置封装]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[工作在]{style="font-family:宋体"}[MP]{lang="EN-US"}[方式下，绑定的虚拟模板接口为]{style="font-family:宋体"}[Virtual-Template1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1488121733}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp mp virtual-template 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1548948499}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp]{lang="EN-US"}**]{#struct_0_x2041_67218_x857162079}
:::

::: {#-1559920555 .myid}
[]{#_Toc404785090}[]{#struct_0_x2041_67218_x442804013}[]{#_Toc342919795}[]{#_Toc335656819}[]{#_Toc323804933}[]{#_Toc347925534}[]{#_Toc350266115}[]{#_Toc259009526}

**PPP和MP \-- MP配置命令 \-- reset counters interface mp-group**

------------------------------------------------------------------------

[**[reset counters interface mp-group]{lang="EN-US"}**]{#struct_0_x2041_67218_x967741380}[命令用来清除]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_481924618}

[**[reset counters interface]{lang="EN-US"}**[ \[ **mp-group** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x2041_67218_x2036934254}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_146139948}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_695804842}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1467001958}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1829554282}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x92315431}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x249614742}

[**[mp-group]{lang="EN-US"}**]{#struct_0_x2041_67218_x966758340}[：清除]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x2041_67218_2056813707}[：]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口的编号。取值范围为已创建的]{style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_589085111}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_x2041_67218_x880356955}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_179383748}**[mp-group]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_x1379480505}**[mp-group]{lang="EN-US"}**[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_983597738}**[mp-group]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[MP-group]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_730519091}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x966823876}[清除接口]{style="font-family:宋体"}[MP-group3]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface mp-group 3]{lang="EN-US"}]{#struct_0_x2041_67218_2063105942}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_845712877}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface ]{lang="EN-US"}**]{#struct_0_x2041_67218_x1641159786}**[mp-group]{lang="EN-US"}**
:::

::: {#-994061322 .myid}
[]{#_Toc404785091}[]{#struct_0_x2041_67218_x1224851178}[]{#_Toc342919796}[]{#_Toc335656820}[]{#_1.2.10__ppp}

**PPP和MP \-- MP配置命令 \-- reset counters interface virtual-access**

------------------------------------------------------------------------

[**[reset counters interface virtual-access]{lang="EN-US"}**]{#struct_0_x2041_67218_x1677369105}[命令用来清除]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x36540291}

[**[reset counters interface]{lang="EN-US"}**[ \[ **virtual-access** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x2041_67218_1161235065}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x60515561}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_598801316}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x988352047}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1766630569}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1771456174}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1194127395}

[**[virtual-access]{lang="EN-US"}**]{#struct_0_x2041_67218_x262091486}[：清除]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x2041_67218_677614835}[：]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的编号。取值范围为已创建的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1865125299}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_x2041_67218_598735780}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_705217634}**[virtual-]{lang="EN-US"}[access]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_x319729722}**[virtual-]{lang="EN-US"}[access]{lang="EN-US"}**[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[VA]{lang="EN-US"}[接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_1788281599}**[virtual-]{lang="EN-US"}[access]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[VA]{lang="EN-US"}[接口的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1498026937}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_192838743}[清除]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface virtual-access 10]{lang="EN-US"}]{#struct_0_x2041_67218_1681178475}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1254412927}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface ]{lang="EN-US"}**]{#struct_0_x2041_67218_231357273}**[virtual-]{lang="EN-US"}[access]{lang="EN-US"}**
:::

::::: {#-780779607 .myid}
[]{#_Toc404785092}[]{#struct_0_x2041_67218_598670244}[]{#_Toc342919797}[]{#_Toc335656821}[]{#_Toc303865071}[]{#_Toc215545670}[]{#_Toc215479545}[]{#_Toc322966212}[]{#_Toc259009545}[]{#_Toc136938094}[]{#_Toc96758168}[]{#_Toc85625770}

**PPP和MP \-- MP配置命令 \-- service**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image003.png){#图片 7 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x2041_67218_x1592164901}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_1456277672}
:::

[ ]{lang="EN-US"}

[**[service]{lang="EN-US"}**]{#struct_0_x2041_67218_x61410025}[命令用来指定转发当前虚拟模板接口下]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口流量的业务板。]{style="font-family:宋体"}

[**[undo service]{lang="EN-US"}**]{#struct_0_x2041_67218_480367124}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x954301372}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_242384276}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[service slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x849473645}

[**[undo service slot]{lang="EN-US"}**]{#struct_0_x2041_67218_x1545167689}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2041_67218_598604708}[模式：]{style="font-family:宋体"}

[**[service ]{lang="EN-US"}[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1605974969}

[**[undo service ]{lang="EN-US"}[chassis]{lang="EN-US"}**]{#struct_0_x2041_67218_1472835407}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1280798256}

[[没有指定转发当前虚拟模板接口下]{style="font-family:宋体"}[VA]{lang="EN-US"}]{#struct_0_x2041_67218_455230268}[接口流量的业务板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1581898048}

[[虚拟模板接口视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1248605228}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_169010625}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_598539172}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_874568494}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1981975244}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x75121322}[：指定单板所在的槽位号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2041_67218_1120179219}[：指定设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x2100478370}[：指定设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2041_67218_1655000373}[：指定成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x756886266}[：指定成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x871029481}

[[没有通过]{style="font-family:宋体"}**[service]{lang="EN-US"}**]{#struct_0_x2041_67218_1631774752}[命令指定转发虚拟模板接口下]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口流量的业务板时，会自动选择主控板作为转发虚拟模板接口下]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口流量的业务板。在这种情况下，为了避免主控板处理过多的业务，建议在虚拟模板接口下通过]{style="font-family:宋体"}**[service]{lang="EN-US"}**[命令指定转发该接口下]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口流量的业务板。]{style="font-family:宋体"}

[[需要注意的是，如果拔出指定的转发流量业务板，即使]{style="font-family:宋体"}[VA]{lang="EN-US"}]{#struct_0_x2041_67218_91439688}[接口]{style="font-family:宋体"}[UP]{lang="EN-US"}[，流量也转发不通；如果重新插入指定的转发流量业务板，则流量可以恢复在指定板正常转发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_598473636}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1659457609}[指定在]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板转发虚拟模板接口]{style="font-family:宋体"}[10]{lang="EN-US"}[下]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的流量。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x347409329}

[\[Sysname\] interface virtual-template 10]{lang="EN-US"}

[\[Sysname-Virtual-Template10\] service slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_488385219}[指定在]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备转发虚拟模板接口]{style="font-family:宋体"}[10]{lang="EN-US"}[下]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的流量。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_51214282}

[\[Sysname\] interface virtual-template 10]{lang="EN-US"}

[\[Sysname-Virtual-Template10\] service slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_286115963}[指定在]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板转发虚拟模板接口]{style="font-family:宋体"}[10]{lang="EN-US"}[下]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的流量。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1874007722}

[\[Sysname\] interface virtual-template 10]{lang="EN-US"}

[\[Sysname-Virtual-Template10\]]{lang="EN-US"}[ ]{lang="EN-US"}[service ]{lang="IT"}[chassis]{lang="EN-US"}[ ]{lang="EN-US"}[2 slot 2]{lang="IT"}
:::::

::: {#1170655049 .myid}
[]{#_Toc404785093}[]{#struct_0_x2041_67218_598408100}[]{#_Toc342919798}[]{#_Toc335656822}[]{#_Toc136938095}[]{#_Toc96758169}[]{#_Toc322966213}

**PPP和MP \-- MP配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x2041_67218_1284365065}[命令用来关闭接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_x2041_67218_x1138508134}[命令用来打开接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1220094651}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x2041_67218_x1736704975}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x2041_67218_2020505032}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x424621650}

[[接口处于打开状态。]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1765771720}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1563427606}

[[MP-group]{lang="EN-US"}]{#struct_0_x2041_67218_598342564}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_200584701}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_359035955}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1309685329}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_73951917}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_298046352}[关闭接口]{style="font-family:宋体"}[MP-group3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1138357980}

[\[Sysname\] interface mp-group 3]{lang="EN-US"}

[\[Sysname-MP-group3\] shutdown[]{#_1.2.13__ppp}]{lang="EN-US"}
:::

[\
]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

::: {.Section3 style="layout-grid:15.75pt"}
:::

::: {#-534435856 .myid}
[]{#_Toc404785096}[]{#struct_0_x2041_67218_1371205282}[]{#_Toc366514050}[]{#_Toc336084864}[]{#_Toc332298253}

**PPPoE \-- PPPoE Server配置命令 \-- display pppoe-server session packet**

------------------------------------------------------------------------

[**[display pppoe-server session packet]{lang="EN-US"}**]{#struct_0_x2041_67218_322212626}[命令用来显示]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1482014193}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2041_67218_1371664034}

[**[display pppoe-server ]{lang="EN-US"}[session packet]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2041_67218_x1621752018}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_x1517737391}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display pppoe-server ]{lang="EN-US"}[session packet]{lang="EN-US"}**[ { **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **interface** *interface-type interface-number* }]{lang="EN-US"}]{#struct_0_x2041_67218_1371598498}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2041_67218_x799961195}[模式：]{style="font-family:宋体"}

[**[display pppoe-server ]{lang="EN-US"}[session ]{lang="EN-US"}**]{#struct_0_x2041_67218_x226840075}**[packet]{lang="EN-US"}**[ { **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] *\|* ]{lang="EN-US"}**[interface ]{lang="EN-US"}***[interface-type interface-number ]{lang="EN-US"}*[}]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1371532962}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1922243988}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_124621291}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1371467426}

[[network-operator]{lang="EN-US"}]{#struct_0_x2041_67218_342326156}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1094623157}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2041_67218_1371926178}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1488973701}

[**[interface]{lang="EN-US"}***[ interface]{lang="EN-US"}*[-*type interface*-*number*]{lang="EN-US"}]{#struct_0_x2041_67218_1589838256}[：显示指定接口的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息。]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[-*type interface*-*number*]{lang="EN-US"}[用来指定接口的类型和编号。对于集中式设备，如果不指定本参数，则显示所有接口的]{style="font-family:
宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_1371860642}[：显示指定单板的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定本参数时，将显示所有单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x35113981}[：显示指定成员设备的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定本参数时，将显示所有成员设备的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_1387854336}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定本参数时，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_1008673348}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定本参数时，将显示所有成员设备上所有单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1444329257}[：显示指定单板的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定本参数时，将显示所有单板上的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2041_67218_663624791}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1371401891}

[]{#_Toc60111176}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_379830255}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_189228686}[查看]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server session packet interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x2041_67218_1371336355}

[Total PPPoE sessions: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: GE1/0/1                   Session ID: 1]{lang="EN-US"}

[  InPackets: 37                                 OutPackets: 38]{lang="EN-US"}

[  InBytes: ]{lang="EN-US"}[390]{lang="PT-BR"}[                                  OutBytes: ]{lang="EN-US"}[406]{lang="PT-BR"}

[  InDrops: 0                                    OutDrops: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: GE1/0/1                   Session ID: 2]{lang="EN-US"}

[  InPackets: 67                                 OutPackets: 48]{lang="EN-US"}

[  InBytes: ]{lang="EN-US"}[490]{lang="PT-BR"}[                                  OutBytes: ]{lang="EN-US"}[806]{lang="PT-BR"}

[  InDrops: 1                                    OutDrops: 2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_1864102089}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_801848539}[查看]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server session packet interface vlan-interface 1]{lang="EN-US"}]{#struct_0_x2041_67218_1371270819}

[Total PPPoE sessions: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                     Session ID: 1]{lang="EN-US"}

[  InPackets: 37                                 OutPackets: 38]{lang="EN-US"}

[  InBytes: ]{lang="EN-US"}[390]{lang="PT-BR"}[                                  OutBytes: ]{lang="EN-US"}[406]{lang="PT-BR"}

[  InDrops: 0                                    OutDrops: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                     Session ID: 2]{lang="EN-US"}

[  InPackets: 39                                 OutPackets: 40]{lang="EN-US"}

[  InBytes: ]{lang="EN-US"}[340]{lang="PT-BR"}[                                  OutBytes: ]{lang="EN-US"}[496]{lang="PT-BR"}

[  InDrops: 1                                    OutDrops: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1188940472}[查看]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server session packet interface vlan-interface 1]{lang="EN-US"}]{#struct_0_x2041_67218_1371205283}

[Total PPPoE sessions on slot 3: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                     Session ID: 1]{lang="EN-US"}

[  InPackets: 40                                 OutPackets: 58]{lang="EN-US"}

[  InBytes: ]{lang="EN-US"}[690]{lang="PT-BR"}[                                  OutBytes: ]{lang="EN-US"}[506]{lang="PT-BR"}

[  InDrops: 3                                    OutDrops: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total PPPoE sessions on slot 4: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                     Session ID: 1]{lang="EN-US"}

[  InPackets: 43                                 OutPackets: 59]{lang="EN-US"}

[  InBytes: ]{lang="EN-US"}[790]{lang="PT-BR"}[                                  OutBytes: ]{lang="EN-US"}[576]{lang="PT-BR"}

[  InDrops: 2                                    OutDrops: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                     Session ID: 2]{lang="EN-US"}

[  InPackets: 35                                 OutPackets: 36]{lang="EN-US"}

[  InBytes: ]{lang="EN-US"}[370]{lang="PT-BR"}[                                  OutBytes: ]{lang="EN-US"}[386]{lang="PT-BR"}

[  InDrops: 0                                    OutDrops: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_322278162}[查看]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server session packet interface vlan-interface 1]{lang="EN-US"}]{#struct_0_x2041_67218_1371664035}

[Total PPPoE sessions on chassis 1 slot 3: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                     Session ID: 1]{lang="EN-US"}

[  InPackets: 40                                 OutPackets: 58]{lang="EN-US"}

[  InBytes: ]{lang="EN-US"}[690]{lang="PT-BR"}[                                  OutBytes: ]{lang="EN-US"}[506]{lang="PT-BR"}

[  InDrops: 3                                    OutDrops: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total PPPoE sessions on chassis 1 slot 4: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                     Session ID: 1]{lang="EN-US"}

[  InPackets: 40                                 OutPackets: 58]{lang="EN-US"}

[  InBytes: ]{lang="EN-US"}[690]{lang="PT-BR"}[                                  OutBytes: ]{lang="EN-US"}[506]{lang="PT-BR"}

[  InDrops: 3                                    OutDrops: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total PPPoE sessions on chassis 2 slot 1: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                     Session ID: 1]{lang="EN-US"}

[  InPackets: 43                                 OutPackets: 59]{lang="EN-US"}

[  InBytes: ]{lang="EN-US"}[790]{lang="PT-BR"}[                                  OutBytes: ]{lang="EN-US"}[576]{lang="PT-BR"}

[  InDrops: 2                                    OutDrops: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                     Session ID: 2]{lang="EN-US"}

[  InPackets: 35                                 OutPackets: 36]{lang="EN-US"}

[  InBytes: ]{lang="EN-US"}[370]{lang="PT-BR"}[                                  OutBytes: ]{lang="EN-US"}[386]{lang="PT-BR"}

[  InDrops: 0                                    OutDrops: 0]{lang="EN-US"}

[[表2-1 ]{lang="EN-US"}[display pppoe-server session packet]{lang="EN-US"}]{#struct_0_x2041_67218_x1621686482}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1479227664}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_1371598499}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_x800026731}

[[Ethernet interface]{lang="EN-US"}]{#struct_0_x2041_67218_1371532963}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_1371467427}[会话绑定的接口]{style="font-family:宋体"}

[[Session ID]{lang="EN-US"}]{#struct_0_x2041_67218_342391692}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_1371926179}[会话的编号]{style="font-family:宋体"}

[[InPackets]{lang="EN-US"}]{#struct_0_x2041_67218_1489039237}

[[接收报文数]{style="font-family:宋体"}]{#struct_0_x2041_67218_1371860643}

[[OutPackets]{lang="EN-US"}]{#struct_0_x2041_67218_x1357481469}

[[发送报文数]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1099082541}

[[InBytes]{lang="EN-US"}]{#struct_0_x2041_67218_x1357547005}

[[接收字节数]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1357612541}

[[OutBytes]{lang="EN-US"}]{#struct_0_x2041_67218_x843661825}

[[发送字节数]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1357678077}

[[InDrops]{lang="EN-US"}]{#struct_0_x2041_67218_1584329322}

[[接收非法并丢弃的报文数]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1357219325}

[[OutDrops]{lang="EN-US"}]{#struct_0_x2041_67218_x1357284861}

[[发送非法并丢弃的报文数]{style="font-family:宋体"}]{#struct_0_x2041_67218_x2111524857}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1357350397}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface]{lang="EN-US"}**]{#struct_0_x2041_67218_x1172589341}**[ ]{lang="EN-US"}[virtual-access]{lang="EN-US"}**

::: {#-871850364 .myid}
[]{#_Toc404785097}[]{#struct_0_x2041_67218_x1538857375}[]{#_Toc366514051}

**PPPoE \-- PPPoE Server配置命令 \-- display pppoe-server session summary**

------------------------------------------------------------------------

[**[display pppoe-server session summary]{lang="EN-US"}**]{#struct_0_x2041_67218_x1357415933}[命令用来显示]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_180594497}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x278334158}

[**[display pppoe-server ]{lang="EN-US"}[session summary]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2041_67218_x1356957181}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_x699752908}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display pppoe-server ]{lang="EN-US"}[session summary]{lang="EN-US"}**[ { **slot** *slot-number* \[ **cpu** *cpu-number* \] *\|* **interface** *interface-type interface-number* }]{lang="EN-US"}]{#struct_0_x2041_67218_x1191035631}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2041_67218_x1357022717}[模式：]{style="font-family:宋体"}

[**[display pppoe-server ]{lang="EN-US"}[session ]{lang="EN-US"}**]{#struct_0_x2041_67218_182103858}**[summary]{lang="EN-US"}**[ { **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] *\|* ]{lang="EN-US"}**[interface ]{lang="EN-US"}***[interface-type interface-number ]{lang="EN-US"}*[}]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2000541872}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1357481468}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1629800814}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1836436776}

[[network-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x1357547004}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x147179446}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x1718146502}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1357612540}

[**[interface]{lang="EN-US"}***[ interface]{lang="EN-US"}*[-*type interface*-*number*]{lang="EN-US"}]{#struct_0_x2041_67218_722422116}[：显示指定接口的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[-*type interface*-*number*]{lang="EN-US"}[用来指定接口的类型和编号。对于集中式设备，如果不指定本参数，则显示所有接口的]{style="font-family:
宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_338792121}[：显示指定单板的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定本参数时，将显示所有单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1357678076}[：显示指定成员设备的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定本参数时，将显示所有成员设备的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x2100543906}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定本参数时，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1144554033}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定本参数时，将显示所有成员设备上所有单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_488484707}[：显示指定单板的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定本参数时，将显示所有单板上的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x2065389632}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1880526182}

[[通过物理接口上线的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x1880591718}[会话信息只在物理接口所在单板显示，通过逻辑接口上线的全局]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话信息将在所有单板显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_503470714}

[]{#_Toc60111175}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_x1357219324}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_234363862}[查看]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[]{#struct_0_x2041_67218_318102637}[]{#_Toc95359206}[]{#_Toc85604317}[]{#_Toc81386696}[]{#_Toc74661819}[]{#_Toc72589782}[]{#_Toc72589509}[]{#_Toc72588994}[]{#_Toc65921164}[]{#_Toc65919112}[]{#_Toc65919087}[]{#_Toc65910721}[]{#_Toc65909966}[]{#_Toc60125176}[\<Sysname\> display pppoe-server session summary interface gigabitethernet 1/0/1]{lang="EN-US"}

[Total PPPoE sessions: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: GE1/0/1                  Session ID: 1]{lang="EN-US"}

[  PPP interface: VA1                           State: PADR_RCVD]{lang="EN-US"}

[  Remote MAC: 00e0-1500-7100                   Local MAC: 00e0-1400-7300]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: GE1/0/1                  Session ID: 2]{lang="EN-US"}

[  PPP interface: VA2                           State: OPEN]{lang="EN-US"}

[  Remote MAC:00e0-1600-7200                    Local MAC: 00e0-1400-7400]{lang="EN-US"}

[  Service VLAN: 2                              Customer VLAN: 155]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1880198502}[查看所有接口的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server session summary]{lang="EN-US"}]{#struct_0_x2041_67218_x314573316}

[Total PPPoE sessions: 2]{lang="EN-US"}

[Local PPPoE sessions: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: GE1/0/2                  Session ID: 1]{lang="EN-US"}

[  PPP interface: VA1                           State: OPEN]{lang="EN-US"}

[  Remote MAC: 0000-0000-0005                   Local MAC: 0000-5e00-0101]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: RAGG1                    Session ID: 1]{lang="EN-US"}

[  PPP interface: VA0                           State: OPEN ]{lang="EN-US"}

[  Remote MAC: 0050-56c0-0005                   Local MAC: 0000-5e00-0102]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x314638852}[查看主控板]{style="font-family:宋体"}[Slot 0]{lang="EN-US"}[上的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server session summary slot 0]{lang="EN-US"}]{#struct_0_x2041_67218_x314704388}

[Total PPPoE sessions on slot 0: 1]{lang="EN-US"}

[Local PPPoE sessions on slot 0: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: RAGG1                    Session ID: 1]{lang="EN-US"}

[  PPP interface: VA0                           State: OPEN]{lang="EN-US"}

[  Remote MAC: 0050-56c0-0005                   Local MAC: 0000-5e00-0102]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_927966516}[查看接口板]{style="font-family:宋体"}[Slot 2]{lang="EN-US"}[上的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server session summary slot 2]{lang="EN-US"}]{#struct_0_x2041_67218_x314769924}

[Total PPPoE sessions on slot 2: 2]{lang="EN-US"}

[Local PPPoE sessions on slot 2: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: GE2/0/2                  Session ID: 1]{lang="EN-US"}

[  PPP interface: VA1                           State: OPEN]{lang="EN-US"}

[  Remote MAC: 0000-0000-0005                   Local MAC: 0000-5e00-0101]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[   ]{lang="EN-US"}

[  Ethernet interface: RAGG1                    Session ID: 1]{lang="EN-US"}

[  PPP interface: VA0                           State: OPEN ]{lang="EN-US"}

[  Remote MAC: 0050-56c0-0005                   Local MAC: 0000-5e00-0102]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x314311172}[查看成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的主控板]{style="font-family:宋体"}[Slot 0]{lang="EN-US"}[上的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server session summary chassis 1 slot 0]{lang="EN-US"}]{#struct_0_x2041_67218_x314376708}

[Total PPPoE sessions on chassis 1 slot 0: 1]{lang="EN-US"}

[Local PPPoE sessions on chassis 1 slot 0: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: RAGG1                    Session ID: 1]{lang="EN-US"}

[  PPP interface: VA0                           State: OPEN]{lang="EN-US"}

[  Remote MAC: 0050-56c0-0005                   Local MAC: 0000-5e00-0102]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x314442244}[查看成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的接口板]{style="font-family:宋体"}[Slot 2]{lang="EN-US"}[上的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server session summary chassis 1 slot 2]{lang="EN-US"}]{#struct_0_x2041_67218_x314507780}

[Total PPPoE sessions on chassis 1 slot 2: 2]{lang="EN-US"}

[Local PPPoE sessions on chassis 1 slot 2: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: GE2/0/2                  Session ID: 1]{lang="EN-US"}

[  PPP interface: VA1                           State: OPEN]{lang="EN-US"}

[  Remote MAC: 0000-0000-0005                   Local MAC: 0000-5e00-0101]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: RAGG1                    Session ID: 1]{lang="EN-US"}

[  PPP interface: VA0                           State: OPEN ]{lang="EN-US"}

[  Remote MAC: 0050-56c0-0005                   Local MAC: 0000-5e00-0102]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_x1357284860}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_617358498}[查看]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server session summary interface vlan-interface 1]{lang="EN-US"}]{#struct_0_x2041_67218_x1357350396}

[Total PPPoE sessions: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                    Session ID: 1]{lang="EN-US"}

[  PPP interface: VA1                           State: PADR_RCVD]{lang="EN-US"}

[  Remote MAC: 00e0-1500-7100                   Local MAC: 00e0-1400-7300]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                    Session ID: 2]{lang="EN-US"}

[  PPP interface: VA2                           State: OPEN]{lang="EN-US"}

[  Remote MAC: 00e0-1500-7100                   Local MAC: 00e014007400]{lang="EN-US"}

[  Service VLAN: 2                              Customer VLAN: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_393494600}[查看]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server session summary interface vlan-interface 1]{lang="EN-US"}]{#struct_0_x2041_67218_x1357415932}

[Total PPPoE sessions on slot 1: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                    Session ID: 1]{lang="EN-US"}

[  PPP interface: VA1                           State: PADR_RCVD]{lang="EN-US"}

[  Remote MAC: 00e0-1500-7100                   Local MAC: 00e0-1400-7300]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total PPPoE sessions on slot 2: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                    Session ID: 1]{lang="EN-US"}

[  PPP interface: VA1                           State: PADR_RCVD]{lang="EN-US"}

[  Remote MAC: 00e0-1500-7100                   Local MAC: 00e0-1400-7300]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                    Session ID: 2]{lang="EN-US"}

[  PPP interface: VA2                           State: OPEN]{lang="EN-US"}

[  Remote MAC: 00e0-1500-7100                   Local MAC: 00e0-1400-7400]{lang="EN-US"}

[  Service VLAN: 2                              Customer VLAN: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1746678438}[查看]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server session summary interface vlan-interface 1]{lang="EN-US"}]{#struct_0_x2041_67218_x1356957180}

[Total PPPoE sessions on chassis 1 slot 1: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                    Session ID: 1]{lang="EN-US"}

[  PPP interface: VA1                           State: PADR_RCVD]{lang="EN-US"}

[  Remote MAC: 00e0-1500-7100                   Local MAC: 00e0-1400-7200]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total PPPoE sessions on chassis 1 slot 2: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                    Session ID: 1]{lang="EN-US"}

[  PPP interface: VA1                           State: PADR_RCVD]{lang="EN-US"}

[  Remote MAC: 00e0-1500-7100                   Local MAC: 00e0-1400-9300]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total PPPoE sessions on chassis 2 slot 2: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                    Session ID: 1]{lang="EN-US"}

[  PPP interface: VA1                           State: PADR_RCVD]{lang="EN-US"}

[  Remote MAC: 00e0-1500-7100                   Local MAC: 00e0-1400-7300]{lang="EN-US"}

[  Service VLAN: N/A                            Customer VLAN: N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Ethernet interface: Vlan1                    Session ID: 2]{lang="EN-US"}

[  PPP interface: VA2                           State: OPEN]{lang="EN-US"}

[  Remote MAC: 00e0-1500-7100                   Local MAC: 00e0-1400-7400]{lang="EN-US"}

[  Service VLAN: 2                              Customer VLAN: 1]{lang="EN-US"}

[[表2-2 ]{lang="EN-US"}[display pppoe-server session summary]{lang="EN-US"}]{#struct_0_x2041_67218_866331033}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1493357438}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1357022716}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1383980083}

[[Total PPPoE sessions]{lang="EN-US"}]{#struct_0_x2041_67218_x314507781}

[[（集中式设备）上线]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x314049029}[会话总数（包括通过物理接口和逻辑接口上线的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话总数）]{style="font-family:宋体"}

[[Local PPPoE sessions]{lang="EN-US"}]{#struct_0_x2041_67218_x314114565}

[[（集中式设备）通过物理接口上线的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x314573318}[会话总数]{style="font-family:宋体"}

[[（当命令行中指定了接口时，不显示本字段）]{style="font-family:宋体"}]{#struct_0_x2041_67218_x314704390}

[[Total PPPoE sessions on slot *slot-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x314769926}

[[（分布式设备－独立运行模式）上线]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x314311174}[会话总数（指定单板显示时，包含通过本板物理接口上线的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话和全局]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话总数）]{style="font-family:宋体"}

[[Local PPPoE sessions on slot *slot-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x314442246}

[[（分布式设备－独立运行模式）通过本板物理接口上线的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x314507782}[会话总数]{style="font-family:宋体"}

[[（当命令行中指定了接口时，不显示本字段）]{style="font-family:宋体"}]{#struct_0_x2041_67218_x314049030}

[[Total PPPoE sessions on slot *slot-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x314114566}

[[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2041_67218_x314573319}[设备）上线]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话总数（指定成员设备显示时，包含通过本成员设备的物理接口上线的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话和全局]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话总数）]{style="font-family:宋体"}

[[Local PPPoE sessions on slot *slot-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x314704391}

[[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2041_67218_x314769927}[设备）通过本成员设备的物理接口上线的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话总数]{style="font-family:宋体"}

[[（当命令行中指定了接口时，不显示本字段）]{style="font-family:宋体"}]{#struct_0_x2041_67218_x314376711}

[[Total PPPoE sessions on chassis *chassis-number* slot *slot-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x314442247}

[[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2041_67218_x314507783}[模式）上线]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话总数（指定单板显示时，包含通过本板物理接口上线的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话和全局]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话总数）]{style="font-family:宋体"}

[[Local PPPoE sessions on chassis *chassis-number* slot *slot-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x314114567}

[[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2041_67218_x314573312}[模式）通过本板物理接口上线的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话总数]{style="font-family:宋体"}

[[（当命令行中指定了接口时，不显示本字段）]{style="font-family:宋体"}]{#struct_0_x2041_67218_x314638848}

[[Ethernet interface]{lang="EN-US"}]{#struct_0_x2041_67218_x1357481467}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x1357547003}[会话绑定的接口]{style="font-family:宋体"}

[[Session ID]{lang="EN-US"}]{#struct_0_x2041_67218_612335441}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x1357612539}[会话的编号]{style="font-family:宋体"}

[[PPP interface]{lang="EN-US"}]{#struct_0_x2041_67218_x1357678075}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x1547838560}[会话的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x2041_67218_x1357219323}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_1800447803}[会话的状态，取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PADR_RCVD]{lang="EN-US"}]{#struct_0_x2041_67218_x1357284859}[：表示]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话正在创建中，处于会话协商阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OPEN]{lang="EN-US"}]{#struct_0_x2041_67218_x1357350395}[：表示]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[处于会话阶段]{style="font-family:宋体"}

[[Remote MAC]{lang="EN-US"}]{#struct_0_x2041_67218_1959578541}

[[对端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2041_67218_x1357415931}[地址]{style="font-family:宋体"}

[[Local MAC]{lang="EN-US"}]{#struct_0_x2041_67218_x1356957179}

[[本端]{style="font-family:宋体"}]{#struct_0_x2041_67218_x343719156}[MAC]{lang="PT-BR"}[地址]{style="font-family:宋体"}

[[Service VLAN]{lang="EN-US"}]{#struct_0_x2041_67218_x1357022715}

[[服务提供商]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2041_67218_x1357481466}[（]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示没有此信息）]{style="font-family:宋体"}

[[Customer VLAN]{lang="EN-US"}]{#struct_0_x2041_67218_467001400}

[[用户]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2041_67218_x1357547002}[（]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示没有此信息）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-549973214 .myid}
[]{#_Toc404785098}[]{#struct_0_x2041_67218_x953748500}[]{#_Toc366514052}

**PPPoE \-- PPPoE Server配置命令 \-- display pppoe-server throttled-mac**

------------------------------------------------------------------------

[**[display pppoe-server throttled-mac]{lang="EN-US"}**]{#struct_0_x2041_67218_307009412}[命令用来显示被扼制的用户信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1357612538}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2041_67218_366126220}

[**[display pppoe-server ]{lang="EN-US"}[throttled-mac ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2041_67218_518337597}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_x1357678074}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display pppoe-server ]{lang="EN-US"}[throttled-mac ]{lang="EN-US"}**[{ **slot** *slot-number* \[ **cpu** *cpu-number* \] *\|* ]{lang="EN-US"}]{#struct_0_x2041_67218_18245381}**[interface ]{lang="EN-US"}***[interface-type interface-number ]{lang="EN-US"}*[}]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2041_67218_x1357219322}[模式：]{style="font-family:宋体"}

[**[display pppoe-server ]{lang="EN-US"}[throttled-mac ]{lang="EN-US"}**[{ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] *\|* ]{lang="EN-US"}]{#struct_0_x2041_67218_x928435552}**[interface ]{lang="EN-US"}***[interface-type interface-number ]{lang="EN-US"}*[}]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1452170358}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1357284858}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_973523322}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x35608707}

[[network-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x1357350394}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x769304814}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x285281427}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1357415930}

[**[interface]{lang="EN-US"}***[ interface]{lang="EN-US"}*[-*type interface*-*number*]{lang="EN-US"}]{#struct_0_x2041_67218_583879024}[：显示指定接口下的被扼制的用户信息。]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[-*type interface*-*number*]{lang="EN-US"}[用来指定接口的类型和编号。对于集中式设备，如果不指定本参数，则显示所有接口的被扼制的用户信息。]{style="font-family:
宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_2013332666}[：显示指定单板的被扼制的用户信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定本参数时，将显示所有单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1356957178}[：显示指定成员设备的被扼制的用户信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定本参数时，将显示所有成员设备的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_628273913}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的被扼制的用户信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定本参数时，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_1222364785}[：显示指定成员设备上指定单板的被扼制的用户信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定本参数时，将显示所有成员设备上所有单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1741477718}[：显示指定单板的被扼制的用户信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定本参数时，将显示所有单板上的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x2065127490}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的被扼制的用户信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1076665969}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_x1357022714}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x221180669}[查看]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口的被扼制的用户信息。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server throttled-mac interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x2041_67218_x585695025}

[Total 3 client MACs:]{lang="EN-US"}

[  Interface   Remote MAC     Start time            Remaining time(s)]{lang="EN-US"}

[  GE1/0/1     00e0-1500-4100 2010-12-01,12:10:30   55]{lang="EN-US"}

[  GE1/0/1     00e0-1500-4000 2010-12-01,12:10:40   65]{lang="EN-US"}

[  GE1/0/1     00e0-1500-3300 2010-12-01,12:10:50   75]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1357481465}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_870285927}[查看]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的被扼制的用户信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server throttled-mac interface vlan-interface 1]{lang="EN-US"}]{#struct_0_x2041_67218_x1357547001}

[Total 3 client MACs:]{lang="EN-US"}

[  Interface        Remote MAC     Start time           Remaining time(s)]{lang="EN-US"}

[  Vlan1            00e0-1500-4100 2010-12-01,12:10:30  55]{lang="EN-US"}

[  Vlan1            00e0-1500-4000 2010-12-01,12:10:40  65]{lang="EN-US"}

[  Vlan1            00e0-1500-3300 2010-12-01,12:10:50  75]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x550463973}[查看]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的被扼制的用户信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server throttled-mac interface vlan-interface 1]{lang="EN-US"}]{#struct_0_x2041_67218_924357822}

[Total 1 client MACs in slot 1:]{lang="EN-US"}

[  Interface        Remote MAC      Start time           Remaining time(s)]{lang="EN-US"}

[  Vlan1            00e0-1500-4100  2010-12-01,12:10:30  55]{lang="EN-US"}

[Total 2 client MACs in slot 2:]{lang="EN-US"}

[  Interface        Remote MAC      Start time            Remaining time(s)]{lang="EN-US"}

[  Vlan1            00e0-1500-6300  2010-12-01,12:10:30   55]{lang="EN-US"}

[  Vlan1            00e0-1500-6000  2010-12-01,12:10:40   65]{lang="EN-US"}

[  Vlan1            00e0-1500-6300  2010-12-01,12:10:50   75]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1357612537}[查看]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的被扼制的用户信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server throttled-mac interface vlan-interface 1]{lang="EN-US"}]{#struct_0_x2041_67218_x1650296415}

[Total 1 client MACs in slot 1 of chassis 1:]{lang="EN-US"}

[  Interface        Remote MAC      Start time           Remaining time(s)]{lang="EN-US"}

[  Vlan1            00e0-1500-4100  2010-12-01,12:10:30  55]{lang="EN-US"}

[Total 1 client MACs in slot 2 of chassis 1:]{lang="EN-US"}

[  Interface        Remote MAC      Start time           Remaining time(s)]{lang="EN-US"}

[  Vlan1            00e0-1700-4100  2010-12-01,12:10:30  55]{lang="EN-US"}

[Total 2 client MACs in slot 1 of chassis 2:]{lang="EN-US"}

[  Interface        Remote MAC     Start time            Remaining time(s)]{lang="EN-US"}

[  Vlan1            00e0-1500-6300 2010-12-01,12:10:30   55]{lang="EN-US"}

[  Vlan1            00e0-1500-6000 2010-12-01,12:10:40   65]{lang="EN-US"}

[  Vlan1            00e0-1500-6300 2010-12-01,12:10:50   75]{lang="EN-US"}

[[表2-3 ]{lang="EN-US"}[display pppoe-server throttled-mac]{lang="EN-US"}]{#struct_0_x2041_67218_x1357678073}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1515184864}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_x385039146}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1357219321}

[[Interface]{lang="EN-US"}]{#struct_0_x2041_67218_x1357284857}

[[被扼制的用户的上线接口]{style="font-family:宋体"}]{#struct_0_x2041_67218_1376807849}

[[Remote MAC]{lang="EN-US"}]{#struct_0_x2041_67218_x1357350393}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2041_67218_1153009487}[地址]{style="font-family:宋体"}

[[Start time]{lang="EN-US"}]{#struct_0_x2041_67218_x1357415929}

[[开始扼制的时间]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1356957177}

[[Remaining time(s)]{lang="EN-US"}]{#struct_0_x2041_67218_x1862748930}

[[剩余扼制时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1357022713}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x2143494970}

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[pppoe-server throttle per-mac]{lang="EN-US"}**]{#struct_0_x2041_67218_x1357481464}

::: {#1274939334 .myid}
[]{#_Toc404785099}[]{#struct_0_x2041_67218_x695798014}[]{#_Toc366514053}

**PPPoE \-- PPPoE Server配置命令 \-- display pppoe-server va-pool**

------------------------------------------------------------------------

[**[display pppoe-server va-pool]{lang="EN-US"}**]{#struct_0_x2041_67218_x464617106}[命令用来显示]{style="font-family:
宋体"}[VA]{lang="EN-US"}[池信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1357547000}

[**[display pp]{lang="EN-US"}**]{#struct_0_x2041_67218_x2116547914}[]{#_GoBack}**[poe-server va-pool]{lang="EN-US"}**

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2021562831}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1357612536}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x84212474}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x717341093}

[[network-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x1357678072}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1181044795}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x2116204075}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1357219320}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x2091234966}[显示]{style="font-family:宋体"}[VA]{lang="EN-US"}[池信息。]{style="font-family:宋体"}[（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server va-pool]{lang="PT-BR"}]{#struct_0_x2041_67218_1158992792}

[VT interface         Size      Unused/State]{lang="PT-BR"}

[Virtual-Template1    1000      900]{lang="PT-BR"}

[Virtual-Template2    1000      Creating]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2041_67218_956836327}[显示]{style="font-family:宋体"}[VA]{lang="PT-BR"}[池信息。（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[/]{lang="PT-BR"}[集中式]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server va-pool]{lang="PT-BR"}]{#struct_0_x2041_67218_x1262039096}

[Location    VT interface         Size      Unused/State]{lang="PT-BR"}

[            Virtual-Template1    1000      900]{lang="PT-BR"}

[0/cpu1      Virtual-Template2    1000      1000]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2041_67218_x1702475479}[显示]{style="font-family:宋体"}[VA]{lang="PT-BR"}[池信息。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server va-pool]{lang="PT-BR"}]{#struct_0_x2041_67218_956901863}

[Location    VT interface         Size      Unused/State]{lang="PT-BR"}

[-           Virtual-Template1    1000      900]{lang="PT-BR"}

[1/0/cpu1    Virtual-Template2    1000      1000]{lang="PT-BR"}

[[表2-4 ]{lang="EN-US"}[display pppoe-server va-pool]{lang="EN-US"}]{#struct_0_x2041_67218_x1357284856}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1540087868}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_x189276092}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1357350392}

[[Location]{lang="EN-US"}]{#struct_0_x2041_67218_x1357415928}

[[VA]{lang="EN-US"}]{#struct_0_x2041_67218_227583128}[池所在的成员设备、单板和]{style="font-family:宋体"}[CPU]{lang="EN-US"}[（集中式设备没有该显示字段；显示"]{style="font-family:宋体"}[-]{lang="EN-US"}["时表示全局]{style="font-family:宋体"}[VA]{lang="EN-US"}[池；不支持按]{style="font-family:宋体"}[CPU]{lang="EN-US"}[显示的设备则显示"]{style="font-family:宋体"}[\*]{lang="EN-US"}["，例如]{style="font-family:宋体"}[1/0/\*]{lang="EN-US"}[）]{style="font-family:宋体"}

[[VT interface]{lang="PT-BR"}]{#struct_0_x2041_67218_x1356957176}

[[使用]{style="font-family:宋体"}[VA]{lang="EN-US"}]{#struct_0_x2041_67218_x296664989}[池的虚拟模板]{style="font-family:宋体"}

[[Size]{lang="PT-BR"}]{#struct_0_x2041_67218_x1357022712}

[[用户申请的]{style="font-family:宋体"}[VA]{lang="EN-US"}]{#struct_0_x2041_67218_564832832}[池容量]{style="font-family:宋体"}

[[Unused]{lang="PT-BR"}[/State]{lang="EN-US"}]{#struct_0_x2041_67218_564767296}

[[用户可以使用的]{style="font-family:宋体"}[VA]{lang="EN-US"}]{#struct_0_x2041_67218_x1911076253}[池容量]{style="font-family:宋体"}[/VA]{lang="EN-US"}[池当前的状态（]{style="font-family:宋体"}[Creating]{lang="EN-US"}[表示正在创建]{style="font-family:宋体"}[VA]{lang="EN-US"}[池；]{style="font-family:宋体"}[Destroying]{lang="EN-US"}[表示正在删除]{style="font-family:宋体"}[VA]{lang="EN-US"}[池）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_147630267}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pppoe-server virtual-template va-pool]{lang="EN-US"}**]{#struct_0_x2041_67218_564701760}

::::: {#996595085 .myid}
[]{#_Toc404785100}[]{#struct_0_x2041_67218_x314114560}[]{#_Toc376765047}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server access-delay**

------------------------------------------------------------------------

[**[pppoe-server access-delay]{lang="EN-US"}**]{#struct_0_x2041_67218_x314638849}[命令用来配置用户接入响应延迟时间。]{style="font-family:
宋体"}

[**[undo pppoe-server access-delay]{lang="EN-US"}**]{#struct_0_x2041_67218_x314704385}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x314769921}

[**[pppoe-server access-delay]{lang="EN-US"}**[ *delay-time*]{lang="EN-US"}]{#struct_0_x2041_67218_x314311169}

[**[undo pppoe-server access-delay]{lang="EN-US"}**]{#struct_0_x2041_67218_545414567}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x314376705}

[[对用户接入响应不延时。]{style="font-family:宋体"}]{#struct_0_x2041_67218_528530290}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x314442241}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_x314507777}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_2096908060}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_x314049025}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x314114561}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_2069079168}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x717857843}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x717923379}

[*[delay-time]{lang="EN-US"}*]{#struct_0_x2041_67218_x717988915}[：用户接入响应延迟时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[25500]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x718054451}

[[本命令用来配置]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}]{#struct_0_x2041_67218_x717661235}[对接入用户进行响应的延迟时间，系统按照配置的时间延迟响应从此接口上线用户的首个报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x717726771}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x717333555}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置用户接入响应延迟时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x717857844}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server access-delay 100]{lang="EN-US"}
:::::

::::: {#1330595566 .myid}
[]{#_Toc404785101}[]{#struct_0_x2041_67218_x1858475062}[]{#_Toc366514054}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server access-line-id bas-info**

------------------------------------------------------------------------

[[**[pppoe-server access-line-id bas-info]{lang="EN-US"}**]{.ItemListCharChar}]{#struct_0_x2041_67218_564636224}[命令用来配置]{style="font-family:宋体"}[在]{style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性中自动插入]{style="font-family:宋体"}[BAS]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_x1505605190}[**[ access-line-id bas-info]{lang="EN-US"}**]{.ItemListCharChar}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1356610436}

[**[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_565094976}[**[ access-line-id bas-info]{lang="EN-US"}**]{.ItemListCharChar}[ \[ **cn-163** \]]{lang="EN-US"}

[**[undo ]{lang="EN-US"}[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_x1409858752}[**[ access-line-id bas-info]{lang="EN-US"}**]{.ItemListCharChar}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1330110968}

[[在]{style="font-family:宋体"}[nas-port-id]{lang="EN-US"}]{#struct_0_x2041_67218_565029440}[属性中不自动插入]{style="font-family:宋体"}[BAS]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_952058338}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_209563437}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_x717792308}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_x717333556}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564963904}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x559395570}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x2000377031}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x717399092}

[**[cn-163]{lang="EN-US"}**]{#struct_0_x2041_67218_x653983089}[：插入中国电信]{style="font-family:宋体"}[163]{lang="EN-US"}[格式的]{style="font-family:宋体"}[BAS]{lang="EN-US"}[信息。不指定本参数时，插入中国电信格式的]{style="font-family:宋体"}[BAS]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x717857845}

[[BAS]{lang="EN-US"}]{#struct_0_x2041_67218_x718054453}[信息的格式分为两种：中国电信格式和中国电信]{style="font-family:宋体"}[163]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[中国电信格式的]{lang="EN-US" style="font-family:宋体"}[BAS]{lang="EN-US"}]{#struct_0_x2041_67218_x717792309}[信息格式同中国电信格式的]{lang="EN-US" style="font-family:宋体"}[circuit-id]{lang="EN-US"}[中的]{lang="EN-US" style="font-family:宋体"}[DSLAM]{lang="EN-US"}[上行口信息的格式一致（具体介绍请参见]{lang="EN-US" style="font-family:宋体"}**[pppoe-server access-line-id circuirt-id ]{lang="EN-US"}[parse-mode]{lang="EN-US"}**[命令），只是在]{lang="EN-US" style="font-family:宋体"}[BAS]{lang="EN-US"}[信息中，这个接口指的是]{lang="EN-US" style="font-family:宋体"}[BAS]{lang="EN-US"}[设备上]{lang="EN-US" style="font-family:宋体"}[DSLAM]{lang="EN-US"}[接入的接口，而不是]{lang="EN-US" style="font-family:宋体"}[DSLAM]{lang="EN-US"}[上行口。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[中国电信]{style="font-family:宋体"}]{#struct_0_x2041_67218_x717792303}[163]{lang="EN-US"}[格式的]{style="font-family:宋体"}[BAS]{lang="EN-US"}[信息格式如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}2-5]{lang="EN-US"}](?1330595566#_Ref375745552)[所示。其中，]{style="font-family:宋体"}*[NAS_slot/NAS_subslot/NAS_port]{lang="EN-US"}*[表示]{style="font-family:宋体"}[BAS]{lang="EN-US"}[设备上]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[接入的接口编号信息，]{style="font-family:宋体"}[vpi]{lang="EN-US"}[、]{style="font-family:宋体"}[vci]{lang="EN-US"}[表示]{style="font-family:宋体"}[VPI]{lang="EN-US"}[、]{style="font-family:宋体"}[VCI]{lang="EN-US"}[信息，]{style="font-family:宋体"}[vlanid]{lang="EN-US"}[、]{style="font-family:宋体"}[vlanid2]{lang="EN-US"}[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[信息，其中]{style="font-family:宋体"}[vlanid]{lang="EN-US"}[表示内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}[vlanid2]{lang="EN-US"}[表示外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，主接口的]{style="font-family:宋体"}[vlanid]{lang="EN-US"}[总为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[]{#struct_0_x2041_67218_x717857840}[[表2-5 ]{lang="EN-US"}[中国电信]{style="font-family:
黑体"}[163]{lang="EN-US"}]{#_Ref375745552}[格式的]{style="font-family:黑体"}[BAS]{lang="EN-US"}[信息格式]{style="font-family:黑体"}

[]{#table_struct_0_48548706}[[接口类型]{style="font-family:黑体"}]{#struct_0_x2041_67218_x717923376}
:::::

[[BAS]{lang="EN-US"}]{#struct_0_x2041_67218_x718054448}[信息格式]{style="font-family:黑体"}

[[ATM]{lang="EN-US"}]{#struct_0_x2041_67218_x717595696}[接口]{style="font-family:宋体"}

[[slot=*NAS_slot*;subslot=*NAS_subslot*;port=*NAS_port*;vpi=*XPI*;vci=*XCI*;]{lang="EN-US"}]{#struct_0_x2041_67218_848750386}

[[主接口或没有携带双层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2041_67218_848226097}[信息的接口]{style="font-family:宋体"}

[[slot=*NAS_slot*;subslot=*NAS_subslot*;port=*NAS_port*;vlanid=*VLAN id*;]{lang="EN-US"}]{#struct_0_x2041_67218_848160560}

[[携带双层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2041_67218_848029488}[信息的接口]{style="font-family:宋体"}

[[slot=*NAS_slot*;subslot=*NAS_subslot*;port=*NAS_port*;vlanid=*VLAN id*;vlanid2=*VLAN id2*;]{lang="EN-US"}]{#struct_0_x2041_67218_848291631}

[ ]{lang="EN-US"}

[[本命令用来配置是否]{style="font-family:宋体"}]{#struct_0_x2041_67218_848226102}[在]{style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性中自动插入]{style="font-family:宋体"}[BAS]{lang="EN-US"}[信息：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置为不自动插入]{lang="EN-US" style="font-family:宋体"}[BAS]{lang="EN-US"}]{#struct_0_x2041_67218_848160566}[信息，则]{lang="EN-US" style="font-family:宋体"}[BAS]{lang="EN-US"}[设备上传给]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{lang="EN-US" style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性由命令]{lang="EN-US" style="font-family:宋体"}**[pppoe-server access-line-id content]{lang="EN-US"}**[决定]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置为自动插入]{style="font-family:宋体"}]{#struct_0_x2041_67218_848095030}[BAS]{lang="EN-US"}[信息，则]{style="font-family:宋体"}[BAS]{lang="EN-US"}[设备最终上传给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性内容将由本命令决定：]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[如果]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_848029494}[插入中国电信]{lang="EN-US" style="font-family:宋体"}[163]{lang="EN-US"}[格式]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[BAS]{lang="EN-US"}[信息]{style="font-family:宋体"}[，则将相应的]{lang="EN-US" style="font-family:宋体"}[BAS]{lang="EN-US"}[信息插入到解析时新构造的]{lang="EN-US" style="font-family:宋体"}[circuit-id]{lang="EN-US"}[前面]{lang="EN-US" style="font-family:宋体"}[，并将此"]{style="font-family:宋体"}[BAS]{lang="EN-US"}[信息]{lang="EN-US" style="font-family:宋体"}[+]{lang="EN-US"}[circuit-id]{lang="EN-US"}["内容作为]{style="font-family:
宋体"}[nas-port-id]{lang="EN-US"}[属性上传给]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[如果插入中国电信格式]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_544957349}[的]{style="font-family:宋体"}[BAS]{lang="EN-US"}[信息]{style="font-family:宋体"}[，则将相应的]{lang="EN-US" style="font-family:宋体"}[BAS]{lang="EN-US"}[信息和原]{lang="EN-US" style="font-family:宋体"}[circuit-id]{lang="EN-US"}[信息里的]{lang="EN-US" style="font-family:宋体"}[DSLAM]{lang="EN-US"}[上的用户接入信息拼装成中国电信格式的]{lang="EN-US" style="font-family:宋体"}[circuit-id]{lang="EN-US"}[，并将此]{style="font-family:宋体"}[中国电信格式的]{lang="EN-US" style="font-family:宋体"}[circuit-id]{lang="EN-US"}[内容作为]{style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性上传给]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是，当在]{style="font-family:宋体"}[nas-port-id]{lang="EN-US"}]{#struct_0_x2041_67218_848357174}[属性中插入]{style="font-family:宋体"}[BAS]{lang="EN-US"}[信息时，若]{style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性中还包含]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[，会导致]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器无法正确解析。所以，用户需要通过配置保证，在]{style="font-family:宋体"}[BAS]{lang="EN-US"}[设备信任接收到的报文中的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[的内容的情况下插入]{style="font-family:宋体"}[BAS]{lang="EN-US"}[信息时，上传给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性的内容中仅包含]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[，不能包含]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1691216806}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_564767297}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置在]{style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性中自动插入]{style="font-family:宋体"}[BAS]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1911076252}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server access-line-id bas-info]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1418453674}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pppoe-server access-line-id circuirt-id parse-mode]{lang="EN-US"}**]{#struct_0_x2041_67218_x1858475061}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol"}]{.ItemListCharChar}**[pppoe-server[ access-line-id content]{.ItemListCharChar}]{lang="EN-US"}**]{#struct_0_x2041_67218_848160565}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pppoe-server access-line-id trust]{lang="EN-US"}**]{#struct_0_x2041_67218_x1413621819}

::::: {#1555399465 .myid}
[]{#_Toc404785102}[]{#struct_0_x2041_67218_2065791888}[]{#_Toc366514055}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server access-line-id circuit-id parse-mode**

------------------------------------------------------------------------

[**[pppoe-server ]{lang="EN-US"}**]{#struct_0_x2041_67218_564636225}[**[access-line-id ]{lang="EN-US"}**]{.ItemListCharChar}**[circuit-id ]{lang="EN-US"}**[**[parse-mode]{lang="EN-US"}**]{.ItemListCharChar}[命令用来配置接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[中]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的解析格式。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_x1505605191}[**[ access-line-id ]{lang="EN-US"}**]{.ItemListCharChar}**[circuit-id ]{lang="EN-US"}**[**[parse-mode]{lang="EN-US"}**]{.ItemListCharChar}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1372272919}

[**[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_565094977}[**[ access-line-id ]{lang="EN-US"}**]{.ItemListCharChar}**[circuirt-id ]{lang="EN-US"}**[**[parse-mode ]{lang="EN-US"}**]{.ItemListCharChar}[{ **[cn-telecom]{style="font-family:\"Arial\",\"sans-serif\""}** \| **[tr-101]{style="font-family:\"Arial\",\"sans-serif\""}** }]{lang="EN-US"}

[**[undo ]{lang="EN-US"}[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_x1409858753}[**[ access-line-id ]{lang="EN-US"}**]{.ItemListCharChar}**[circuit-id ]{lang="EN-US"}**[**[parse-mode]{lang="EN-US"}**]{.ItemListCharChar}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x235972973}

[[接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2041_67218_565029441}[中]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的解析格式为]{style="font-family:宋体"}[TR-101]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_952058339}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_209563436}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_848029493}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_848488245}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564963905}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x559395569}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x2000966854}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564898369}

[**[cn-telecom]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_261733670}[：中国电信格式。]{style="font-family:宋体"}

[**[tr-101]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_x401874634}[：]{style="font-family:宋体"}[TR-101]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_565357121}

[[circuit-id]{lang="EN-US"}]{#struct_0_x2041_67218_2013175765}[的格式分为两种：]{style="font-family:宋体"}[TR-101]{lang="EN-US"}[格式和中国电信格式。本命令用来设置设备采用哪种格式来解析]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[。]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[TR-101]{lang="EN-US"}]{#struct_0_x2041_67218_x564505074}[格式]{lang="EN-US" style="font-family:宋体"}

[[TR-101]{lang="EN-US"}]{#struct_0_x2041_67218_565291585}[格式如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当使用]{lang="EN-US" style="font-family:宋体"}[ATM/DSL]{lang="EN-US"}]{#struct_0_x2041_67218_2038549497}[时，格式为：]{style="font-family:宋体"}[Access-Node-Identifier atm slot/port:vpi.vci]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当使用]{lang="EN-US" style="font-family:宋体"}[Ethernet/DSL]{lang="EN-US"}]{#struct_0_x2041_67218_x1268827919}[时，格式为：]{style="font-family:宋体"}[Access-Node-Identifier eth slot/port\[:vlan-id\]]{lang="EN-US"}[。]{style="font-family:宋体"}

[[表示]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}]{#struct_0_x2041_67218_564832834}[上的用户接入信息，其中，]{style="font-family:宋体"}[Access-Node-Identifier]{lang="EN-US"}[表示接入节点标识符（即]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[设备标识符），后半部分的信息表示]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[上用户接入的接口信息。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[中国电信格式]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_x2118133816}

[[中国电信格式如下：]{style="font-family:宋体"}[{atm\|eth\|trunk} NAS_slot/NAS_subslot/NAS_port:XPI.XCI AccessNodeIdentifier/ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port\[:ANI_XPI.ANI_XCI\]]{lang="EN-US"}]{#struct_0_x2041_67218_x125132865}[。其中，前半部分的]{style="font-family:宋体"}[{atm\|eth\|trunk} NAS_slot/NAS_subslot/NAS_port:XPI.XCI]{lang="EN-US"}[表示]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[上行口信息，包括上行接口、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[、]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[等信息（当使用]{style="font-family:宋体"}[ATM/DSL]{lang="EN-US"}[时，]{style="font-family:宋体"}[XPI.XCI]{lang="EN-US"}[表示]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[信息；当使用]{style="font-family:宋体"}[Ethernet/DSL]{lang="EN-US"}[时，]{style="font-family:宋体"}[XPI.XCI]{lang="EN-US"}[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[信息）；后半部分表示]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[上的用户接入信息，包括]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[设备标识符、用户接入接口等信息。]{style="font-family:宋体"}

[[例如：]{style="font-family:宋体"}[ge 1/0/1:4096.2345 guangzhou001/1/31/63/31/127]{lang="EN-US"}]{#struct_0_x2041_67218_564767298}[，其含义为：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DSLAM]{lang="EN-US"}]{#struct_0_x2041_67218_x1911076263}[上行口信息为：上行接口类型为以太网接口，接口所在槽号为]{style="font-family:宋体"}[1]{lang="EN-US"}[、子槽号为]{style="font-family:宋体"}[0]{lang="EN-US"}[、端口号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[4096]{lang="EN-US"}[（]{style="font-family:宋体"}[4096]{lang="EN-US"}[表示无效]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[），内层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2345]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DSLAM]{lang="EN-US"}]{#struct_0_x2041_67218_147433659}[上的用户接入信息为：接入节点]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的标识为]{style="font-family:宋体"}[guangzhou001]{lang="EN-US"}[，]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的机架号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，用户接入接口所在机框号为]{style="font-family:宋体"}[31]{lang="EN-US"}[，槽号为]{style="font-family:宋体"}[63]{lang="EN-US"}[，子槽号为]{style="font-family:宋体"}[31]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[127]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564701762}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1858475060}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[采用中国电信格式来解析接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[中]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_499707947}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server access-line-id circuit-id parse-mode cn-telecom]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564636226}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pppoe-server access-line-id circuit-id]{lang="EN-US"}**]{#struct_0_x2041_67218_x1505605192}**[ trans]{lang="EN-US"}[-]{lang="EN-US"}[format]{lang="EN-US"}**
:::::

::::: {#-1682098209 .myid}
[]{#_Toc404785103}[]{#struct_0_x2041_67218_1775557446}[]{#_Toc366514056}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server access-line-id circuit-id trans-format**

------------------------------------------------------------------------

[**[pppoe-server ]{lang="EN-US"}**]{#struct_0_x2041_67218_565094978}[**[access-line-id ]{lang="EN-US"}**]{.ItemListCharChar}**[circuit-id ]{lang="EN-US"}[trans-format]{lang="EN-US"}**[命令用来配置接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[中]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的传输格式。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[pppoe-server ]{lang="EN-US"}**]{#struct_0_x2041_67218_x1409858758}[**[access-line-id ]{lang="EN-US"}**]{.ItemListCharChar}**[circuit-id]{lang="EN-US"}[ trans-format]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1445826554}

[**[pppoe-server ]{lang="EN-US"}**]{#struct_0_x2041_67218_565029442}[**[access-line-id ]{lang="EN-US"}**]{.ItemListCharChar}**[circuit-id]{lang="EN-US"}[ trans-format]{lang="EN-US"}**[ { **[ascii]{style="font-family:\"Arial\",\"sans-serif\""}** \| **hex** }]{lang="EN-US"}

[**[undo ]{lang="EN-US"}[pppoe-server ]{lang="EN-US"}**]{#struct_0_x2041_67218_952058336}[**[access-line-id ]{lang="EN-US"}**]{.ItemListCharChar}**[circuit-id]{lang="EN-US"}[ trans-format]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_209563443}

[[接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2041_67218_564963906}[中]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的传输格式为字符串格式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x559395572}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_x2000245959}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_445072642}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_445007106}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564898370}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1694581457}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_520093564}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_565357122}

[**[ascii]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_2013175768}[：字符串格式，指的是用字符形式传送]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[hex]{lang="EN-US"}**]{#struct_0_x2041_67218_565291586}[：十六进制格式，指的是用十六进制数字传送]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2038549500}

[[circuit-id]{lang="EN-US"}]{#struct_0_x2041_67218_1070283002}[可以选择使用字符串或者十六进制的格式进行传输。]{style="font-family:宋体"}

[[比如]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}]{#struct_0_x2041_67218_564832835}[的内容为]{style="font-family:宋体"}[00010002]{lang="EN-US"}[，则使用不同格式传输时，其报文内容如下（前两个字节为]{style="font-family:宋体"}[TYPE]{lang="EN-US"}[和]{style="font-family:宋体"}[Length]{lang="EN-US"}[的值）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[字符串格式：]{lang="EN-US" style="font-family:宋体"}[01 08 30 30 30 31 30 30 30 32]{lang="EN-US"}]{#struct_0_x2041_67218_x2118133817}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[十六进制格式：]{lang="EN-US" style="font-family:宋体"}[01 04 00 01 00 02]{lang="EN-US"}]{#struct_0_x2041_67218_1440951076}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564767299}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1911076262}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[使用十六进制格式传输]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1418650282}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server access-line-id circuit-id trans-format hex]{lang="EN-US"}
:::::

::::: {#853748540 .myid}
[]{#_Toc404785104}[]{#struct_0_x2041_67218_564701763}[]{#_Toc366514057}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server access-line-id content**

------------------------------------------------------------------------

[**[pppoe-server ]{lang="EN-US"}**]{#struct_0_x2041_67218_x1858475059}[**[access-line-id content]{lang="EN-US"}**]{.ItemListCharChar}[命令用来设置上传给]{style="font-family:
宋体"}[RADIUS]{lang="EN-US"}[服务器的]{style="font-family:
宋体"}[nas-port-id]{lang="EN-US"}[属性中包含的内容。]{style="font-family:
宋体"}

[**[undo ]{lang="EN-US"}[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_x1872748440}[**[ access-line-id content]{lang="EN-US"}**]{.ItemListCharChar}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564636227}

[**[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_x1505605193}[**[ access-line-id content]{lang="EN-US"}**]{.ItemListCharChar}[ { **[all]{style="font-family:\"Arial\",\"sans-serif\""}** \[ *separator* \] \| **[circuit-id]{style="font-family:\"Arial\",\"sans-serif\""}** \| **[remote-id]{style="font-family:\"Arial\",\"sans-serif\""}** }]{lang="EN-US"}

[**[undo ]{lang="EN-US"}[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_209473505}[**[ access-line-id content]{lang="EN-US"}**]{.ItemListCharChar}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_565094979}

[[上传给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x2041_67218_x1409858759}[服务器的]{style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性中仅包含]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1283056801}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_565029443}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_445138177}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_445072641}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_952058337}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_209563442}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x872669480}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564963907}

[**[all]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_x559395571}[：上传]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[和]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[separator]{lang="EN-US"}*]{#struct_0_x2041_67218_x2000442567}[：分隔符，长度为一个字符，缺省情况下为空格。]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[与]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[通过该分隔符连接在一起后上传。]{style="font-family:宋体"}

[**[circuit-id]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_564898371}[：仅上传]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[remote-id]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_x1694581458}[：仅上传]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1852559431}

[[在含有]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}]{#struct_0_x2041_67218_565291587}[的组网中，]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[通过接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[（]{style="font-family:宋体"}[access-line-id]{lang="EN-US"}[）把用户的物理位置信息传送给]{style="font-family:宋体"}[BAS]{lang="EN-US"}[设备（]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[功能部署在]{style="font-family:宋体"}[BAS]{lang="EN-US"}[设备上）]{style="font-family:宋体"}[，接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[的内容包括]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[和]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[两部分（]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的介绍请参见]{style="font-family:宋体"}**[pppoe-server access-line-id circuit-id parse-mode]{lang="EN-US"}**[命令，]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[的介绍请参见]{style="font-family:宋体"}**[pppoe-server access-line-id remote-id trans-format]{lang="EN-US"}**[命令）。]{style="font-family:宋体"}[BAS]{lang="EN-US"}[设备采用一定的规则解析接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[后，把解析后的内容通过]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[的]{style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器通过收到的]{style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性和数据库中已配置好的物理位置信息比较，验证用户的物理位置信息是否正确。]{style="font-family:宋体"}

[[通过本命令可以配置]{style="font-family:宋体"}[BAS]{lang="EN-US"}]{#struct_0_x2041_67218_2038549499}[设备是否上传]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[和]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器。]{style="font-family:宋体"}[BAS]{lang="EN-US"}[设备根据本命令的配置进行如下处理：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果仅上传]{lang="EN-US" style="font-family:宋体"}[circuit-id]{lang="EN-US"}]{#struct_0_x2041_67218_x1267910415}[，则]{lang="EN-US" style="font-family:宋体"}[BAS]{lang="EN-US"}[复制解析后的]{lang="EN-US" style="font-family:宋体"}[circuit-id]{lang="EN-US"}[到]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性中，传送到]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果仅上传]{lang="EN-US" style="font-family:宋体"}[remote-id]{lang="EN-US"}]{#struct_0_x2041_67218_564832836}[，则]{lang="EN-US" style="font-family:宋体"}[BAS]{lang="EN-US"}[复制解析后的]{lang="EN-US" style="font-family:宋体"}[remote-id]{lang="EN-US"}[到]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性中，传送到]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果两者均上传，则]{lang="EN-US" style="font-family:宋体"}[BAS]{lang="EN-US"}]{#struct_0_x2041_67218_x2118133818}[解析出]{lang="EN-US" style="font-family:宋体"}[remote-id]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[circuit-id]{lang="EN-US"}[后，在二者之间加入指定的分隔符，然后一起复制到]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性中，传送到]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2041_67218_444810503}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分隔符可以是所有可见字符，但如果用户配置的分隔符是可能出现在]{lang="EN-US" style="font-family:宋体"}[circuit-id]{lang="EN-US"}]{#struct_0_x2041_67218_x931701919}[和]{lang="EN-US" style="font-family:宋体"}[remote-id]{lang="EN-US"}[两个字符串中的字符，则会使最终]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器解析的结果不可预知，所以需要选择合适的分隔符。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在没有配置]{lang="EN-US" style="font-family:宋体"}**[pppoe-server access-line-id bas-info]{lang="EN-US"}**]{#struct_0_x2041_67218_445072647}[命令的情况下，上传给]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{lang="EN-US" style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性中包含的内容由本命令的配置决定。在配置了]{lang="EN-US" style="font-family:宋体"}**[pppoe-server access-line-id bas-info]{lang="EN-US"}**[命令的情况下，上传给]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{lang="EN-US" style="font-family:宋体"}[nas-port-id]{lang="EN-US"}[属性中包含的内容请参见]{lang="EN-US" style="font-family:宋体"}**[pppoe-server access-line-id bas-info]{lang="EN-US"}**[命令的介绍。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564767300}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1627111164}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[仅上传]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_719300705}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server access-line-id content circuit-id]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564701764}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pppoe-server access-line-id bas-info]{lang="EN-US"}**]{#struct_0_x2041_67218_445400327}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pppoe-server access-line-id circuit-id parse-mode]{lang="EN-US"}**]{#struct_0_x2041_67218_x1858475066}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pppoe-server access-line-id remote-id trans-format]{lang="EN-US"}**]{#struct_0_x2041_67218_x306861107}
:::::

::::: {#274780948 .myid}
[]{#_Toc404785105}[]{#struct_0_x2041_67218_682452609}[]{#_Toc366514058}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server access-line-id remote-id trans-format**

------------------------------------------------------------------------

[**[pppoe-server ]{lang="EN-US"}**]{#struct_0_x2041_67218_564636228}[**[access-line-id ]{lang="EN-US"}**]{.ItemListCharChar}**[remote-id ]{lang="EN-US"}[trans-format]{lang="EN-US"}**[命令用来配置接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[中]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[的传输格式**。**]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_x1505605178}[**[ access-line-id ]{lang="EN-US"}**]{.ItemListCharChar}**[remote-id ]{lang="EN-US"}[trans-format]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1711923292}

[**[pppoe-server ]{lang="EN-US"}**]{#struct_0_x2041_67218_565094980}[**[access-line-id ]{lang="EN-US"}**]{.ItemListCharChar}**[remote-id]{lang="EN-US"}[ trans-format]{lang="EN-US"}**[ { **[ascii]{style="font-family:\"Arial\",\"sans-serif\""}** \| **hex** }]{lang="EN-US"}

[**[undo ]{lang="EN-US"}[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_164119362}[**[ access-line-id ]{lang="EN-US"}**]{.ItemListCharChar}**[remote-id trans-format]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_411160349}

[[接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2041_67218_565029444}[中]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[的传输格式为字符串格式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_952058334}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_209563441}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_444876038}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_444810502}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564963908}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x559395582}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x2000245960}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564898372}

[**[ascii]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_x1694581455}[：字符串格式，指的是用字符形式传送]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[hex]{lang="EN-US"}**]{#struct_0_x2041_67218_1682892978}[：十六进制格式，指的是用十六进制数字传送]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_565357124}

[[remote-id]{lang="EN-US"}]{#struct_0_x2041_67218_2013175770}[为]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[中继设备（比如]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[）的系统]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[可以选择使用字符串或者十六进制的格式进行传输。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x564308467}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_565291588}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使用十六进制格式传输]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_2038549494}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server access-line-id remote-id trans-format hex]{lang="EN-US"}
:::::

::::: {#1841410656 .myid}
[]{#_Toc404785106}[]{#struct_0_x2041_67218_x1268631311}[]{#_Toc366514059}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server access-line-id trust**

------------------------------------------------------------------------

[[**[pppoe-server access-line-id trust]{lang="EN-US"}**]{.ItemListCharChar}]{#struct_0_x2041_67218_564832837}[命令用来配置设备信任接收到的报文中的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[的内容。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_x2118133819}[**[ access-line-id trust]{lang="EN-US"}**]{.ItemListCharChar}[命令用来]{style="font-family:宋体"}[恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_634382022}

[**[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_564767301}[**[ access-line-id trust]{lang="EN-US"}**]{.ItemListCharChar}

[**[undo ]{lang="EN-US"}[pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_1627111165}[**[ access-line-id trust]{lang="EN-US"}**]{.ItemListCharChar}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_719366241}

[[设备不信任接收到的报文中的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2041_67218_564701765}[的内容。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1858475065}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_96423420}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_445138182}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_445007110}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_564636229}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1505605179}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_565094981}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_164119361}

[[本命令用来配置设备是否信任接收到的报文中的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2041_67218_411160346}[的内容：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设置为信任模式时，]{lang="EN-US" style="font-family:宋体"}[BAS]{lang="EN-US"}]{#struct_0_x2041_67218_565029445}[设备会解析收到报文中携带的]{lang="EN-US" style="font-family:宋体"}[circuit-id]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[remote-id]{lang="EN-US"}[的信息，并根据解析出来的信息构造新的]{lang="EN-US" style="font-family:宋体"}[circuit-id]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[remote-id]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x2041_67218_x872669478}[设置为不信任]{lang="EN-US" style="font-family:宋体"}[模式]{style="font-family:宋体"}[时，]{lang="EN-US" style="font-family:宋体"}[BAS]{lang="EN-US"}[设备]{lang="EN-US" style="font-family:宋体"}[将不]{style="font-family:宋体"}[再解析报文中携带的]{lang="EN-US" style="font-family:宋体"}[circuit-id]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[remote-id]{lang="EN-US"}[的信息，新构造的]{lang="EN-US" style="font-family:宋体"}[circuit-id]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[remote-id]{lang="EN-US"}[的内容]{style="font-family:宋体"}[均为空]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[需要注意的是，当设置为信任模式时，如果解析]{style="font-family:宋体"}[PADR]{lang="EN-US"}]{#struct_0_x2041_67218_564898373}[报文中的]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[或]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[失败，则丢弃此]{style="font-family:宋体"}[PADR]{lang="EN-US"}[报文，不回应]{style="font-family:宋体"}[PADS]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1045990377}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_565357125}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置信任接收到的报文中的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[的内容。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_2013175769}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server access-line-id trust]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x563718642}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pppoe-server access-line-id circuirt-id parse-mode]{lang="EN-US"}**]{#struct_0_x2041_67218_2038549493}
:::::

::::: {#547380314 .myid}
[]{#_Toc404785107}[]{#struct_0_x2041_67218_x1268565775}[]{#_Toc366514060}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server bind**

------------------------------------------------------------------------

[**[pppoe-server bind]{lang="EN-US"}**]{#struct_0_x2041_67218_2130916773}[命令用来在接口上启用]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[协议，将该接口与指定的虚拟模板接口绑定。]{style="font-family:宋体"}

[**[undo pppoe-server bind]{lang="EN-US"}**]{#struct_0_x2041_67218_288955924}[命令用来在相应接口关闭]{style="font-family:宋体"}[PPPoEServer]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1148634405}

[**[pppoe-server bind virtual-template ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_2130851237}

[**[undo pppoe-server bind]{lang="EN-US"}**]{#struct_0_x2041_67218_1434948346}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1247364912}

[[接口上的]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}]{#struct_0_x2041_67218_2130785701}[协议处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_681296244}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_x415564011}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_2011549799}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_2011025510}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2130720165}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1685780351}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x874703326}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2131178917}

[**[virtual-template]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_x2041_67218_1822469392}[：指定虚拟模板接口。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[表示虚拟模板接口号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1435847894}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上启用]{lang="EN-US" style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}]{#struct_0_x2041_67218_2131113381}[协议时，可以绑定不存在的虚拟模板。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口上已经]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2041_67218_1816558812}[启用]{lang="EN-US" style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[绑定了虚拟模板接口，则不能直接使用该命令绑定新的虚拟模板接口，需要先关闭]{lang="EN-US" style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[协议后，再重新启用]{lang="EN-US" style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[时绑定新的虚拟模板接口。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在接口上同时启用]{lang="EN-US" style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}]{#struct_0_x2041_67218_882026843}[与]{lang="EN-US" style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[功能，则]{lang="EN-US" style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[功能不生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x750587258}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_2131047845}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上启用]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[协议，将接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[与虚拟模板接口]{style="font-family:宋体"}[Virtual-Template1]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x84497715}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server bind virtual-template 1]{lang="EN-US"}
:::::

::::: {#-650686269 .myid}
[]{#_Toc404785108}[]{#struct_0_x2041_67218_2130982309}[]{#_Toc366514061}[]{#_Toc336084869}[]{#_Toc332298259}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server session-limit**

------------------------------------------------------------------------

[**[pppoe-server session-limit]{lang="EN-US"}**]{#struct_0_x2041_67218_x926158713}[命令用来配置接口上所能创建]{style="font-family:
宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目。]{style="font-family:
宋体"}

[**[undo ]{lang="EN-US"}[pppoe-server session-limit]{lang="EN-US"}**]{#struct_0_x2041_67218_x196303442}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_779143159}

[**[pppoe-server session-limit ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_2131441061}

[**[undo ]{lang="EN-US"}[pppoe-server session-limit]{lang="EN-US"}**]{#struct_0_x2041_67218_x1687055231}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_290519740}

[[不限制接口上所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_2131375525}[会话的数目。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1471529202}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_1998068465}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_2011156582}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_2011091046}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2130916774}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_289152532}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x2063554018}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2130851238}

[*[number]{lang="EN-US"}*]{#struct_0_x2041_67218_1435669242}[：接口上所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x475577070}

[[系统创建会话时，需同时满足如下限制，若其中任何一项不满足，则无法创建会话：]{style="font-family:宋体"}]{#struct_0_x2041_67218_2130785702}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口下每个用户所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_681099636}[PPPoE]{lang="FR"}[会话的最大数目限制]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口下每个]{style="font-family:宋体"}]{#struct_0_x2041_67218_100716927}[VLAN]{lang="EN-US"}[所能创建]{style="font-family:宋体"}[PPPoE]{lang="FR"}[会话的最大数目限制]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_2130720166}[PPPoE]{lang="EN-US"}[会话的最大数目限制]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[单板所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1685714815}[PPPoE]{lang="EN-US"}[会话的最大数目限制（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[成员设备所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_77699976}[PPPoE]{lang="EN-US"}[会话的最大数目限制（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_1911649167}[PPPoE]{lang="EN-US"}[会话的最大数目限制（集中式设备）]{style="font-family:宋体"}

[[本命令配置后仅对新创建的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_2131178918}[会话有效，对已经创建的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话无效，即不会导致已经上线的用户下线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1823452432}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1650189165}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_2131113382}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server session-limit 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1816755420}

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[pppoe-server session]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_x1878564201}**[-]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}[limit per-mac]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[pppoe-server session-limit per-vlan]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_2131047846}

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[pppoe-server session]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_x84694323}**[-]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}[limit total]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**
:::::

::::: {#-190797618 .myid}
[]{#_Toc404785109}[]{#struct_0_x2041_67218_2131598615}[]{#_Toc366514062}[]{#_Toc336084870}[]{#_Toc332298260}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server session-limit per-mac**

------------------------------------------------------------------------

[**[pppoe-server session-limit per-mac]{lang="EN-US"}**]{#struct_0_x2041_67218_2130982310}[命令用来配置在接口下，每个用户所能创建]{style="font-family:宋体"}[PPPoE]{lang="FR"}[会话的最大数目。]{style="font-family:宋体"}

[**[undo pppoe-server session-limit per-mac]{lang="EN-US"}**]{#struct_0_x2041_67218_x926748538}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x581261738}

[**[pppoe-server session-limit per-mac ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_2131441062}

[**[undo pppoe-server session-limit per-mac]{lang="EN-US"}**]{#struct_0_x2041_67218_x1687251839}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_115777434}

[[每个用户可创建]{style="font-family:宋体"}[100]{lang="EN-US"}]{#struct_0_x2041_67218_2131375526}[个]{style="font-family:宋体"}[PPPoE]{lang="FR"}[会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1471463666}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_x1533630180}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_2010959973}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_2010828901}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2130916775}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_289086996}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1522545079}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x643771032}

[*[number]{lang="EN-US"}*]{#struct_0_x2041_67218_2130851239}[：每个用户所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1435603706}

[[每个用户通过]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2041_67218_x1247835788}[地址进行标识。]{style="font-family:宋体"}

[[系统创建会话时，需同时满足如下限制，若其中任何一项不满足，则无法创建会话：]{style="font-family:宋体"}]{#struct_0_x2041_67218_2130785703}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口下每个用户所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_681165172}[PPPoE]{lang="FR"}[会话的最大数目限制]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口下每个]{style="font-family:宋体"}]{#struct_0_x2041_67218_879718877}[VLAN]{lang="EN-US"}[所能创建]{style="font-family:宋体"}[PPPoE]{lang="FR"}[会话的最大数目限制]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_2130720167}[PPPoE]{lang="EN-US"}[会话的最大数目限制]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[单板所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1685649279}[PPPoE]{lang="EN-US"}[会话的最大数目限制（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[成员设备所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_172216589}[PPPoE]{lang="EN-US"}[会话的最大数目限制（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_2131178919}[PPPoE]{lang="EN-US"}[会话的最大数目限制（集中式设备）]{style="font-family:宋体"}

[[本命令配置后仅对新创建的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_1823386896}[会话有效，对已经创建的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话无效，即不会导致已经上线的用户下线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1955247418}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_2131113383}[配置在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下，每个用户所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1816689884}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server session-limit per-mac 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1827130072}

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[pppoe-server session]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_2131047847}**[-]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}[limit]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[pppoe-server session]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_x84628787}**[-]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}[limit per-vlan]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[pppoe-server ]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_x2079733346}**[session-limit]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}[ total]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**
:::::

::::: {#-239892598 .myid}
[]{#_Toc404785110}[]{#struct_0_x2041_67218_2130982311}[]{#_Toc366514063}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server session-limit per-vlan**

------------------------------------------------------------------------

[**[pppoe-server session-limit per-vlan]{lang="EN-US"}**]{#struct_0_x2041_67218_x926683002}[命令用来配置在接口下，每个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[所能创建]{style="font-family:宋体"}[PPPoE]{lang="FR"}[会话的最大数目。]{style="font-family:宋体"}

[**[undo pppoe-server session-limit per-vlan]{lang="EN-US"}**]{#struct_0_x2041_67218_x124887189}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2131441063}

[**[pppoe-server session-limit per-vlan ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1687186303}

[**[undo pppoe-server session-limit ]{lang="EN-US"}[per-vlan]{lang="EN-US"}**]{#struct_0_x2041_67218_x1229509326}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2131375527}

[[不限制每个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2041_67218_1471398130}[所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数目。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1990824021}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_2130916776}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_2011091045}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_2011549797}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_289283604}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_944780382}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1010897459}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2130851240}

[*[number]{lang="EN-US"}*]{#struct_0_x2041_67218_1435144955}[：每个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x379501931}

[[系统创建会话时，需同时满足如下限制，若其中任何一项不满足，则无法创建会话：]{style="font-family:宋体"}]{#struct_0_x2041_67218_2130785704}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口下每个用户所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_681492852}[PPPoE]{lang="FR"}[会话的最大数目限制]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口下每个]{style="font-family:宋体"}]{#struct_0_x2041_67218_952929565}[VLAN]{lang="EN-US"}[所能创建]{style="font-family:宋体"}[PPPoE]{lang="FR"}[会话的最大数目限制]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_2130720168}[PPPoE]{lang="EN-US"}[会话的最大数目限制]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[单板所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1686108031}[PPPoE]{lang="EN-US"}[会话的最大数目限制（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[成员设备所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_1224562268}[PPPoE]{lang="EN-US"}[会话的最大数目限制（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_2131178920}[PPPoE]{lang="EN-US"}[会话的最大数目限制（集中式设备）]{style="font-family:宋体"}

[[本命令配置后仅对新创建的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_1822928143}[会话有效，对已经创建的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话无效，即不会导致已经上线的用户下线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1668884587}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_2131113384}[配置在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下，每个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1816886492}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server session-limit per-vlan 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x293016230}

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[pppoe-server sessions limit]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_2131047848}

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[pppoe-server sessions limit per-mac]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_x83776819}

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[pppoe-server ]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_566724503}**[sessions limit]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}[ total]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**
:::::

::: {#-1595928165 .myid}
[]{#_Toc404785111}[]{#struct_0_x2041_67218_2130982312}[]{#_Toc366514064}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server session-limit total**

------------------------------------------------------------------------

[**[pppoe-server ]{lang="EN-US"}[session-limit total]{lang="EN-US"}**]{#struct_0_x2041_67218_x926879610}[命令用来配置系统所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目。]{style="font-family:宋体"}

[**[undo pppoe-server ]{lang="EN-US"}[session-limit total]{lang="EN-US"}**]{#struct_0_x2041_67218_198187854}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x384446058}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2041_67218_2131441064}

[**[pppoe-server ]{lang="EN-US"}[session-limit total]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1687382911}

[**[undo pppoe-server ]{lang="EN-US"}[session-limit total]{lang="EN-US"}**]{#struct_0_x2041_67218_x598010258}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_2131375528}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[pppoe-server ]{lang="EN-US"}[session-limit slot]{lang="EN-US"}***[ slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] **total** *number*]{lang="EN-US"}]{#struct_0_x2041_67218_1472381170}

[**[undo pppoe-server ]{lang="EN-US"}[session-limit slot]{lang="EN-US"}***[ slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] **total**]{lang="EN-US"}]{#struct_0_x2041_67218_x519978866}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2041_67218_2130916777}[模式：]{style="font-family:宋体"}

[**[pppoe-server ]{lang="EN-US"}[session-limit chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] **total** *number*]{lang="EN-US"}]{#struct_0_x2041_67218_289218068}

[**[undo pppoe-server ]{lang="EN-US"}[session-limit chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] **total**]{lang="EN-US"}]{#struct_0_x2041_67218_x580891693}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2130851241}

[[不限制系统所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_1435079419}[会话的数目。（集中式设备）]{style="font-family:宋体"}

[[不限制单板所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x95861417}[会话的数目。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[不限制成员设备所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_2130785705}[会话的数目。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_681558388}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1467910402}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2130720169}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1686042495}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x320953376}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2131178921}

[*[number]{lang="EN-US"}*]{#struct_0_x2041_67218_1822862607}[：系统所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number ]{lang="EN-US"}***[total ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_704846862}[：指定单板所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number ]{lang="EN-US"}***[total ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_x515584446}[：指定成员设备所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number ]{lang="EN-US"}***[total ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_1878105816}[：指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number ]{lang="EN-US"}***[total ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_2131113385}[：指定成员设备上指定单板所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number ]{lang="EN-US"}***[total ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1360358726}[：指定单板所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2041_67218_1066974857}[：指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1816820956}

[[系统创建会话时，需同时满足如下限制，若其中任何一项不满足，则无法创建会话：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1432288224}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口下每个用户所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_2131047849}[PPPoE]{lang="FR"}[会话的最大数目限制]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口下每个]{style="font-family:宋体"}]{#struct_0_x2041_67218_x83711283}[VLAN]{lang="EN-US"}[所能创建]{style="font-family:宋体"}[PPPoE]{lang="FR"}[会话的最大数目限制]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_961465157}[PPPoE]{lang="EN-US"}[会话的最大数目限制]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[单板所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_2130982313}[PPPoE]{lang="EN-US"}[会话的最大数目限制（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[成员设备所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_x926814074}[PPPoE]{lang="EN-US"}[会话的最大数目限制（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_x2062078099}[PPPoE]{lang="EN-US"}[会话的最大数目限制（集中式设备）]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2041_67218_2131441065}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统、单板所能创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1687317375}[PPPoE]{lang="EN-US"}[会话的最大数目还受设备的规格限制，如果用户配置的值大于设备的规格，则以设备的规格为准。各设备的规格与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令配置后仅对新创建的]{style="font-family:宋体"}]{#struct_0_x2041_67218_220371909}[PPPoE]{lang="EN-US"}[会话有效，对已经创建的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话无效，即不会导致已经上线的用户下线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2131375529}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1472315634}[配置系统所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目为]{style="font-family:宋体"}[3000]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x893545730}

[\[Sysname\] pppoe-server session-limit total 3000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_2130916778}[配置]{style="font-family:宋体"}[3]{lang="EN-US"}[号单板所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目为]{style="font-family:宋体"}[1500]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_288366100}

[\[Sysname\] pppoe-server session-limit slot 3 total 1500]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1980096462}[配置]{style="font-family:宋体"}[3]{lang="EN-US"}[号成员设备所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目为]{style="font-family:宋体"}[1500]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_2130851242}

[\[Sysname\] pppoe-server session-limit slot 3 total 1500]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1435276027}[配置]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[3]{lang="EN-US"}[号单板所能创建]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的最大数目为]{style="font-family:宋体"}[1500]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_349973541}

[\[Sysname\] pppoe-server session-limit chassis 2 slot 3 total 1500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2130785706}

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[pppoe-server session]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_681361780}**[-]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}[limit]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[pppoe-server session]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_x784377067}**[-]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}[limit per-mac]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[pppoe-server session]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2041_67218_1485611635}**[-]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}[limit per-vlan]{lang="EN-US" style="font-family:\"Arial\",\"sans-serif\""}**
:::

::::: {#454252667 .myid}
[]{#_Toc404785112}[]{#struct_0_x2041_67218_2130720170}[]{#_Toc366514065}[]{#_Toc336084878}[]{#_Toc334811135}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server tag ac-name**

------------------------------------------------------------------------

[**[pppoe-server tag ac-name]{lang="EN-US"}**]{#struct_0_x2041_67218_x1685583744}[命令用来配置]{style="font-family:
宋体"}[PPPoE Server]{lang="EN-US"}[的]{style="font-family:
宋体"}[AC Name]{lang="EN-US"}[（]{style="font-family:宋体"}[Access Concentrator Name]{lang="EN-US"}[，接入集中器名称）。]{style="font-family:宋体"}

[**[undo pppoe-server tag ac-name]{lang="EN-US"}**]{#struct_0_x2041_67218_14441773}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2131178922}

[**[pppoe-server tag ac-name ]{lang="EN-US"}**]{#struct_0_x2041_67218_1822797071}*[name]{lang="EN-US"}*

[**[undo pppoe-server tag ac-name]{lang="EN-US"}**]{#struct_0_x2041_67218_1525268203}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2131113386}

[[PPPoE Server]{lang="EN-US"}]{#struct_0_x2041_67218_1817017564}[的]{style="font-family:宋体"}[AC Name]{lang="EN-US"}[为设备名称。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1822000698}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_2131047850}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_2011091052}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_2011549804}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x84301106}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1123646205}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_2130982314}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x926486394}

[*[name]{lang="EN-US"}*]{#struct_0_x2041_67218_1836980265}[：]{style="font-family:宋体"}[AC Name]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2131441066}

[[本命令用来配置]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}]{#struct_0_x2041_67218_x1687513983}[的]{style="font-family:宋体"}[AC Name]{lang="EN-US"}[，]{style="font-family:宋体"}[PADO]{lang="EN-US"}[报文中会携带]{style="font-family:宋体"}[AC Name]{lang="EN-US"}[，]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[可以根据]{style="font-family:宋体"}[AC Name]{lang="EN-US"}[来选择]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[（]{style="font-family:宋体"}[H3C]{lang="EN-US"}[实现的]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[暂不支持该功能）。]{style="font-family:宋体"}

[[需要注意的是，系统不支持全部空格的]{style="font-family:宋体"}[AC Name]{lang="EN-US"}]{#struct_0_x2041_67218_x1134274707}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_304457137}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_2131375530}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[的]{style="font-family:宋体"}[AC Name]{lang="EN-US"}[为]{style="font-family:宋体"}[pppoes]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_1471856881}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server tag ac-name pppoes]{lang="EN-US"}
:::::

::::: {#2098247383 .myid}
[]{#_Toc404785113}[]{#struct_0_x2041_67218_x1919160407}[]{#_Toc366514066}[]{#_Toc336084879}[]{#_Toc334811136}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server tag ppp-max-payload**

------------------------------------------------------------------------

[**[pppoe-server tag ppp-max-payload]{lang="EN-US"}**]{#struct_0_x2041_67218_x597966582}[命令用来使能对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[最大负载]{style="font-family:宋体"}[TAG]{lang="EN-US"}[的支持，并指定最大负载的范围。]{style="font-family:宋体"}

[**[undo pppoe-server tag ppp-max-payload]{lang="EN-US"}**]{#struct_0_x2041_67218_x1817571385}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1433157063}

[**[pppoe-server tag ppp-max-payload ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_x2041_67218_x598032118}**[minimum ]{lang="EN-US"}***[minvalue ]{lang="EN-US"}***[maximum ]{lang="EN-US"}***[maxvalue ]{lang="EN-US"}*[\]]{lang="EN-US"}

[**[undo pppoe-server tag ppp-max-payload]{lang="EN-US"}**]{#struct_0_x2041_67218_1098267659}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1988545933}

[[不支持]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x598097654}[最大负载]{style="font-family:宋体"}[TAG]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1483971032}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_1211165413}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_2010894443}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_2010828907}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x598163190}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1616132153}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1259574540}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1096241662}

[**[minimum ]{lang="EN-US"}***[minvalue]{lang="EN-US"}*]{#struct_0_x2041_67218_x597704438}[：最大负载的最小值，取值范围为]{style="font-family:宋体"}[64]{lang="EN-US"}[～]{style="font-family:宋体"}[4470]{lang="EN-US"}[，单位为字节，缺省值为]{style="font-family:宋体"}[1492]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[**[maximum ]{lang="EN-US"}***[maxvalue]{lang="EN-US"}*]{#struct_0_x2041_67218_1671297200}[：最大负载的最大值，取值范围为]{style="font-family:宋体"}[64]{lang="EN-US"}[～]{style="font-family:宋体"}[4470]{lang="EN-US"}[，单位为字节，缺省值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}*[maxvalue]{lang="EN-US"}*[值要大于等于]{style="font-family:宋体"}*[minvalue]{lang="EN-US"}*[值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1391950927}

[[PPP]{lang="EN-US"}]{#struct_0_x2041_67218_x597769974}[最大负载]{style="font-family:宋体"}[TAG]{lang="EN-US"}[主要提供对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的载荷超过]{style="font-family:宋体"}[1492]{lang="EN-US"}[的大报文支持，最大程度上减少报文的分片。]{style="font-family:宋体"}[PPP]{lang="EN-US"}[最大负载]{style="font-family:宋体"}[TAG]{lang="EN-US"}[包含在]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[端发送的]{style="font-family:宋体"}[PADI]{lang="EN-US"}[和]{style="font-family:宋体"}[PADR]{lang="EN-US"}[报文里。如果]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[端发送的此]{style="font-family:宋体"}[TAG]{lang="EN-US"}[值处于本命令配置的范围内，则]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[将此]{style="font-family:宋体"}[TAG]{lang="EN-US"}[原样拷贝至回复的]{style="font-family:宋体"}[PADO]{lang="EN-US"}[和]{style="font-family:宋体"}[PADS]{lang="EN-US"}[报文中；否则就认为报文的请求无效，不向]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[端回复]{style="font-family:宋体"}[PADO]{lang="EN-US"}[或]{style="font-family:宋体"}[PADS]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}]{#struct_0_x2041_67218_523111637}[不支持此]{style="font-family:宋体"}[TAG]{lang="EN-US"}[，此时如果收到的]{style="font-family:宋体"}[PADI]{lang="EN-US"}[和]{style="font-family:宋体"}[PADR]{lang="EN-US"}[报文中包含此]{style="font-family:宋体"}[TAG]{lang="EN-US"}[，则直接忽略，不在回应的]{style="font-family:宋体"}[PADO]{lang="EN-US"}[和]{style="font-family:宋体"}[PADS]{lang="EN-US"}[报文中携带此]{style="font-family:宋体"}[TAG]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}**[jumboframe enable]{lang="EN-US"}**]{#struct_0_x2041_67218_x2002642243}[命令可以改变接口支持的超长帧的大小，]{style="font-family:宋体"}**[jumboframe enable]{lang="EN-US"}**[命令配置的超长帧的最大长度应大于]{style="font-family:宋体"}**[pppoe-server tag ppp-max-payload]{lang="EN-US"}**[命令配置的最大负载的最大值。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x597835510}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_896173178}[使能对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[最大负载]{style="font-family:宋体"}[TAG]{lang="EN-US"}[的支持，并指定最大负载的范围为]{style="font-family:宋体"}[1494]{lang="EN-US"}[～]{style="font-family:宋体"}[1508]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x309534235}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server tag ppp-max-payload minimum 1494 maximum 1508]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x597901046}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[jumboframe enable]{lang="EN-US"}**]{#struct_0_x2041_67218_1675538922}[（接口管理命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[以太网接口）]{style="font-family:宋体"}
:::::

::::::: {#779632774 .myid}
[]{#_Toc404785114}[]{#struct_0_x2041_67218_1974135788}[]{#_Toc399832793}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server tag service-name**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2041_67218_x1237609807}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_x1480164041}
:::

[ ]{lang="EN-US"}

[**[pppoe-server tag service-name]{lang="EN-US"}**]{#struct_0_x2041_67218_110237342}[命令用来配置]{style="font-family:
宋体"}[PPPoE Server]{lang="EN-US"}[的]{style="font-family:
宋体"}[Service Name]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo pppoe-server tag service-name]{lang="EN-US"}**]{#struct_0_x2041_67218_304328564}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_706862397}

[**[pppoe-server tag service-name]{lang="EN-US"}**[ *name*]{lang="EN-US"}]{#struct_0_x2041_67218_x828729618}

[**[undo pppoe-server tag service-name]{lang="EN-US"}**]{#struct_0_x2041_67218_408051847}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_886881727}

[[PPPoE Server]{lang="EN-US"}]{#struct_0_x2041_67218_2049744541}[的]{style="font-family:宋体"}[Service Name]{lang="EN-US"}[为空。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x67345202}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_1705569206}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image001.png){#图片 1 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2041_67218_x711050055}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_891277749}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1022127299}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x2097562058}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1158032094}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x590456656}

[*[name]{lang="EN-US"}*]{#struct_0_x2041_67218_x1459024033}[：]{style="font-family:宋体"}[Service Name]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_833781466}

[[当组网环境中存在两个或者两个以上]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}]{#struct_0_x2041_67218_x1766892222}[提供不同的服务时，]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[可以根据自身的]{style="font-family:宋体"}[Service Name]{lang="EN-US"}[选择不同的服务器来建立连接，这时]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[将根据本机上的]{style="font-family:宋体"}[Service Name]{lang="EN-US"}[来进行匹配处理。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}]{#struct_0_x2041_67218_1691947086}[收到客户端的]{style="font-family:宋体"}[PADI/PADR]{lang="EN-US"}[报文时，需要检查报文中的]{style="font-family:宋体"}[Service Name TAG]{lang="EN-US"}[字段并和本机上配置的]{style="font-family:宋体"}[Service Name]{lang="EN-US"}[进行匹配，具体处理过程有以下两步：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[PPPoE Server]{lang="EN-US"}]{#struct_0_x2041_67218_2111491112}[将收到]{lang="EN-US" style="font-family:宋体"}[PADI]{lang="EN-US"}[报文中的]{lang="EN-US" style="font-family:宋体"}[Service-Name TAG]{lang="EN-US"}[字段与本地配置的]{lang="EN-US" style="font-family:宋体"}[Service Name]{lang="EN-US"}[进行匹配，且匹配规则如下：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果此]{lang="EN-US" style="font-family:宋体"}[TAG]{lang="EN-US"}]{#struct_0_x2041_67218_536642702}[字段内容不为空，且]{lang="EN-US" style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[端也配置了]{lang="EN-US" style="font-family:宋体"}[Service Name]{lang="EN-US"}[，则需要进行精确匹配，只有相同，服务器端才接受并回应]{lang="EN-US" style="font-family:宋体"}[PADO]{lang="EN-US"}[报文；如果不相同，则不接受。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果此]{lang="EN-US" style="font-family:宋体"}[TAG]{lang="EN-US"}]{#struct_0_x2041_67218_1570851261}[字段内容为空，或者]{lang="EN-US" style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[端没有配置]{lang="EN-US" style="font-family:宋体"}[Service Name]{lang="EN-US"}[，则服务器端需要接受并回应]{lang="EN-US" style="font-family:宋体"}[PADO]{lang="EN-US"}[报文。]{lang="EN-US" style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[PPPoE Server]{lang="EN-US"}]{#struct_0_x2041_67218_602259305}[将收到]{lang="EN-US" style="font-family:宋体"}[PADR]{lang="EN-US"}[报文中的]{lang="EN-US" style="font-family:宋体"}[Service-Name TAG]{lang="EN-US"}[字段与本地配置的]{lang="EN-US" style="font-family:宋体"}[Service Name]{lang="EN-US"}[进行匹配，且匹配规则如下：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果此]{lang="EN-US" style="font-family:宋体"}[TAG]{lang="EN-US"}]{#struct_0_x2041_67218_x981568670}[字段内容不为空，且]{lang="EN-US" style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[端也配置了]{lang="EN-US" style="font-family:宋体"}[Service Name]{lang="EN-US"}[，则需要进行精确匹配，只有相同，服务器端才接受并回应]{lang="EN-US" style="font-family:宋体"}[PADS]{lang="EN-US"}[报文和创建]{lang="EN-US" style="font-family:宋体"}[Session]{lang="EN-US"}[；如果不相同，则不能创建]{lang="EN-US" style="font-family:宋体"}[Session]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果此]{lang="EN-US" style="font-family:宋体"}[TAG]{lang="EN-US"}]{#struct_0_x2041_67218_x1959419914}[字段内容为空，或者]{lang="EN-US" style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[端没有配置]{lang="EN-US" style="font-family:宋体"}[Service Name]{lang="EN-US"}[，则服务器端需要接受并回应]{lang="EN-US" style="font-family:宋体"}[PADR]{lang="EN-US"}[报文和创建]{lang="EN-US" style="font-family:宋体"}[Session]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1851890104}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x841931767}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[的]{style="font-family:宋体"}[Service Name]{lang="EN-US"}[为]{style="font-family:宋体"}[pppoes]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_179471944}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server tag service-name pppoes]{lang="EN-US"}
:::::::

::::: {#152691710 .myid}
[]{#_Toc336084880}[]{#_Toc404785115}[]{#struct_0_x2041_67218_876056461}[]{#_Toc366514067}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server throttle per-mac**

------------------------------------------------------------------------

[**[pppoe-server throttle per-mac]{lang="EN-US"}**]{#struct_0_x2041_67218_x597442294}[命令用来配置接口允许每个用户创建会话的速度。]{style="font-family:
宋体"}

[**[undo ]{lang="EN-US"}[pppoe-server throttle per-mac]{lang="EN-US"}**]{#struct_0_x2041_67218_x1426375433}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1964054767}

[**[pppoe-server throttle per-mac ]{lang="EN-US"}***[session-requests session-request-period blocking-period]{lang="EN-US"}*]{#struct_0_x2041_67218_x597507830}

[**[undo ]{lang="EN-US"}[pppoe-server throttle per-mac]{lang="EN-US"}**]{#struct_0_x2041_67218_73112225}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1158089578}

[[不限制会话建立的速度。]{style="font-family:宋体"}]{#struct_0_x2041_67218_x597966581}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1817636921}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_x1625005241}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VE-L3VPN]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image004.jpg){#图片 8 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2041_67218_2011091051}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_2011549803}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x346532359}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x598032117}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1097284619}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1766861658}

[*[session-requests]{lang="EN-US"}*]{#struct_0_x2041_67218_x598097653}[：在监视时间段内允许每个用户的会话数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100000]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[session-request-period]{lang="EN-US"}*]{#struct_0_x2041_67218_1484298712}[：监视时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[blocking-period]{lang="EN-US"}*]{#struct_0_x2041_67218_309449435}[：扼制时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x598163189}

[[设备可以通过此命令来限制特定接口下每个用户（每个用户通过]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2041_67218_x1616590904}[地址进行标识）创建会话的速度。如果用户建立会话的速度达到门限值，即在监视时间段内该用户的会话请求数目超过本命令配置的允许数目，则扼制该用户的会话请求，即在监视时间段内该用户的超出允许数目的请求都会被丢弃，并输出对应的]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息。如果扼制时间配置为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示不扼制会话请求，但仍然会输出]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[系统使用监控表和扼制表来共同控制用户创建会话的速度：]{style="font-family:宋体"}]{#struct_0_x2041_67218_x961550475}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[监视表：监视各用户在监视时间周期内创建的会话数。监视表的规格为]{style="font-family:宋体"}]{#struct_0_x2041_67218_x597704437}[8K]{lang="EN-US"}[。当监视表达到规格时，对新用户的会话请求不进行监视和扼制，正常建立会话。监视表项的老化时间为配置的]{style="font-family:宋体"}*[session-request-period]{lang="EN-US"}*[值，老化后对用户重新监视。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[扼制表：当某用户建立会话的速度超过门限值时，会将该用户的信息加入扼制表，扼制该用户的会话请求。扼制表规格为]{style="font-family:宋体"}]{#struct_0_x2041_67218_1670445232}[8K]{lang="EN-US"}[。当扼制表达到规格时，对新用户的会话请求只进行监视和发送]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息，但不触发扼制。扼制表项的老化时间为配置的]{style="font-family:宋体"}*[blocking-period]{lang="EN-US"}*[值，老化后对用户重新监视。]{style="font-family:宋体"}

[[修改本命令的配置后，系统将删除已记录的监视表和扼制表，重新开始监视每个用户的会话请求。]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1293512106}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x597769973}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_523570389}[配置接口允许每个用户创建会话的速度。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1445562030}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server throttle per-mac 100 100 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x597835509}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pppoe-server throttled-mac]{lang="EN-US"}**]{#struct_0_x2041_67218_896631929}
:::::

::: {#-1223156360 .myid}
[]{#_Toc404785116}[]{#struct_0_x2041_67218_x1842397824}[]{#_Toc366514068}

**PPPoE \-- PPPoE Server配置命令 \-- pppoe-server virtual-template va-pool**

------------------------------------------------------------------------

[**[pppoe-server virtual-template va-pool]{lang="EN-US"}**]{#struct_0_x2041_67218_x597901045}[命令用来配置]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}

[**[undo pppoe-server ]{lang="EN-US"}[virtual-template va-pool]{lang="EN-US"}**]{#struct_0_x2041_67218_1675735530}[命令用来删除]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1172073869}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2041_67218_165026205}

[**[pppoe-server virtual-template]{lang="EN-US"}**[ *template-number* **va-pool** *va-volume*]{lang="EN-US"}]{#struct_0_x2041_67218_x597442293}

[**[undo ]{lang="EN-US"}[pppoe-server virtual-template]{lang="EN-US"}**[ *template-number* **va-pool**]{lang="EN-US"}]{#struct_0_x2041_67218_x1426703113}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_728707291}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[pppoe-server virtual-template ]{lang="EN-US"}***[template-number ]{lang="EN-US"}*[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **va-pool** *va-volume*]{lang="EN-US"}]{#struct_0_x2041_67218_x597507829}

[**[undo ]{lang="EN-US"}[pppoe-server virtual-template]{lang="EN-US"}**[ *template-number* \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **va-pool**]{lang="EN-US"}]{#struct_0_x2041_67218_73702050}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2041_67218_x904887725}[模式：]{style="font-family:宋体"}

[**[pppoe-server virtual-template ]{lang="EN-US"}***[template-number ]{lang="EN-US"}*[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **va-pool** *va-volume*]{lang="EN-US"}]{#struct_0_x2041_67218_x597966580}

[**[undo ]{lang="EN-US"}[pppoe-server virtual-template]{lang="EN-US"}**[ *template-number* \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **va-pool**]{lang="EN-US"}]{#struct_0_x2041_67218_x1817702457}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1784299639}

[[不存在]{style="font-family:宋体"}[VA]{lang="EN-US"}]{#struct_0_x2041_67218_x598032116}[池。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1097350155}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1743890227}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x598097652}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1484364248}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x89044483}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_303954066}

[**[virtual-template ]{lang="EN-US"}***[template-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x598163188}[：指定需要使用]{style="font-family:宋体"}[VA]{lang="EN-US"}[池的虚拟模板接口。该接口必须已经存在。]{style="font-family:宋体"}

[**[va-pool ]{lang="EN-US"}***[va-volume]{lang="EN-US"}*]{#struct_0_x2041_67218_x1616656440}[：指定需要创建的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池的大小，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。实际可以配置的最大值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1476098494}[：在指定单板上创建局部]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则表示创建全局]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_x597704436}[：在指定成员设备上创建局部]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，则表示创建全局]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_1878040280}[：在指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上创建局部]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，则表示创建全局]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_1670379696}[：在指定成员设备的指定单板上创建局部]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则表示创建全局]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2041_67218_1419523327}[：在指定单板上创建局部]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，则表示创建全局]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2041_67218_1066843782}[：在指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上创建局部]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x443016275}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x597769972}[在建立连接时需要创建]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口（]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口用于]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[与]{style="font-family:宋体"}[PPP]{lang="EN-US"}[之间的报文传递），在用户下线后需要删除]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口。由于创建]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口需要一定的时间，所以如果有大量用户上线]{style="font-family:宋体"}[/]{lang="EN-US"}[下线时，]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[的连接建立、连接拆除性能会受到影响。]{style="font-family:宋体"}

[[使用]{style="font-family:宋体"}[VA]{lang="EN-US"}]{#struct_0_x2041_67218_523504853}[池对]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[的连接建立、连接拆除性能有显著提高。]{style="font-family:宋体"}[VA]{lang="EN-US"}[池是在建立连接前事先创建的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的集合。创建]{style="font-family:宋体"}[VA]{lang="EN-US"}[池后，当需要创建]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口时，直接从]{style="font-family:宋体"}[VA]{lang="EN-US"}[池中获取一个]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口，加快了]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[连接的建立速度。当用户下线后，直接把]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口放入]{style="font-family:宋体"}[VA]{lang="EN-US"}[池中，不需要删除]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口，加快了]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[连接的拆除速度。当]{style="font-family:宋体"}[VA]{lang="EN-US"}[池中的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口耗光后，仍需在建立]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[连接时再创建]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口，在用户下线后删除]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2041_67218_423471344}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个虚拟模板接口只能关联一个全局]{style="font-family:宋体"}]{#struct_0_x2041_67218_x597835508}[VA]{lang="EN-US"}[池，在每个单板上只能关联一个局部]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。通过某单板上的以太网接口上线的用户，只能使用上线以太网接口绑定的虚拟模板接口在该单板上关联的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。如果想要修改使用的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池的大小，只能先删除原来的配置，然后重新配置]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建]{style="font-family:宋体"}]{#struct_0_x2041_67218_896697465}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[VA]{lang="EN-US"}[池需要花费一定的时间，请用户耐心等待。在]{style="font-family:宋体"}[VA]{lang="EN-US"}[池创建]{style="font-family:宋体"}[/]{lang="EN-US"}[删除过程中（还没创建]{style="font-family:宋体"}[/]{lang="EN-US"}[删除完成）允许用户上线]{style="font-family:宋体"}[/]{lang="EN-US"}[下线，但正在创建]{style="font-family:宋体"}[/]{lang="EN-US"}[删除的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池不生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统可能由于资源不足不能创建用户指定容量的]{lang="EN-US" style="font-family:宋体"}[VA]{lang="EN-US"}]{#struct_0_x2041_67218_x1129103125}[池，用户可以通过]{lang="EN-US" style="font-family:宋体"}**[display pppoe-server va-pool]{lang="EN-US"}**[命令查看实际可用的]{lang="EN-US" style="font-family:宋体"}[VA]{lang="EN-US"}[池的容量以及]{lang="EN-US" style="font-family:宋体"}[VA]{lang="EN-US"}[池的状态。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VA]{lang="EN-US"}]{#struct_0_x2041_67218_x597901044}[池会占用较多的系统内存，请用户根据实际情况创建合适大小的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除]{style="font-family:宋体"}]{#struct_0_x2041_67218_1675669994}[VA]{lang="EN-US"}[池时，如果已有在线用户使用该]{style="font-family:宋体"}[VA]{lang="EN-US"}[池中的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口，不会导致这些用户下线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1842013350}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x597442292}[为虚拟模板]{style="font-family:宋体"}[2]{lang="EN-US"}[创建容量为]{style="font-family:宋体"}[1000]{lang="EN-US"}[的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1426768649}

[\[Sysname\] pppoe-server virtual-template 2 va-pool 1000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x2053260130}

[**[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;font-weight:normal"}[display pppoe-server va-pool]{lang="EN-US"}**]{#struct_0_x2041_67218_x1562172732}
:::

::: {#-1199643691 .myid}
[]{#struct_0_x2041_67218_x597507828}[]{#_Toc404785117}[]{#_Toc366514069}

**PPPoE \-- PPPoE Server配置命令 \-- reset pppoe-server**

------------------------------------------------------------------------

[**[reset pppoe-server]{lang="EN-US"}**]{#struct_0_x2041_67218_73636514}[命令用来在]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[端清除]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1554991138}

[**[reset pppoe-server]{lang="EN-US"}**[ {]{lang="EN-US"}]{#struct_0_x2041_67218_x597966579}[ **all**]{lang="EN-US"}[ \|]{lang="EN-US"}[ **interface** ]{lang="EN-US"}*[interface-type interface-number]{lang="EN-US"}*[ \| ]{lang="EN-US"}**[virtual-template ]{lang="EN-US"}***[number ]{lang="EN-US"}*[}]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1818161220}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_x2063454793}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x598032115}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1097415691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x947145215}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x598097651}

[**[all]{lang="EN-US"}**]{#struct_0_x2041_67218_1484167640}[：清除全部]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2041_67218_x2052729560}[：清除指定接口的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[用来指定接口的类型和编号。]{style="font-family:宋体"}

[**[virtual-template ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_x598163187}[：清除指定虚拟模板接口的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1616197688}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_2130075316}[在]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[端清除]{style="font-family:宋体"}[Virtual-template1]{lang="EN-US"}[上的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[\<Sysname\> reset pppoe-server virtual-template 1]{lang="EN-US"}]{#struct_0_x2041_67218_x597704435}
:::

::::: {#-1585416173 .myid}
[]{#_Toc259009562}[]{#_Toc136938106}[]{#_Toc96758180}[]{#_Toc37216128}[]{#_Toc29117277}[]{#_Toc404785119}[]{#struct_0_x2041_67218_1510355229}[]{#_Toc335730726}

**PPPoE \-- PPPoE Client配置命令 \-- dialer diagnose**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PPP命令.files/image001.png){#图片 3 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2041_67218_x520658154}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2041_67218_1374398070}
:::

[ ]{lang="EN-US"}

[**[dialer diagnose]{lang="EN-US"}**]{#struct_0_x2041_67218_x283209647}[命令用来配置]{style="font-family:宋体"}[DDR]{lang="EN-US"}[应用工作在诊断模式。]{style="font-family:宋体"}

[**[undo dialer diagnose]{lang="EN-US"}**]{#struct_0_x2041_67218_1378161671}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1383907408}

[**[dialer diagnose]{lang="EN-US"}**[ \[ **interval** ]{lang="EN-US"}*[interval]{lang="EN-US"}*[ \]]{lang="EN-US"}]{#struct_0_x2041_67218_x1226058724}

[**[undo dialer diagnose]{lang="EN-US"}**]{#struct_0_x2041_67218_1157753327}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_599260068}

[[DDR]{lang="EN-US"}]{#struct_0_x2041_67218_x807974809}[应用工作在非诊断模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1092338739}

[[Dialer]{lang="EN-US"}]{#struct_0_x2041_67218_878818299}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1196599276}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1180253842}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1820853021}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x737832789}

[*[interval]{lang="EN-US"}*]{#struct_0_x2041_67218_x907555756}[：诊断时间间隔，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_598801317}

[[只有当]{style="font-family:宋体"}[Dialer]{lang="EN-US"}]{#struct_0_x2041_67218_x988352048}[接口用于]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[时，此配置才生效。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}]{#struct_0_x2041_67218_x1766958249}[工作在诊断模式时，设备会在配置完成后立即发起]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[呼叫，建立链接，链接建立后隔]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[时间，设备会自动断开该链接，并启动自动拨号定时器，等待自动拨号定时器超时再重新发起]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[呼叫建立链接。通过定期建立、删除呼叫，可以监控]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[链路是否处于正常工作状态。]{style="font-family:宋体"}

[[当工作在诊断模式时，]{style="font-family:宋体"}**[dialer timer idle]{lang="EN-US"}**]{#struct_0_x2041_67218_1828326639}[命令配置的]{style="font-family:宋体"}[Idle]{lang="EN-US"}[定时器失效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1244575024}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x633079390}[设置接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[工作在诊断模式，诊断时间间隔为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_312021476}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] dialer diagnose interval 300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2118146222}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer timer autodial]{lang="EN-US"}**]{#struct_0_x2041_67218_598735781}[（]{style="font-family:宋体"}[二层技术]{lang="EN-US" style="font-family:宋体"}[-]{lang="EN-US"}[广域网接入]{lang="EN-US" style="font-family:宋体"}[命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[DDR]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer timer idle]{lang="EN-US"}**]{#struct_0_x2041_67218_705217635}[（]{style="font-family:宋体"}[二层技术]{lang="EN-US" style="font-family:宋体"}[-]{lang="EN-US"}[广域网接入]{lang="EN-US" style="font-family:宋体"}[命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[DDR]{lang="EN-US"}[）]{style="font-family:宋体"}
:::::

::: {#-209471781 .myid}
[]{#_Toc404785120}[]{#struct_0_x2041_67218_x319729721}

**PPPoE \-- PPPoE Client配置命令 \-- display pppoe-client session packet**

------------------------------------------------------------------------

[]{#_Toc32639296}[**[display pppoe-client session packet]{lang="EN-US"}**]{#struct_0_x2041_67218_1788478207}[命令用来显示]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的协议报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_2016203285}

[**[display pppoe-client session]{lang="EN-US"}**[ **packet** \[ **dial-bundle-number** *number* \]]{lang="EN-US"}]{#struct_0_x2041_67218_x1947297127}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1285118358}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_870503040}[]{#_Toc32639298}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_598670245}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1592164900}

[[network-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x1272605683}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1569685747}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x1673287640}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1213989091}

[**[dial-bundle-number]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x2041_67218_613251109}[：显示指定]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的协议报文统计信息。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果不指定]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话，则显示所有]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的协议报文统计信息。]{style="font-family:宋体"}

[]{#struct_0_x2041_67218_2094957101}[[【使用指导】]{style="font-family:黑体"}]{#_Toc32639299}

[**[display pppoe-client session packet]{lang="EN-US"}**]{#struct_0_x2041_67218_315277182}[命令用来显示]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的协议报文统计信息。]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的数据报文统计信息可以通过]{style="font-family:宋体"}**[display interface virtual-access]{lang="EN-US"}**[命令查看指定]{style="font-family:宋体"}[Virtual Access]{lang="EN-US"}[接口的详细信息获得。]{style="font-family:宋体"}

[]{#struct_0_x2041_67218_598604709}[[【举例】]{style="font-family:黑体"}]{#_Toc32639300}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1605974970}[显示所有]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的协议报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-client session packet]{lang="EN-US"}]{#struct_0_x2041_67218_x1612343844}

[Bundle:    1                     Interface:  GE1/0/1]{lang="EN-US"}

[InPackets: 19                    OutPackets: 19]{lang="EN-US"}

[InBytes:   816                   OutBytes:   816]{lang="EN-US"}

[InDrops:   0                     OutDrops:   0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Bundle:    2                     Interface:  GE1/0/1]{lang="EN-US"}

[InPackets: 18                    OutPackets: 18]{lang="EN-US"}

[InBytes:   730                   OutBytes:   730]{lang="EN-US"}

[InDrops:   0                     OutDrops:   0]{lang="EN-US"}

[]{#struct_0_x2041_67218_x1189865589}[]{#_Toc95359210}[]{#_Toc85604321}[]{#_Toc81386700}[]{#_Toc74661823}[]{#_Toc72589786}[]{#_Toc72589513}[]{#_Toc72588998}[]{#_Toc65921168}[]{#_Toc65919116}[]{#_Toc65919091}[]{#_Toc65910725}[]{#_Toc65909970}[]{#_Toc60125180}[]{#_Toc60111179}[]{#_Toc37215872}[]{#_Toc37215717}[]{#_Toc35242429}[]{#_Toc34733769}[]{#_Toc34733520}[[表2-6 ]{lang="EN-US"}[display pppoe-client session packet]{lang="EN-US"}]{#_Toc33587015}[命令显示信息]{style="font-family:黑体"}[描述表]{style="font-family:黑体"}

[]{#table_struct_0_708762174}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_1177585481}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_598539173}

[[Bundle]{lang="EN-US"}]{#struct_0_x2041_67218_874568495}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_1981975243}[会话所属的]{style="font-family:宋体"}[Dialer bundle]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_x2041_67218_x75055786}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_385204786}[会话对应的以太网接口，即在该以太网接口上建立]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}

[[InPackets]{lang="EN-US"}]{#struct_0_x2041_67218_1794894924}

[[接收报文数]{style="font-family:宋体"}]{#struct_0_x2041_67218_2061445650}

[[OutPackets]{lang="EN-US"}]{#struct_0_x2041_67218_598473637}

[[发送报文数]{style="font-family:宋体"}]{#struct_0_x2041_67218_1659457610}

[[InBytes]{lang="EN-US"}]{#struct_0_x2041_67218_x346950576}

[[接收字节数]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1848503890}

[[OutBytes]{lang="EN-US"}]{#struct_0_x2041_67218_x1398268473}

[[发送字节数]{style="font-family:宋体"}]{#struct_0_x2041_67218_598408101}

[[InDrops]{lang="EN-US"}]{#struct_0_x2041_67218_1284365064}

[[接收非法并丢弃的报文数]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1138442598}

[[OutDrops]{lang="EN-US"}]{#struct_0_x2041_67218_x611835199}

[[发送非法并丢弃的报文数]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1625804550}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1795962213}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface]{lang="EN-US"}**]{#struct_0_x2041_67218_598342565}**[ ]{lang="EN-US"}[virtual-access]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset pppoe-client session packet]{lang="EN-US"}**]{#struct_0_x2041_67218_200584700}

::: {#168958191 .myid}
[]{#_Toc404785121}[]{#struct_0_x2041_67218_359035954}

**PPPoE \-- PPPoE Client配置命令 \-- display pppoe-client session summary**

------------------------------------------------------------------------

[**[display pppoe-client session summary]{lang="EN-US"}**]{#struct_0_x2041_67218_1309685330}[命令用来显示]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的概要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_73362092}

[**[display pppoe-client session]{lang="EN-US"}**[ **summary** \[ **dial-bundle-number** *number* \]]{lang="EN-US"}]{#struct_0_x2041_67218_x1123928877}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1451875772}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_1495078945}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_599325605}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1510355228}

[[network-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x520592618}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x1329337747}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2041_67218_x1474548730}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1215762611}

[**[dial-bundle-number]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x2041_67218_1915165583}[：显示指定]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的概要信息。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果不指定]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话，则显示所有]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_382362319}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x2023650968}[显示所有]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-client session summary]{lang="EN-US"}]{#struct_0_x2041_67218_599260069}

[Bundle ID    Interface    VA          RemoteMAC      LocalMAC       State]{lang="EN-US"}

[1      1     GE1/0/1      VA0         00e0-1400-4300 00e0-1500-4100 SESSION]{lang="EN-US"}

[2      1     GE1/0/2      VA1         00e0-1500-4300 00e0-1600-4100 SESSION]{lang="EN-US"}

[[表2-7 ]{lang="EN-US"}[display pppoe-client session summary]{lang="EN-US"}]{#struct_0_x2041_67218_x807974810}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_734654160}[[字段]{style="font-family:黑体"}]{#struct_0_x2041_67218_1092797492}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2041_67218_1230556384}

[[Bundle]{lang="EN-US"}]{#struct_0_x2041_67218_1116023626}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x1388402858}[会话所属的]{style="font-family:宋体"}[Dialer bundle]{lang="EN-US"}

[[ID]{lang="EN-US"}]{#struct_0_x2041_67218_598801314}

[[Session ID]{lang="EN-US"}]{#struct_0_x2041_67218_x988352049}[，]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的编号]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x2041_67218_x1767023785}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x455012100}[会话所属的以太网接口]{style="font-family:宋体"}

[[VA]{lang="EN-US"}]{#struct_0_x2041_67218_2019428463}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x1763729922}[会话创建的]{style="font-family:宋体"}[Virtual Access]{lang="EN-US"}[接口]{style="font-family:宋体"}

[[RemoteMAC]{lang="EN-US"}]{#struct_0_x2041_67218_598735778}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x14826406}[会话所属的对端以太网接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[LocalMAC]{lang="EN-US"}]{#struct_0_x2041_67218_2043428410}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_1058266290}[会话所属的本端以太网接口的]{style="font-family:宋体"}[MAC]{lang="PT-BR"}[地址]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x2041_67218_2006542760}

[[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_x1722864040}[会话所处的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_x2041_67218_598670242}[：初始化状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PADI SENT]{lang="EN-US"}]{#struct_0_x2041_67218_x1592164895}[：已发送]{lang="EN-US" style="font-family:宋体"}[PADI]{lang="EN-US"}[报文、等待]{lang="EN-US" style="font-family:宋体"}[PADO]{lang="EN-US"}[报文状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PADR SENT]{lang="EN-US"}]{#struct_0_x2041_67218_x869910979}[：已发送]{lang="EN-US" style="font-family:宋体"}[PADR]{lang="EN-US"}[报文、等待]{lang="EN-US" style="font-family:宋体"}[PADS]{lang="EN-US"}[报文状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SESSION]{lang="EN-US"}]{#struct_0_x2041_67218_486089124}[：会话协商成功]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#530539368 .myid}
[]{#_Toc404785122}[]{#struct_0_x2041_67218_1472180728}[]{#_Toc259009563}[]{#_Toc136938107}[]{#_Toc96758181}[]{#_Toc37216129}[]{#_Toc29117275}

**PPPoE \-- PPPoE Client配置命令 \-- pppoe-client**

------------------------------------------------------------------------

[]{#_Toc32639286}[**[pppoe-client]{lang="EN-US"}**]{#struct_0_x2041_67218_598604706}[命令用来建立一个]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话，并且指定该会话所对应的]{style="font-family:宋体"}[Dialer bundle]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo pppoe-client]{lang="EN-US"}**]{#struct_0_x2041_67218_x1605974979}[命令用来删除一个]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1472769871}

[**[pppoe-client dial-bundle-number]{lang="EN-US"}**[ *number* \[ **no-hostuniq** \]]{lang="EN-US"}]{#struct_0_x2041_67218_x421389510}

[**[undo pppoe-client dial-bundle-number]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x2041_67218_x371058069}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x11510591}

[[接口下没有配置]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_x2041_67218_1888825324}[会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1972519565}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2041_67218_x1616179906}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层虚拟以太网接口视图]{style="font-family:宋体"}[[/]{lang="EN-US"}]{#_Toc32639288}[三层虚拟以太网子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/WLAN]{lang="EN-US"}[以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_598539170}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_874568492}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_1981975246}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x75252394}

[**[dial-bundle-number]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x2041_67218_1028756636}[：与]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话相对应的]{style="font-family:宋体"}[Dialer bundle]{lang="EN-US"}[编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。参数]{style="font-family:宋体"}*[number]{lang="EN-US"}*[可以用来唯一标识一个]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话，也可以把它作为]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的编号。]{style="font-family:宋体"}

[**[no-hostuniq]{lang="EN-US"}**]{#struct_0_x2041_67218_x1746449844}[：在]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[发起的呼叫中不携带]{style="font-family:宋体"}[Host-Uniq]{lang="EN-US"}[字段。缺省情况下，呼叫中携带]{style="font-family:宋体"}[Host-Uniq]{lang="EN-US"}[字段。]{style="font-family:宋体"}[Host-Uniq]{lang="EN-US"}[字段用来唯一标识一个]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[。当接口下配置了多个]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话时，为了区分不同]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的报文，可以配置在]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[呼叫报文中携带]{style="font-family:宋体"}[Host-Uniq]{lang="EN-US"}[字段。]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[收到携带]{style="font-family:宋体"}[Host-Uniq]{lang="EN-US"}[字段的报文后，必须在应答报文中携带]{style="font-family:宋体"}[Host-Uniq]{lang="EN-US"}[字段，内容和请求报文中的]{style="font-family:宋体"}[Host-Uniq]{lang="EN-US"}[字段相同。设备收到]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[的应答报文后，根据]{style="font-family:宋体"}[Host-Uniq]{lang="EN-US"}[字段的值可以唯一确定应答报文所属的]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[。]{style="font-family:宋体"}

[]{#struct_0_x2041_67218_682393618}[[【举例】]{style="font-family:黑体"}]{#_Toc32639290}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1513958852}[在三层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上建立一个]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_598473634}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-client dial-bundle-number 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1659457607}[在三层虚拟以太网接口]{style="font-family:宋体"}[Virtual-Ethernet0]{lang="EN-US"}[上建立一个]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x346753969}

[\[Sysname\] interface virtual-ethernet 0]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet0\] pppoe-client dial-bundle-number 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_1717804244}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[上建立一个]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x644098420}

[\[Sysname\] interface vlan-interface 1]{lang="EN-US"}

[\[Sysname-Vlan-interface1\] pppoe-client dial-bundle-number 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_100906307}[在]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[以太网接口]{style="font-family:宋体"}[WLAN-Ethernet1]{lang="EN-US"}[上建立一个]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2041_67218_x1105023148}

[\[Sysname\] interface wlan-ethernet 1]{lang="EN-US"}

[\[Sysname-WLAN-Ethernet1\] pppoe-client dial-bundle-number 1]{lang="EN-US"}
:::

::: {#-2003292843 .myid}
[]{#_Toc404785123}[]{#struct_0_x2041_67218_598408098}[]{#_Toc259009564}[]{#_Toc136938108}[]{#_Toc96758182}[]{#_Toc37216130}[]{#_Toc29117276}

**PPPoE \-- PPPoE Client配置命令 \-- reset pppoe-client**

------------------------------------------------------------------------

[]{#_Toc32639291}[**[reset pppoe-client]{lang="EN-US"}**]{#struct_0_x2041_67218_x635214218}[命令用来复位]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x577237115}

[**[reset pppoe-client]{lang="EN-US"}**[ { **all** \| **dial-bundle-number** *number* }]{lang="EN-US"}]{#struct_0_x2041_67218_x577877788}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1716434415}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_98286410}[]{#_Toc32639293}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1379952220}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_2049976763}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x854164892}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_598342562}

[**[all]{lang="EN-US"}**]{#struct_0_x2041_67218_200584699}[：复位所有的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[dial-bundle-number ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_x1942880352}[：复位与指定]{style="font-family:宋体"}[Dialer bundle]{lang="EN-US"}[相对应的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1487012829}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1778271576}[PPPoE]{lang="EN-US"}[会话工作在永久在线模式时，如果使用]{style="font-family:宋体"}**[reset pppoe-client]{lang="EN-US"}**[命令复位]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话，设备会在自动拨号定时器超时后自动重新建立]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x2041_67218_x1183453977}[PPPoE]{lang="EN-US"}[会话工作在按需拨号模式时，如果使用]{style="font-family:宋体"}**[reset pppoe-client]{lang="EN-US"}**[命令复位]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话，设备会在有数据需要传送时，才重新建立]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[]{#struct_0_x2041_67218_2013146254}[[【举例】]{style="font-family:黑体"}]{#_Toc32639295}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x1713118860}[复位所有的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[\<Sysname\> reset pppoe-client all]{lang="EN-US"}]{#struct_0_x2041_67218_599325602}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_1510355231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer timer autodial]{lang="EN-US"}**]{#struct_0_x2041_67218_x520133867}[（二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[广域网接入命令参考]{style="font-family:宋体"}[/DDR]{lang="EN-US"}[）]{style="font-family:宋体"}
:::

::: {#-890099646 .myid}
[]{#_Toc404785124}[]{#struct_0_x2041_67218_1036803747}

**PPPoE \-- PPPoE Client配置命令 \-- reset pppoe-client session packet**

------------------------------------------------------------------------

[**[reset pppoe-client session packet]{lang="EN-US"}**]{#struct_0_x2041_67218_x1095792462}[命令用来清除]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的协议报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1138547755}

[**[reset pppoe-client session packet]{lang="EN-US"}**[ \[ **dial-bundle-number** *number* \]]{lang="EN-US"}]{#struct_0_x2041_67218_94965410}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2041_67218_976344378}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2041_67218_944950968}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2041_67218_599260066}

[[network-admin]{lang="EN-US"}]{#struct_0_x2041_67218_x807974799}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2041_67218_372294716}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2041_67218_x1600014923}

[**[dial-bundle-number ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x2041_67218_279467604}[：清除指定]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的协议报文统计信息。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果不指定]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话，则清除所有]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的协议报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2041_67218_59848103}

[[\# ]{lang="EN-US"}]{#struct_0_x2041_67218_x187996375}[清除所有的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话的协议报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset pppoe-client session packet]{lang="EN-US"}]{#struct_0_x2041_67218_1804676736}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2041_67218_69471451}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pppoe-client session packet]{lang="EN-US"}**]{#struct_0_x2041_67218_598801315}
:::
