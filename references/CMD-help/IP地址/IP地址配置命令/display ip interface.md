::: {#-241902328 .myid}
[]{#_Toc404786077}[]{#struct_0_10809_18680_x2020720399}[]{#_Toc130529682}[]{#_Toc94411693}[]{#_Toc94499889}[]{#_Toc94500098}

**IP地址 \-- IP地址配置命令 \-- display ip interface**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ip** **interface**]{lang="EN-US"}]{#struct_0_10809_18680_2130689527}[命令用来显示三层接口与]{style="font-family:宋体"}[IP]{lang="EN-US"}[相关的配置和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10809_18680_1242948826}

[**[display]{lang="EN-US"}**[ **ip** **interface** \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_10809_18680_2128013189}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10809_18680_x2002680536}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10809_18680_1684403342}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10809_18680_1343685198}

[[network-admin]{lang="EN-US"}]{#struct_0_10809_18680_1931994570}

[[network-operator]{lang="EN-US"}]{#struct_0_10809_18680_431243659}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10809_18680_x894051883}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10809_18680_83407006}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10809_18680_1624716511}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_10809_18680_1218136647}[：显示指定接口的相关信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10809_18680_1243014362}

[**[display]{lang="EN-US"}**[ **ip** **interface**]{lang="EN-US"}]{#struct_0_10809_18680_x954830480}[命令用来查看三层接口与]{style="font-family:宋体"}[IP]{lang="EN-US"}[相关的配置和统计信息，包括接口上接收和发送的单播报文数、字节数和组播报文数，以及接口上收到的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[无效报文数和]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文数等。]{style="font-family:宋体"}

[[通过对显示信息中报文收发情况的分析，可以初步判断网络是否遭到攻击和攻击的可能来源。]{style="font-family:宋体"}]{#struct_0_10809_18680_1786114837}

[[如果不指定参数，则显示所有三层接口的相关信息。]{style="font-family:宋体"}]{#struct_0_10809_18680_x1330886209}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10809_18680_973064301}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_x1739675876}

[[\# ]{lang="EN-US"}]{#struct_0_10809_18680_1670924966}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[与]{style="font-family:宋体"}[IP]{lang="EN-US"}[相关的配置和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_10809_18680_1243604186}

[GigabitEthernet1/0/1 current state: DOWN]{lang="EN-US"}

[Line protocol current state: DOWN]{lang="EN-US"}

[Internet Address is 1.1.1.1/8 Primary]{lang="EN-US"}

[Broadcast address: 1.255.255.255]{lang="EN-US"}

[The Maximum Transmit Unit: 1500 bytes]{lang="EN-US"}

[input packets : 0, bytes : 0, multicasts : 0]{lang="EN-US"}

[output packets : 0, bytes : 0, multicasts : 0]{lang="EN-US"}

[TTL invalid packet number:         0]{lang="EN-US"}

[ICMP packet input number:          0]{lang="EN-US"}

[  Echo reply:                      0]{lang="EN-US"}

[  Unreachable:                     0]{lang="EN-US"}

[  Source quench:                   0]{lang="EN-US"}

[  Routing redirect:                0]{lang="EN-US"}

[  Echo request:                    0]{lang="EN-US"}

[  Router advert:                   0]{lang="EN-US"}

[  Router solicit:                  0]{lang="EN-US"}

[  Time exceed:                     0]{lang="EN-US"}

[  IP header bad:                   0]{lang="EN-US"}

[  Timestamp request:               0]{lang="EN-US"}

[  Timestamp reply:                 0]{lang="EN-US"}

[  Information request:             0]{lang="EN-US"}

[  Information reply:               0]{lang="EN-US"}

[  Netmask request:                 0]{lang="EN-US"}

[  Netmask reply:                   0]{lang="EN-US"}

[  Unknown type:                    0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_x569937616}

[[\# ]{lang="EN-US"}]{#struct_0_10809_18680_1835291108}[显示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[与]{style="font-family:宋体"}[IP]{lang="EN-US"}[相关的配置和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip interface vlan-interface 10]{lang="EN-US"}]{#struct_0_10809_18680_1243669722}

[Vlan-interface10 current state: DOWN]{lang="EN-US"}

[Line protocol current state: DOWN]{lang="EN-US"}

[Internet Address is 1.1.1.1/8 Primary]{lang="EN-US"}

[Broadcast address: 1.255.255.255]{lang="EN-US"}

[The Maximum Transmit Unit: 1500 bytes]{lang="EN-US"}

[input packets : 0, bytes : 0, multicasts : 0]{lang="EN-US"}

[output packets : 0, bytes : 0, multicasts : 0]{lang="EN-US"}

[TTL invalid packet number:         0]{lang="EN-US"}

[]{#_Toc17279916}[[ICMP packet input number:          0]{lang="EN-US"}]{#_Toc533579659}

[  Echo reply:                      0]{lang="EN-US"}

[  Unreachable:                     0]{lang="EN-US"}

[  Source quench:                   0]{lang="EN-US"}

[  Routing redirect:                0]{lang="EN-US"}

[  Echo request:                    0]{lang="EN-US"}

[  Router advert:                   0]{lang="EN-US"}

[  Router solicit:                  0]{lang="EN-US"}

[  Time exceed:                     0]{lang="EN-US"}

[  IP header bad:                   0]{lang="EN-US"}

[  Timestamp request:               0]{lang="EN-US"}

[  Timestamp reply:                 0]{lang="EN-US"}

[  Information request:             0]{lang="EN-US"}

[  Information reply:               0]{lang="EN-US"}

[  Netmask request:                 0]{lang="EN-US"}

[  Netmask reply:                   0]{lang="EN-US"}

[  Unknown type:                    0]{lang="EN-US"}

[]{#struct_0_10809_18680_923294981}[]{#_Toc138413281}[[表1-1 ]{lang="EN-US"}[display ip interface]{lang="EN-US"}]{#_Toc138236204}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1870374836}[[字段]{style="font-family:黑体"}]{#struct_0_10809_18680_982410314}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10809_18680_2141761438}

[[current state]{lang="EN-US"}]{#struct_0_10809_18680_1423485906}

[[接口当前的物理状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_10809_18680_1243079899}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively DOWN]{lang="EN-US"}]{#struct_0_10809_18680_1347902784}[：表示该接口已经通过]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_10809_18680_x228501119}[：该接口的管理状态为开启，但物理状态为关闭（可能因为没有连接好或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_10809_18680_1202877909}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol current state]{lang="EN-US"}]{#struct_0_10809_18680_x21200717}

[[链路层协议当前状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_10809_18680_1652966993}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_10809_18680_1662085198}[：该接口的协议状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_10809_18680_1243145435}[：该接口的协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP (spoofing)]{lang="EN-US"}]{#struct_0_10809_18680_957933029}[：该接口的协议状态为欺骗性开启，即虽然接口的链路层协议状态显示是开启的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Internet Address]{lang="EN-US"}]{#struct_0_10809_18680_1983075128}

[[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_10809_18680_1766375035}[地址，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址后可携带如下参数：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Primary]{lang="EN-US"}]{#struct_0_10809_18680_x485123342}[：表示手动配置的主]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sub]{lang="EN-US"}]{#struct_0_10809_18680_x1646538808}[：表示手动配置的从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MTunnel]{lang="EN-US"}]{#struct_0_10809_18680_1058497752}[：表示]{lang="EN-US" style="font-family:宋体"}[MTunnel]{lang="EN-US"}[口]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSLVPN]{lang="EN-US"}]{#struct_0_10809_18680_1243210971}[：表示]{lang="EN-US" style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[虚接口]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP-Negotiated]{lang="EN-US"}]{#struct_0_10809_18680_223953945}[：表示]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[动态协商]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unnumbered]{lang="EN-US"}]{#struct_0_10809_18680_x615106307}[：表示借用]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP-Allocated]{lang="EN-US"}]{#struct_0_10809_18680_856144719}[：表示]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[动态分配]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BOOTP-Allocated]{lang="EN-US"}]{#struct_0_10809_18680_x1514496732}[：表示]{lang="EN-US" style="font-family:
  宋体"}[BOOTP]{lang="EN-US"}[动态分配]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Cluster]{lang="EN-US"}]{#struct_0_10809_18680_207583506}[：表示集群]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Mad]{lang="EN-US"}]{#struct_0_10809_18680_1243276507}[：表示]{lang="EN-US" style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[Broadcast address]{lang="EN-US"}]{#struct_0_10809_18680_x974354314}

[[接口所在网段的广播地址]{style="font-family:宋体"}]{#struct_0_10809_18680_714921099}

[[The Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_10809_18680_50932245}

[[接口的最大传输单元，单位为字节]{style="font-family:宋体"}]{#struct_0_10809_18680_418585306}

[[input packets, bytes, multicasts]{lang="EN-US"}]{#struct_0_10809_18680_1242817755}

[[output packets, bytes, multicasts]{lang="EN-US"}]{#struct_0_10809_18680_210041802}

[[接口上接收和发送的单播报文数、字节数以及组播报文数（设备启动后就开始统计此信息）]{style="font-family:宋体"}]{#struct_0_10809_18680_x404308793}

[[TTL invalid packet number]{lang="EN-US"}]{#struct_0_10809_18680_x1513318942}

[[接口上收到的]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_10809_18680_x722875331}[无效的报文个数（设备启动后就开始统计此信息）]{style="font-family:宋体"}

[[ICMP packet input number:]{lang="EN-US"}]{#struct_0_10809_18680_1242883291}

[[  Echo reply:]{lang="EN-US"}]{#struct_0_10809_18680_945999418}

[[  Unreachable:]{lang="EN-US"}]{#struct_0_10809_18680_1706258830}

[[  Source quench:]{lang="EN-US"}]{#struct_0_10809_18680_x1566127870}

[[  Routing redirect:]{lang="EN-US"}]{#struct_0_10809_18680_1054878089}

[[  Echo request:]{lang="EN-US"}]{#struct_0_10809_18680_1242948827}

[[  Router advert:]{lang="EN-US"}]{#struct_0_10809_18680_2127947653}

[[  Router solicit:]{lang="EN-US"}]{#struct_0_10809_18680_960147830}

[[  Time exceed:]{lang="EN-US"}]{#struct_0_10809_18680_x1777736219}

[[  IP header bad:]{lang="EN-US"}]{#struct_0_10809_18680_x1624553842}

[[  Timestamp request:]{lang="EN-US"}]{#struct_0_10809_18680_1243014363}

[[  Timestamp reply:]{lang="EN-US"}]{#struct_0_10809_18680_x954764944}

[[  Information request:]{lang="EN-US"}]{#struct_0_10809_18680_x505274308}

[[  Information reply:]{lang="EN-US"}]{#struct_0_10809_18680_654230315}

[[  Netmask request:]{lang="EN-US"}]{#struct_0_10809_18680_1243604187}

[[  Netmask reply:]{lang="EN-US"}]{#struct_0_10809_18680_x570003152}

[[  Unknown type:]{lang="EN-US"}]{#struct_0_10809_18680_188708402}

[[接口上收到的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_10809_18680_2142652896}[报文的总数（设备启动后就开始统计此信息），包括如下报文：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Echo]{lang="EN-US"}]{#struct_0_10809_18680_1243669723}[应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不可达报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_923229445}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[源站抑制报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_1787650172}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由重定向报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_606435114}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Echo]{lang="EN-US"}]{#struct_0_10809_18680_1243079896}[请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由器通告报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_1348754752}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由器请求报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_x1192988402}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[超时报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_x287113942}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_10809_18680_1243145432}[报文头错误报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[时间戳请求报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_958391781}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[时间戳响应报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_627373106}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[信息请求报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_x1904959010}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[信息响应报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_1243210968}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[掩码请求报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_223364122}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[掩码响应报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_x1737780161}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[未知类型报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_1243276504}

[]{#_Toc69790677}[[ ]{lang="EN-US"}]{#_Toc130529683}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10809_18680_x974550922}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **ip** **interface** **brief**]{lang="EN-US"}]{#struct_0_10809_18680_1537671774}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**[ **address**]{lang="EN-US"}]{#struct_0_10809_18680_x344416200}

::: {#-1134969791 .myid}
[]{#_Toc404786078}[]{#struct_0_10809_18680_x509192788}

**IP地址 \-- IP地址配置命令 \-- display ip interface brief**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ip** **interface** **brief**]{lang="EN-US"}]{#struct_0_10809_18680_1533806496}[命令]{style="font-family:宋体"}[用来显示三层接口与]{style="font-family:宋体"}[IP]{lang="EN-US"}[相关的简要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10809_18680_634202853}

[**[display]{lang="EN-US"}**[ **ip** **interface** \[ *interface-type* \[ *interface-number* \] \] **brief** \[ **description** \]]{lang="EN-US"}]{#struct_0_10809_18680_727894828}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10809_18680_419854218}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10809_18680_1242817752}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10809_18680_209583050}

[[network-admin]{lang="EN-US"}]{#struct_0_10809_18680_x1241953500}

[[network-operator]{lang="EN-US"}]{#struct_0_10809_18680_x1525564526}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10809_18680_x1301828760}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10809_18680_x255081134}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10809_18680_581074187}

[*[interface-type]{lang="EN-US"}*]{#struct_0_10809_18680_1285193772}[：显示指定类型接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[基本配置信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_10809_18680_x754384197}[：显示指定接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[基本配置信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_10809_18680_x1721122472}[：显示接口完整的描述信息。如果不指定该参数，则最多可以显示]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符，如果超过]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符，那么则显示前]{style="font-family:宋体"}[14]{lang="EN-US"}[个字符和"]{style="font-family:宋体"}[...]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10809_18680_1242883288}

[**[display]{lang="EN-US"}**[ **ip** **interface** **brief**]{lang="EN-US"}]{#struct_0_10809_18680_946589243}[命令用来查看三层接口与]{style="font-family:宋体"}[IP]{lang="EN-US"}[相关的简要信息，包括接口的物理和链路层协议状态、]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、描述信息等。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_10809_18680_1550867347}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定接口类型和接口编号，则显示所有三层接口的]{style="font-family:宋体"}]{#struct_0_10809_18680_x254479409}[IP]{lang="EN-US"}[基本配置信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果只指定接口类型，不指定接口编号，则显示该类型所有三层接口的]{style="font-family:宋体"}]{#struct_0_10809_18680_x1028119866}[IP]{lang="EN-US"}[基本配置信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定接口类型和接口编号，则显示指定接口的]{style="font-family:宋体"}]{#struct_0_10809_18680_17371704}[IP]{lang="EN-US"}[基本配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10809_18680_876610911}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_x813875913}

[[\# ]{lang="EN-US"}]{#struct_0_10809_18680_x1970130703}[显示]{style="font-family:宋体"}[GigabitEthernet]{lang="EN-US"}[接口的基本配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip interface gigabitethernet brief]{lang="EN-US"}]{#struct_0_10809_18680_1242948824}

[\*down: administratively down]{lang="EN-US"}

[(s): spoofing  (l): loopback]{lang="EN-US"}

[Interface                Physical Protocol IP Address      Description]{lang="EN-US"}

[GE1/0/1                  up       up       5.5.5.1         Link to CoreRo\...]{lang="EN-US"}

[\<Sysname\> display ip interface gigabitethernet brief description]{lang="EN-US"}

[\*down: administratively down]{lang="EN-US"}

[(s): spoofing  (l): loopback]{lang="EN-US"}

[Interface                Physical Protocol IP Address      Description]{lang="EN-US"}

[GE1/0/1                  up       up       5.5.5.1         Link to CoreRouter]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_2127882117}

[[\# ]{lang="EN-US"}]{#struct_0_10809_18680_x643166322}[显示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的基本配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip interface vlan-interface brief]{lang="EN-US"}]{#struct_0_10809_18680_1906857258}

[\*down: administratively down]{lang="EN-US"}

[(s): spoofing  (l): loopback]{lang="EN-US"}

[Interface                Physical Protocol IP Address      Description]{lang="EN-US"}

[Vlan10                   down     down     6.6.6.1         Link to CoreRo\...]{lang="EN-US"}

[Vlan2                    down     down     7.7.7.1         \--]{lang="EN-US"}

[\<Sysname\> display ip interface vlan-interface brief description]{lang="EN-US"}

[\*down: administratively down]{lang="EN-US"}

[(s): spoofing  (l): loopback]{lang="EN-US"}

[Interface                Physical Protocol IP Address      Description]{lang="EN-US"}

[Vlan10                   down     down     6.6.6.1         Link to CoreRouter]{lang="EN-US"}

[Vlan2                    down     down     7.7.7.1         \--]{lang="EN-US"}

[]{#struct_0_10809_18680_517570742}[]{#_Toc138413282}[]{#_Toc138236205}[[表1-2 ]{lang="EN-US"}[display ip interface brief]{lang="EN-US"}]{#_Toc94583059}[命令]{style="font-family:黑体"}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1862545157}[[字段]{style="font-family:黑体"}]{#struct_0_10809_18680_x1752601677}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10809_18680_1243014360}

[[\*down: administratively down]{lang="EN-US"}]{#struct_0_10809_18680_x954699408}

[[接口处于管理]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_10809_18680_x574086392}[状态，即采用]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令关闭了该接口]{style="font-family:宋体"}

[[(s) : spoofing]{lang="EN-US"}]{#struct_0_10809_18680_1077853493}

[[接口的欺骗属性，即接口的链路层协议状态显示是]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_10809_18680_x842356575}[的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_10809_18680_2031703378}

[[接口的名称]{style="font-family:宋体"}]{#struct_0_10809_18680_2032237851}

[[Physical]{lang="EN-US"}]{#struct_0_10809_18680_1243604184}

[[接口的物理状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_10809_18680_x570068688}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\*down]{lang="EN-US"}]{#struct_0_10809_18680_x2074518342}[：表示该接口已经通过]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_10809_18680_x573351756}[：该接口的管理状态为开启，但物理状态为关闭（可能因为没有连接好或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_10809_18680_80514461}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_10809_18680_x956933513}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_10809_18680_1243669720}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_10809_18680_923426053}[：该接口的协议状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down(l)]{lang="EN-US"}]{#struct_0_10809_18680_x1317903481}[：该接口的协议状态为]{style="font-family:宋体"}[loopback down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_10809_18680_x330091806}[：该接口的协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up(l)]{lang="EN-US"}]{#struct_0_10809_18680_1647585950}[：该接口的协议状态为]{style="font-family:宋体"}[loopback up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up(s)]{lang="EN-US"}]{#struct_0_10809_18680_138439956}[：该接口的协议状态为]{lang="EN-US" style="font-family:宋体"}[spoofing up]{lang="EN-US"}

[[IP Address]{lang="EN-US"}]{#struct_0_10809_18680_x944748714}

[[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_10809_18680_x1513441718}[地址（如果未配置则显示"]{style="font-family:宋体"}[\--]{lang="EN-US"}["）]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_10809_18680_1243079897}

[[接口的描述信息（如果未配置则显示"]{style="font-family:宋体"}[\--]{lang="EN-US"}]{#struct_0_10809_18680_1348820288}["）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10809_18680_x447331626}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **ip** **interface**]{lang="EN-US"}]{#struct_0_10809_18680_1766884746}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**[ **address**]{lang="EN-US"}]{#struct_0_10809_18680_306390323}

::: {#1613709608 .myid}
[]{#_Toc404786079}[]{#struct_0_10809_18680_x1129404425}[]{#_Toc130529684}

**IP地址 \-- IP地址配置命令 \-- ip address**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**[ **address**]{lang="EN-US"}]{#struct_0_10809_18680_876956094}[命令用来配置接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip** **address**]{lang="EN-US"}]{#struct_0_10809_18680_x670405365}[命令用来删除接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10809_18680_1243145433}

[**[ip]{lang="EN-US"}**[ **address** *ip-address* { *mask-length* \| *mask* } \[ **sub** \]]{lang="EN-US"}]{#struct_0_10809_18680_958326245}

[**[undo]{lang="EN-US"}**[ **ip** **address** \[ *ip-address* { *mask-length \| mask* } \[ **sub** \] \]]{lang="EN-US"}]{#struct_0_10809_18680_x2117948406}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10809_18680_1519497327}

[[没有为接口配置]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_10809_18680_x1095468739}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10809_18680_x716120406}

[[接口视图]{style="font-family:宋体"}]{#struct_0_10809_18680_1684328985}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10809_18680_x1721773388}

[[network-admin]{lang="EN-US"}]{#struct_0_10809_18680_x1569967381}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10809_18680_x1126460132}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10809_18680_1243210969}

[*[ip-address]{lang="EN-US"}*]{#struct_0_10809_18680_223429658}[：接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，为点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_10809_18680_x1503715542}[：子网掩码长度，即掩码中连续"]{style="font-family:宋体"}[1]{lang="EN-US"}["的个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[，当接口为]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口时，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_10809_18680_x1503933383}[：接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址相应的子网掩码，为点分十进制格式。]{style="font-family:宋体"}

[**[sub]{lang="EN-US"}**]{#struct_0_10809_18680_2033874234}[：表示该地址为接口的从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。为了实现一个接口下的多个子网之间能够通信，需要在接口上配置从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10809_18680_x1195231959}

[**[ip]{lang="EN-US"}**[ **address**]{lang="EN-US"}]{#struct_0_10809_18680_x156506588}[命令用来配置接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。设备的每个接口可以配置多个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，其中一个为主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，其余为从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。一般情况下，一个接口只需配置一个主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，有时为了实现一个接口下的多个子网之间能够通信，需要在接口上配置从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[当配置主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_10809_18680_401815248}[地址时，如果接口上已经有主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则新配置的地址将覆盖原有的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，成为新的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[当接口被配置为通过]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}]{#struct_0_10809_18680_222824083}[或]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[动态获取、通过]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协商分配或借用其他接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址后，不能再给该接口配置从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip** **address**]{lang="EN-US"}]{#struct_0_10809_18680_1243276505}[命令中不指定任何参数表示删除该接口的所有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **ip** **address** *ip-address* { *mask* \| *mask-length* }]{lang="EN-US"}[表示删除主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **ip** **address** *ip-address* { *mask* \| *mask-length* } **sub**]{lang="EN-US"}[表示删除指定的从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。在单独删除主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前必须先删除对应的所有从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[同一接口的主、从]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_10809_18680_x974485386}[地址可以在同一网段，但不同接口之间、主接口及其子接口之间、同一主接口下不同子接口之间的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不可以在同一网段。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10809_18680_x1991745448}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_494687923}

[[\# ]{lang="EN-US"}]{#struct_0_10809_18680_x851949859}[为接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[129.102.0.1]{lang="EN-US"}[，从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[202.38.160.1]{lang="EN-US"}[，子网掩码都为]{style="font-family:宋体"}[255.255.255.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10809_18680_1859134248}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-Ethernet1/1\] ip address 129.102.0.1 255.255.255.0]{lang="EN-US"}

[\[Sysname-Ethernet1/1\] ip address 202.38.160.1 255.255.255.0 sub]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_934040202}

[[\# ]{lang="EN-US"}]{#struct_0_10809_18680_1666414534}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[129.12.0.1]{lang="EN-US"}[，从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[202.38.160.1]{lang="EN-US"}[，子网掩码都为]{style="font-family:宋体"}[255.255.255.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10809_18680_1242817753}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ip address 129.12.0.1 255.255.255.0]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ip address 202.38.160.1 255.255.255.0 sub]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10809_18680_209648586}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **ip** **interface**]{lang="EN-US"}]{#struct_0_10809_18680_x2131973505}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **ip** **interface** **brief**]{lang="EN-US"}]{#struct_0_10809_18680_x1847095716}
:::

::::: {#-1068038803 .myid}
[]{#_Toc404786080}[]{#struct_0_10809_18680_1052836638}[]{#_Toc130529685}[]{#_Toc95362152}[]{#_Toc534082403}

**IP地址 \-- IP地址配置命令 \-- ip address unnumbered**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP地址命令.files/image001.png){#图片 1 width="62" height="27"}]{lang="EN-US"}]{#struct_0_10809_18680_878995560}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_10809_18680_x375531224}
:::

**[ ]{lang="EN-US"}**

[**[ip]{lang="EN-US"}**[ **address** **unnumbered**]{lang="EN-US"}]{#struct_0_10809_18680_x1478914621}[命令用来配置本接口借用指定接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip** **address** **unnumbered**]{lang="EN-US"}]{#struct_0_10809_18680_1242883289}[命令用来取消借用其它接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10809_18680_946523707}

[**[ip]{lang="EN-US"}**[ **address** **unnumbered** **interface** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_10809_18680_1558684116}

[**[undo]{lang="EN-US"}**[ **ip** **address** **unnumbered**]{lang="EN-US"}]{#struct_0_10809_18680_1089098339}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10809_18680_1862914715}

[[不借用其它接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_10809_18680_x636082926}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10809_18680_x1495282970}

[[接口视图]{style="font-family:宋体"}]{#struct_0_10809_18680_152090081}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10809_18680_1439445687}

[[network-admin]{lang="EN-US"}]{#struct_0_10809_18680_1242948825}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10809_18680_2127816581}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10809_18680_572210473}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_10809_18680_x1570418607}[：]{style="font-family:宋体"}[被借用接口的接口类型及接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10809_18680_x968772379}

[[所谓"]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_10809_18680_x881980772}[地址借用"，是指一个接口上没有配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，但为了使该接口能正常使用，就向同一设备上其它有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的接口借用一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址[]{#_Toc57619075}[]{#_Toc57631810}[]{#_Toc57704709}[]{#_Toc59351167}[]{#_Toc59418581}[]{#_Toc59422734}[]{#_Toc59422975}[]{#_Toc59423687}。]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_10809_18680_584402250}[地址借用的使用场景如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_10809_18680_1860258204}[IP]{lang="EN-US"}[地址资源比较匮乏的环境下，为了节约]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址资源，可以配置某个接口借用其他接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某个接口只是偶尔使用，可以配置该接口借用其他接口的]{style="font-family:宋体"}]{#struct_0_10809_18680_x1637568714}[IP]{lang="EN-US"}[地址，而不必让其一直占用一个单独的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[Loopback]{lang="EN-US"}]{#struct_0_10809_18680_302352197}[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址可被其它接口借用，但本身不能借用其它接口的地址。]{style="font-family:宋体"}

[[一个接口的地址可以借给多个接口。如果被借用接口有多个手动配置的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_10809_18680_1243014361}[地址，则只有手动配置的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址能被借用。]{style="font-family:宋体"}

[[由于借用方接口本身没有]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_10809_18680_x954633872}[地址，无法在此接口上启用动态路由协议。所以必须手动配置一条到对端网段的静态路由，才能实现设备间的连通。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10809_18680_x104753925}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_2140372204}

[[\# ]{lang="EN-US"}]{#struct_0_10809_18680_1419005308}[配置]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[借用以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10809_18680_299393782}

[\[Sysname\] interface tunnel 0 mode gre]{lang="FR"}

[\[Sysname-Tunnel0\] ip address unnumbered interface gigabitethernet 1/0/1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10809_18680_1560067964}

[[\# ]{lang="EN-US"}]{#struct_0_10809_18680_856654862}[配置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[POS2/1/1]{lang="EN-US"}[借用]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10809_18680_1243604185}

[\[Sysname\] interface pos 2/1/1]{lang="EN-US"}

[\[Sysname-Pos2/1/1\] ip address unnumbered interface vlan-interface 100]{lang="EN-US"}
:::::
