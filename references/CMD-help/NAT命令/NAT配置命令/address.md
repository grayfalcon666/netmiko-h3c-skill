::: {#-1944810517 .myid}
[]{#_Toc404786479}[]{#struct_0_83269_x5501_x218606494}[]{#_Ref311208439}[]{#_Toc185927308}[]{#_Toc123026768}

**NAT命令 \-- NAT配置命令 \-- address**

------------------------------------------------------------------------

[**[address]{lang="EN-US"}**]{#struct_0_83269_x5501_x1879393252}[命令用来添加一个地址组成员。]{style="font-family:宋体"}

[**[undo address]{lang="FR"}**]{#struct_0_83269_x5501_x1064154522}[命令用来删除一个地址组成员。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x767199070}

[**[address ]{lang="EN-US"}***[start-address end-address]{lang="EN-US"}*]{#struct_0_83269_x5501_1940516992}

[**[undo address ]{lang="EN-US"}***[start-address end-address]{lang="EN-US"}*]{#struct_0_83269_x5501_793610138}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x207898814}

[[不存在地址组成员]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1529309507}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x974773555}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x2025490630}[地址组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1503661321}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_32020544}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_876275287}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x2143136126}

[*[start-address end-address]{lang="EN-US"}*]{#struct_0_83269_x5501_131964627}[：]{style="font-family:
宋体"}[地址组成员的起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和结束]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[，如果]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[和]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*[相同，则表示只有一个地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x152900078}

[[一个]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x207964350}[地址组是多个地址组成员的集合。当需要对到达外部网络的数据报文进行地址转换时，报文的源地址将被转换为地址组成员中的某个地址。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_83269_x5501_499434544}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个地址组成员所包含的地址数目不能超过]{style="font-family:宋体"}]{#struct_0_83269_x5501_194879832}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[各地址组成员的]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1387141041}[IP]{lang="EN-US"}[地址段不能互相重叠。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在多形态防火墙设备上，配置的所有地址组成员包含的地址总数不能少于安全引擎（或安全插卡）的数量。]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1138029879}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1129122486}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1550195951}[在]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址组]{style="font-family:宋体"}[2]{lang="EN-US"}[中添加两个地址组成员。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x273228307}

[\[Sysname\] nat address-group 2]{lang="EN-US"}

[\[Sysname-address-group-2\] address 10.1.1.1 10.1.1.15]{lang="EN-US"}

[\[Sysname-address-group-2\] address 10.1.1.20 10.1.1.30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_2042715397}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat address-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x208029886}
:::

::: {#-926991832 .myid}
[]{#_Toc404786480}[]{#struct_0_83269_x5501_x443443301}[]{#_Toc363572598}

**NAT命令 \-- NAT配置命令 \-- block-size**

------------------------------------------------------------------------

[**[block-size]{lang="PT-BR"}**]{#struct_0_83269_x5501_x1490117453}[命令用来设置端口块大小。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_83269_x5501_1940419895}**[block-size]{lang="PT-BR"}**[命令用来将端口块大小恢复为默认值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x443508837}

[**[block-size]{lang="EN-US"}**[ *block-size*]{lang="EN-US"}]{#struct_0_83269_x5501_x1517373946}

[**[undo]{lang="EN-US"}**[ **block-size**]{lang="EN-US"}]{#struct_0_83269_x5501_x1080910625}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1709731479}

[[一个端口块中包含]{style="font-family:宋体"}[256]{lang="EN-US"}]{#struct_0_83269_x5501_x1338992612}[个端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_265497549}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_318361656}[端口块组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1860675474}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x1587887829}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x163588048}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x923435951}

[*[block-size]{lang="EN-US"}*]{#struct_0_83269_x5501_1346216842}[：端口块大小，即一个端口块中所包含的端口数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[。其中]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x444098661}

[[在一个端口块组中，需要根据私网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_x140724928}[地址个数，以及公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址个数及其端口范围，确定一个合理的端口块大小值。端口块大小值不能超过公网地址的端口范围值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1462583047}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1837453066}[配置端口块组]{style="font-family:宋体"}[1]{lang="EN-US"}[的端口块大小为]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x792169381}

[\[Sysname\] nat port-block-group 1]{lang="EN-US"}

[\[Sysname-port-block-group-1\] block-size 1024]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1735783386}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x1773032926}
:::

::: {#746474922 .myid}
[]{#_Toc404786481}[]{#struct_0_83269_x5501_1037175273}

**NAT命令 \-- NAT配置命令 \-- display nat all**

------------------------------------------------------------------------

[**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_906612216}[命令用来显示所有的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1390060819}

[**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_1445510773}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1269480658}

[[任意]{style="font-family:宋体"}]{#struct_0_83269_x5501_1559413011}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x2014067012}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x1255029421}

[[network-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x208095422}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_688600967}

[[mdc-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x1759565393}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x35466112}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x12157394}[显示所有的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat all]{lang="EN-US"}]{#struct_0_83269_x5501_x207767741}

[NAT address group information:]{lang="EN-US"}

[  Totally 5 NAT address groups.]{lang="EN-US"}

[  Address group 1:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.10         202.110.10.15]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 2:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.20         202.110.10.25]{lang="EN-US"}

[      202.110.10.30         202.110.10.35]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 3:]{lang="EN-US"}

[    Port range: 1024-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.40         202.110.10.50]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 4:]{lang="EN-US"}

[    Port range: 10001-65535]{lang="EN-US"}

[    Port block size: 500]{lang="EN-US"}

[    Extended block number: 1]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.60         202.110.10.65]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 6:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      \-\--                   \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT server group information:]{lang="EN-US"}

[  Totally 3 NAT server groups.]{lang="EN-US"}

[  Group Number        Inside IP             Port        Weight]{lang="EN-US"}

[  1                   192.168.0.26          23          100]{lang="EN-US"}

[                      192.168.0.27          23          500]{lang="EN-US"}

[  2                   \-\--                   \-\--         \-\--]{lang="EN-US"}

[  3                   192.168.0.26          69          100]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT inbound information:]{lang="EN-US"}

[  Totally 1 NAT inbound rules.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    ACL: 2038         Address group: 2      Add route: Y]{lang="EN-US"}

[    NO-PAT:Y         Reversible: N]{lang="EN-US"}

[    VPN instance: vpn_nat]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT outbound information:]{lang="EN-US"}

[  Totally 2 NAT outbound rules.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[    ACL: 2036         Address group: 1      Port-preserved: Y]{lang="EN-US"}

[    NO-PAT: N         Reversible: N]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: address group, and ACL.]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[    ACL: 2037         Address group: 1      Port-preserved: N]{lang="EN-US"}

[    NO-PAT: Y         Reversible: Y]{lang="EN-US"}

[    VPN instance: vpn_nat]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: ACL.]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT internal server information:]{lang="EN-US"}

[  Totally 4 internal servers.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/3]{lang="EN-US"}

[    Protocol: 6(TCP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.1/23]{lang="EN-US"}

[    Local IP/port : 192.168.10.15/23]{lang="EN-US"}

[    ACL           : 2000]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/4]{lang="EN-US"}

[    Protocol: 6(TCP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.1/23-30]{lang="EN-US"}

[    Local IP/port : 192.168.10.15-192.168.10.22/23]{lang="EN-US"}

[    Global VPN    : vpn1]{lang="EN-US"}

[    Local VPN     : vpn3]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/4]{lang="EN-US"}

[    Protocol: 255(Reserved)]{lang="EN-US"}

[    Global IP/port: 50.1.1.100/\-\--]{lang="EN-US"}

[    Local IP/port : 192.168.10.150/\-\--]{lang="EN-US"}

[    Global VPN    : vpn2]{lang="EN-US"}

[    Local VPN     : vpn4]{lang="EN-US"}

[    ACL           : 3000]{lang="EN-US"}

[    Config status : Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, and ACL.]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/5]{lang="EN-US"}

[    Protocol: 17(UDP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.2/23]{lang="EN-US"}

[    Local IP/port : server group 1]{lang="EN-US"}

[                    1.1.1.1/21            (Connections: 10)]{lang="EN-US"}

[                    192.168.100.200/80    (Connections: 20)]{lang="EN-US"}

[    Global VPN    : vpn1]{lang="EN-US"}

[    Local VPN     : vpn3]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[Static NAT mappings:]{lang="EN-US"}

[  Totally 2 inbound static NAT mappings.]{lang="EN-US"}

[  Net-to-net:]{lang="EN-US"}

[    Global IP    : 2.2.2.1 -- 2.2.2.255]{lang="EN-US"}

[    Local IP     : 1.1.1.0]{lang="EN-US"}

[    Netmask      : 255.255.255.0]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    ACL          : 3000]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IP-to-IP:]{lang="EN-US"}

[    Global IP    : 5.5.5.5]{lang="EN-US"}

[    Local IP     : 4.4.4.4]{lang="EN-US"}

[    Global VPN   : vpn3]{lang="EN-US"}

[    Local VPN    : vpn4]{lang="EN-US"}

[    ACL          : 2001]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, global VPN, and ACL.]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Totally 2 outbound static NAT mappings.]{lang="EN-US"}

[  Net-to-net:]{lang="EN-US"}

[    Local IP     : 1.1.1.1 - 1.1.1.255]{lang="EN-US"}

[    Global IP    : 2.2.2.0]{lang="EN-US"}

[    Netmask      : 255.255.255.0]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    ACL          : 3000]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IP-to-IP:]{lang="EN-US"}

[    Local IP     : 4.4.4.4]{lang="EN-US"}

[    Global IP    : 5.5.5.5]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    ACL:         : 2001]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: ACL.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interfaces enabled with static NAT:]{lang="EN-US"}

[  Totally 2 interfaces enabled with static NAT.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/3]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT DNS mappings:]{lang="EN-US"}

[  Totally 2 NAT DNS mappings.]{lang="EN-US"}

[  Domain name  : www.server.com]{lang="EN-US"}

[  Global IP    : 6.6.6.6]{lang="EN-US"}

[  Global port  : 23]{lang="EN-US"}

[  Protocol     : TCP(6)]{lang="EN-US"}

[  Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Domain name  : www.service.com]{lang="EN-US"}

[  Global IP    : \-\--]{lang="EN-US"}

[  Global port  : 12]{lang="EN-US"}

[  Protocol     : TCP(6) ]{lang="EN-US"}

[  Config status: Inactive]{lang="EN-US"}

[  Reasons for inactive status: ]{lang="EN-US"}

[    The following items don\'t exist or aren\'t effective: interface IP address.]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT logging:]{lang="EN-US"}

[  Log enable          : Enabled(ACL 2000)]{lang="EN-US"}

[  Flow-begin          : Disabled]{lang="EN-US"}

[  Flow-end            : Disabled]{lang="EN-US"}

[  Flow-active         : Enabled(10 minutes)]{lang="EN-US"}

[  Port-block-assign   : Disabled]{lang="EN-US"}

[  Port-block-withdraw : Disabled]{lang="EN-US"}

[  Alarm               : Disabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT hairpinning:]{lang="EN-US"}

[  Totally 2 interfaces enabled with NAT hairpinning.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT mapping behavior:]{lang="EN-US"}

[  Mapping mode : ]{lang="EN-US"}[Endpoint-Independent]{lang="EN-US"}

[  ACL          : 2050]{lang="EN-US"}

[  Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT ALG:]{lang="EN-US"}

[  DNS        : Enabled]{lang="EN-US"}

[  FTP        : Disabled]{lang="EN-US"}

[  H323       : Enabled]{lang="EN-US"}

[  ICMP-ERROR : Enabled]{lang="EN-US"}

[  ILS        : Enabled]{lang="EN-US"}

[  MGCP       : Enabled]{lang="EN-US"}

[  NBT        : Enabled]{lang="EN-US"}

[  PPTP       : Enabled]{lang="EN-US"}

[  RSH        : Enabled]{lang="EN-US"}

[  RTSP       : Enabled]{lang="EN-US"}

[  SCCP       : Enabled]{lang="EN-US"}

[  SIP        : Disabled]{lang="EN-US"}

[  SQLNET     : Enabled]{lang="EN-US"}

[  TFTP       : Enabled]{lang="EN-US"}

[  XDMCP      : Enabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT port block group information:]{lang="EN-US"}

[  Totally 3 NAT port block groups.]{lang="EN-US"}

[  Port block group 1:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Block size: 256]{lang="EN-US"}

[    Local IP address information:]{lang="EN-US"}

[      Start address        End address          VPN instance]{lang="EN-US"}

[      172.16.1.1           172.16.1.254         \-\--]{lang="EN-US"}

[      192.168.1.1          192.168.1.254        vpna]{lang="EN-US"}

[      192.168.3.1          192.168.3.254        vpna]{lang="EN-US"}

[    Global IP pool information:]{lang="EN-US"}

[      Start address        End address]{lang="EN-US"}

[      201.1.1.1            201.1.1.10]{lang="EN-US"}

[      201.1.1.21           201.1.1.25]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Port block group 2:]{lang="EN-US"}

[    Port range: 10001-30000]{lang="EN-US"}

[    Block size: 500]{lang="EN-US"}

[    Local IP address information:]{lang="EN-US"}

[      Start address        End address          VPN instance]{lang="EN-US"}

[      10.1.1.1             10.1.10.255          vpnb]{lang="EN-US"}

[    Global IP pool information:]{lang="EN-US"}

[      Start address        End address]{lang="EN-US"}

[      202.10.10.101        202.10.10.120]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Port block group 3:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Block size: 256]{lang="EN-US"}

[    Local IP address information:]{lang="EN-US"}

[      Start address        End address          VPN instance]{lang="EN-US"}

[      \-\--                  \-\--                  \-\--]{lang="EN-US"}

[    Global IP pool information:]{lang="EN-US"}

[      Start address        End address]{lang="EN-US"}

[      \-\--                  \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT outbound port block group information:]{lang="EN-US"}

[  Totally 2 outbound port block group items.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    Port block group: 2]{lang="EN-US"}

[    Config status   : Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    Port block group: 10]{lang="EN-US"}

[    Config status   : Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: port block group.]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x489517068}[显示所有的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置信息。（分布式设备]{style="font-family:宋体"}[－]{style="font-size:10.0pt;
font-family:宋体;color:black"}[独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat all]{lang="EN-US"}]{#struct_0_83269_x5501_x892867131}

[NAT address group information:]{lang="EN-US"}

[  Totally 5 NAT address groups.]{lang="EN-US"}

[  Address group 1:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.10         202.110.10.15]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 2:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.20         202.110.10.25]{lang="EN-US"}

[      202.110.10.30         202.110.10.35]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 3:]{lang="EN-US"}

[    Port range: 1024-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.40         202.110.10.50]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 4:]{lang="EN-US"}

[    Port range: 10001-65535]{lang="EN-US"}

[    Port block size: 500]{lang="EN-US"}

[    Extended block number: 1]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.60         202.110.10.65]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 6:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      \-\--                   \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT server group information:]{lang="EN-US"}

[  Totally 3 NAT server groups.]{lang="EN-US"}

[  Group Number        Inside IP             Port        Weight]{lang="EN-US"}

[  1                   192.168.0.26          23          100]{lang="EN-US"}

[                      192.168.0.27          23          500]{lang="EN-US"}

[  2                   \-\--                   \-\--         \-\--]{lang="EN-US"}

[  3                   192.168.0.26          69          100]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT inbound information:]{lang="EN-US"}

[  Totally 1 NAT inbound rules.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[    ACL: 2038         Address group: 2      Add route: Y]{lang="EN-US"}

[    NO-PAT: Y         Reversible: N]{lang="EN-US"}

[    VPN instance: vpn_nat]{lang="EN-US"}

[    Service card: Slot 2]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT outbound information:]{lang="EN-US"}

[  Totally 2 NAT outbound rules.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    ACL: 2036         Address group: 1      Port-preserved: Y]{lang="EN-US"}

[    NO-PAT: N         Reversible: N]{lang="EN-US"}

[    Service card: \-\--]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: address group, and ACL.]{lang="EN-US"}

[      Service card not specified. ]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    ACL: 2037         Address group: 1      Port-preserved: N]{lang="EN-US"}

[    NO-PAT: Y         Reversible: Y]{lang="EN-US"}

[    VPN instance: vpn_nat]{lang="EN-US"}

[    Service card: \-\--]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      Service card not specified. ]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT internal server information:]{lang="EN-US"}

[  Totally 4 internal servers.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/3]{lang="EN-US"}

[    Protocol: 6(TCP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.1/23]{lang="EN-US"}

[    Local IP/port : 192.168.10.15/23]{lang="EN-US"}

[    ACL           : 2000]{lang="EN-US"}

[    Service card  : Slot 2]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/4]{lang="EN-US"}

[    Protocol: 6(TCP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.1/23-30]{lang="EN-US"}

[    Local IP/port : 192.168.10.15-192.168.10.22/23]{lang="EN-US"}

[    Global VPN    : vpn1]{lang="EN-US"}

[    Local VPN     : vpn3]{lang="EN-US"}

[    Service card  : Slot 2]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/4]{lang="EN-US"}

[    Protocol: 255(Reserved)]{lang="EN-US"}

[    Global IP/port: 50.1.1.100/\-\--]{lang="EN-US"}

[    Local IP/port : 192.168.10.150/\-\--]{lang="EN-US"}

[    Global VPN    : vpn2]{lang="EN-US"}

[    Local VPN     : vpn4]{lang="EN-US"}

[    ACL           : 3000]{lang="EN-US"}

[    Service card  : Slot 2]{lang="EN-US"}

[    Config status : Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, and ACL.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/5]{lang="EN-US"}

[    Protocol: 17(UDP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.2/23]{lang="EN-US"}

[    Local IP/port : server group 1]{lang="EN-US"}

[                    192.168.0.26/23       (Connections: 10)]{lang="EN-US"}

[                    192.168.0.27/23       (Connections: 20)]{lang="EN-US"}

[    Global VPN    : vpn1]{lang="EN-US"}

[    Local VPN     : vpn3]{lang="EN-US"}

[    Service card  : Slot 2]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[Static NAT mappings:]{lang="EN-US"}

[  Totally 2 inbound static NAT mappings.]{lang="EN-US"}

[  Net-to-net:]{lang="EN-US"}

[    Global IP    : 2.2.2.1 -- 2.2.2.255]{lang="EN-US"}

[    Local IP     : 1.1.1.0]{lang="EN-US"}

[    Netmask      : 255.255.255.0]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    ACL          : 2000]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IP-to-IP:]{lang="EN-US"}

[    Global IP    : 5.5.5.5]{lang="EN-US"}

[    Local IP     : 4.4.4.4]{lang="EN-US"}

[    Global VPN   : vpn3]{lang="EN-US"}

[    Local VPN    : vpn4]{lang="EN-US"}

[    ACL          : 2001]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, global VPN, and ACL.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Totally 2 outbound static NAT mappings.]{lang="EN-US"}

[  Net-to-net:]{lang="EN-US"}

[    Local IP     : 1.1.1.1 - 1.1.1.255]{lang="EN-US"}

[    Global IP    : 2.2.2.0]{lang="EN-US"}

[    Netmask      : 255.255.255.0]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    ACL          : 2000]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IP-to-IP:]{lang="EN-US"}

[    Local IP     : 4.4.4.4]{lang="EN-US"}

[    Global IP    : 5.5.5.5]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    ACL:         : 2001]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: ACL.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interfaces enabled with static NAT:]{lang="EN-US"}

[  Totally 2 interfaces enabled with static NAT.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/4]{lang="EN-US"}

[    Service card : Slot 2]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/6]{lang="EN-US"}

[    Service card : \-\--]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      Service card not specified.]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT DNS mappings:]{lang="EN-US"}

[  Totally 2 NAT DNS mappings.]{lang="EN-US"}

[  Domain name  : www.server.com]{lang="EN-US"}

[  Global IP    : 6.6.6.6]{lang="EN-US"}

[  Global port  : 23]{lang="EN-US"}

[  Protocol     : TCP(6)]{lang="EN-US"}

[  Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Domain name  : www.service.com]{lang="EN-US"}

[  Global IP    : \-\--]{lang="EN-US"}

[  Global port  : 12]{lang="EN-US"}

[  Protocol     : TCP(6) ]{lang="EN-US"}

[  Config status: Inactive]{lang="EN-US"}

[  Reasons for inactive status: ]{lang="EN-US"}

[    The following items don\'t exist or aren\'t effective: interface IP address.]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT logging:]{lang="EN-US"}

[  Log enable          : Enabled(ACL 2000)]{lang="EN-US"}

[  Flow-begin          : Disabled]{lang="EN-US"}

[  Flow-end            : Disabled]{lang="EN-US"}

[  Flow-active         : Enabled(10 minutes)]{lang="EN-US"}

[  Port-block-assign   : Disabled]{lang="EN-US"}

[  Port-block-withdraw : Disabled]{lang="EN-US"}

[  Alarm               : Disabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT hairpinning:]{lang="EN-US"}

[  Totally 2 interfaces enabled with NAT hairpinning.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/4]{lang="EN-US"}

[    Service card : Slot 2]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/6]{lang="EN-US"}

[    Service card : Slot 2]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT mapping behavior:]{lang="EN-US"}

[  Mapping mode : ]{lang="EN-US"}[Endpoint-Independent]{lang="EN-US"}

[  ACL          : 2050]{lang="EN-US"}

[  Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT ALG:]{lang="EN-US"}

[  DNS        : Enabled]{lang="EN-US"}

[  FTP        : Enabled]{lang="EN-US"}

[  H323       : Enabled]{lang="EN-US"}

[  ICMP-ERROR : Enabled]{lang="EN-US"}

[  ILS        : Enabled]{lang="EN-US"}

[  MGCP       : Enabled]{lang="EN-US"}

[  NBT        : Enabled]{lang="EN-US"}

[  PPTP       : Enabled]{lang="EN-US"}

[  RTSP       : Enabled]{lang="EN-US"}

[  RSH        : Enabled]{lang="EN-US"}

[  SCCP       : Enabled]{lang="EN-US"}

[  SIP        : Enabled]{lang="EN-US"}

[  SQLNET     : Enabled]{lang="EN-US"}

[  TFTP       : Enabled]{lang="EN-US"}

[  XDMCP      : Disabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT port block group information:]{lang="EN-US"}

[  Totally 3 NAT port block groups.]{lang="EN-US"}

[  Port block group 1:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Block size: 256]{lang="EN-US"}

[    Local IP address information:]{lang="EN-US"}

[      Start address        End address          VPN instance]{lang="EN-US"}

[      172.16.1.1           172.16.1.254         \-\--]{lang="EN-US"}

[      192.168.1.1          192.168.1.254        vpna]{lang="EN-US"}

[      192.168.3.1          192.168.3.254        vpna]{lang="EN-US"}

[    Global IP pool information:]{lang="EN-US"}

[      Start address        End address]{lang="EN-US"}

[      201.1.1.1            201.1.1.10]{lang="EN-US"}

[      201.1.1.21           201.1.1.25]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Port block group 2:]{lang="EN-US"}

[    Port range: 10001-30000]{lang="EN-US"}

[    Block size: 500]{lang="EN-US"}

[    Local IP address information:]{lang="EN-US"}

[      Start address        End address          VPN instance]{lang="EN-US"}

[      10.1.1.1             10.1.10.255          vpnb]{lang="EN-US"}

[    Global IP pool information:]{lang="EN-US"}

[      Start address        End address]{lang="EN-US"}

[      202.10.10.101        202.10.10.120]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Port block group 3:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Block size: 256]{lang="EN-US"}

[    Local IP address information:]{lang="EN-US"}

[      Start address        End address          VPN instance]{lang="EN-US"}

[      \-\--                  \-\--                  \-\--]{lang="EN-US"}

[    Global IP pool information:]{lang="EN-US"}

[      Start address        End address]{lang="EN-US"}

[      \-\--                  \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT outbound port block group information:]{lang="EN-US"}

[  ]{lang="EN-US"}[Totally]{lang="EN-US"}[ 2 outbound port block group items.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    Port block group: 2]{lang="EN-US"}

[    Config status   : Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    Port block group: 10]{lang="EN-US"}

[    Config status   : Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: port block group.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_542612293}[显示所有的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置信息。（分布式设备]{style="font-family:宋体"}[－]{style="font-size:10.0pt;
font-family:宋体;color:black"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display nat all]{lang="EN-US"}]{#struct_0_83269_x5501_x1296217194}

[NAT address group information:]{lang="EN-US"}

[  Totally 5 NAT address groups.]{lang="EN-US"}

[  Address group 1:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.10         202.110.10.15]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 2:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.20         202.110.10.25]{lang="EN-US"}

[      202.110.10.30         202.110.10.35]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 3:]{lang="EN-US"}

[    Port range: 1024-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.40         202.110.10.50]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 4:]{lang="EN-US"}

[    Port range: 10001-65535]{lang="EN-US"}

[    Port block size: 500]{lang="EN-US"}

[    Extended block number: 1]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.60         202.110.10.65]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 6:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      \-\--                   \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT server group information:]{lang="EN-US"}

[  Totally 3 NAT server groups.]{lang="EN-US"}

[  Group Number        Inside IP             Port        Weight]{lang="EN-US"}

[  1                   192.168.0.26          23          100]{lang="EN-US"}

[                      192.168.0.27          23          500]{lang="EN-US"}

[  2                   \-\--                   \-\--         \-\--]{lang="EN-US"}

[  3                   192.168.0.26          69          100]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT inbound information:]{lang="EN-US"}

[  Totally 1 NAT inbound rules.]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/1]{lang="EN-US"}

[    ACL: 2038         Address group: 2      Add route: Y]{lang="EN-US"}

[    NO-PAT: Y         Reversible: N]{lang="EN-US"}

[    VPN instance: vpn_nat]{lang="EN-US"}

[    Service card: Chassis 2 Slot 5]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT outbound information:]{lang="EN-US"}

[  Totally 2 NAT outbound rules.]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/2]{lang="EN-US"}

[    ACL: 2036         Address group: 1      Port-preserved: Y]{lang="EN-US"}

[    NO-PAT: N         Reversible: N]{lang="EN-US"}

[    Service card: \-\--]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      Service card not specified.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/2]{lang="EN-US"}

[    ACL: 2037         Address group: 1      Port-preserved: N]{lang="EN-US"}

[    NO-PAT: Y         Reversible: Y]{lang="EN-US"}

[    VPN instance: vpn_nat]{lang="EN-US"}

[    Service card: \-\--]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      Service card not specified.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT internal server information:]{lang="EN-US"}

[  Totally 4 internal servers.]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/3]{lang="EN-US"}

[    Protocol: 6(TCP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.1/23]{lang="EN-US"}

[    Local IP/port : 192.168.10.15/23]{lang="EN-US"}

[    ACL           : 2000]{lang="EN-US"}

[    Service card  : Chassis 2 Slot 5]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/4]{lang="EN-US"}

[    Protocol: 6(TCP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.1/23-30]{lang="EN-US"}

[    Local IP/port : 192.168.10.15-192.168.10.22/23]{lang="EN-US"}

[    Global VPN    : vpn1]{lang="EN-US"}

[    Local VPN     : vpn3]{lang="EN-US"}

[    Service card  : Chassis 2 Slot 5]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/4]{lang="EN-US"}

[    Protocol: 255(Reserved)]{lang="EN-US"}

[    Global IP/port: 50.1.1.100/\-\--]{lang="EN-US"}

[    Local IP/port : 192.168.10.150/\-\--]{lang="EN-US"}

[    Global VPN    : vpn2]{lang="EN-US"}

[    Local VPN     : vpn4]{lang="EN-US"}

[    ACL           : 3000]{lang="EN-US"}

[    Service card  : Chassis 2 Slot 5]{lang="EN-US"}

[    Config status : Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, and ACL.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/5]{lang="EN-US"}

[    Protocol: 17(UDP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.2/23]{lang="EN-US"}

[    Local IP/port : server group 1]{lang="EN-US"}

[                    192.168.0.26/23       (Connections: 10)]{lang="EN-US"}

[                    192.168.0.27/23       (Connections: 20)]{lang="EN-US"}

[    Global VPN    : vpn1]{lang="EN-US"}

[    Local VPN     : vpn3]{lang="EN-US"}

[    Service card  : Chassis 2 Slot 5]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[Static NAT mappings:]{lang="EN-US"}

[  Totally 2 inbound static NAT mappings.]{lang="EN-US"}

[  Net-to-net:]{lang="EN-US"}

[    Global IP : 2.2.2.1 -- 2.2.2.255]{lang="EN-US"}

[    Local IP  : 1.1.1.0]{lang="EN-US"}

[    Netmask   : 255.255.255.0]{lang="EN-US"}

[    Global VPN: vpn2]{lang="EN-US"}

[    Local VPN : vpn1]{lang="EN-US"}

[    ACL       : 2000]{lang="EN-US"}

[    Reversible: Y]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IP-to-IP:]{lang="EN-US"}

[    Global IP : 5.5.5.5]{lang="EN-US"}

[    Local IP  : 4.4.4.4]{lang="EN-US"}

[    Global VPN: vpn3]{lang="EN-US"}

[    Local VPN : vpn4]{lang="EN-US"}

[    ACL       : 2001]{lang="EN-US"}

[    Reversible: Y]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, global VPN, and ACL.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Totally 2 outbound static NAT mappings.]{lang="EN-US"}

[  Net-to-net:]{lang="EN-US"}

[    Local IP  : 1.1.1.1 - 1.1.1.255]{lang="EN-US"}

[    Global IP : 2.2.2.0]{lang="EN-US"}

[    Netmask   : 255.255.255.0]{lang="EN-US"}

[    Local VPN : vpn1]{lang="EN-US"}

[    Global VPN: vpn2]{lang="EN-US"}

[    ACL       : 2000]{lang="EN-US"}

[    Reversible: Y]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IP-to-IP:]{lang="EN-US"}

[    Local IP  : 4.4.4.4]{lang="EN-US"}

[    Global IP : 5.5.5.5]{lang="EN-US"}

[    Local VPN : vpn1]{lang="EN-US"}

[    Global VPN: vpn2]{lang="EN-US"}

[    ACL:      : 2001]{lang="EN-US"}

[    Reversible: Y]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: ACL.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interfaces enabled with static NAT:]{lang="EN-US"}

[  Totally 2 interfaces enabled with static NAT.]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/4]{lang="EN-US"}

[    Service card : Chassis 2 Slot 5]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/6]{lang="EN-US"}

[    Service card : \-\--]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      Service card not specified.]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT DNS mappings:]{lang="EN-US"}

[  Totally 2 NAT DNS mappings.]{lang="EN-US"}

[  Domain name  : www.server.com]{lang="EN-US"}

[  Global IP    : 6.6.6.6]{lang="EN-US"}

[  Global port  : 23]{lang="EN-US"}

[  Protocol     : TCP(6)]{lang="EN-US"}

[  Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Domain name  : www.service.com]{lang="EN-US"}

[  Global IP    : \-\--]{lang="EN-US"}

[  Global port  : 12]{lang="EN-US"}

[  Protocol     : TCP(6) ]{lang="EN-US"}

[  Config status: Inactive]{lang="EN-US"}

[  Reasons for inactive status: ]{lang="EN-US"}

[    The following items don\'t exist or aren\'t effective: interface IP address.]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT logging:]{lang="EN-US"}

[  Log enable          : Enabled(ACL 2000)]{lang="EN-US"}

[  Flow-begin          : Disabled]{lang="EN-US"}

[  Flow-end            : Disabled]{lang="EN-US"}

[  Flow-active         : Enabled(10 minutes)]{lang="EN-US"}

[  Port-block-assign   : Disabled]{lang="EN-US"}

[  Port-block-withdraw : Disabled]{lang="EN-US"}

[  Alarm               : Disabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT hairpinning:]{lang="EN-US"}

[  Totally 2 interfaces enabled with NAT hairpinning.]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/1]{lang="EN-US"}

[    Service card : Chassis 2 Slot 5]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/2]{lang="EN-US"}

[    Service card : Chassis 2 Slot 5]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT mapping behavior:]{lang="EN-US"}

[  Mapping mode : ]{lang="EN-US"}[Endpoint-Independent]{lang="EN-US"}

[  ACL          : 2050]{lang="EN-US"}

[  Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT ALG:]{lang="EN-US"}

[  DNS        : Enabled]{lang="EN-US"}

[  FTP        : Enabled]{lang="EN-US"}

[  H323       : Enabled]{lang="EN-US"}

[  ICMP-ERROR : Enabled]{lang="EN-US"}

[  ILS        : Enabled]{lang="EN-US"}

[  MGCP       : Enabled]{lang="EN-US"}

[  NBT        : Enabled]{lang="EN-US"}

[  PPTP       : Enabled]{lang="EN-US"}

[  RTSP       : Enabled]{lang="EN-US"}

[  RSH        : Enabled]{lang="EN-US"}

[  SCCP       : Enabled]{lang="EN-US"}

[  SIP        : Enabled]{lang="EN-US"}

[  SQLNET     : Enabled]{lang="EN-US"}

[  TFTP       : Enabled]{lang="EN-US"}

[  XDMCP      : Disabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT port block group information:]{lang="EN-US"}

[  Totally 3 NAT port block groups.]{lang="EN-US"}

[  Port block group 1:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Block size: 256]{lang="EN-US"}

[    Local IP address information:]{lang="EN-US"}

[      Start address        End address          VPN instance]{lang="EN-US"}

[      172.16.1.1           172.16.1.254         \-\--]{lang="EN-US"}

[      192.168.1.1          192.168.1.254        vpna]{lang="EN-US"}

[      192.168.3.1          192.168.3.254        vpna]{lang="EN-US"}

[    Global IP pool information:]{lang="EN-US"}

[      Start address        End address]{lang="EN-US"}

[      201.1.1.1            201.1.1.10]{lang="EN-US"}

[      201.1.1.21           201.1.1.25]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Port block group 2:]{lang="EN-US"}

[    Port range: 10001-30000]{lang="EN-US"}

[    Block size: 500]{lang="EN-US"}

[    Local IP address information:]{lang="EN-US"}

[      Start address        End address          VPN instance]{lang="EN-US"}

[      10.1.1.1             10.1.10.255          vpnb]{lang="EN-US"}

[    Global IP pool information:]{lang="EN-US"}

[      Start address        End address]{lang="EN-US"}

[      202.10.10.101        202.10.10.120]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Port block group 3:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Block size: 256]{lang="EN-US"}

[    Local IP address information:]{lang="EN-US"}

[      Start address        End address          VPN instance]{lang="EN-US"}

[      \-\--                  \-\--                  \-\--]{lang="EN-US"}

[    Global IP pool information:]{lang="EN-US"}

[      Start address        End address]{lang="EN-US"}

[      \-\--                  \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[NAT outbound port block group information:]{lang="EN-US"}

[  ]{lang="EN-US"}[Totally]{lang="EN-US"}[ 2 outbound port block group items.]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/2]{lang="EN-US"}

[    Port block group: 2]{lang="EN-US"}

[    Config status   : Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/2]{lang="EN-US"}

[    Port block group: 10]{lang="EN-US"}

[    Config status   : Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: port block group.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[[上述显示信息是目前所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_1300778834}[配置信息的集合。由于部分]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置（]{style="font-family:宋体"}**[nat address-group]{lang="EN-US"}**[、]{style="font-family:宋体"}**[nat server-group]{lang="EN-US"}**[、]{style="font-family:宋体"}**[nat inbound]{lang="EN-US"}**[、]{style="font-family:宋体"}**[nat outbound]{lang="EN-US"}**[、]{style="font-family:宋体"}**[nat server]{lang="EN-US"}**[、]{style="font-family:宋体"}**[nat static]{lang="EN-US"}**[、]{style="font-family:宋体"}**[nat static net-to-net]{lang="EN-US"}**[、]{style="font-family:宋体"}**[nat static enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[nat dns-map]{lang="EN-US"}**[、]{style="font-family:宋体"}**[nat log]{lang="EN-US"}**[、]{style="font-family:宋体"}**[nat port-block-group]{lang="EN-US"}**[和]{style="font-family:宋体"}**[nat outbound port-block-group]{lang="EN-US"}**[）有自己独立的显示命令，且此处显示信息的格式与各命令对应的显示信息的格式相同的，所以此处不对这些配置的显示字段的含义进行写详细解释，如有需要，请参考各独立的显示命令。下面的表格将给出相关显示命令的参见信息并仅解释]{style="font-family:宋体"}**[nat hairpin enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[nat mapping-behavior]{lang="EN-US"}**[和]{style="font-family:宋体"}**[nat alg]{lang="EN-US"}**[配置的显示字段的含义。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[display nat all]{lang="EN-US"}]{#struct_0_83269_x5501_x2072852380}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x793727168}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_1357865264}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_291429640}

[[NAT address group information]{lang="EN-US"}]{#struct_0_83269_x5501_x769465960}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_85944400}[地址组的配置信息，详细字段解释请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-2]{lang="EN-US"}](?212897139#_Ref332718363)["]{style="font-family:宋体"}

[[NAT server group information]{lang="EN-US"}]{#struct_0_83269_x5501_x207833277}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_2085125448}[内部服务器组的配置信息，详细字段解释请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-13]{lang="EN-US"}](?-2052594180#_Ref334106521)["]{style="font-family:
  宋体"}

[[NAT inbound information:]{lang="EN-US"}]{#struct_0_83269_x5501_552710547}

[[入方向动态地址转换的配置信息，详细字段解释请参见"]{style="font-family:宋体"}]{#struct_0_83269_x5501_x100219672}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-5]{lang="EN-US"}](?-1724764660#_Ref334104209)["]{style="font-family:
  宋体"}

[[NAT outbound information]{lang="EN-US"}]{#struct_0_83269_x5501_1176635948}

[[出方向动态地址转换的配置信息，详细字段解释请参见"]{style="font-family:宋体"}]{#struct_0_83269_x5501_908563090}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-8]{lang="EN-US"}](?-1864024100#_Ref334105167)["]{style="font-family:
  宋体"}

[[NAT internal server information]{lang="EN-US"}]{#struct_0_83269_x5501_x207898813}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1529637187}[内部服务器的配置信息，详细字段解释请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-12]{lang="EN-US"}](?-347761546#_Ref334105524)["]{style="font-family:
  宋体"}

[[Static NAT mappings]{lang="EN-US"}]{#struct_0_83269_x5501_x26631278}

[[静态地址转换的配置信息，详细字段解释请参见"]{style="font-family:宋体"}]{#struct_0_83269_x5501_x379319775}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-15]{lang="EN-US"}](?1118470241#_Ref334167313)["]{style="font-family:
  宋体"}

[[NAT DNS mappings]{lang="EN-US"}]{#struct_0_83269_x5501_226617522}

[[NAT DNS mapping]{lang="EN-US"}]{#struct_0_83269_x5501_404721135}[的配置信息，详细字段解释请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-3]{lang="EN-US"}](?-891847204#_Ref334101543)["]{style="font-family:
  宋体"}

[[NAT logging]{lang="EN-US"}]{#struct_0_83269_x5501_x207964349}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_499893295}[日志功能的配置信息，详细字段解释请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-6]{lang="EN-US"}](?-463444198#_Ref334104166)["]{style="font-family:宋体"}

[[NAT hairpinning]{lang="EN-US"}]{#struct_0_83269_x5501_x879601370}

[[NAT hairpin]{lang="EN-US"}]{#struct_0_83269_x5501_x2092790233}[功能]{style="font-family:宋体"}

[[Totally *n* interfaces enabled NAT hairpinning]{lang="EN-US"}]{#struct_0_83269_x5501_x208029885}

[[当前有]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_83269_x5501_1037240809}[个接口使能]{style="font-family:宋体"}[NAT hairpin]{lang="EN-US"}[功能]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_83269_x5501_x710273699}

[[使能]{style="font-family:宋体"}[NAT hairpin]{lang="EN-US"}]{#struct_0_83269_x5501_x641043422}[功能的接口]{style="font-family:宋体"}

[[Service card]{lang="EN-US"}]{#struct_0_83269_x5501_x892932667}

[[显示提供]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_673151274}[处理的业务板。如果接口下没有指定业务板，则显示为"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x2055732081}

[[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_x1296515783}

[[显示]{style="font-family:宋体"}[NAT hairpin]{lang="EN-US"}]{#struct_0_83269_x5501_1076435801}[配置的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_x1224043948}[：生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x939986834}[：不生效]{style="font-family:宋体"}

[[Reasons for inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_626097107}

[[当]{style="font-family:宋体"}[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_x1161999466}[字段为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}[时，显示]{style="font-family:宋体"}[NAT hairpin]{lang="EN-US"}[配置不生效的原因]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service card not specified]{lang="EN-US"}]{#struct_0_83269_x5501_x1838301635}[：没有指定]{style="font-family:
  宋体"}[提供]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[处理的]{lang="EN-US" style="font-family:宋体"}[业务板]{style="font-family:宋体"}

[[NAT mapping behavior]{lang="EN-US"}]{#struct_0_83269_x5501_55876560}

[[PAT]{lang="EN-US"}]{#struct_0_83269_x5501_x208095421}[方式下的地址转换模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Endpoint-Independent]{lang="EN-US"}]{#struct_0_83269_x5501_688797575}[：表示不关心对端地址和端口]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Address and Port-Dependent]{lang="EN-US"}]{#struct_0_83269_x5501_1357750686}[：表示关心对端地址和端口]{lang="EN-US" style="font-family:宋体"}

[[ACL]{lang="EN-US"}]{#struct_0_83269_x5501_284107944}

[[引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_83269_x5501_x208160957}[编号。如果没有配置，则显示"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_x758714939}

[[显示]{style="font-family:宋体"}]{#struct_0_83269_x5501_807369002}[NAT mapping behavior]{lang="EN-US"}[配置的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_x1921514353}[：生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x1142920398}[：不生效]{style="font-family:宋体"}

[[Reasons for inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_x355430412}

[[当]{style="font-family:宋体"}[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_1210653529}[字段为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}[时，显示]{style="font-family:宋体"}[NAT mapping behavior]{lang="EN-US"}[配置不生效的原因]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The following items don\'t exist or aren\'t effective: ACL]{lang="EN-US"}]{#struct_0_83269_x5501_x805769106}[：引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在]{style="font-family:宋体"}

[[Global flow-table status]{lang="EN-US"}]{#struct_0_83269_x5501_x1645155995}

[[针对]{style="font-family:宋体"}[Global]{lang="EN-US"}]{#struct_0_83269_x5501_x1265513235}[地址下发流表的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_x44650929}[：生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x1422906709}[：不生效]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1645090459}

[[Local  flow-table status]{lang="EN-US"}]{#struct_0_83269_x5501_560714480}

[[针对]{style="font-family:宋体"}[Local]{lang="EN-US"}]{#struct_0_83269_x5501_179168562}[地址下发流表的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_x1607682503}[：生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x1644238491}[：不生效]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x132481531}

[[Reasons for flow-table inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_x637964807}

[[当下发流表的状态为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_852103307}[时，显示流表不生效的原因]{style="font-family:宋体"}

[[其中，]{style="font-family:宋体"}[Not enough resources are available to complete the operation]{lang="EN-US"}]{#struct_0_83269_x5501_x943281346}[表示因为资源不足导致下发流表失败]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1644172955}

[[NAT ALG]{lang="EN-US"}]{#struct_0_83269_x5501_281473244}

[[各协议的]{style="font-family:宋体"}[NAT ALG]{lang="EN-US"}]{#struct_0_83269_x5501_1392381779}[功能开启信息]{style="font-family:宋体"}

[[NAT port block group information]{lang="EN-US"}]{#struct_0_83269_x5501_1122575107}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_1961022828}[端口块组的配置信息，详细字段解释请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-11]{lang="EN-US"}](?-367314176#_Ref363572644)["]{style="font-family:
  宋体"}

[[NAT outbound port block group information]{lang="EN-US"}]{#struct_0_83269_x5501_1121985283}

[[NAT444]{lang="EN-US"}]{#struct_0_83269_x5501_514708720}[端口块静态映射的配置信息，详细字段解释请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-9]{lang="EN-US"}](?1628387509#_Ref363572645)["]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#212897139 .myid}
[]{#_Toc404786482}[]{#struct_0_83269_x5501_x1856248780}

**NAT命令 \-- NAT配置命令 \-- display nat address-group**

------------------------------------------------------------------------

[**[display nat address-group]{lang="EN-US"}**]{#struct_0_83269_x5501_399056549}[命令用来显示]{style="font-family:
宋体"}[NAT]{lang="EN-US"}[地址组配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1865699750}

[**[display nat address-group]{lang="EN-US"}**[ \[ *group-number* \]]{lang="EN-US"}]{#struct_0_83269_x5501_529609501}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x208226493}

[[任意]{style="font-family:宋体"}]{#struct_0_83269_x5501_1115478509}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_640330105}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x1348371872}

[[network-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x527782283}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1021110968}

[[mdc-operator]{lang="EN-US" style="color:black"}*[ ]{lang="EN-US" style="color:blue"}*]{#struct_0_83269_x5501_380646339}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_735618888}

[*[group-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x207243453}**[：]{style="font-family:宋体"}**[地址组编号，取值范围为[0]{lang="EN-US"}～]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[。其中]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。如果不设置该值，则显示所有地址组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1691974688}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1327245817}[显示所有地址组的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display nat address-group]{lang="EN-US"}]{#struct_0_83269_x5501_x1946692016}

[NAT address group information:]{lang="EN-US"}

[  Totally 5 NAT address groups.]{lang="EN-US"}

[  Address group 1:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.10         202.110.10.15]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 2:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.20         202.110.10.25]{lang="EN-US"}

[      202.110.10.30         202.110.10.35]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 3:]{lang="EN-US"}

[    Port range: 1024-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.40         202.110.10.50]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 4:]{lang="EN-US"}

[    Port range: 10001-65535]{lang="EN-US"}

[    Port block size: 500]{lang="EN-US"}

[    Extended block number: 1]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.60         202.110.10.65]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Address group 6:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      \-\--                   \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_379768399}[显示指定地址组的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display nat address-group 1]{lang="EN-US"}]{#struct_0_83269_x5501_x424742252}

[  Address group 1:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Address information:]{lang="EN-US"}

[      Start address         End address]{lang="EN-US"}

[      202.110.10.10         202.110.10.15]{lang="EN-US"}

[ ]{lang="EN-US"}

[]{#struct_0_83269_x5501_x207308989}[[表1-2 ]{lang="EN-US"}[display nat address-group]{lang="EN-US"}]{#_Ref332718363}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x805269389}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_445486561}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_67946400}

[[NAT address group information]{lang="EN-US"}]{#struct_0_83269_x5501_x868726779}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_885644552}[地址组信息]{style="font-family:宋体"}

[[Totally *n* NAT ]{lang="FR"}[address ]{lang="EN-US"}]{#struct_0_83269_x5501_x463997139}[groups]{lang="FR"}

[[当前有]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1061203483}*[n]{lang="FR"}*[个地址组]{style="font-family:宋体"}

[[Address group]{lang="EN-US"}]{#struct_0_83269_x5501_1358316203}

[[地址组编号]{style="font-family:宋体"}]{#struct_0_83269_x5501_1660447122}

[[Port range]{lang="EN-US"}]{#struct_0_83269_x5501_1122378500}

[[地址的端口范围]{style="font-family:宋体"}]{#struct_0_83269_x5501_1149753563}

[[Block size]{lang="EN-US"}]{#struct_0_83269_x5501_x686633248}

[[端口块大小。如果没有配置，则不显示]{style="font-family:宋体"}]{#struct_0_83269_x5501_1122312964}

[[Extended block number]{lang="EN-US"}]{#struct_0_83269_x5501_1196236087}

[[增量端口块数。]{style="font-family:宋体"}]{#struct_0_83269_x5501_772162077}[如果没有配置，则不显示]{style="font-family:宋体"}

[[Address information]{lang="EN-US"}]{#struct_0_83269_x5501_1122771716}

[[地址组成员信息]{style="font-family:宋体"}]{#struct_0_83269_x5501_x390617061}

[[Start address]{lang="EN-US"}]{#struct_0_83269_x5501_x1845853306}

[[地址组成员的起始地址。如果没有配置，则显示]{style="font-family:宋体"}["\-\--"]{lang="EN-US"}]{#struct_0_83269_x5501_x923831272}

[[End address]{lang="EN-US"}]{#struct_0_83269_x5501_x1432521100}

[[地址组成员的结束地址。如果没有配置，则显示]{style="font-family:宋体"}["\-\--"]{lang="EN-US"}]{#struct_0_83269_x5501_x1084118170}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_252824909}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat address-group]{lang="EN-US"}**]{#struct_0_83269_x5501_1358250667}

::: {#-891847204 .myid}
[]{#_Toc404786483}[]{#struct_0_83269_x5501_98116949}

**NAT命令 \-- NAT配置命令 \-- display nat dns-map**

------------------------------------------------------------------------

[**[display nat dns-map]{lang="EN-US"}**]{#struct_0_83269_x5501_x386545478}[命令用来显示]{style="font-family:宋体"}[NAT DNS mapping]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x303068203}

[**[display nat dns-map]{lang="EN-US"}**]{#struct_0_83269_x5501_131962198}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x954232752}

[[任意]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1715468116}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1019697558}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1342269616}

[[network-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1358185131}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x1490297366}

[[mdc-operator]{lang="EN-US" style="color:black"}*[ ]{lang="EN-US" style="color:blue"}*]{#struct_0_83269_x5501_x1006731387}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x262911748}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x879716800}[显示所有]{style="font-family:宋体"}[NAT DNS mapping]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display nat dns-map]{lang="EN-US"}]{#struct_0_83269_x5501_1358119595}

[NAT DNS mapping information:]{lang="EN-US"}

[  Totally 2 NAT DNS mappings.]{lang="EN-US"}

[  Domain name  : www.server.com]{lang="EN-US"}

[  Global IP    : 6.6.6.6]{lang="EN-US"}

[  Global port  : 23]{lang="EN-US"}

[  Protocol     : TCP(6)]{lang="EN-US"}

[  Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Domain name  : www.service.com]{lang="EN-US"}

[  Global IP    : \-\--]{lang="EN-US"}

[  Global port  : 12]{lang="EN-US"}

[  Protocol     : TCP(6) ]{lang="EN-US"}

[  Config status: Inactive]{lang="EN-US"}

[  Reasons for inactive status:]{lang="EN-US"}

[    The following items don\'t exist or aren\'t effective: interface IP address.]{lang="EN-US"}

[ ]{lang="EN-US"}

[]{#struct_0_83269_x5501_437409064}[[表1-3 ]{lang="EN-US"}[display nat dns-map]{lang="EN-US"}]{#_Ref334101543}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x803061911}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_454303744}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_x549394489}

[[NAT DNS mapping information]{lang="EN-US"}]{#struct_0_83269_x5501_1358054059}

[[NAT DNS mapping]{lang="EN-US"}]{#struct_0_83269_x5501_x1081126232}[配置信息]{style="font-family:宋体"}

[[Totally *n* NAT DNS mappings]{lang="EN-US"}]{#struct_0_83269_x5501_x1462131486}

[[当前有]{style="font-family:宋体"}]{#struct_0_83269_x5501_x616560037}*[n]{lang="FR"}*[条]{style="font-family:宋体"}[DNS mapping]{lang="EN-US"}[配置]{style="font-family:宋体"}

[[Domain name]{lang="EN-US"}]{#struct_0_83269_x5501_1146671742}

[[DNS]{lang="EN-US"}]{#struct_0_83269_x5501_1392228395}[域名]{style="font-family:宋体"}

[[Global IP]{lang="EN-US"}]{#struct_0_83269_x5501_1293267982}

[[外网地址。如果配置使用的是]{style="font-family:宋体"}[Easy IP]{lang="EN-US"}]{#struct_0_83269_x5501_1357988523}[方式，则此处显示指定的接口的地址。"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["表示接口下没有配置外网地址]{style="font-family:宋体"}

[[Global port]{lang="EN-US"}]{#struct_0_83269_x5501_x1335506752}

[[外网端口号]{style="font-family:宋体"}]{#struct_0_83269_x5501_202219262}

[[Protocol]{lang="EN-US"}]{#struct_0_83269_x5501_202182706}

[[协议名称以及协议编号]{style="font-family:宋体"}]{#struct_0_83269_x5501_1514844610}

[[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_1970037344}

[[显示]{style="font-family:宋体"}[DNS mapping]{lang="EN-US"}]{#struct_0_83269_x5501_x758846011}[配置的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_807237930}[：生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x1921645425}[：不生效]{lang="EN-US" style="font-family:宋体"}

[[Reasons for inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_1779038434}

[[当]{style="font-family:宋体"}[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_x355561484}[字段为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}[时，显示]{style="font-family:宋体"}[DNS mapping]{lang="EN-US"}[配置不生效的原因]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The]{lang="EN-US"}[ following items don\'t exist or aren\'t effective: interface IP address]{lang="EN-US"}]{#struct_0_83269_x5501_1210522457}[：]{lang="EN-US" style="font-family:宋体"}[引用的]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[没有配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x779561335}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat dns-map]{lang="EN-US"}**]{#struct_0_83269_x5501_1357922987}

::: {#-1982605037 .myid}
[]{#_Toc404786484}[]{#struct_0_83269_x5501_x548062532}[]{#_Ref311207139}

**NAT命令 \-- NAT配置命令 \-- display nat eim**

------------------------------------------------------------------------

[**[display nat eim]{lang="EN-US"}**]{#struct_0_83269_x5501_220342070}[命令用来显示]{style="font-family:宋体"}[NAT EIM]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1591535635}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_83269_x5501_519539673}

[**[display nat eim]{lang="EN-US"}**]{#struct_0_83269_x5501_76099845}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_83269_x5501_446293468}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display nat eim ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_83269_x5501_527831012}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_83269_x5501_x787078104}[模式：]{style="font-family:宋体"}

[**[display nat eim ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_83269_x5501_1357857451}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1256066097}

[[任意]{style="font-family:宋体"}]{#struct_0_83269_x5501_936168233}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1774888347}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1535879747}

[[network-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_2037859411}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x1084409904}

[[mdc-operator]{lang="EN-US" style="color:black"}*[ ]{lang="EN-US" style="color:blue"}*]{#struct_0_83269_x5501_x622998482}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1414027620}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_1358840491}[：显示指定单板上的]{style="font-family:宋体"}[EIM]{lang="EN-US"}[表项信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[EIM]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_486810640}[：显示指定成员设备上的]{style="font-family:宋体"}[EIM]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[s]{lang="EN-US"}[lot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。若不指定该参数，则表示显示所有成员设备上的]{style="font-family:宋体"}[EIM]{lang="EN-US"}[表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x1511281332}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[EIM]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[EIM]{lang="EN-US"}[表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x1063650806}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[EIM]{lang="EN-US"}[表项信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[若不指定该参数，则表示显示所有成员设备的所有单板上的]{style="font-family:宋体"}[EIM]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x1107996805}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[EIM]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[EIM]{lang="EN-US"}[表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_83269_x5501_1122509569}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[EIM]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_2095860402}

[[EIM]{lang="EN-US"}]{#struct_0_83269_x5501_1089162020}[表项是报文在进行]{style="font-family:宋体"}[Endpoint-Independent Mapping]{lang="EN-US"}[方式的]{style="font-family:宋体"}[PAT]{lang="EN-US"}[转换时创建的]{style="font-family:宋体"}[，它记录了内网和外网的转换关系（]{style="font-family:宋体"}[内网地址和端口]{style="font-family:宋体"}[\<\--\>NAT]{lang="EN-US"}[地址和端口），该表项有以下两个作用：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[保证后续来自相同源地址和源端口的新建连接与首次连接使用相同的转换关系。]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1276539365}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[允许外网主机向]{style="font-family:宋体"}]{#struct_0_83269_x5501_x760299867}[NAT]{lang="EN-US"}[地址和端口发起的新建连接根据]{style="font-family:宋体"}[EIM]{lang="EN-US"}[表项进行反向地址转换。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1176113058}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1575362648}[显示]{style="font-family:宋体"}[NAT EIM]{lang="EN-US"}[表项的信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat eim]{lang="EN-US"}]{#struct_0_83269_x5501_1358774955}

[Local  IP/port: 192.168.100.100/1024]{lang="EN-US"}

[Global IP/port: 200.100.1.100/2048]{lang="EN-US"}

[Local  VPN: vpn1 ]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Protocol: TCP(6)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local  IP/port: 192.168.100.200/2048]{lang="EN-US"}

[Global IP/port: 200.100.1.200/4096]{lang="EN-US"}

[Protocol: UDP(17)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1511632311}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上的]{style="font-family:宋体"}[NAT EIM]{lang="EN-US"}[表项信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display nat eim slot 1]{lang="EN-US"}]{#struct_0_83269_x5501_1358316204}

[Slot 1:]{lang="EN-US"}

[Local  IP/port: 192.168.100.100/1024]{lang="EN-US"}

[Global IP/port: 200.100.1.100/2048]{lang="EN-US"}

[Local  VPN: vpn1 ]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Protocol: TCP(6)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local  IP/port: 192.168.100.200/2048]{lang="EN-US"}

[Global IP/port: 200.100.1.200/4096]{lang="EN-US"}

[Protocol: UDP(17)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1660381586}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备上的]{style="font-family:宋体"}[NAT EIM]{lang="EN-US"}[表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat eim slot 1]{lang="EN-US"}]{#struct_0_83269_x5501_x1836463999}

[Slot 1:]{lang="EN-US"}

[Local  IP/port: 192.168.100.100/1024]{lang="EN-US"}

[Global IP/port: 200.100.1.100/2048]{lang="EN-US"}

[Local  VPN: vpn1 ]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Protocol: TCP(6)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local  IP/port: 192.168.100.200/2048]{lang="EN-US"}

[Global IP/port: 200.100.1.200/4096]{lang="EN-US"}

[Protocol: UDP(17)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x340847609}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上的]{style="font-family:宋体"}[NAT EIM]{lang="EN-US"}[表项信息。（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display nat eim chassis 1 slot 0]{lang="EN-US"}]{#struct_0_83269_x5501_1358250668}

[Slot 0 in chassis 1:]{lang="EN-US"}

[Local  IP/port: 192.168.100.100/1024]{lang="EN-US"}

[Global IP/port: 200.100.1.100/2048]{lang="EN-US"}

[Local  VPN: vpn1 ]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Protocol: TCP(6)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local  IP/port: 192.168.100.200/2048]{lang="EN-US"}

[Global IP/port: 200.100.1.200/4096]{lang="EN-US"}

[Protocol: UDP(17)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1122771713}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[NAT EIM]{lang="EN-US"}[表项信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display nat eim slot 1 cpu 0]{lang="EN-US"}]{#struct_0_83269_x5501_x390420453}

[CPU 0 on slot 1:]{lang="EN-US"}

[Local  IP/port: 192.168.100.100/1024]{lang="EN-US"}

[Global IP/port: 200.100.1.100/2048]{lang="EN-US"}

[Local  VPN: vpn1 ]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Protocol: TCP(6)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local  IP/port: 192.168.100.200/2048]{lang="EN-US"}

[Global IP/port: 200.100.1.200/4096]{lang="EN-US"}

[Protocol: UDP(17)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x2103826904}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备上的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[NAT EIM]{lang="EN-US"}[表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat eim slot 1 cpu 0]{lang="EN-US"}]{#struct_0_83269_x5501_1122706177}

[CPU 0 on slot 1:]{lang="EN-US"}

[Local  IP/port: 192.168.100.100/1024]{lang="EN-US"}

[Global IP/port: 200.100.1.100/2048]{lang="EN-US"}

[Local  VPN: vpn1 ]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Protocol: TCP(6)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local  IP/port: 192.168.100.200/2048]{lang="EN-US"}

[Global IP/port: 200.100.1.200/4096]{lang="EN-US"}

[Protocol: UDP(17)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_406276688}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[NAT EIM]{lang="EN-US"}[表项信息。（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display nat eim chassis 1 slot 1 cpu 0]{lang="EN-US"}]{#struct_0_83269_x5501_1122640641}

[CPU 0 on slot 1 in chassis 1:]{lang="EN-US"}

[Local  IP/port: 192.168.100.100/1024]{lang="EN-US"}

[Global IP/port: 200.100.1.100/2048]{lang="EN-US"}

[Local  VPN: vpn1 ]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Protocol: TCP(6)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local  IP/port: 192.168.100.200/2048]{lang="EN-US"}

[Global IP/port: 200.100.1.200/4096]{lang="EN-US"}

[Protocol: UDP(17)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display nat eim]{lang="EN-US"}]{#struct_0_83269_x5501_97527125}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x775248066}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_450964741}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_x17732228}

[[Local IP/port]{lang="EN-US"}]{#struct_0_83269_x5501_2070735708}

[[内网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_693012024}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[Global IP/port]{lang="EN-US"}]{#struct_0_83269_x5501_1358185132}

[[外网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_x1490231830}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[Local VPN]{lang="EN-US"}]{#struct_0_83269_x5501_399563224}

[[内网地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_83269_x5501_x152148165}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。如果不属于任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则不显示该字段]{style="font-family:宋体"}

[[Global VPN]{lang="EN-US"}]{#struct_0_83269_x5501_x1357080872}

[[外网地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_83269_x5501_x1983246888}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。如果不属于任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则不显示该字段]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_83269_x5501_1358119596}

[[协议名称以及协议编号]{style="font-family:宋体"}]{#struct_0_83269_x5501_437343528}

[[Total entries found]{lang="EN-US"}]{#struct_0_83269_x5501_x184451503}

[[当前查找到的]{style="font-family:宋体"}[EIM]{lang="EN-US"}]{#struct_0_83269_x5501_x438126203}[表项的个数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_42727642}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat mapping-behavior]{lang="EN-US"}**]{#struct_0_83269_x5501_x1814628584}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat outbound]{lang="EN-US"}**]{#struct_0_83269_x5501_1765400500}

::: {#-1724764660 .myid}
[]{#_Toc404786485}[]{#struct_0_83269_x5501_2010141511}

**NAT命令 \-- NAT配置命令 \-- display nat inbound**

------------------------------------------------------------------------

[**[display nat inbound]{lang="EN-US"}**]{#struct_0_83269_x5501_1358054060}[命令用来显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[入方向动态地址转换的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1080536405}

[**[display nat inbound]{lang="EN-US"}**]{#struct_0_83269_x5501_x1491050849}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x666115146}

[[任意]{style="font-family:宋体"}]{#struct_0_83269_x5501_2078435267}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_521176793}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_253192550}

[[network-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1198243913}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1357988524}

[[mdc-operator]{lang="EN-US" style="color:black"}*[ ]{lang="EN-US" style="color:blue"}*]{#struct_0_83269_x5501_x1335441216}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1150309215}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x826551328}[显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[入接口动态地址转换的配置信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat inbound]{lang="EN-US"}]{#struct_0_83269_x5501_x1921710961}

[NAT inbound information:]{lang="EN-US"}

[  Totally 2 NAT inbound rules.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    ACL: 2038         Address group: 2      Add route: Y]{lang="EN-US"}

[    NO-PAT: Y         Reversible: N]{lang="EN-US"}

[    VPN instance: vpn1]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: GigabitEthernet1/0/3]{lang="EN-US"}

[    ACL: 2037         Address group: 1      Add route: Y]{lang="EN-US"}

[    NO-PAT: Y         Reversible: N]{lang="EN-US"}

[    VPN instance: vpn2]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, and ACL.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1457947126}[显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[入接口动态地址转换的配置信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat inbound]{lang="EN-US"}]{#struct_0_83269_x5501_x355627020}

[NAT inbound information:]{lang="EN-US"}

[  Totally 2 NAT inbound rules.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    ACL: 2038         Address group: 2      Add route: Y]{lang="EN-US"}

[    NO-PAT: Y         Reversible: N]{lang="EN-US"}

[    VPN instance: vpn1]{lang="EN-US"}

[    Service card: Slot 5]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: GigabitEthernet1/0/3]{lang="EN-US"}

[    ACL: 2037         Address group: 1      Add route: Y]{lang="EN-US"}

[    NO-PAT: Y         Reversible: N]{lang="EN-US"}

[    VPN instance: vpn2]{lang="EN-US"}

[    Service card: \-\--]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, and ACL.]{lang="EN-US"}

[      Service card not specified.]{lang="EN-US"}

[Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1210456921}[显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[入接口动态地址转换的配置信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat inbound]{lang="EN-US"}]{#struct_0_83269_x5501_1624143314}

[NAT inbound information:]{lang="EN-US"}

[  Totally 2 NAT inbound rules.]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/2]{lang="EN-US"}

[    ACL: 2038         Address group: 2      Add route: Y]{lang="EN-US"}

[    NO-PAT: Y         Reversible: N]{lang="EN-US"}

[    VPN instance: vpn1]{lang="EN-US"}

[    Service card: Chassis 2 slot 5]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: GigabitEthernet1/3/0/3]{lang="EN-US"}

[    ACL: 2037         Address group: 1      Add route: Y]{lang="EN-US"}

[    NO-PAT: Y         Reversible: N]{lang="EN-US"}

[    VPN instance: vpn2]{lang="EN-US"}

[    Service card: \-\--]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, and ACL.]{lang="EN-US"}

[      Service card not specified.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[]{#struct_0_83269_x5501_841519504}[[表1-5 ]{lang="EN-US"}[display nat inbound]{lang="EN-US"}]{#_Ref334104209}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x779058834}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_1371045026}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_1357922988}

[[NAT inbound information]{lang="EN-US"}]{#struct_0_83269_x5501_x547210564}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_1167003813}[入方向动态地址转换的配置信息]{style="font-family:宋体"}

[[Totally *n* NAT inbound rules]{lang="EN-US"}]{#struct_0_83269_x5501_1111142812}

[[当前存在]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_83269_x5501_x1368187951}[条入入方向动态地址转换配置]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_83269_x5501_1915793511}

[[入方向动态地址转换配置所在的接口]{style="font-family:宋体"}]{#struct_0_83269_x5501_1357857452}

[[ACL]{lang="EN-US"}]{#struct_0_83269_x5501_x1256131633}

[[引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_83269_x5501_879428360}[编号]{style="font-family:宋体"}

[[Address group]{lang="EN-US"}]{#struct_0_83269_x5501_x284879706}

[[入方向动态地址转换使用的地址组]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1100671695}

[[Add route]{lang="EN-US"}]{#struct_0_83269_x5501_1510575612}

[[是否添加路由。若其值为"]{style="font-family:宋体"}[Y]{lang="EN-US"}]{#struct_0_83269_x5501_1358840492}["，则表示有报文命中此项入接口动态地址转换配置时，设备会自动添加一条路由；否则，不添加]{style="font-family:宋体"}

[[NO-PAT]{lang="EN-US"}]{#struct_0_83269_x5501_486876176}

[[是否使用]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}]{#struct_0_83269_x5501_120173515}[方式进行地址转换。若其值为"]{style="font-family:宋体"}[Y]{lang="EN-US"}["，则表示使用]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[方式；若其值为"]{style="font-family:宋体"}[N]{lang="EN-US"}["，则表示使用]{style="font-family:宋体"}[PAT]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[Reversible]{lang="EN-US"}]{#struct_0_83269_x5501_x1479972203}

[[是否允许反向地址转换。若其值为"]{style="font-family:宋体"}[Y]{lang="EN-US"}]{#struct_0_83269_x5501_x324098959}["，则表示]{style="font-family:宋体"}[在某方向上发起的连接已成功建立地址转换表项的情况下，允许反方向发起的连接使用已建立的地址转换表项进行地址转换；否则，不允许]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_83269_x5501_498640199}

[[地址组所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_83269_x5501_1358774956}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。如果不属于任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则不显示该字段]{style="font-family:宋体"}

[[Service card]{lang="EN-US"}]{#struct_0_83269_x5501_807106858}

[[显示提供]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1921776497}[处理的业务板。如果接口下没有指定业务板，则显示为"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x355692556}

[[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_1210391385}

[[显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x806031250}[配置的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_760052691}[：生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_999617301}[：不生效]{style="font-family:宋体"}

[[Reasons for inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_x1162327146}

[[当]{style="font-family:宋体"}[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_403756795}[字段为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}[时，显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[入方向动态地址转换的配置不生效的原因]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The following items don\'t exist or aren\'t effective: local VPN, ]{lang="EN-US"}]{#struct_0_83269_x5501_x759042619}[address]{lang="EN-US"}[ group, and ACL]{lang="EN-US"}[：配置中地址组所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例、地址组、]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或不生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service card not specified]{lang="EN-US"}]{#struct_0_83269_x5501_807041322}[：没有指定提供]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[处理业务板]{lang="EN-US" style="font-family:宋体"}

[[Global flow-table status]{lang="EN-US"}]{#struct_0_83269_x5501_x2048243910}

[[针对]{style="font-family:宋体"}[Global]{lang="EN-US"}]{#struct_0_83269_x5501_x246825206}[地址下发流表的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_340571137}[：生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x2048440518}[：不生效]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x749921754}

[[Reasons for flow-table inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_441157192}

[[当下发流表的状态为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x1041531988}[时，显示流表不生效的原因]{style="font-family:宋体"}

[[其中，]{style="font-family:宋体"}[Not enough resources are available to complete the operation]{lang="EN-US"}]{#struct_0_83269_x5501_x983473754}[表示因为资源不足导致下发流表失败]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x2048374982}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1511435703}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat inbound]{lang="EN-US"}**]{#struct_0_83269_x5501_x1608616688}

::: {#-463444198 .myid}
[]{#_Toc404786486}[]{#struct_0_83269_x5501_589583642}

**NAT命令 \-- NAT配置命令 \-- display nat log**

------------------------------------------------------------------------

[**[display nat log]{lang="EN-US"}**]{#struct_0_83269_x5501_x1533726855}[命令用来显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[日志功能的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x641205422}

[**[display nat log]{lang="EN-US"}**]{#struct_0_83269_x5501_x1115573544}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1358316201}

[[任意]{style="font-family:宋体"}]{#struct_0_83269_x5501_1660578194}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_172469847}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_202692720}

[[network-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1916514683}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1027266294}

[[mdc-operator]{lang="EN-US" style="color:black"}*[ ]{lang="EN-US" style="color:blue"}*]{#struct_0_83269_x5501_x798799133}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x954528559}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_184588103}[显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[日志功能的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display nat log]{lang="EN-US"}]{#struct_0_83269_x5501_1358250665}

[NAT logging:]{lang="EN-US"}

[  Log enable          : Enabled(ACL 2000)]{lang="EN-US"}

[  Flow-begin          : Disabled]{lang="EN-US"}

[  Flow-end            : Disabled]{lang="EN-US"}

[  Flow-active         : Enabled(10 minutes)]{lang="EN-US"}

[  Port-block-assign   : Disabled]{lang="EN-US"}

[  Port-block-withdraw : Disabled]{lang="EN-US"}

[  Alarm               : Disabled]{lang="EN-US"}

[]{#struct_0_83269_x5501_98248021}[[表1-6 ]{lang="EN-US"}[display nat log]{lang="EN-US"}]{#_Ref334104166}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x777708180}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1472983479}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_x243842209}

[[NAT logging]{lang="EN-US"}]{#struct_0_83269_x5501_x1754388324}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_717305256}[日志功能的配置信息]{style="font-family:宋体"}

[[Log enable]{lang="EN-US"}]{#struct_0_83269_x5501_1358185129}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1489773079}[日志开关的开启情况。如果]{style="font-family:宋体"}[NAT]{lang="EN-US"}[日志开关处于开启状态，且指定了]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，则同时显示指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Flow-begin]{lang="EN-US"}]{#struct_0_83269_x5501_x363735888}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1473157002}[会话新建日志开关的开启情况]{style="font-family:宋体"}

[[Flow-end]{lang="EN-US"}]{#struct_0_83269_x5501_483612114}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_1383566104}[会话删除日志开关的开启情况]{style="font-family:宋体"}

[[Flow-active]{lang="EN-US"}]{#struct_0_83269_x5501_1358119593}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_437540136}[活跃流日志开关的开启情况以及阈值信息。如果]{style="font-family:宋体"}[NAT]{lang="EN-US"}[活跃流日志开关处于开启状态，则同时显示配置的生成活跃流日志的时间间隔（单位为分）]{style="font-family:宋体"}

[[Port-block-assign]{lang="FR"}]{#struct_0_83269_x5501_1122771714}

[[端口块分配的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}]{#struct_0_83269_x5501_1122706178}[用户]{style="font-family:宋体"}[日志]{style="font-family:宋体"}[开关的开启情况]{style="font-family:宋体"}

[[Port-block-withdraw]{lang="FR"}]{#struct_0_83269_x5501_405555792}

[[端口块回收的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}]{#struct_0_83269_x5501_1122640642}[用户]{style="font-family:宋体"}[日志]{style="font-family:宋体"}[开关的开启情况]{style="font-family:宋体"}

[[Alarm]{lang="FR"}]{#struct_0_83269_x5501_x1160891494}

[[NAT444]{lang="EN-US"}]{#struct_0_83269_x5501_1122575106}[告警信息日志开关的开启情况]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_485207023}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log enable]{lang="EN-US"}**]{#struct_0_83269_x5501_1331761165}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log flow-active]{lang="EN-US"}**]{#struct_0_83269_x5501_139763749}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log flow-begin]{lang="EN-US"}**]{#struct_0_83269_x5501_x2087793395}

::: {#-507934372 .myid}
[]{#_Toc404786487}[]{#struct_0_83269_x5501_798076795}[]{#_Ref311210160}[]{#_Ref311207173}

**NAT命令 \-- NAT配置命令 \-- display nat no-pat**

------------------------------------------------------------------------

[**[display nat no-pat]{lang="EN-US"}**]{#struct_0_83269_x5501_x1595688203}[命令用来显示]{style="font-family:宋体"}[NAT NO-PAT]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_987318742}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_83269_x5501_1358054057}

[**[display nat no-pat]{lang="EN-US"}**]{#struct_0_83269_x5501_x1080470872}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_83269_x5501_x2093496946}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display nat no-pat ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] ]{lang="EN-US"}]{#struct_0_83269_x5501_1435586860}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_83269_x5501_x1205458116}[模式：]{style="font-family:宋体"}

[**[display nat no-pat ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_83269_x5501_2065289924}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1585244470}

[[任意]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1646746477}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1357988521}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x1335637824}

[[network-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x76237068}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_2131697914}

[[mdc-operator]{lang="EN-US" style="color:black"}*[ ]{lang="EN-US" style="color:blue"}*]{#struct_0_83269_x5501_1857268492}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1857473058}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x1620064585}[：显示指定单板上的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表项信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[若不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_1244991903}[：显示指定成员设备上的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表项信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[若不指定该参数，则表示显示所有成员设备上的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[（集中]{style="font-family:宋体"}[式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设]{style="font-family:宋体"}[备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_1217536487}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x1493452982}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表项信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[若不指定该参数，则表示显示所有成员设备的所有单板上的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x1691488832}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_83269_x5501_1122444031}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1357922985}

[[NO-PAT]{lang="EN-US"}]{#struct_0_83269_x5501_x547931460}[表项记录了动态分配的一对一地址映射关系，该表项有两个作用：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[保证后续同方向的新连接使用与第一个连接相同的地址转换关系。]{style="font-family:宋体"}]{#struct_0_83269_x5501_1944159819}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[反方向的新连接可以使用]{style="font-family:宋体"}]{#struct_0_83269_x5501_1261788459}[NO-PAT]{lang="EN-US"}[表进行地址转换。]{style="font-family:宋体"}

[**[nat inbound]{lang="EN-US"}**]{#struct_0_83269_x5501_x1888899432}[和]{style="font-family:宋体"}**[nat outbound]{lang="EN-US"}**[配]{style="font-family:宋体"}[置的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[方式在转换报文地址之后都需要创建]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表。这两种配置创建的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表类型不同，不能互相使用，因此分成两类进行显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1334105576}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1291530760}[显示]{style="font-family:宋体"}[NAT NO-PAT]{lang="EN-US"}[表项。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat no-pat]{lang="EN-US"}]{#struct_0_83269_x5501_1357857449}

[Global  IP: 200.100.1.100]{lang="EN-US"}

[Local   IP: 192.168.100.100]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Local  VPN: vpn1]{lang="EN-US"}

[Reversible: N ]{lang="EN-US"}

[Type      : Inbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local   IP: 192.168.100.200]{lang="EN-US"}

[Global  IP: 200.100.1.200]{lang="EN-US"}

[Reversible: Y ]{lang="EN-US"}

[Type      : Outbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1256590384}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上的]{style="font-family:宋体"}[NAT NO-PAT]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display nat no-pat slot 1]{lang="EN-US"}]{#struct_0_83269_x5501_387764162}

[Slot 1:]{lang="EN-US"}

[Global  IP: 200.100.1.100]{lang="EN-US"}

[Local   IP: 192.168.100.100]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Local  VPN: vpn1]{lang="EN-US"}

[Reversible: N ]{lang="EN-US"}

[Type      : Inbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local   IP: 192.168.100.200]{lang="EN-US"}

[Global  IP: 200.100.1.200]{lang="EN-US"}

[Reversible: Y ]{lang="EN-US"}

[Type      : Outbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1887061970}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[NAT NO-PAT]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[集中]{style="font-family:宋体"}[式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设]{style="font-family:宋体"}[备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat no-pat slot 1]{lang="EN-US"}]{#struct_0_83269_x5501_1358840489}

[Slot 1:]{lang="EN-US"}

[Global  IP: 200.100.1.100]{lang="EN-US"}

[Local   IP: 192.168.100.100]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Local  VPN: vpn1]{lang="EN-US"}

[Reversible: N ]{lang="EN-US"}

[Type      : Inbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local   IP: 192.168.100.200]{lang="EN-US"}

[Global  IP: 200.100.1.200]{lang="EN-US"}

[Reversible: Y ]{lang="EN-US"}

[Type      : Outbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_486286353}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上的]{style="font-family:宋体"}[NAT NO-PAT]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display nat no-pat chassis 1 slot 1]{lang="EN-US"}]{#struct_0_83269_x5501_1358774953}

[Slot 1 in chassis 1:]{lang="EN-US"}

[Global  IP: 200.100.1.100]{lang="EN-US"}

[Local   IP: 192.168.100.100]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Local  VPN: vpn1]{lang="EN-US"}

[Reversible: N ]{lang="EN-US"}

[Type      : Inbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local   IP: 192.168.100.200]{lang="EN-US"}

[Global  IP: 200.100.1.200]{lang="EN-US"}

[Reversible: Y ]{lang="EN-US"}

[Type      : Outbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1122575103}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[NAT NO-PAT]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display nat no-pat slot 1 cpu 0]{lang="EN-US"}]{#struct_0_83269_x5501_1961284972}

[CPU 0 on slot 1:]{lang="EN-US"}

[Global  IP: 200.100.1.100]{lang="EN-US"}

[Local   IP: 192.168.100.100]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Local  VPN: vpn1]{lang="EN-US"}

[Reversible: N ]{lang="EN-US"}

[Type      : Inbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local   IP: 192.168.100.200]{lang="EN-US"}

[Global  IP: 200.100.1.200]{lang="EN-US"}

[Reversible: Y ]{lang="EN-US"}

[Type      : Outbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1121985279}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[NAT NO-PAT]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[集中]{style="font-family:宋体"}[式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设]{style="font-family:宋体"}[备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat no-pat slot 1 cpu 0]{lang="EN-US"}]{#struct_0_83269_x5501_515364075}

[CPU 0 on slot 1:]{lang="EN-US"}

[Global  IP: 200.100.1.100]{lang="EN-US"}

[Local   IP: 192.168.100.100]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Local  VPN: vpn1]{lang="EN-US"}

[Reversible: N ]{lang="EN-US"}

[Type      : Inbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local   IP: 192.168.100.200]{lang="EN-US"}

[Global  IP: 200.100.1.200]{lang="EN-US"}

[Reversible: Y ]{lang="EN-US"}

[Type      : Outbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1121919743}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[NAT NO-PAT]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display nat no-pat chassis 1 slot 1 cpu 0]{lang="EN-US"}]{#struct_0_83269_x5501_104287280}

[CPU 0 on slot 1 in chassis 1:]{lang="EN-US"}

[Global  IP: 200.100.1.100]{lang="EN-US"}

[Local   IP: 192.168.100.100]{lang="EN-US"}

[Global VPN: vpn2]{lang="EN-US"}

[Local  VPN: vpn1]{lang="EN-US"}

[Reversible: N ]{lang="EN-US"}

[Type      : Inbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local   IP: 192.168.100.200]{lang="EN-US"}

[Global  IP: 200.100.1.200]{lang="EN-US"}

[Reversible: Y ]{lang="EN-US"}

[Type      : Outbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found: 2]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display nat no-pat]{lang="EN-US"}]{#struct_0_83269_x5501_x1511763383}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x783754753}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1351421435}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_1737791423}

[[Local IP]{lang="EN-US"}]{#struct_0_83269_x5501_x2057265124}

[[内网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_361821620}[地址]{style="font-family:宋体"}

[[Global IP]{lang="EN-US"}]{#struct_0_83269_x5501_1358316202}

[[外网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_1660512658}[地址]{style="font-family:宋体"}

[[Local VPN]{lang="EN-US"}]{#struct_0_83269_x5501_x1806353319}

[[内网地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_83269_x5501_520070324}[的实例名称。如果不属于任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则该行不显示]{style="font-family:宋体"}

[[Global VPN]{lang="EN-US"}]{#struct_0_83269_x5501_492412654}

[[外网地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_83269_x5501_1941452098}[的实例名称。如果不属于任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则该行不显示]{style="font-family:宋体"}

[[Reversible]{lang="EN-US"}]{#struct_0_83269_x5501_x1208264157}

[[是否允许反向地址转换。若其值为"]{style="font-family:宋体"}[Y]{lang="EN-US"}]{#struct_0_83269_x5501_1358250666}["，则表示]{style="font-family:宋体"}[在某方向上发起的连接已成功建立地址转换表项的情况下，允许反方向发起的连接使用已建立的地址转换表项进行地址转换]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_83269_x5501_98182485}

[[NO-PAT]{lang="EN-US"}]{#struct_0_83269_x5501_x592340182}[表项类型]{style="font-family:宋体"}

[[Inbound]{lang="EN-US"}]{#struct_0_83269_x5501_1137452507}[：入方向动态地址转换过程中创建的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[Outbound]{lang="EN-US"}]{#struct_0_83269_x5501_x101974579}[：出方向动态地址转换过程中创建的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[Total entries found]{lang="EN-US"}]{#struct_0_83269_x5501_1358185130}

[[当前查找到的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1490362902}[表项的个数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_979476986}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat inbound]{lang="EN-US"}**]{#struct_0_83269_x5501_x1420272390}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat outbound]{lang="EN-US"}**]{#struct_0_83269_x5501_1703983605}

::: {#-1864024100 .myid}
[]{#_Toc404786488}[]{#struct_0_83269_x5501_1833872935}

**NAT命令 \-- NAT配置命令 \-- display nat outbound**

------------------------------------------------------------------------

[**[display nat outbound]{lang="EN-US"}**]{#struct_0_83269_x5501_x686490294}[命令用来显示出方向动态地址转换的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1546238734}

[**[display nat outbound]{lang="EN-US"}**]{#struct_0_83269_x5501_763494720}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1358119594}

[[任意]{style="font-family:宋体"}]{#struct_0_83269_x5501_437474600}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x706487285}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x383955142}

[[network-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1131056210}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_254946276}

[[mdc-operator]{lang="EN-US" style="color:black"}*[ ]{lang="EN-US" style="color:blue"}*]{#struct_0_83269_x5501_1001082532}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_249969333}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x653594980}[显示出方向动态地址转换的配置信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat outbound]{lang="EN-US"}]{#struct_0_83269_x5501_1358054058}

[NAT outbound information:]{lang="EN-US"}

[  Totally 2 NAT outbound rules.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[    ACL: 2036         Address group: 1      Port-preserved: Y]{lang="EN-US"}

[    NO-PAT: N         Reversible: N]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[    ACL: 2037         Address group: \-\--    Port-preserved: N]{lang="EN-US"}

[    NO-PAT: Y         Reversible: Y]{lang="EN-US"}

[    VPN instance: vpn_nat]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: global VPN, and ACL]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[    DS-Lite B4 ACL: 2100         Address group: 0      Port-preserved: N]{lang="EN-US"}

[    NO-PAT: N         Reversible: N]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x671879058}[显示出方向动态地址转换的配置信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat outbound]{lang="EN-US"}]{#struct_0_83269_x5501_894204883}

[NAT outbound information:]{lang="EN-US"}

[  Totally 2 NAT outbound rules.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[    ACL: 2036         Address group: 1      Port-preserved: Y]{lang="EN-US"}

[    NO-PAT: N         Reversible: N]{lang="EN-US"}

[    Service card: Slot 5]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    ACL: 2037         Address group: 2      Port-preserved: N]{lang="EN-US"}

[    NO-PAT: Y         Reversible: Y]{lang="EN-US"}

[    VPN instance: vpn_nat]{lang="EN-US"}

[    Service card: Slot 5]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: global VPN, and ACL.]{lang="EN-US"}

[      Service card not specified.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[    DS-Lite B4 ACL: 2100         Address group: 0      Port-preserved: N]{lang="EN-US"}

[    NO-PAT: N         Reversible: N]{lang="EN-US"}

[    Service card: Slot 5]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1028174954}[显示出方向动态地址转换的配置信息。（分布式设备]{style="font-family:宋体"}[－]{style="font-size:10.0pt;font-family:宋体;color:black"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display nat outbound]{lang="EN-US"}]{#struct_0_83269_x5501_537908987}

[NAT outbound information:]{lang="EN-US"}

[  Totally 2 NAT outbound rules.]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/1]{lang="EN-US"}

[    ACL: 2036         Address group: 1      Port-preserved: Y]{lang="EN-US"}

[    NO-PAT: N         Reversible: N]{lang="EN-US"}

[    Service card: Chassis 2 Slot 5]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/2]{lang="EN-US"}

[    ACL: 2037         Address group: 1      Port-preserved: N]{lang="EN-US"}

[    NO-PAT: Y         Reversible: Y]{lang="EN-US"}

[    VPN instance: vpn_nat]{lang="EN-US"}

[    Service card: \-\--]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: global VPN, and ACL.]{lang="EN-US"}

[      Service card not specified.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet3/0/1]{lang="EN-US"}

[    DS-Lite B4 ACL: 2100         Address group: 0      Port-preserved: N]{lang="EN-US"}

[    NO-PAT: N         Reversible: N]{lang="EN-US"}

[    Service card: Chassis 2 Slot 5]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[]{#struct_0_83269_x5501_x1081060696}[[表1-8 ]{lang="EN-US"}[display nat outbound]{lang="EN-US"}]{#_Ref334105167}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x787222687}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_x854920610}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_1602876143}

[[NAT outbound information]{lang="EN-US"}]{#struct_0_83269_x5501_x1488253925}

[[出方向动态地址转换的配置信息]{style="font-family:宋体"}]{#struct_0_83269_x5501_1357988522}

[[Totally *n* NAT outbound rules]{lang="EN-US"}]{#struct_0_83269_x5501_x1335572288}

[[当前存在]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_83269_x5501_x1089574550}[条出方向动态地址转换]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_83269_x5501_1567874470}

[[出方向动态地址转换配置所在的接口]{style="font-family:宋体"}]{#struct_0_83269_x5501_1267213622}

[[ACL]{lang="EN-US"}]{#struct_0_83269_x5501_x1500270115}

[[引用的]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}]{#struct_0_83269_x5501_1357922986}[编号。如果没有配置，则显示"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[DS-Lite B4 ACL]{lang="EN-US"}]{#struct_0_83269_x5501_x1931545600}

[[DS-Lite B4]{lang="EN-US"}]{#struct_0_83269_x5501_307802585}[引用的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Address group]{lang="EN-US"}]{#struct_0_83269_x5501_x548128068}

[[出方向动态地址转换使用的地址组。如果没有配置，则显示"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}]{#struct_0_83269_x5501_156087712}["]{style="font-family:宋体"}

[[Port-preserved]{lang="EN-US"}]{#struct_0_83269_x5501_x1914010878}

[[PAT]{lang="EN-US"}]{#struct_0_83269_x5501_x597470645}[方式下，是否尽量不转换端口]{style="font-family:宋体"}

[[NO-PAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1030347224}

[[是否使用]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}]{#struct_0_83269_x5501_1357857450}[方式进行转换。若其值为"]{style="font-family:宋体"}[N]{lang="EN-US"}["，则表示使用]{style="font-family:宋体"}[PAT]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[Reversible]{lang="EN-US"}]{#struct_0_83269_x5501_x1256000561}

[[是否允许反向地址转换。若其值为"]{style="font-family:宋体"}[Y]{lang="EN-US"}]{#struct_0_83269_x5501_651204292}["，则表示]{style="font-family:宋体"}[在某方向上发起的连接已成功建立地址转换表项的情况下，允许反方向发起的连接使用已建立的地址转换表项进行地址转换]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_83269_x5501_183041639}

[[地址组所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_83269_x5501_1770466152}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。如果不属于任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则不显示该字段]{style="font-family:宋体"}

[[Service card]{lang="EN-US"}]{#struct_0_83269_x5501_x221605900}

[[显示提供]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_1344478041}[处理的业务板。如果接口下没有指定业务板，则显示为"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x671944594}

[[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_894139347}

[[显示配置的状态]{style="font-family:宋体"}]{#struct_0_83269_x5501_537843451}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_2103927392}[：生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x624955963}[：不生效]{style="font-family:宋体"}

[[Reasons for inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_941127978}

[[当]{style="font-family:宋体"}[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_x1787755377}[字段为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}[时，显示配置不生效的原因]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The following items don\'t exist or aren\'t effective:]{lang="EN-US"}[ global VPN, interface IP address, ]{lang="EN-US"}]{#struct_0_83269_x5501_1344412505}[address]{lang="EN-US"}[ group, and ACL]{lang="EN-US"}[：配置中地址组所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例、接口地址、地址组、]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或不生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service card not specified]{lang="EN-US"}]{#struct_0_83269_x5501_x672010130}[：没有指定]{style="font-family:
  宋体"}[提供]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[处理的]{lang="EN-US" style="font-family:宋体"}[业务板]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NAT address conflicts]{lang="EN-US"}]{#struct_0_83269_x5501_x1028306026}[：]{lang="EN-US" style="font-family:
  宋体"}[NAT]{lang="EN-US"}[地址冲突]{lang="EN-US" style="font-family:
  宋体"}

[[Global flow-table status]{lang="EN-US"}]{#struct_0_83269_x5501_x2048047300}

[[针对]{style="font-family:宋体"}[Global]{lang="EN-US"}]{#struct_0_83269_x5501_x786645244}[地址下发流表的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_x987395018}[：生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x2047981764}[：不生效]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_866651169}

[[Reasons for flow-table inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_x1437343325}

[[当下发流表状态为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x1280682702}[时，显示流表不生效的原因]{style="font-family:宋体"}

[[其中，]{style="font-family:宋体"}[Not enough resources are available to complete the operation]{lang="EN-US"}]{#struct_0_83269_x5501_160826116}[表示因为资源不足导致下发流表失败]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_1210161352}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1358840490}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat outbound]{lang="EN-US"}**]{#struct_0_83269_x5501_486745104}

::: {#1628387509 .myid}
[]{#_Toc404786489}[]{#struct_0_83269_x5501_1122706176}[]{#_Toc363572607}

**NAT命令 \-- NAT配置命令 \-- display nat outbound port-block-group**

------------------------------------------------------------------------

[**[display nat outbound port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_406211152}[命令用来显]{style="font-family:宋体"}[示]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块静态映射的配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1117736187}

[**[display nat outbound port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_1122640640}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1160760422}

[[任意视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x255912947}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1122575104}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1961219436}

[[network-operator]{lang="EN-US"}]{#struct_0_83269_x5501_1287660494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1121985280}

[[mdc-operator]{lang="EN-US"}]{#struct_0_83269_x5501_514774256}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_284510785}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1121919744}[显示]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块静态映射的配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display nat outbound port-block-group]{lang="EN-US"}]{#struct_0_83269_x5501_104483888}

[NAT outbound port block group information:]{lang="EN-US"}

[  Totally 2 outbound port block group items.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    Port block group: 2]{lang="EN-US"}

[    Config status   : Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    Port block group: 10]{lang="EN-US"}

[    Config status   : Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: port block group.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[]{#struct_0_83269_x5501_x789122362}[[表1-9 ]{lang="EN-US"}[display nat outbound port-block-group ]{lang="EN-US"}]{#_Ref363572645}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1261906046}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_432626478}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_x789056826}

[[NAT outbound port block group information]{lang="EN-US"}]{#struct_0_83269_x5501_1940073789}

[[NAT444]{lang="EN-US"}]{#struct_0_83269_x5501_x789253434}[端口块静态映射的配置信息]{style="font-family:宋体"}

[[Totally ]{lang="EN-US"}]{#struct_0_83269_x5501_x789187898}*[n]{lang="FR"}*[ ]{lang="FR"}[outbound port block group items]{lang="EN-US"}

[[当前存在]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_83269_x5501_404070958}[条]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块静态映射配置]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_83269_x5501_x789384506}

[[NAT444]{lang="EN-US"}]{#struct_0_83269_x5501_x1499326700}[端口块静态映射配置所在的接口]{style="font-family:宋体"}

[[Port block group]{lang="EN-US"}]{#struct_0_83269_x5501_x789318970}

[[端口块组编号]{style="font-family:宋体"}]{#struct_0_83269_x5501_x789515578}

[[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_x672075666}

[[显示配置的状态]{style="font-family:宋体"}]{#struct_0_83269_x5501_894008275}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_x1028371562}[：生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_537712379}[：不生效]{style="font-family:宋体"}

[[Reasons for inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_x625087035}

[[当]{style="font-family:宋体"}[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_940996906}[字段为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}[时，显示配置不生效的原因]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The following items don\'t exist or aren\'t effective: port block group]{lang="EN-US"}]{#struct_0_83269_x5501_x1787886449}[：配置中端口块组不存在或不生效]{style="font-family:宋体"}

[[Global flow-table status]{lang="EN-US"}]{#struct_0_83269_x5501_x2048309444}

[[针对]{style="font-family:宋体"}[Global]{lang="EN-US"}]{#struct_0_83269_x5501_x1206661977}[地址下发流表的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_x2048243908}[：生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x602990030}[：不生效]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x723127865}

[[Local  flow-table status]{lang="EN-US"}]{#struct_0_83269_x5501_x381252553}

[[针对]{style="font-family:宋体"}[Local]{lang="EN-US"}]{#struct_0_83269_x5501_x1823778035}[地址下发流表的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_x347946574}[：生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_2131318284}[：不生效]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x2048440516}

[[Reasons for flow-table inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_x1200260448}

[[当下发流表的状态为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x465157821}[时，显示流表不生效的原因]{style="font-family:宋体"}

[[其中，]{style="font-family:宋体"}[Not enough resources are available to complete the operation]{lang="EN-US"}]{#struct_0_83269_x5501_41308412}[表示因为资源不足导致下发流表失败]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_1250856984}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1206553558}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;
font-family:Wingdings"}**[nat outbound port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_479440553}

::: {#-2018595197 .myid}
[]{#_Toc404786490}[]{#struct_0_83269_x5501_x789450042}[]{#_Toc363572608}

**NAT命令 \-- NAT配置命令 \-- display nat port-block**

------------------------------------------------------------------------

[**[display ]{lang="EN-US"}[nat port-block]{lang="EN-US"}**]{#struct_0_83269_x5501_x751811347}[命令用来显示端口块表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x56656275}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_83269_x5501_x789646650}

[**[display nat port-block ]{lang="EN-US"}**[{ **dynamic** \[ **ds-lite-b4** \] \| **static** }]{lang="EN-US"}]{#struct_0_83269_x5501_33042022}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_83269_x5501_x1968166221}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display nat port-block ]{lang="EN-US"}**[{ **dynamic** \[ **ds-lite-b4** \] \| **static** } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_83269_x5501_x789581114}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_83269_x5501_x789122361}[模式：]{style="font-family:宋体"}

[**[display nat port-block ]{lang="EN-US"}**[{ **dynamic** \[ **ds-lite-b4** \] \| **static** } \[ ]{lang="EN-US"}]{#struct_0_83269_x5501_432823086}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x789056825}

[[任意视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_1940139325}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x71410392}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x789253433}

[[network-operator]{lang="EN-US"}]{#struct_0_83269_x5501_49532843}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_100942407}

[[mdc-operator]{lang="EN-US"}]{#struct_0_83269_x5501_x789187897}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_404529710}

[**[dynamic]{lang="EN-US"}**]{#struct_0_83269_x5501_x789384505}[：显示动态端口块表项。]{style="font-family:宋体"}

[**[ds-lite-b4]{lang="EN-US"}**]{#struct_0_83269_x5501_399212389}[：显示基于]{style="font-family:宋体"}[DS-Lite B4]{lang="EN-US"}[地址的端口块表项。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_83269_x5501_x1499392236}[：显示静态端口块表项。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x1682603829}[：显示指定单板上的]{style="font-family:宋体"}[端口块]{style="font-family:宋体"}[表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[端口块]{style="font-family:宋体"}[表项信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x789318969}[：显示指定成员设备上的]{style="font-family:宋体"}[端口块]{style="font-family:宋体"}[表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。若不指定该参数，则表示显示所有成员设备上的]{style="font-family:宋体"}[端口块]{style="font-family:宋体"}[表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_1620689942}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的端口块]{style="font-family:宋体"}[表项信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的端口块]{style="font-family:宋体"}[表项信息]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x789450041}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[端口块]{style="font-family:宋体"}[表项信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若不指定该参数，则表示显示所有成员设备的所有单板上的]{style="font-family:宋体"}[端口块]{style="font-family:宋体"}[表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x1679995636}[：]{style="font-family:宋体"}[显示指定单板上的端口块]{style="font-family:宋体"}[表项信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若不指定该参数，则表示显示所有单板上的端口块]{style="font-family:宋体"}[表项信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x751745811}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的端口块表项信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1957581917}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x789646649}[显示静态端口块表项。]{style="font-family:宋体"}

[[\<Sysname\> display nat port-block static]{lang="EN-US"}]{#struct_0_83269_x5501_33631845}

[Static port-block mapping tables:]{lang="EN-US"}

[Local VPN     Local IP         Global IP        Port block   Connections]{lang="EN-US"}

[\-\--           100.100.100.111  202.202.100.101  10001-10256  0]{lang="EN-US"}

[\-\--           100.100.100.112  202.202.100.101  10257-10512  0]{lang="EN-US"}

[\-\--           100.100.100.113  202.202.100.101  10513-10768  0]{lang="EN-US"}

[vpn012345678  100.100.100.113  202.202.100.101  10769-11024  0]{lang="EN-US"}

[901234567890]{lang="EN-US"}

[1234567]{lang="EN-US"}

[Total entries found: 4]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x789581113}[显示动态端口块表项。]{style="font-family:宋体"}

[[\<Sysname\> display nat port-block dynamic]{lang="EN-US"}]{#struct_0_83269_x5501_x331040412}

[Dynamic port-block mapping tables:]{lang="EN-US"}

[Local VPN     Local IP         Global IP        Port block   Connections]{lang="EN-US"}

[\-\--           101.1.1.12       192.168.135.201  10001-11024  1]{lang="EN-US"}

[Total entries found: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1547374028}[显示基于]{style="font-family:宋体"}[DS-Lite B4]{lang="EN-US"}[地址的端口块表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display nat port-block dynamic ds-lite-b4]{lang="EN-US"}]{#struct_0_83269_x5501_1973190501}

[Local VPN     DS-Lite B4 addr  Global IP        Port block   Connections]{lang="EN-US"}

[\-\--           2000::2          192.168.135.201  10001-11024  1]{lang="EN-US"}

[Total entries found: 1]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display nat port-block ]{lang="EN-US"}]{#struct_0_83269_x5501_151773614}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1291586605}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_x789122364}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_x789056828}

[[Static port-block mapping tables]{lang="EN-US"}]{#struct_0_83269_x5501_24739906}

[[静态端口块表项信息]{style="font-family:宋体"}]{#struct_0_83269_x5501_934094048}

[[Dynamic port-block mapping tables]{lang="EN-US"}]{#struct_0_83269_x5501_2073191103}

[[动态]{style="font-family:宋体"}]{#struct_0_83269_x5501_171619210}[端口块表项信息]{style="font-family:宋体"}

[[Local VPN]{lang="FR"}]{#struct_0_83269_x5501_x789253436}

[[私网]{style="font-family:宋体"}]{#struct_0_83269_x5501_49336235}[IP]{lang="FR"}[地址所属]{style="font-family:宋体"}[VPN]{lang="FR"}[，"]{style="font-family:宋体"}[\-\--]{lang="FR"}["表示不属于任何]{style="font-family:宋体"}[VPN]{lang="FR"}

[[Local IP]{lang="FR"}]{#struct_0_83269_x5501_x789187900}

[[私网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_x789384508}[地址]{style="font-family:宋体"}

[[DS-Lite B4 addr]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_83269_x5501_x305711896}

[[DS-Lite B4]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_83269_x5501_1614374441}[设备的]{style="font-size:10.0pt;font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Global IP]{lang="FR"}]{#struct_0_83269_x5501_x789318972}

[[公网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_x1910792247}[地址]{style="font-family:宋体"}

[[Port block]{lang="FR"}]{#struct_0_83269_x5501_x789515580}

[[端口块（起始端口[-]{lang="EN-US"}结束端口）]{style="font-family:宋体"}]{#struct_0_83269_x5501_x789450044}

[[Connections]{lang="FR"}]{#struct_0_83269_x5501_x789646652}

[[当前使用本端口块中的端口建立的连接数]{style="font-family:宋体"}]{#struct_0_83269_x5501_33173094}

[ ]{lang="EN-US"}

::: {#-367314176 .myid}
[]{#_Toc404786491}[]{#struct_0_83269_x5501_x789581116}[]{#_Toc363572609}

**NAT命令 \-- NAT配置命令 \-- display nat port-block-group**

------------------------------------------------------------------------

[**[display nat port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x331368092}[命令用来显示]{style="font-family:
宋体"}[NAT]{lang="EN-US"}[端口块组配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1268090643}

[**[display nat ]{lang="EN-US"}[port-block-group]{lang="EN-US"}**[ \[ *group-number* \]]{lang="EN-US"}]{#struct_0_83269_x5501_x789122363}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_432692014}

[[任意视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x789056827}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1940008253}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x850597711}

[[network-operator]{lang="EN-US"}]{#struct_0_83269_x5501_x789253435}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_49401771}

[[mdc-operator]{lang="EN-US"}]{#struct_0_83269_x5501_75230318}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x789187899}

[*[group-number]{lang="EN-US"}*]{#struct_0_83269_x5501_404136494}[：]{style="font-family:宋体"}[端口块组]{style="font-family:宋体"}[编号，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[。其中]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。如果不设置该值，则显示所有端口块组的配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x789384507}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1499261164}[显示所有端口块组的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display nat port-block-group]{lang="EN-US"}]{#struct_0_83269_x5501_x789318971}

[NAT port block group information:]{lang="EN-US"}

[  Totally 3 NAT port block groups.]{lang="EN-US"}

[  Port block group 1:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Block size: 256]{lang="EN-US"}

[    Local IP address information:]{lang="EN-US"}

[      Start address        End address          VPN instance]{lang="EN-US"}

[      172.16.1.1           172.16.1.254         \-\--]{lang="EN-US"}

[      192.168.1.1          192.168.1.254        vpna]{lang="EN-US"}

[      192.168.3.1          192.168.3.254        vpna]{lang="EN-US"}

[    Global IP pool information:]{lang="EN-US"}

[      Start address        End address]{lang="EN-US"}

[      201.1.1.1            201.1.1.10]{lang="EN-US"}

[      201.1.1.21           201.1.1.25]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Port block group 2:]{lang="EN-US"}

[    Port range: 10001-30000]{lang="EN-US"}

[    Block size: 500]{lang="EN-US"}

[    Local IP address information:]{lang="EN-US"}

[      Start address        End address          VPN instance]{lang="EN-US"}

[      10.1.1.1             10.1.10.255          vpnb]{lang="EN-US"}

[    Global IP pool information:]{lang="EN-US"}

[      Start address        End address]{lang="EN-US"}

[      202.10.10.101        202.10.10.120]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Port block group 3:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Block size: 256]{lang="EN-US"}

[    Local IP address information:]{lang="EN-US"}

[      Start address        End address          VPN instance]{lang="EN-US"}

[      \-\--                  \-\--                  \-\--]{lang="EN-US"}

[    Global IP pool information:]{lang="EN-US"}

[      Start address        End address]{lang="EN-US"}

[      \-\--                  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1910726711}[显示端口块组]{style="font-family:宋体"}[1]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display nat port-block-group 1]{lang="EN-US"}]{#struct_0_83269_x5501_x789515579}

[  Port block group 1:]{lang="EN-US"}

[    Port range: 1-65535]{lang="EN-US"}

[    Block size: 256]{lang="EN-US"}

[    Local IP address information:]{lang="EN-US"}

[      Start address        End address          VPN instance]{lang="EN-US"}

[      172.16.1.1           172.16.1.254         \-\--]{lang="EN-US"}

[      192.168.1.1          192.168.1.254        vpna]{lang="EN-US"}

[      192.168.3.1          192.168.3.254        vpna]{lang="EN-US"}

[    Global IP pool information:]{lang="EN-US"}

[      Start address        End address]{lang="EN-US"}

[      201.1.1.1            201.1.1.10]{lang="EN-US"}

[      201.1.1.21           201.1.1.25]{lang="EN-US"}

[]{#struct_0_83269_x5501_1206488022}[[表1-11 ]{lang="EN-US"}[display nat port-block-group ]{lang="EN-US"}]{#_Ref363572644}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1286096781}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_x789450043}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_x789646651}

[[NAT port block group information]{lang="EN-US"}]{#struct_0_83269_x5501_33107558}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x789581115}[端口块组]{style="font-family:宋体"}[信息]{style="font-family:宋体"}

[[Totally ]{lang="EN-US"}]{#struct_0_83269_x5501_x789122366}*[n]{lang="FR"}*[ NAT port block groups]{lang="EN-US"}

[[当前有]{style="font-family:宋体"}]{#struct_0_83269_x5501_432888622}*[n]{lang="FR"}*[个端口块组]{style="font-family:宋体"}

[[Port block group *m*]{lang="EN-US"}]{#struct_0_83269_x5501_x789056830}

[[端口块组编号]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_83269_x5501_x789253438}

[[Port range]{lang="EN-US"}]{#struct_0_83269_x5501_49205163}

[[公网地址的端口范围]{style="font-family:宋体"}]{#struct_0_83269_x5501_x789187902}

[[Block size]{lang="EN-US"}]{#struct_0_83269_x5501_x789384510}

[[端口块大小]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1499195629}

[[Local IP address information]{lang="EN-US"}]{#struct_0_83269_x5501_x789318974}

[[私网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_x789515582}[地址成员信息]{style="font-family:宋体"}

[[Global IP pool information]{lang="EN-US"}]{#struct_0_83269_x5501_1205898201}

[[公网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_x789450046}[地址成员信息]{style="font-family:宋体"}

[[Start address]{lang="EN-US"}]{#struct_0_83269_x5501_x789646654}

[[私网]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_83269_x5501_33304166}[公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址成员的起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果没有配置，则显示"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[End address]{lang="EN-US"}]{#struct_0_83269_x5501_x789581118}

[[私网]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_83269_x5501_x789122365}[公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址成员的成员结束]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果没有配置，则显示"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_83269_x5501_433085230}

[[私网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_x789056829}[地址成员所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。如果没有配置，则显示"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1939877181}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x789253437}

::: {#-347761546 .myid}
[]{#_Toc404786492}[]{#struct_0_83269_x5501_x879053844}

**NAT命令 \-- NAT配置命令 \-- display nat server**

------------------------------------------------------------------------

[**[display nat server]{lang="EN-US"}**]{#struct_0_83269_x5501_x1741326798}[命令用来显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1399340518}

[**[display nat server]{lang="EN-US"}**]{#struct_0_83269_x5501_2050447569}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x162666283}

[[任意]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1762796240}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_83269_x5501_75316}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1358774954}

[[network-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x1511566775}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x148228513}

[[mdc-operator]{lang="EN-US" style="color:black"}*[ ]{lang="EN-US" style="color:blue"}*]{#struct_0_83269_x5501_2016261507}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1923122119}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x661250824}[显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器的信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat server]{lang="EN-US"}]{#struct_0_83269_x5501_1358316199}

[NAT internal server information:]{lang="EN-US"}

[  Totally 4 internal servers.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/3]{lang="EN-US"}

[    Protocol: 6(TCP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.1/23]{lang="EN-US"}

[    Local IP/port : 192.168.10.15/23]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/4]{lang="EN-US"}

[    Protocol: 6(TCP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.1/23-30]{lang="EN-US"}

[    Local IP/port : 192.168.10.15-192.168.10.22/23]{lang="EN-US"}

[    Global VPN    : vpn1]{lang="EN-US"}

[    Local VPN     : vpn3]{lang="EN-US"}

[    Config status : Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN.]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/4]{lang="EN-US"}

[    Protocol: 255(Reserved)]{lang="EN-US"}

[    Global IP/port: 50.1.1.100/\-\--]{lang="EN-US"}

[    Local IP/port : 192.168.10.150/\-\--]{lang="EN-US"}

[    Global VPN    : vpn2]{lang="EN-US"}

[    Local VPN     : vpn4]{lang="EN-US"}

[    Config status : Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: interface IP address.]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/5]{lang="EN-US"}

[    Protocol: 17(UDP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.2/23]{lang="EN-US"}

[    Local IP/port : server group 1]{lang="EN-US"}

[                    1.1.1.1/21            (Connections: 10)]{lang="EN-US"}

[                    192.168.100.200/80    (Connections: 20)]{lang="EN-US"}

[    Global VPN    : vpn1]{lang="EN-US"}

[    Local VPN     : vpn3]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1653734257}[显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器的信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat server]{lang="EN-US"}]{#struct_0_83269_x5501_x537989010}

[NAT internal server information:]{lang="EN-US"}

[  Totally 4 internal servers.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/3]{lang="EN-US"}

[    Protocol: 6(TCP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.1/23]{lang="EN-US"}

[    Local IP/port : 192.168.10.15/23]{lang="EN-US"}

[    Service card  : \-\--]{lang="EN-US"}

[    Config status : Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      Service card not specified.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/4]{lang="EN-US"}

[    Protocol: 6(TCP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.1/23-30]{lang="EN-US"}

[    Local IP/port : 192.168.10.15-192.168.10.22/23]{lang="EN-US"}

[    Global VPN    : vpn1]{lang="EN-US"}

[    Local VPN     : vpn3]{lang="EN-US"}

[    Service card  : \-\--]{lang="EN-US"}

[    Config status : Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN.]{lang="EN-US"}

[      Service card not specified.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/4]{lang="EN-US"}

[    Protocol: 255(Reserved)]{lang="EN-US"}

[    Global IP/port: 50.1.1.100/\-\--]{lang="EN-US"}

[    Local IP/port : 192.168.10.150/\-\--]{lang="EN-US"}

[    Global VPN    : vpn2]{lang="EN-US"}

[    Local VPN     : vpn4]{lang="EN-US"}

[    Service card  : Slot 5]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/5]{lang="EN-US"}

[    Protocol: 17(UDP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.2/23]{lang="EN-US"}

[    Local IP/port : server group 1]{lang="EN-US"}

[                    1.1.1.1/21            (Connections: 10)]{lang="EN-US"}

[                    192.168.100.200/80    (Connections: 20)]{lang="EN-US"}

[    Global VPN    : vpn1]{lang="EN-US"}

[    Local VPN     : vpn10]{lang="EN-US"}

[    Service card  : Slot 5]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x827976909}[显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器的信息。（分布式设备]{style="font-family:宋体"}[－]{style="font-size:10.0pt;
font-family:宋体;color:black"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display nat server]{lang="EN-US"}]{#struct_0_83269_x5501_x894284906}

[NAT internal server information:]{lang="EN-US"}

[  Totally 4 internal servers.]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/3]{lang="EN-US"}

[    Protocol: 6(TCP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.1/23]{lang="EN-US"}

[    Local IP/port : 192.168.10.15/23]{lang="EN-US"}

[    Service card  : \-\--]{lang="EN-US"}

[    Config status : Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      Service card not specified.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/4]{lang="EN-US"}

[    Protocol: 6(TCP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.1/23-30]{lang="EN-US"}

[    Local IP/port : 192.168.10.15-192.168.10.22/23]{lang="EN-US"}

[    Global VPN    : vpn1]{lang="EN-US"}

[    Local VPN     : vpn3]{lang="EN-US"}

[    Service card  : \-\--]{lang="EN-US"}

[    Config status : Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      Service card not specified.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/4]{lang="EN-US"}

[    Protocol: 255(Reserved)]{lang="EN-US"}

[    Global IP/port: 50.1.1.100/\-\--]{lang="EN-US"}

[    Local IP/port : 192.168.10.150/\-\--]{lang="EN-US"}

[    Global VPN    : vpn2]{lang="EN-US"}

[    Local VPN     : vpn4]{lang="EN-US"}

[    Service card  : Chassis 2 Slot 5]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/5]{lang="EN-US"}

[    Protocol: 17(UDP)]{lang="EN-US"}

[    Global IP/port: 50.1.1.2/23]{lang="EN-US"}

[    Local IP/port : server group 1]{lang="EN-US"}

[                    1.1.1.1/21            (Connections: 10)]{lang="EN-US"}

[                    192.168.100.200/80    (Connections: 20)]{lang="EN-US"}

[    Global VPN    : vpn1]{lang="EN-US"}

[    Local VPN     : vpn3]{lang="EN-US"}

[    Service card  : Chassis 2 Slot 5]{lang="EN-US"}

[    Config status : Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[]{#struct_0_83269_x5501_87124363}[[表1-12 ]{lang="EN-US"}[display nat server]{lang="EN-US"}]{#_Ref334105524}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x785876121}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_1358250663}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_97854805}

[[NAT internal server information]{lang="EN-US"}]{#struct_0_83269_x5501_1333094553}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_1549091506}[内部服务器的配置信息]{style="font-family:宋体"}

[[Totally *n* internal servers]{lang="EN-US"}]{#struct_0_83269_x5501_183941232}

[[当前存在]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_83269_x5501_x1926103601}[条内部服务器配置]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_83269_x5501_637508277}

[[内部服务器配置所在的接口]{style="font-family:宋体"}]{#struct_0_83269_x5501_1358185127}

[[Protocol]{lang="EN-US"}]{#struct_0_83269_x5501_x1489904151}

[[内部服务器的协议编号以及协议名称]{style="font-family:宋体"}]{#struct_0_83269_x5501_x754104374}

[[Global IP/port]{lang="EN-US"}]{#struct_0_83269_x5501_x278126698}

[[内部服务器的外网地址]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_83269_x5501_x779567721}[端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Global IP]{lang="EN-US"}]{#struct_0_83269_x5501_x521713304}[可以是单个地址，也可以是一个连续的地址段。如果使用]{lang="EN-US" style="font-family:宋体"}[Easy IP]{lang="EN-US"}[方式，则此处显示指定的接口的地址；如果接口下没有配置地址，则]{lang="EN-US" style="font-family:宋体"}[Global IP]{lang="EN-US"}[显示为"]{lang="EN-US" style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[port]{lang="EN-US"}]{#struct_0_83269_x5501_1358119591}[可以是单个端口，也可以是一个连续的端口段。如果指定的协议没有端口的概念，则]{style="font-family:宋体"}[port]{lang="EN-US"}[显示为"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[Local IP/port]{lang="EN-US"}]{#struct_0_83269_x5501_437671208}

[[对于普通内部服务器，显示服务器的内网地址]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_83269_x5501_1519847831}[端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local IP]{lang="EN-US"}]{#struct_0_83269_x5501_x1874298694}[可以是单个地址，也可以是一个连续的地址段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[port]{lang="EN-US"}]{#struct_0_83269_x5501_600924371}[可以是单个端口，也可以是一个连续的端口段。如果指定的协议没有端口的概念，则]{style="font-family:宋体"}[port]{lang="EN-US"}[显示为"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[对于负载分担内部服务器，显示内部服务器组编号以及服务器组成员的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_1358054055}[地址、端口和连接数]{style="font-family:宋体"}

[[Global VPN]{lang="EN-US"}]{#struct_0_83269_x5501_x1080339800}

[[外网地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_83269_x5501_405257324}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。如果不属于任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则不显示该字段]{style="font-family:宋体"}

[[Local VPN]{lang="EN-US"}]{#struct_0_83269_x5501_1233302116}

[[内网地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_83269_x5501_209780341}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。]{style="font-family:宋体"} [如果不属于任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则不显示该字段]{style="font-family:宋体"}

[[ACL]{lang="EN-US"}]{#struct_0_83269_x5501_x87715852}

[[引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_83269_x5501_1478368089}[编号。如果没有配置，则不显示该字段]{style="font-family:宋体"}

[[Service card]{lang="EN-US"}]{#struct_0_83269_x5501_1028029395}

[[显示提供]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x894350442}[处理的业务板。如果接口下没有指定业务板，则显示为"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x2057149856}

[[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_x491065915}

[[显示配置的状态]{style="font-family:宋体"}]{#struct_0_83269_x5501_1075018026}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_x87781388}[：生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x538120082}[：不生效]{style="font-family:宋体"}

[[Reasons for inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_1027963859}

[[当]{style="font-family:宋体"}[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_x894415978}[字段为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}[时，显示配置不生效的原因]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The following items don\'t exist or aren\'t effective: local VPN, global VPN, interface IP address, server group, and ACL]{lang="EN-US"}]{#struct_0_83269_x5501_x2057215392}[：配置中内网地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例、外网地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例、接口地址、服务器组、]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或不生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service card not specified]{lang="EN-US"}]{#struct_0_83269_x5501_x491131451}[：没有指定]{style="font-family:
  宋体"}[提供]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[处理的]{lang="EN-US" style="font-family:宋体"}[业务板]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Server configuration conflicts]{lang="EN-US"}]{#struct_0_83269_x5501_x1653930865}[：]{style="font-family:
  宋体"}[NAT]{lang="EN-US"}[内部服务器配置冲突]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NAT address conflicts]{lang="EN-US"}]{#struct_0_83269_x5501_x87846924}[：]{lang="EN-US" style="font-family:
  宋体"}[NAT]{lang="EN-US"}[地址冲突]{lang="EN-US" style="font-family:
  宋体"}

[[Global flow-table status]{lang="EN-US"}]{#struct_0_83269_x5501_x2047981770}

[[针对]{style="font-family:宋体"}[Global]{lang="EN-US"}]{#struct_0_83269_x5501_x1102651763}[地址下发流表的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_422533585}[：生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x2048178378}[：不生效]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x975881999}

[[Local  flow-table status]{lang="EN-US"}]{#struct_0_83269_x5501_x768307601}

[[针对]{style="font-family:宋体"}[Local]{lang="EN-US"}]{#struct_0_83269_x5501_146362687}[地址下发流表的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_1325469477}[：生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x2048112842}[：不生效]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_1991566500}

[[Reasons for flow-table inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_x1857404608}

[[当下发流表的状态为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_413265183}[时，显示流表不生效的原因]{style="font-family:宋体"}

[[其中，]{style="font-family:宋体"}[Not enough resources are available to complete the operation]{lang="EN-US"}]{#struct_0_83269_x5501_x2048309450}[表示因为资源不足导致下发流表失败]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_1119002387}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1357988519}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat server]{lang="EN-US"}**]{#struct_0_83269_x5501_x1335113533}

::: {#-2052594180 .myid}
[]{#_Toc404786493}[]{#struct_0_83269_x5501_x1182763330}

**NAT命令 \-- NAT配置命令 \-- display nat server-group**

------------------------------------------------------------------------

[**[display nat server-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x1456949633}[命令用来显示]{style="font-family:
宋体"}[NAT]{lang="EN-US"}[内部服务器组的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_507550807}

[**[display nat server-group ]{lang="EN-US"}**[\[ *group-number* \]]{lang="EN-US"}]{#struct_0_83269_x5501_871726995}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1490202833}

[[任意]{style="font-family:宋体"}]{#struct_0_83269_x5501_x264228946}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x542082106}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1357922983}

[[network-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x547800388}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1556484569}

[[mdc-operator]{lang="EN-US" style="color:black"}*[ ]{lang="EN-US" style="color:blue"}*]{#struct_0_83269_x5501_1255625246}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_997973444}

[*[group-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x346086114}[：]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器组编号。]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果不设置该值，则显示所有内部服务器组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1826073401}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_159510509}[显示所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器组的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display nat server-group]{lang="EN-US"}]{#struct_0_83269_x5501_1357857447}

[NAT server group information:]{lang="EN-US"}

[  Totally 3 NAT server groups.]{lang="EN-US"}

[  Group Number        Inside IP             Port        Weight]{lang="EN-US"}

[  1                   192.168.0.26          23          100]{lang="EN-US"}

[                      192.168.0.27          23          500]{lang="EN-US"}

[  2                   \-\--                   \-\--         \-\--]{lang="EN-US"}

[  3                   192.168.0.26          69          100]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1255935024}[显示指定]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器组的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display nat server-group 1]{lang="EN-US"}]{#struct_0_83269_x5501_x2046020894}

[  Group Number        Inside IP             Port        Weight]{lang="EN-US"}

[  1                   192.168.0.26          23          100]{lang="EN-US"}

[                      192.168.0.27          23          500]{lang="EN-US"}

[ ]{lang="EN-US"}

[]{#struct_0_83269_x5501_x1507958445}[[表1-13 ]{lang="EN-US"}[display nat server-group]{lang="EN-US"}]{#_Ref334106521}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x755512285}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_2090368139}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_987670194}

[[NAT server group information]{lang="EN-US"}]{#struct_0_83269_x5501_1358840487}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_486679569}[内部服务器组信息]{style="font-family:宋体"}

[[Totally *n* NAT server groups]{lang="FR"}]{#struct_0_83269_x5501_1835501100}

[[当前有]{style="font-family:宋体"}]{#struct_0_83269_x5501_1518641117}*[n]{lang="FR"}*[个内部服务器组]{style="font-family:宋体"}

[[Group Number]{lang="FR"}]{#struct_0_83269_x5501_1283297352}

[[内部服务器组编号]{lang="EN-US" style="font-family:
  宋体"}]{#struct_0_83269_x5501_x225913464}

[[Inside IP]{lang="EN-US"}]{#struct_0_83269_x5501_1358774951}

[[内部服务器组成员在内网的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_x1511894455}[地址。如果没有配置，则显示"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_83269_x5501_x1098978015}

[[内部服务器组成员在内网的端口。如果没有配置，则显示"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}]{#struct_0_83269_x5501_814752975}["]{style="font-family:宋体"}

[[Weight]{lang="EN-US"}]{#struct_0_83269_x5501_x131893624}

[[内部服务器组成员的权重值。如果没有配置，则显示"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}]{#struct_0_83269_x5501_1358316200}["]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1660643730}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat server-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x1023626919}

::: {#-2107415383 .myid}
[]{#_Toc404786494}[]{#struct_0_83269_x5501_x1960984958}

**NAT命令 \-- NAT配置命令 \-- display nat session**

------------------------------------------------------------------------

[**[display nat session]{lang="EN-US"}**]{#struct_0_83269_x5501_x1829306748}[命令用来显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话，即]{style="font-family:宋体"}[经过]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址转换处理的会话。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1854637885}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_83269_x5501_1466178588}

[**[display nat session ]{lang="EN-US"}**[\[ { **source-ip** *source-ip* \| **destination-ip** *destination-ip* } \* ]{lang="EN-US"}]{#struct_0_83269_x5501_1874308813}[\[ **vpn-instance** *vpn-name* \]]{lang="DA"}[ ]{lang="DA"}[\] \[ **verbose** \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_83269_x5501_x943222701}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display nat session ]{lang="EN-US"}**[\[ { **source-ip** *source-ip* \| **destination-ip** *destination-ip* } \*]{lang="EN-US"}]{#struct_0_83269_x5501_1358250664}[ \[ **vpn-instance** *vpn -name* \]]{lang="DA"}[ ]{lang="DA"}[\] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_83269_x5501_98313557}[模式：]{style="font-family:宋体"}

[**[display nat session ]{lang="EN-US"}**[\[ { **source-ip** *source-ip* \| **destination-ip** *destination-ip* } \* ]{lang="EN-US"}]{#struct_0_83269_x5501_1687207746}[\[ **vpn-instance** *vpn -name* \]]{lang="DA"}[ ]{lang="DA"}[\] \[ ]{lang="EN-US"}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x721169016}

[[任意]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1911285178}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_331516500}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1323457109}

[[network-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x899367231}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_503945826}

[[mdc-operator]{lang="EN-US" style="color:black"}*[ ]{lang="EN-US" style="color:blue"}*]{#struct_0_83269_x5501_1358185128}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1489838615}

[**[source-ip]{lang="EN-US"}**[ *source-ip*]{lang="EN-US"}]{#struct_0_83269_x5501_x170122710}[：显示指定源地址的会话。]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[表示源地址，该地址必须是创建会话的报文的源地址。]{style="font-family:宋体"}

[**[destination-ip]{lang="EN-US"}**[ *destination-ip*]{lang="EN-US"}]{#struct_0_83269_x5501_2060512051}[：显示指定目的地址的会话。]{style="font-family:宋体"}*[destination-ip]{lang="EN-US"}*[表示目的地址，该地址必须是创建会话的报文的目的地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="DA"}**]{#struct_0_83269_x5501_x231591769}*[ vpn-name]{lang="DA"}*[：显示指定目的]{style="font-family:宋体"}[VPN]{lang="DA"}[的会话。]{style="font-family:宋体"}*[vpn-name]{lang="DA"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。该]{style="font-family:宋体"}[VPN]{lang="DA"}[必须是报文中携带的]{style="font-family:宋体"}[VPN]{lang="DA"}[。]{style="font-family:宋体"}[如果不指定该参数，则显示目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[不属于任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的会话。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x56201765}[：显示指定单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[若不指定该参数，则显示所有单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话（分布式设备]{style="font-family:宋体"}[－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x85241703}[：显示指定成员设备上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[若不指定该参数，则显示所有成员设备上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x974041221}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x959921587}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[若不指定该参数，则显示所有成员设备的所有单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_1910017282}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_83269_x5501_776830507}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_83269_x5501_1131970139}[：显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话的详细信息。如果不配置则显示会话的概要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1358119592}

[[如果不指定任何参数，则显示所有的]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_437605672}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1250174044}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1954058919}[显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话的详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat session verbose]{lang="EN-US"}]{#struct_0_83269_x5501_1358054056}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.10/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application: SSH]{lang="FR"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[[Total sessions found: 1]{lang="FR" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_83269_x5501_x1080405336}

[[\# ]{lang="FR"}]{#struct_0_83269_x5501_2146415738}[显示]{style="font-family:宋体"}[1]{lang="FR"}[号单板上]{style="font-family:
宋体"}[NAT]{lang="FR"}[会话的详细信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat session slot 1 verbose]{lang="EN-US"}]{#struct_0_83269_x5501_1357988520}

[Slot 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application: SSH]{lang="FR"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[[Total sessions found: 1]{lang="FR" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_83269_x5501_x1335703360}

[[\# ]{lang="FR"}]{#struct_0_83269_x5501_x286870076}[显示]{style="font-family:宋体"}[1]{lang="FR"}[号成员设备上]{style="font-family:
宋体"}[NAT]{lang="FR"}[会话的详细信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="FR"}[设备]{style="font-family:宋体"}[）]{style="font-family:
宋体"}

[[\<Sysname\> display nat session slot 1 verbose]{lang="FR"}]{#struct_0_83269_x5501_1357922984}

[Slot 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application: SSH]{lang="FR"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[[Total sessions found: 1]{lang="FR" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_83269_x5501_x547996996}

[[\# ]{lang="FR"}]{#struct_0_83269_x5501_x42445289}[显示]{style="font-family:宋体"}[1]{lang="FR"}[号成员设备上]{style="font-family:
宋体"}[1]{lang="FR"}[号单板的]{style="font-family:宋体"}[NAT]{lang="FR"}[会话的详细信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="FR"}[模式]{style="font-family:
宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat session chassis 1 slot 1 verbose]{lang="EN-US"}]{#struct_0_83269_x5501_1357857448}

[Slot 1 in chassis 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application: SSH]{lang="FR"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[[Total sessions found: 1]{lang="FR" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_83269_x5501_x1256524848}

[[\# ]{lang="FR"}]{#struct_0_83269_x5501_776961577}[显示]{style="font-family:宋体"}[1]{lang="FR"}[号单板的]{style="font-family:
宋体"}[0]{lang="FR"}[号]{style="font-family:宋体"}[CPU]{lang="FR"}[上]{style="font-family:宋体"}[NAT]{lang="FR"}[会话的详细信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat session slot 1 cpu 0 verbose]{lang="EN-US"}]{#struct_0_83269_x5501_776568361}

[CPU 0 on slot 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application: SSH]{lang="FR"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[[Total sessions found: 1]{lang="FR" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_83269_x5501_47027953}

[[\# ]{lang="FR"}]{#struct_0_83269_x5501_776437289}[显示]{style="font-family:宋体"}[1]{lang="FR"}[号成员设备的]{style="font-family:
宋体"}[0]{lang="FR"}[号]{style="font-family:宋体"}[CPU]{lang="FR"}[上]{style="font-family:宋体"}[NAT]{lang="FR"}[会话的详细信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="FR"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat session slot 1]{lang="FR"}[ cpu 1]{lang="EN-US"}]{#struct_0_83269_x5501_776699434}[ ]{lang="EN-US"}[verbose]{lang="FR"}

[CPU 0 on slot 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application: SSH]{lang="FR"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[[Total sessions found: 1]{lang="FR" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_83269_x5501_x1951856241}

[[\# ]{lang="FR"}]{#struct_0_83269_x5501_x1951987313}[显示]{style="font-family:宋体"}[1]{lang="FR"}[号成员设备上]{style="font-family:
宋体"}[1]{lang="FR"}[号单板的]{style="font-family:宋体"}[0]{lang="FR"}[号]{style="font-family:宋体"}[CPU]{lang="FR"}[上]{style="font-family:宋体"}[NAT]{lang="FR"}[会话的详细信息。]{style="font-family:
宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:
宋体"}[－]{style="font-family:宋体"}[IRF]{lang="FR"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat session chassis 1 slot 1 cpu 0 verbose]{lang="EN-US"}]{#struct_0_83269_x5501_x1952380529}

[CPU 0 on slot 1 in chassis 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application: SSH]{lang="FR"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[[Total sessions found: 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_83269_x5501_x1951921780}

[[表1-14 ]{lang="EN-US"}[display nat session]{lang="EN-US"}]{#struct_0_83269_x5501_1027771724}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_686476266}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_x12474340}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_x152412340}

[[Initiator]{lang="EN-US"}]{#struct_0_83269_x5501_1803684183}

[[发起方的会话信息]{style="font-family:宋体"}]{#struct_0_83269_x5501_1005843996}

[[Responder]{lang="FR"}]{#struct_0_83269_x5501_x1536840114}

[[响应方的会话信息]{style="font-family:宋体"}]{#struct_0_83269_x5501_1358840488}

[[Source IP/port]{lang="EN-US"}]{#struct_0_83269_x5501_486220817}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_1356372538}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[Destination IP/port]{lang="FR"}]{#struct_0_83269_x5501_x1712309247}

[[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_391470609}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[DS-Lite tunnel peer]{lang="EN-US"}]{#struct_0_83269_x5501_x250789030}

[[DS-Lite]{lang="FR"}]{#struct_0_83269_x5501_1956127468}[隧道对端地址。会话不属于任何]{style="font-family:宋体"}[DS-Lite]{lang="FR"}[隧道时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[本字段显示为]{style="font-family:宋体"}["]{style="font-family:宋体"}[-]{lang="FR"}["]{style="font-family:宋体"}

[[VPN instance/VLAN ID/VLL ID]{lang="FR"}]{#struct_0_83269_x5501_130086071}

[[会话所属的]{style="font-family:宋体"}[MPLS L3VPN/]{lang="EN-US"}]{#struct_0_83269_x5501_294855393}[二层转发时会话所属的]{style="font-family:宋体"}[VLAN ID/]{lang="EN-US"}[二层转发时会话所属的]{style="font-family:宋体"}[INLINE]{lang="EN-US"}[。如果未指定则显示"]{style="font-family:宋体"}[-/-/-]{lang="EN-US"}["]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_83269_x5501_1358774952}

[[传输层协议类型，包括：]{style="font-family:宋体"}[DCCP]{lang="EN-US"}]{#struct_0_83269_x5501_x1511697847}[、]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[、]{style="font-family:宋体"}[Raw IP ]{lang="EN-US"}[、]{style="font-family:宋体"}[SCTP]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP-Lite]{lang="EN-US"}

[[Inbound interface]{lang="FR"}]{#struct_0_83269_x5501_x250592422}

[[报文的入接口]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1895823054}

[[Source security zone]{lang="FR"}]{#struct_0_83269_x5501_x449454190}

[[源安全域，即入接口所属的安全域。若接口不属于任何安全域，则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_83269_x5501_427179753}["]{style="font-family:宋体"}

[[该参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x250657958}

[[State]{lang="EN-US"}]{#struct_0_83269_x5501_x42977207}

[[会话状态]{lang="EN-US" style="font-family:
  宋体"}]{#struct_0_83269_x5501_x2056656208}

[[Application]{lang="EN-US"}]{#struct_0_83269_x5501_x1370567152}

[[应用层协议类型，取值包括：]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1708511122}[FTP]{lang="EN-US"}[、]{style="font-family:宋体"}[DNS]{lang="EN-US"}[等，]{style="font-family:宋体"}[OTHER]{lang="FR"}[表示未知协议类型，其对应的端口为非知名端口]{style="font-family:宋体"}

[[Start time]{lang="FR"}]{#struct_0_83269_x5501_x800847518}

[[会话创建时间]{style="font-family:宋体"}]{#struct_0_83269_x5501_1113608118}

[[TTL]{lang="EN-US"}]{#struct_0_83269_x5501_x382424646}

[[会话剩余存活时间，单位为秒]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1370632688}

[[Initiator-\>Responder]{lang="FR"}]{#struct_0_83269_x5501_x1370698224}

[[发起方到响应方的报文数、报文字节数]{style="font-family:宋体"}]{#struct_0_83269_x5501_x62863546}

[[Responder-\>Initiator]{lang="FR"}]{#struct_0_83269_x5501_x212622390}

[[响应方到发起方的报文数、报文字节数]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1848907344}

[[Total sessions found]{lang="EN-US"}]{#struct_0_83269_x5501_x1370763760}

[[当前查找到的会话表总数]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1077012062}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_709581014}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset nat session]{lang="EN-US"}**]{#struct_0_83269_x5501_x2002304973}

::: {#1118470241 .myid}
[]{#_Toc404786495}[]{#struct_0_83269_x5501_x1342238077}

**NAT命令 \-- NAT配置命令 \-- display nat static**

------------------------------------------------------------------------

[**[display nat static]{lang="EN-US"}**]{#struct_0_83269_x5501_x284480764}[命令用来显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[静态地址转换的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_810566896}

[**[display nat static]{lang="EN-US"}**]{#struct_0_83269_x5501_1340072463}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370829296}

[[任意]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1823399223}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1124972124}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_38667132}

[[network-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x997219935}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_1293552653}

[[mdc-operator]{lang="EN-US" style="color:black"}*[ ]{lang="EN-US" style="color:blue"}*]{#struct_0_83269_x5501_x864391471}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1139108475}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1517701566}[显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[静态地址转换的配置信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat static]{lang="EN-US"}]{#struct_0_83269_x5501_x1370960368}

[Static NAT mappings:]{lang="EN-US"}

[  Totally 2 inbound static NAT mappings.]{lang="EN-US"}

[  Net-to-net:]{lang="EN-US"}

[    Global IP    : 1.1.1.1 - 1.1.1.255]{lang="EN-US"}

[    Local IP     : 2.2.2.0]{lang="EN-US"}

[    Netmask      : 255.255.255.0]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    ACL          : 2000]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IP-to-IP:]{lang="EN-US"}

[    Global IP    : 5.5.5.5]{lang="EN-US"}

[    Local IP     : 4.4.4.4]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    ACL          : 2000]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[   Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, global VPN, and ACL.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Totally 2 outbound static NAT mappings.]{lang="EN-US"}

[  Net-to-net:]{lang="EN-US"}

[    Local IP     : 1.1.1.1 - 1.1.1.255]{lang="EN-US"}

[    Global IP    : 2.2.2.0]{lang="EN-US"}

[    Netmask      : 255.255.255.0]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    ACL          : 2000]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IP-to-IP:]{lang="EN-US"}

[    Local IP     : 4.4.4.4]{lang="EN-US"}

[    Global IP    : 5.5.5.5]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    ACL:         : 2001]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, and global VPN.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interfaces enabled with static NAT:]{lang="EN-US"}

[  Totally 2 interfaces enabled with static NAT.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/3]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1433954321}[显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[静态地址转换的配置信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat static]{lang="EN-US"}]{#struct_0_83269_x5501_1698213561}

[Static NAT mappings:]{lang="EN-US"}

[  Totally 2 inbound static NAT mappings.]{lang="EN-US"}

[  Net-to-net:]{lang="EN-US"}

[    Global IP    : 1.1.1.1 - 1.1.1.255]{lang="EN-US"}

[    Local IP     : 2.2.2.0]{lang="EN-US"}

[    Netmask      : 255.255.255.0]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    ACL          : 2000]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IP-to-IP:]{lang="EN-US"}

[    Global IP   : 5.5.5.5]{lang="EN-US"}

[    Local IP     : 4.4.4.4]{lang="EN-US"}

[    Global VPN   : vpn3]{lang="EN-US"}

[    Local VPN    : vpn4]{lang="EN-US"}

[    ACL          : 2001]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, global VPN, and ACL.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[Totally 2 outbound static NAT mappings.]{lang="EN-US"}

[  Net-to-net:]{lang="EN-US"}

[    Local IP     : 1.1.1.1 - 1.1.1.255]{lang="EN-US"}

[    Global IP    : 2.2.2.0]{lang="EN-US"}

[    Netmask      : 255.255.255.0]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    ACL          : 2000]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IP-to-IP:]{lang="EN-US"}

[    Local IP     : 4.4.4.4]{lang="EN-US"}

[    Global IP    : 5.5.5.5]{lang="EN-US"}

[    Local VPN    : vpn4]{lang="EN-US"}

[    Global VPN   : vpn3]{lang="EN-US"}

[    ACL:         : 2000]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, and global VPN.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interfaces enabled with static NAT:]{lang="EN-US"}

[  Totally 2 interfaces enabled with static NAT.]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    Service card : Slot 5]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/3]{lang="EN-US"}

[    Service card : \-\--]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      Service card not specified.]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_132129620}[显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[静态地址转换的配置信息。（分布式设备]{style="font-family:宋体"}[－]{style="font-size:10.0pt;
font-family:宋体;color:black"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display nat static]{lang="EN-US"}]{#struct_0_83269_x5501_x318209074}

[Static NAT mappings:]{lang="EN-US"}

[  Totally 2 inbound static NAT mappings.]{lang="EN-US"}

[  Net-to-net:]{lang="EN-US"}

[    Global IP    : 1.1.1.1 - 1.1.1.255]{lang="EN-US"}

[    Local IP     : 2.2.2.0]{lang="EN-US"}

[    Netmask      : 255.255.255.0]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    ACL          : 2000]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IP-to-IP:]{lang="EN-US"}

[    Global IP    : 5.5.5.5]{lang="EN-US"}

[    Local IP     : 4.4.4.4]{lang="EN-US"}

[    Global VPN   : vpn3]{lang="EN-US"}

[    Local VPN    : vpn4]{lang="EN-US"}

[    ACL          : 2001]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, global VPN, and ACL.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[Totally 2 outbound static NAT mappings.]{lang="EN-US"}

[  Net-to-net:]{lang="EN-US"}

[    Local IP     : 1.1.1.1 - 1.1.1.255]{lang="EN-US"}

[    Global IP    : 2.2.2.0]{lang="EN-US"}

[    Netmask      : 255.255.255.0]{lang="EN-US"}

[    Local VPN    : vpn1]{lang="EN-US"}

[    Global VPN   : vpn2]{lang="EN-US"}

[    ACL          : 2000]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IP-to-IP:]{lang="EN-US"}

[    Local IP     : 4.4.4.4]{lang="EN-US"}

[    Global IP    : 5.5.5.5]{lang="EN-US"}

[    Local VPN    : vpn4]{lang="EN-US"}

[    Global VPN   : vpn3]{lang="EN-US"}

[    ACL:         : 2000]{lang="EN-US"}

[    Reversible   : Y]{lang="EN-US"}

[    Config status: Inactive]{lang="EN-US"}

[    Reasons for inactive status:]{lang="EN-US"}

[      The following items don\'t exist or aren\'t effective: local VPN, and global VPN.]{lang="EN-US"}

[    Global flow-table status: Active]{lang="EN-US"}

[    Local flow-table status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interfaces enabled with static NAT:]{lang="EN-US"}

[  Totally 2 interfaces enabled with static NAT.]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/2]{lang="EN-US"}

[    Service card : Chassis 2 Slot 5]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: GigabitEthernet1/3/0/3]{lang="EN-US"}

[    Service card : Chassis 2 Slot 5]{lang="EN-US"}

[    Config status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[]{#struct_0_83269_x5501_x1134641538}[[表1-15 ]{lang="EN-US"}[display nat static]{lang="EN-US"}]{#_Ref334167313}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x764304470}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_x741793211}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_995204308}

[[Static NAT mappings]{lang="EN-US"}]{#struct_0_83269_x5501_x1371025904}

[[静态地址转换的配置信息]{style="font-family:宋体"}]{#struct_0_83269_x5501_962792535}

[[Totally *n* inbound static NAT mappings]{lang="EN-US"}]{#struct_0_83269_x5501_x1985153790}

[[当前存在]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_83269_x5501_1090749323}[条入方向静态地址转换的配置]{style="font-family:宋体"}

[[Totally *n* outbound static NAT mappings]{lang="EN-US"}]{#struct_0_83269_x5501_x2119876901}

[[当前存在]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_83269_x5501_99836348}[条出方向静态地址转换的配置]{style="font-family:宋体"}

[[Net-to-net]{lang="EN-US"}]{#struct_0_83269_x5501_x1370042864}

[[网段到网段的静态地址转换映射]{style="font-family:宋体"}]{#struct_0_83269_x5501_1051998011}

[[IP-to-IP]{lang="EN-US"}]{#struct_0_83269_x5501_1314834627}

[[IP]{lang="EN-US"}]{#struct_0_83269_x5501_x656353653}[到]{style="font-family:宋体"}[IP]{lang="EN-US"}[的静态地址转换映射]{style="font-family:宋体"}

[[Local IP]{lang="EN-US"}]{#struct_0_83269_x5501_2125829233}

[[内网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_x540983347}[地址或地址范围]{style="font-family:宋体"}

[[Global IP]{lang="EN-US"}]{#struct_0_83269_x5501_x1370108400}

[[外网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_1467558295}[地址或地址范围]{style="font-family:宋体"}

[[Netmask]{lang="EN-US"}]{#struct_0_83269_x5501_x822694310}

[[IP]{lang="EN-US"}]{#struct_0_83269_x5501_354496301}[地址掩码]{style="font-family:宋体"}

[[Local VPN]{lang="EN-US"}]{#struct_0_83269_x5501_506119600}

[[内网地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_83269_x5501_x1370567151}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。如果不属于任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则不显示该字段]{style="font-family:宋体"}

[[Global VPN]{lang="EN-US"}]{#struct_0_83269_x5501_1020372233}

[[外网地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_83269_x5501_x62382788}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。如果不属于任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则不显示该字段]{style="font-family:宋体"}

[[ACL]{lang="EN-US"}]{#struct_0_83269_x5501_x166294200}

[[引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_83269_x5501_x1370632687}[编号。如果没有配置，则不显示该字段]{style="font-family:宋体"}

[[Reversible]{lang="EN-US"}]{#struct_0_83269_x5501_818394661}

[[是否允许反向地址转换。若其值为"]{style="font-family:宋体"}[Y]{lang="EN-US"}]{#struct_0_83269_x5501_89160535}["，则表示]{style="font-family:宋体"}[在某方向上发起的连接已成功建立地址转换表项的情况下，允许反方向发起的连接使用已建立的地址转换表项进行地址转换]{style="font-family:宋体"}

[[如果没有配置，则不显示该字段]{style="font-family:宋体"}]{#struct_0_83269_x5501_1294797962}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_131998548}

[[Interfaces enabled with static NAT]{lang="EN-US"}]{#struct_0_83269_x5501_379557984}

[[静态地址转换在接口下的使能情况]{style="font-family:宋体"}]{#struct_0_83269_x5501_x638437600}

[[Totally *n* interfaces enabled with static NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1370698223}

[[当前有]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_83269_x5501_1503220395}[个接口使能了静态地址转换]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_83269_x5501_1589716004}

[[使能静态地址转换功能的接口]{style="font-family:宋体"}]{#struct_0_83269_x5501_560160838}

[[Service card]{lang="EN-US"}]{#struct_0_83269_x5501_x1837435456}

[[显示提供]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_1294732426}[服务的业务板。如果接口下没有指定业务板，则显示为"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_131933012}

[[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_x318405682}

[[显示配置的状态]{style="font-family:宋体"}]{#struct_0_83269_x5501_x540418314}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_x137133787}[：生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x1299933201}[：不生效]{style="font-family:宋体"}

[[Reasons for inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_1832234681}

[[当]{style="font-family:宋体"}[Config status]{lang="EN-US"}]{#struct_0_83269_x5501_1381895987}[字段为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}[时，显示配置不生效的原因]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The following items don\'t exist or aren\'t effective:]{lang="EN-US"}[ local VPN, global VPN, and ACL]{lang="EN-US"}]{#struct_0_83269_x5501_1025600091}[：配置中内网地址所属的]{style="font-family:
  宋体"}[VPN]{lang="EN-US"}[实例、外网地址所属的]{style="font-family:
  宋体"}[VPN]{lang="EN-US"}[实例、]{style="font-family:
  宋体"}[ACL]{lang="EN-US"}[不存在或不存在]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service card not specified]{lang="EN-US"}]{#struct_0_83269_x5501_x540483850}[：没有指定]{style="font-family:
  宋体"}[提供]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[服务的]{lang="EN-US" style="font-family:宋体"}[业务板]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NAT address conflicts]{lang="EN-US"}]{#struct_0_83269_x5501_x1703283264}[：]{lang="EN-US" style="font-family:
  宋体"}[NAT]{lang="EN-US"}[地址冲突]{lang="EN-US" style="font-family:
  宋体"}

[[Global flow-table status]{lang="EN-US"}]{#struct_0_83269_x5501_x482159969}

[[针对]{style="font-family:宋体"}[Global]{lang="EN-US"}]{#struct_0_83269_x5501_884216868}[地址下发流表的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_x382795170}[：生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_705661971}[：不生效]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_x482356577}

[[Local  flow-table status]{lang="EN-US"}]{#struct_0_83269_x5501_439430598}

[[针对]{style="font-family:宋体"}[Local]{lang="EN-US"}]{#struct_0_83269_x5501_x396320412}[地址下发流表的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_83269_x5501_228795845}[：生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_x482291041}[：不生效]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_405715167}

[[Reasons for flow-table inactive status]{lang="EN-US"}]{#struct_0_83269_x5501_x2104321265}

[[当下发流表的状态为]{style="font-family:宋体"}[Inactive]{lang="EN-US"}]{#struct_0_83269_x5501_321010025}[时，显示流表不生效的原因]{style="font-family:宋体"}

[[其中，]{style="font-family:宋体"}[Not enough resources are available to complete the operation]{lang="EN-US"}]{#struct_0_83269_x5501_x481439073}[表示因为资源不足导致下发流表失败]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_83269_x5501_578557106}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1792886661}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat static]{lang="EN-US"}**]{#struct_0_83269_x5501_x1370763759}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat static net-to-net]{lang="EN-US"}**]{#struct_0_83269_x5501_845367775}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat static enable]{lang="EN-US"}**]{#struct_0_83269_x5501_1379864096}

::: {#1165772359 .myid}
[]{#_Toc404786496}[]{#struct_0_83269_x5501_x220461454}

**NAT命令 \-- NAT配置命令 \-- display nat statistics**

------------------------------------------------------------------------

[**[display nat statistics]{lang="EN-US"}**]{#struct_0_83269_x5501_989099510}[命令用来显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1471206767}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_83269_x5501_1177022701}

[**[display nat]{lang="EN-US"}**[ **statistics** \[ **summary** \]]{lang="EN-US"}]{#struct_0_83269_x5501_x1029366211}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_83269_x5501_1415264849}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display nat]{lang="EN-US"}**[ **statistics** \[ **summary** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_83269_x5501_x1370829295}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_83269_x5501_905484132}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display nat]{lang="EN-US"}**[ **statistics** \[ **summary** \] \[ ]{lang="EN-US"}]{#struct_0_83269_x5501_x54931704}**[chassis]{lang="SV"}**[ *chassis-number* **slot** *slot-number*]{lang="SV"}[ ]{lang="SV"}[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x184759807}

[[任意]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1132325680}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x72575344}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_201219919}

[[network-operator]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_974006407}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_205164280}

[[mdc-operator]{lang="EN-US" style="color:black"}*[ ]{lang="EN-US" style="color:blue"}*]{#struct_0_83269_x5501_x1370894831}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1933928811}

[**[summary]{lang="EN-US"}**]{#struct_0_83269_x5501_x251051176}[：显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息的摘要信息。不指定该参数时，显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息的详细信息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_644921549}[：显示指定单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若不指定该参数，]{style="font-family:宋体"}[则显示所有单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_427477063}[：显示指定成员设备上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。若不指定该参数，]{style="font-family:宋体"}[则显示所有成员设备上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x974172293}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_681386086}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若不指定该参数，]{style="font-family:宋体"}[则显示所有成员设备的所有单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[-IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_1512827691}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x1952183923}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_766568614}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_628225213}[显示所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息的详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat statistics]{lang="EN-US"}]{#struct_0_83269_x5501_x1370960367}

[  Total session entries: 100]{lang="EN-US"}

[  Total EIM entries: 1]{lang="EN-US"}

[  Total inbound NO-PAT entries: 0]{lang="EN-US"}

[  Total outbound NO-PAT entries: 0]{lang="EN-US"}

[  Total static port block entries: 10]{lang="EN-US"}

[  Total dynamic port block entries: 15]{lang="EN-US"}

[  Active static port block entries: 0]{lang="EN-US"}

[  Active dynamic port block entries: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1596555340}[显示所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息的详细信息。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat statistics]{lang="EN-US"}]{#struct_0_83269_x5501_1645852118}

[Slot 1:]{lang="EN-US"}

[  Total session entries: 100]{lang="EN-US"}

[  Total EIM entries: 1]{lang="EN-US"}

[  Total inbound NO-PAT entries: 0]{lang="EN-US"}

[  Total outbound NO-PAT entries: 0]{lang="EN-US"}

[  Total static port block entries: 10]{lang="EN-US"}

[  Total dynamic port block entries: 15]{lang="EN-US"}

[  Active static port block entries: 0]{lang="EN-US"}

[  Active dynamic port block entries: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_580868504}[显示所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息的详细信息。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat statistics]{lang="EN-US"}]{#struct_0_83269_x5501_2131385015}

[Slot 1 in chassis 1:]{lang="EN-US"}

[  Total session entries: 100]{lang="EN-US"}

[  Total EIM entries: 1]{lang="EN-US"}

[  Total inbound NO-PAT entries: 0]{lang="EN-US"}

[  Total outbound NO-PAT entries: 0]{lang="EN-US"}

[  Total static port block entries: 10]{lang="EN-US"}

[  Total dynamic port block entries: 15]{lang="EN-US"}

[  Active static port block entries: 0]{lang="EN-US"}

[  Active dynamic port block entries: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1596555341}[显示所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息的详细信息。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat statistics]{lang="EN-US"}]{#struct_0_83269_x5501_1645786582}

[CPU 0 on slot 1:]{lang="EN-US"}

[  Total session entries: 100]{lang="EN-US"}

[  Total EIM entries: 1]{lang="EN-US"}

[  Total inbound NO-PAT entries: 0]{lang="EN-US"}

[  Total outbound NO-PAT entries: 0]{lang="EN-US"}

[  Total static port block entries: 10]{lang="EN-US"}

[  Total dynamic port block entries: 15]{lang="EN-US"}

[  Active static port block entries: 0]{lang="EN-US"}

[  Active dynamic port block entries: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1009612838}[显示所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息的详细信息。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat statistics]{lang="EN-US"}]{#struct_0_83269_x5501_x1347390829}

[CPU 0 on slot 1 in chassis 1:]{lang="EN-US"}

[  Total session entries: 100]{lang="EN-US"}

[  Total EIM entries: 1]{lang="EN-US"}

[  Total inbound NO-PAT entries: 0]{lang="EN-US"}

[  Total outbound NO-PAT entries: 0]{lang="EN-US"}

[  Total static port block entries: 10]{lang="EN-US"}

[  Total dynamic port block entries: 15]{lang="EN-US"}

[  Active static port block entries: 0]{lang="EN-US"}

[  Active dynamic port block entries: 0]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display nat statistics]{lang="EN-US"}]{#struct_0_83269_x5501_881781097}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x769486033}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_2037325753}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_2109063403}

[[Total session entries]{lang="EN-US"}]{#struct_0_83269_x5501_x2067488050}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1206758615}[会话表项个数]{style="font-family:宋体"}

[[Total EIM entries]{lang="EN-US"}]{#struct_0_83269_x5501_x665756021}

[[EIM]{lang="EN-US"}]{#struct_0_83269_x5501_x1371025903}[表项个数]{style="font-family:宋体"}

[[Total inbound]{lang="EN-US"}]{#struct_0_83269_x5501_x959521766}[ ]{lang="EN-US" style="font-size:8.5pt;
  font-family:\"Courier New\""}[NO-PAT entries ]{lang="EN-US"}

[[入方向的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}]{#struct_0_83269_x5501_1514241489}[表项个数]{style="font-family:宋体"}

[[Total outbound]{lang="EN-US"}]{#struct_0_83269_x5501_x1157197629}[ ]{lang="EN-US" style="font-size:8.5pt;
  font-family:\"Courier New\""}[NO-PAT entries ]{lang="EN-US"}

[[出方向的]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}]{#struct_0_83269_x5501_x2006234550}[表项个数]{style="font-family:宋体"}

[[Total static port block entries]{lang="EN-US"}]{#struct_0_83269_x5501_x1952314995}

[[当前配置创建的静态端口块表项个数]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1952249459}

[[Total dynamic port block entries]{lang="EN-US"}]{#struct_0_83269_x5501_x1952446067}

[[当前配置可创建的动态端口块表项个数，即可分配的动态端口块总数，包括已分配的端口块和尚未分配的端口块]{style="font-family:宋体"}]{#struct_0_83269_x5501_x385837835}

[[Active static port block entries]{lang="EN-US"}]{#struct_0_83269_x5501_x385772299}

[[当前正在使用的静态端口块表项个数]{style="font-family:宋体"}]{#struct_0_83269_x5501_x385968907}

[[Active dynamic port block entries]{lang="EN-US"}]{#struct_0_83269_x5501_x385903371}

[[当前已创建的动态端口块表项个数，即已分配的动态端口块个数]{style="font-family:宋体"}]{#struct_0_83269_x5501_x386099979}

[]{#_Ref311387206}[[ ]{lang="EN-US"}]{#_Ref311208464}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x250920104}[显示所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息的概要信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display nat statistics summary]{lang="EN-US"}]{#struct_0_83269_x5501_x250723496}

[EIM: Total EIM entries.]{lang="EN-US"}

[SPB: Total static port block entries.]{lang="EN-US"}

[DPB: Total dynamic port block entries.]{lang="EN-US"}

[ASPB: Active static port block entries.]{lang="EN-US"}

[ADPB: Active dynamic port block entries.]{lang="EN-US"}

[Sessions  EIM       SPB       DPB       ASPB      ADPB]{lang="EN-US"}

[100       1         10        15        0         0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x359759803}[显示所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息的概要信息。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat statistics summary]{lang="EN-US"}]{#struct_0_83269_x5501_1185555177}

[EIM: Total EIM entries.]{lang="EN-US"}

[SPB: Total static port block entries.]{lang="EN-US"}

[DPB: Total dynamic port block entries.]{lang="EN-US"}

[ASPB: Active static port block entries.]{lang="EN-US"}

[ADPB: Active dynamic port block entries.]{lang="EN-US"}

[Slot Sessions  EIM       SPB       DPB       ASPB      ADPB]{lang="EN-US"}

[2    0         0         0         1572720   0         0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1524219345}[显示所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息的概要信息。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat statistics summary]{lang="EN-US"}]{#struct_0_83269_x5501_x359759806}

[EIM: Total EIM entries.]{lang="EN-US"}

[SPB: Total static port block entries.]{lang="EN-US"}

[DPB: Total dynamic port block entries.]{lang="EN-US"}

[ASPB: Active static port block entries.]{lang="EN-US"}

[ADPB: Active dynamic port block entries.]{lang="EN-US"}

[Chassis Slot Sessions  EIM       SPB       DPB       ASPB      ADPB]{lang="EN-US"}

[1       2    0         0         0         1572720   0         0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x305818396}[显示所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息的概要信息。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat statistics summary]{lang="EN-US"}]{#struct_0_83269_x5501_x1185245499}

[EIM: Total EIM entries.]{lang="EN-US"}

[SPB: Total static port block entries.]{lang="EN-US"}

[DPB: Total dynamic port block entries.]{lang="EN-US"}

[ASPB: Active static port block entries.]{lang="EN-US"}

[ADPB: Active dynamic port block entries.]{lang="EN-US"}

[Slot CPU Sessions  EIM       SPB       DPB       ASPB      ADPB]{lang="EN-US"}

[2    1   0         0         0         1572720   0         0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_915904194}[显示所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[统计信息的概要信息。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display nat statistics summary]{lang="EN-US"}]{#struct_0_83269_x5501_x1380463102}

[EIM: Total EIM entries.]{lang="EN-US"}

[SPB: Total static port block entries.]{lang="EN-US"}

[DPB: Total dynamic port block entries.]{lang="EN-US"}

[ASPB: Active static port block entries.]{lang="EN-US"}

[ADPB: Active dynamic port block entries.]{lang="EN-US"}

[Chassis Slot CPU Sessions  EIM       SPB       DPB       ASPB      ADPB]{lang="EN-US"}

[1       2    1   0         0         0         1572720   0         0]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display nat statistics summary]{lang="EN-US"}]{#struct_0_83269_x5501_1515305939}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_688793994}[[字段]{style="font-family:黑体"}]{#struct_0_83269_x5501_x250789032}

[[描述]{style="font-family:黑体"}]{#struct_0_83269_x5501_x250592424}

[[Chassis]{lang="EN-US"}]{#struct_0_83269_x5501_x250657960}

[[IRF]{lang="EN-US"}]{#struct_0_83269_x5501_x251116711}[成员编号]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_83269_x5501_x251182247}

[[单板所在的槽位号（]{style="font-family:宋体"}]{#struct_0_83269_x5501_x250985639}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[IRF]{lang="EN-US"}]{#struct_0_83269_x5501_x251051175}[中的成员编号（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[CPU]{lang="EN-US"}]{#struct_0_83269_x5501_x250854567}

[[CPU]{lang="EN-US"}]{#struct_0_83269_x5501_x250920103}[编号]{style="font-family:宋体"}

[[Sessions]{lang="EN-US"}]{#struct_0_83269_x5501_x250723495}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x250789031}[会话表项个数]{style="font-family:宋体"}

[[EIM]{lang="EN-US"}]{#struct_0_83269_x5501_x250592423}

[[EIM]{lang="EN-US"}]{#struct_0_83269_x5501_x250657959}[表项个数]{style="font-family:宋体"}

[[SPB]{lang="EN-US"}]{#struct_0_83269_x5501_1314967233}

[[当前配置创建的静态端口块表项个数]{style="font-family:宋体"}]{#struct_0_83269_x5501_1314901697}

[[DPB]{lang="EN-US"}]{#struct_0_83269_x5501_1315098305}

[[当前配置可创建的动态端口块表项个数，即可分配的动态端口块总数，包括已分配的端口块和尚未分配的端口块]{style="font-family:宋体"}]{#struct_0_83269_x5501_103590397}

[[ASPB]{lang="EN-US"}]{#struct_0_83269_x5501_1315032769}

[[当前正在使用的静态端口块表项个数]{style="font-family:宋体"}]{#struct_0_83269_x5501_1315229377}

[[ADPB]{lang="EN-US"}]{#struct_0_83269_x5501_1315163841}

[[当前已创建的动态端口块表项个数，即已分配的动态端口块个数]{style="font-family:宋体"}]{#struct_0_83269_x5501_1315360449}

[ ]{lang="EN-US"}

::: {#-661135231 .myid}
[]{#_Toc404786497}[]{#struct_0_83269_x5501_x386034443}[]{#_Toc363572615}

**NAT命令 \-- NAT配置命令 \-- global-ip-pool**

------------------------------------------------------------------------

[**[global-ip-pool]{lang="PT-BR"}**]{#struct_0_83269_x5501_1244272238}[命令用来添加一个公网地址成员。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_83269_x5501_x386231051}**[global-ip-pool]{lang="PT-BR"}**[命令用来删除一个公网地址成员。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_882751710}

[**[global-ip-pool]{lang="PT-BR"}**[ ]{lang="PT-BR"}*[start-address]{lang="EN-US"}*[ *end-address*]{lang="EN-US"}]{#struct_0_83269_x5501_x386165515}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_83269_x5501_2032110447}**[global-ip-pool]{lang="PT-BR"}**[ ]{lang="PT-BR"}*[start-address]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x386362123}

[[不存在公网地址成员。]{style="font-family:宋体"}]{#struct_0_83269_x5501_x655271083}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x386296587}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1886245514}[端口块组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x385837834}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1032233792}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x385772298}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x2102174752}

[*[start-address end-address]{lang="EN-US"}*]{#struct_0_83269_x5501_x385968906}[：公网地址成员的起始]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址和结束]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[；如果]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[和]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*[相同，则表示只有一个地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1243963273}

[[在]{style="font-family:宋体"}[NAT444]{lang="EN-US"}]{#struct_0_83269_x5501_x385903370}[端口块静态映射中，端口基于公网地址成员的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为私网地址成员的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址分配端口块。一个公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址可对应的端口块个数，由端口块组配置的公网地址端口范围和端口块大小决定（端口范围除以端口块大小）。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1709387601}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个端口块组内，可以配置多个公网地址成员，但各公网地址成员之间的]{style="font-family:宋体"}]{#struct_0_83269_x5501_x386099978}[IP]{lang="EN-US"}[地址不能重叠。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同端口块组间的公网地址成员的]{style="font-family:宋体"}]{#struct_0_83269_x5501_1324487622}[IP]{lang="EN-US"}[地址可以重叠，但要保证在有地址重叠时端口范围不重叠。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x386034442}

[[\# ]{lang="PT-BR"}]{#struct_0_83269_x5501_1244337774}[在端口块组]{style="font-family:宋体"}[1]{lang="EN-US"}[中]{style="font-family:宋体"}[添加一个公网]{style="font-family:宋体"}[地址成员，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[从]{style="font-family:宋体"}[202.10.1.1]{lang="EN-US"}[到]{style="font-family:宋体"}[202.10.1.10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x386231050}

[\[Sysname\] nat port-block-group 1]{lang="EN-US"}

[\[Sysname-port-block-group-1\] global-ip-pool 202.10.1.1 202.10.1.10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_882817246}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x386165514}
:::

::: {#-1623895185 .myid}
[]{#_Toc404786498}[]{#struct_0_83269_x5501_x1077822051}

**NAT命令 \-- NAT配置命令 \-- inside ip**

------------------------------------------------------------------------

[**[inside ip]{lang="FR"}**]{#struct_0_83269_x5501_x1370042863}[命令用来添加一个内部服务器组成员。]{style="font-family:宋体"}

[**[undo inside ip]{lang="EN-US"}**]{#struct_0_83269_x5501_1811512898}[命令用来删除一个内部服务器组成员。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x647292075}

[**[inside ip]{lang="EN-US"}***[ inside-ip]{lang="EN-US"}*[ **port** *port-number* \[ **weight** *weight-value* \]]{lang="EN-US"}]{#struct_0_83269_x5501_x1131206800}

[**[undo inside]{lang="PT-BR"}**]{#struct_0_83269_x5501_x214128989}[ **ip** *inside-ip* ]{lang="PT-BR"}**[port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1974372630}

[[内部服务器组内没有内部服务器组成员。]{style="font-family:宋体"}]{#struct_0_83269_x5501_1786177618}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1394879198}

[[内部服务器组视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_753625482}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370108399}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x1618145239}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_x1150561868}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1789753861}

[*[inside-ip]{lang="EN-US"}*]{#struct_0_83269_x5501_637246931}[：]{style="font-family:宋体"}[内部服务器组成员的]{style="font-family:宋体"}[IP]{lang="FR"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x536150644}[：]{style="font-family:宋体"}[内部服务器组成员提供服务的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[65535]{lang="FR"}[（]{style="font-family:宋体"}[FTP]{lang="FR"}[数据端口号]{style="font-family:
宋体"}[20]{lang="FR"}[除外）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[weight ]{lang="FR"}**]{#struct_0_83269_x5501_1933828619}*[weight-value]{lang="FR"}*[：]{style="font-family:
宋体"}[内部服务器组成员的权重。]{style="font-family:宋体"}*[weight-value]{lang="FR"}*[表示权值，取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[1000]{lang="FR"}[，缺省为]{style="font-family:
宋体"}[100]{lang="FR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1737836310}

[[内部服务器组成员按照权重比例对外提供服务，权重值越大的内部服务器组成员对外提供服务的比重越大。]{style="font-family:宋体"}]{#struct_0_83269_x5501_292618801}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370567154}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1423656760}[为内部服务器组]{style="font-family:宋体"}[1]{lang="EN-US"}[添加一个内部服务器组成员，其]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.2]{lang="EN-US"}[，服务端口号为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_1121012322}

[[\[Sysname\] nat server-group 1]{lang="EN-US"}]{#struct_0_83269_x5501_x1053287144}

[[\[Sysname-nat-server-group-1\] inside ip 10.1.1.2 port 30]{lang="EN-US"}]{#struct_0_83269_x5501_x1176338374}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1148495765}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat server-group]{lang="EN-US"}**]{#struct_0_83269_x5501_617398085}
:::

::: {#392365000 .myid}
[]{#_Toc404786499}[]{#struct_0_83269_x5501_x385837837}[]{#_Toc363572617}

**NAT命令 \-- NAT配置命令 \-- local-ip-address**

------------------------------------------------------------------------

[**[local-ip-address]{lang="PT-BR"}**]{#struct_0_83269_x5501_x385772301}[命令用来添加一个私网地址成员。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_83269_x5501_x145400873}**[local-ip-address]{lang="PT-BR"}**[命令用来删除一个私网地址成员。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x385968909}

[**[local-ip-address ]{lang="EN-US"}***[start-address]{lang="EN-US"}*[ *end-address* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_83269_x5501_x385903373}

[**[undo]{lang="EN-US"}**[ **local-ip-address** *start-address* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_83269_x5501_x1709190993}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x386099981}

[[不存在私网地址成员。]{style="font-family:宋体"}]{#struct_0_83269_x5501_1324946369}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x386034445}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_1243879022}[端口块组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x386231053}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_882882782}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x386165517}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_2031979375}

[*[start-address]{lang="EN-US"}[ end-address]{lang="EN-US"}*]{#struct_0_83269_x5501_x386362125}[：私网地址成员的起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和结束]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[；如果]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[和]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*[相同，则表示只有一个地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_83269_x5501_x386296589}[：私网地址成员所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示私网地址成员不属于任何一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1886376586}

[[私网地址成员的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_x385837836}[地址作为端口块的使用者，基于端口块组配置的公网地址成员的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为其分配端口块。在一个端口块组内，一个私网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址只分配一个端口块。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_83269_x5501_1032364864}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个端口块组内，可以配置多个私网地址成员，但各私网地址成员之间的]{style="font-family:宋体"}]{#struct_0_83269_x5501_x385772300}[IP]{lang="EN-US"}[地址不能重叠。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同端口块组间的私网地址成员的]{style="font-family:宋体"}]{#struct_0_83269_x5501_x145335337}[IP]{lang="EN-US"}[地址可以重叠。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果一个端口块组中的私网地址总数超过可分配的端口块总数（端口范围除以端口块大小），则在进行]{style="font-family:宋体"}]{#struct_0_83269_x5501_x385968908}[NAT444]{lang="EN-US"}[端口块静态映射时，超出部分的私网地址将无法分配到端口块。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1244618633}

[[\# ]{lang="PT-BR"}]{#struct_0_83269_x5501_x385903372}[在端口块组]{style="font-family:宋体"}[1]{lang="EN-US"}[中]{style="font-family:宋体"}[添加一个私网]{style="font-family:宋体"}[地址成员，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[从]{style="font-family:宋体"}[172.16.1.1]{lang="EN-US"}[到]{style="font-family:宋体"}[172.16.1.255]{lang="EN-US"}[，所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x386099980}

[\[Sysname\] nat port-block-group 1]{lang="EN-US"}

[\[Sysname-port-block-group-1\] local-ip-address 172.16.1.1 172.16.1.255 vpn-instance vpn1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1325011905}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x386034444}
:::

::: {#1779661608 .myid}
[]{#_Toc404786500}[]{#struct_0_83269_x5501_x796256212}

**NAT命令 \-- NAT配置命令 \-- nat address-group**

------------------------------------------------------------------------

[**[nat address-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x1370632690}[命令用来]{style="font-family:宋体"}[创建]{style="font-family:宋体"}[一个地址组，并进入地址组视图]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo nat address-group]{lang="EN-US"}**]{#struct_0_83269_x5501_1221744724}[命令用来]{style="font-family:宋体"}[删除指定的地址组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x947035883}

[**[nat address-group ]{lang="EN-US"}***[group-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x1593265519}

[**[undo nat address-group ]{lang="EN-US"}***[group-number]{lang="EN-US"}*]{#struct_0_83269_x5501_1957146063}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1428133550}

[[不存在地址组]{style="font-family:宋体"}]{#struct_0_83269_x5501_995416899}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x2115508261}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x636478552}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370698226}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1099935868}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_x1972587175}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1361571089}

[*[group-number]{lang="EN-US"}*]{#struct_0_83269_x5501_62739006}[：地址组编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[。其中]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_938878060}

[[一个地址组是多个地址组成员的集合，各个地址组成员通过]{style="font-family:宋体"}**[address]{lang="EN-US"}**]{#struct_0_83269_x5501_1890227481}[命令配置。当需要对数据报文进行动态地址转换时，其源地址将被转换为地址组成员中的某个地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1473039746}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x75359336}[创建一个地址组，编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x1370763762}

[\[Sysname\] nat address-group 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_2055155820}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[address]{lang="EN-US"}**]{#struct_0_83269_x5501_x786116314}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat address-group]{lang="EN-US"}**]{#struct_0_83269_x5501_1756835227}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_x28320509}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat inbound]{lang="EN-US"}**]{#struct_0_83269_x5501_x620786874}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat outbound]{lang="EN-US"}**]{#struct_0_83269_x5501_322967621}
:::

::: {#1990072196 .myid}
[]{#_Toc404786501}[]{#struct_0_83269_x5501_429146729}

**NAT命令 \-- NAT配置命令 \-- nat alg**

------------------------------------------------------------------------

[**[nat alg]{lang="EN-US"}**]{#struct_0_83269_x5501_x1370829298}[命令用来开启指定或所有协]{style="font-family:宋体"}[议类型的]{style="font-family:宋体"}[NAT ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo nat alg]{lang="EN-US"}**]{#struct_0_83269_x5501_952538299}[命令用来关闭指定或所有协议类型的]{style="font-family:宋体"}[NAT ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370894834}

[**[nat alg]{lang="EN-US"}**[ { **all** \| **dns** \| **ftp** \| **h323** \| **icmp-error** ]{lang="EN-US"}]{#struct_0_83269_x5501_1530644284}[\| **ils** \| **mgcp** \| **nbt** \| **pptp** \| **rsh** \| ]{lang="ES-AR"}**[rtsp]{lang="EN-US"}**[ \| **sccp** ]{lang="EN-US"}[\|]{lang="ES-AR"}[ ]{lang="ES-AR"}**[sip]{lang="EN-US"}**[ ]{lang="EN-US"}[\| **sqlnet** \| ]{lang="ES-AR"}**[tftp ]{lang="EN-US"}**[\| ]{lang="ES-AR"}**[xdmcp]{lang="EN-US"}**[ }]{lang="EN-US"}

[**[undo nat alg]{lang="EN-US"}**[ { **all** \| **dns** \| **ftp** \| **h323** \| **icmp-error** ]{lang="EN-US"}]{#struct_0_83269_x5501_1576878708}[\| **ils** \| **mgcp** \| **nbt** \| **pptp** \| **rsh** \| ]{lang="ES-AR"}**[rtsp]{lang="EN-US"}**[ \| **sccp** ]{lang="EN-US"}[\| ]{lang="ES-AR"}**[sip]{lang="EN-US"}**[ ]{lang="EN-US"}[\| **sqlnet** \| ]{lang="ES-AR"}**[tftp]{lang="EN-US"}**[ ]{lang="EN-US"}[\| ]{lang="ES-AR"}**[xdmcp]{lang="EN-US"}**[ }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x939815130}

[[所有协议类型的]{style="font-family:宋体"}[NAT ALG]{lang="EN-US"}]{#struct_0_83269_x5501_x148857839}[功能均处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_836815564}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x727665537}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1696900039}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x606644346}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_x1370960370}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1490937434}

[**[all]{lang="EN-US"}**]{#struct_0_83269_x5501_x1330140088}[：所有可指定的协议的]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[dns]{lang="EN-US"}**]{#struct_0_83269_x5501_236534252}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[DNS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[ftp]{lang="EN-US"}**]{#struct_0_83269_x5501_x831049760}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[h323]{lang="EN-US"}**]{#struct_0_83269_x5501_950407658}[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体"}[H323]{lang="EN-US" style="color:black"}[协议的]{style="font-family:宋体;color:black"}[ALG]{lang="EN-US" style="color:
black"}[功能。]{style="font-family:宋体;color:black"}

[**[icmp-error]{lang="EN-US"}**]{#struct_0_83269_x5501_x526308689}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错控制报文的]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[ils]{lang="ES-AR"}**]{#struct_0_83269_x5501_2135684761}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[ILS]{lang="EN-US"}[（]{style="font-family:宋体"}[Internet Locator Service]{lang="EN-US"}[，互联网定位服务）协议的]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[mgcp]{lang="ES-AR"}**]{#struct_0_83269_x5501_x1948502414}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[MGCP]{lang="EN-US"}[（]{style="font-family:宋体"}[Media Gateway Control Protocol]{lang="EN-US"}[，媒体网关控制协议）协议的]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[nbt]{lang="ES-AR"}**]{#struct_0_83269_x5501_785535978}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[NBT]{lang="EN-US"}[（]{style="font-family:宋体"}[NetBIOS over TCP/IP]{lang="EN-US"}[，基于]{style="font-family:宋体"}[TCP/IP]{lang="EN-US"}[的网络基本输入输出系统）协议的]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[pptp]{lang="ES-AR"}**]{#struct_0_83269_x5501_2135488153}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[PPTP]{lang="EN-US"}[（]{style="font-family:宋体"}[Point-to-Point Tunneling Protocol]{lang="EN-US"}[，点到点隧道协议）协议的]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[rsh]{lang="ES-AR"}**]{#struct_0_83269_x5501_x413815309}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[RSH]{lang="EN-US"}[（]{style="font-family:宋体"}[Remote Shell]{lang="EN-US"}[，远程外壳）协议的]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[rtsp]{lang="PT-BR"}**]{#struct_0_83269_x5501_984131046}[：表示]{style="font-family:宋体"}[RTSP]{lang="PT-BR"}[（]{style="font-family:宋体"}[Real Time Streaming Protocol]{lang="PT-BR"}[，实时流协议）协议]{style="font-family:宋体"}[的]{style="font-family:宋体"}[ALG]{lang="PT-BR"}[功能。]{style="font-family:宋体"}

[**[sccp]{lang="EN-US"}**]{#struct_0_83269_x5501_x1601949454}[：表示]{style="font-family:宋体"}[SCCP]{lang="EN-US"}[（]{style="font-family:宋体"}[Skinny Client Control Protocol]{lang="EN-US"}[，瘦小客户端控制协议）协议的]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[sip]{lang="PT-BR"}**]{#struct_0_83269_x5501_x589995521}[：表示]{style="font-family:宋体"}[SIP]{lang="PT-BR"}[（]{style="font-family:宋体"}[Session Initiation Protocol]{lang="PT-BR"}[，会话初始协议）协议]{style="font-family:宋体"}[的]{style="font-family:宋体"}[ALG]{lang="PT-BR"}[功能。]{style="font-family:宋体"}

[**[sqlnet]{lang="ES-AR"}**]{#struct_0_83269_x5501_2135553689}[：表示]{style="font-family:宋体"}[SQLNET]{lang="EN-US"}[协议的]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[tftp]{lang="PT-BR"}**]{#struct_0_83269_x5501_x1371025906}[：表示]{style="font-family:宋体"}[TFTP]{lang="PT-BR"}[协议]{style="font-family:宋体"}[的]{style="font-family:宋体"}[ALG]{lang="PT-BR"}[功能。]{style="font-family:宋体"}

[**[xdmcp]{lang="EN-US"}**]{#struct_0_83269_x5501_1152351568}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[XDMCP]{lang="EN-US"}[（]{style="font-family:宋体"}[X Display Manager Control Protocol]{lang="EN-US"}[，]{style="font-family:宋体"}[X]{lang="EN-US"}[显示监控）协议的]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x200006879}

[[ALG]{lang="EN-US"}]{#struct_0_83269_x5501_x1055336015}[（]{style="font-family:宋体"}[Application]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[Gateway]{lang="EN-US"}[，应用层网关）主要完成对应用层报文的解析和处理。通常情况下，]{style="font-family:宋体"}[NAT]{lang="EN-US"}[只对报文头中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口信息进行转换，不对应用层数据载荷中的字段进行分析和处理。然而对于一些应用层协议，它们的报文的数据载荷中可能包含]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或端口信息，这些载荷信息也必须进行有效的转换，否则可能导致功能不正常。]{style="font-family:宋体"}

[[例如，]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_83269_x5501_75033293}[应用由数据连接和控制连接共同完成，而数据连接使用的地址和端口由控制连接协商报文中的载荷信息决定，这就需要]{style="font-family:宋体"}[ALG]{lang="EN-US"}[利用]{style="font-family:宋体"}[NAT]{lang="EN-US"}[的相关转换配置]{style="font-family:宋体"}[来完成载荷信息的转换，以保证后续数据连接的正确建立。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_453127385}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1972139247}[开启]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_2063604601}

[[\[Sysname\] nat alg ftp]{lang="EN-US"}]{#struct_0_83269_x5501_x1927734791}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370042866}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_x2080169871}
:::

::: {#-417115213 .myid}
[]{#_Toc404786502}[]{#struct_0_83269_x5501_x1234749182}

**NAT命令 \-- NAT配置命令 \-- nat dns-map**

------------------------------------------------------------------------

[**[nat dns-map]{lang="EN-US"}**]{#struct_0_83269_x5501_x161831898}[命令用来配置一条域名到内部服务器的映射]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo nat dns-map]{lang="EN-US"}**]{#struct_0_83269_x5501_378771050}[命令用来删除一条域名到内部服务器的映射]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x150507758}

[**[nat dns-map domain ]{lang="FR"}**]{#struct_0_83269_x5501_x747126222}*[domain-name]{lang="FR"}***[ protocol ]{lang="FR"}***[pro-type]{lang="EN-US"}*[ { ]{lang="EN-US"}**[interface ]{lang="DA"}***[interface-type]{lang="DA"}*[ *interface-number* ]{lang="DA"}*[\|]{lang="FR"}***[ ip ]{lang="FR"}***[global-ip ]{lang="FR"}*[}]{lang="FR"}**[ port ]{lang="FR"}***[global-port]{lang="FR"}*

[**[undo nat dns-map domain ]{lang="FR"}**]{#struct_0_83269_x5501_259020074}*[domain-name]{lang="FR"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x288994331}

[[不存在域名到内部服务器的映射。]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1370108402}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1664609587}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x888550728}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_800539849}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1876746931}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_1206448203}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_845137982}

[**[domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_83269_x5501_1088712502}[：指定]{style="font-family:宋体"}[内部服务器的合法域名。]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[表示内部服务器的域名，]{style="font-family:宋体"}[由"]{style="font-family:宋体"}[.]{lang="EN-US"}["分隔的字符串组成（如]{style="font-family:宋体"}[aabbcc.com]{lang="EN-US"}[），每个字符串的长度不超过]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，包括"]{style="font-family:宋体"}[.]{lang="EN-US"}["在内的总长度不超过]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符。不区分大小写，字符串中可以包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["或"]{style="font-family:宋体"}[.]{lang="EN-US"}["]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[protocol ]{lang="EN-US"}***[pro-type]{lang="EN-US"}*]{#struct_0_83269_x5501_x475492901}[：]{style="font-family:宋体"}[指定内部服务器的协议类型。]{style="font-family:宋体"}*[pro-type]{lang="EN-US"}*[表示具体的协议类型，取值为]{style="font-family:宋体"}**[tcp]{lang="EN-US"}**[或]{style="font-family:宋体"}**[udp]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x1370567153}[：]{style="font-family:宋体"}[表示使用指定接口的地址作为内部服务器的外网地址。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ ]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[接口类型和接口编号。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ip ]{lang="EN-US"}***[global-ip]{lang="EN-US"}*]{#struct_0_83269_x5501_x142427181}[：]{style="font-family:宋体"}[指定内部服务器提供给外部网络访问的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[global-ip]{lang="EN-US"}*[表示外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[port ]{lang="EN-US"}***[global-port]{lang="EN-US"}*]{#struct_0_83269_x5501_531417679}[：]{style="font-family:宋体"}[指定内部服务器提供给外部网络访问的服务端口号，可输入的形式如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[数字：取值范围为]{style="font-family:宋体"}]{#struct_0_83269_x5501_529390913}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[协议名称：为]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1205129938}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，例如]{style="font-family:宋体"}**[ftp]{lang="EN-US"}**[、]{style="font-family:宋体"}**[telnet]{lang="EN-US"}**[等。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x815392687}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1713641202}[的]{style="font-family:宋体"}[DNS mapping]{lang="EN-US"}[功能需要和]{style="font-family:宋体"}[内部服务器]{style="font-family:宋体"}[配合使用，主要应用于]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器在外网，应用服务器在内网（在]{style="font-family:宋体"}[NAT]{lang="EN-US"}[设备上有对应的]{style="font-family:宋体"}**[nat]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[server]{lang="EN-US"}**[配置），内网用户需要通过域名访问内网应用服务器的场景。]{style="font-family:宋体"}[NAT]{lang="EN-US"}[设备]{style="font-family:宋体"}[对来自外网的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[响应]{style="font-family:宋体"}[报文进行]{style="font-family:宋体"}[DNS]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[ALG]{lang="EN-US"}[处理时，由于载荷中只包含域名和应用服务器的外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址（不包含传输协议类型和端口号），当接口上存在多条]{style="font-family:宋体"}[NAT]{lang="EN-US"}[服务器配置且使用相同的外网地址而内网地址不同时，]{style="font-family:宋体"}[DNS]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[ALG]{lang="EN-US"}[仅使用]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址来匹配]{style="font-family:宋体"}[内部]{style="font-family:宋体"}[服务器可能会得到错误的匹配结果。因此需要借助]{style="font-family:宋体"}[DNS mapping]{lang="EN-US"}[的]{style="font-family:宋体"}[配置，指定域名与应用服务器的外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口和协议的映射关系，由域名获取应用服务器的外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口和协议，进而（在当前]{style="font-family:宋体"}[NAT]{lang="EN-US"}[接口上）精确匹配]{style="font-family:宋体"}[内部]{style="font-family:宋体"}[服务器配置获取应用服务器的内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[设备可支持配置多条]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1670343117}[域名到内部服务器的映射]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370632689}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x700635113}[某公司内部对外提供]{style="font-family:宋体"}[Web]{lang="EN-US"}[服务，内部服务器的域名为]{style="font-family:宋体"}[www.server.com]{lang="EN-US"}[，对外的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[202.112.0.1]{lang="EN-US"}[，服务端口号为]{style="font-family:宋体"}[12345]{lang="EN-US"}[。配置一条域名到内部服务器的映射，使得公司内部用户可以通过域名访问内部]{style="font-family:宋体"}[Web]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_1904097451}

[[\[Sysname\] nat dns-map domain www.server.com protocol tcp ip 202.112.0.1 port 12345]{lang="EN-US"}]{#struct_0_83269_x5501_656441790}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1374184863}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_873727830}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat dns-map]{lang="EN-US"}**]{#struct_0_83269_x5501_x957492291}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[nat server]{lang="EN-US"}**]{#struct_0_83269_x5501_541002074}
:::

::: {#2116993812 .myid}
[]{#_Toc404786503}[]{#struct_0_83269_x5501_1657205789}

**NAT命令 \-- NAT配置命令 \-- nat hairpin enable**

------------------------------------------------------------------------

[**[nat hairpin enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x1370698225}[命令用来使能]{style="font-family:宋体"}[NAT]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[hairpin]{lang="EN-US"}[功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo nat hairpin enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x1628947487}[用来关闭]{style="font-family:宋体"}[NAT]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[hairpin]{lang="EN-US"}[功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x395789596}

[**[nat hairpin enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x396227362}

[**[undo nat hairpin enable]{lang="EN-US"}**]{#struct_0_83269_x5501_619026968}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1136647813}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_912609993}[ ]{lang="EN-US" style="font-family:宋体"}[hairpin]{lang="EN-US"}[功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x657364260}

[[接口视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1341972523}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370763761}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_489071879}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_353935150}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_632461212}

[[NAT hairpin]{lang="EN-US"}]{#struct_0_83269_x5501_x1443561879}[功能用于满足位于内网侧的用户之间或用户与服务器之间通过]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址进行访问的需求，需要与内部服务器（]{style="font-family:宋体"}**[nat server]{lang="EN-US"}**[）、出方向动态地址转换（]{style="font-family:宋体"}**[nat outbound]{lang="EN-US"}**[）或出方向静态地址转换（]{style="font-family:宋体"}**[nat static outbound]{lang="EN-US"}**[）配合工作。使能]{style="font-family:宋体"}[NAT hairpin]{lang="EN-US"}[的内网侧接口上会对报文同时进行源地址和目的地址的转换。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1279245313}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x413953255}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口下开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[hairpin]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x1370829297}

[\[Sysname\] ]{lang="EN-US"}[interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] nat hairpin enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x257315282}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_494447401}
:::

::: {#751298357 .myid}
[]{#_Toc404786504}[]{#struct_0_83269_x5501_1677155564}

**NAT命令 \-- NAT配置命令 \-- nat inbound**

------------------------------------------------------------------------

[**[nat inbound]{lang="EN-US"}**]{#struct_0_83269_x5501_1865913022}[命令用来配置入方向动态地址转换。]{style="font-family:宋体"}

[**[undo nat inbound]{lang="EN-US"}**]{#struct_0_83269_x5501_25800820}[命令用来删除指定的入方向动态地址转换。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_427982366}

[**[nat inbound ]{lang="EN-US"}***[acl-number ]{lang="EN-US"}***[address-group]{lang="EN-US"}**[ *group-number* \[ **vpn-instance** *vpn-instance-name* \] \[ **no-pat** \[ **reversible** \] \[ **add-route** \] \]]{lang="EN-US"}]{#struct_0_83269_x5501_6984497}

[**[undo]{lang="EN-US"}**[ **nat inbound** *acl-number*]{lang="EN-US"}]{#struct_0_83269_x5501_1161741469}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370894833}

[[不存在入方向动态地址转换配置。]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1198239071}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1583726106}

[[接口视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_1812164582}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1115608938}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x1643992648}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_x1924112875}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1130385380}

[*[acl-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x1484200413}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[address-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x1370960369}[：指定地址转换使用的地址组。]{style="font-family:宋体"}*[group-number]{lang="EN-US"}*[为地址组编号，取值范围]{style="font-family:宋体"}[与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_83269_x5501_431442403}[：指定地址组中的地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示地址组中的地址不属于任何一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[no-pat]{lang="EN-US"}**]{#struct_0_83269_x5501_x1035287791}[：表示使用]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[方式进行转换，即转换时不使用报文的端口信息。如果未指定本参数，则表示使用]{style="font-family:宋体"}[PAT]{lang="EN-US"}[方式进行转换，即转换时使用报文的端口信息。]{style="font-family:宋体"}[PAT]{lang="EN-US"}[方式仅支持]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[查询报文，由于]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文没有端口的概念，我们将]{style="font-family:宋体"}[ICMP ID]{lang="EN-US"}[作为]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文的源端口。]{style="font-family:宋体"}

[**[reversible]{lang="EN-US"}**]{#struct_0_83269_x5501_275016116}[：表示允许反向地址转换。即，在外网用户主动向内网发起连接并成功触发建立地址转换表项的情况下，允许内网向该外网用户发起的连接使用已建立的地址转换表项进行目的地址转换。]{style="font-family:宋体"}

[**[add-route]{lang="EN-US"}**]{#struct_0_83269_x5501_x850484339}[：为转换后的地址添加路由表，其目的地址是转换后的地址，出接口为进行地址转换的接口，下一跳为该报文转换前的源地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_336732190}

[[从配置了入方向地址转换的]{style="font-family:宋体"}]{#struct_0_83269_x5501_1754513284}[接口接收到的符合]{style="font-family:宋体"}[ACL permit]{lang="EN-US"}[规则]{style="font-family:宋体"}[的报文，会使用地址组]{style="font-family:宋体"}*[group-number]{lang="EN-US"}*[中的地址进行源地址转换。]{style="font-family:宋体"}

[[入方向地址转换]{style="font-family:宋体"}]{#struct_0_83269_x5501_106284708}[有两种转换方式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PAT]{lang="EN-US"}]{#struct_0_83269_x5501_785875721}[方式：对于从外网到内网的报文，如果符合]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，则使用地址组中的地址进行源地址转换，同时转换源端口（]{style="font-family:宋体"}[IP1/port1]{lang="EN-US"}[转换为]{style="font-family:宋体"}[IP2/port2]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NO-PAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1371025905}[方式：对于从外网到内网的报文，如果符合]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，则使用地址组中的地址]{style="font-family:宋体"}[进行源地址转换，不转换源端口（]{style="font-family:宋体"}[IP1]{lang="EN-US"}[转换为]{style="font-family:宋体"}[IP2]{lang="EN-US"}[）；如果用户配置了]{style="font-family:宋体"}**[reversible]{lang="EN-US"}**[，则允许内网通过]{style="font-family:宋体"}[IP2]{lang="EN-US"}[主动访问外网]{style="font-family:宋体"}[，]{style="font-family:宋体"}[对于此类访问报文，需要进行]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（提取报文的源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口和目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口，并将目的地址转换为]{style="font-family:宋体"}[IP1]{lang="EN-US"}[，然后将源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口和目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口互换去匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[），只有反向匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的报文才能进行转换（将目的地址]{style="font-family:宋体"}[IP2]{lang="EN-US"}[转换为]{style="font-family:宋体"}[IP1]{lang="EN-US"}[），否则不予转换。]{style="font-family:宋体"}

[**[nat inbound]{lang="EN-US"}**]{#struct_0_83269_x5501_x1766090820}[命令]{style="font-family:宋体"}[通常与]{style="font-family:宋体"}**[nat]{lang="EN-US"}**[ ]{lang="EN-US" style="font-family:宋体"}**[outbound]{lang="EN-US"}**[、]{style="font-family:宋体"}**[nat]{lang="EN-US"}**[ ]{lang="EN-US" style="font-family:宋体"}**[server]{lang="EN-US"}**[或]{style="font-family:宋体"}**[nat]{lang="EN-US"}**[ ]{lang="EN-US" style="font-family:宋体"}**[static]{lang="EN-US"}**[配合使用，用于支持在外网侧口上对报文同时进行源和目的转换，即]{style="font-family:宋体"}[双向]{style="font-family:宋体"}[NAT]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_83269_x5501_814229282}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个地址组被]{lang="EN-US" style="font-family:宋体"}**[nat inbound]{lang="EN-US"}**]{#struct_0_83269_x5501_528118893}[配置]{style="font-family:宋体"}[引用后，]{lang="EN-US" style="font-family:宋体"}[就]{style="font-family:宋体"}[不能再被]{lang="EN-US" style="font-family:宋体"}**[nat ]{lang="EN-US"}[out]{lang="EN-US"}[bound]{lang="EN-US"}**[配置]{style="font-family:
宋体"}[引用。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个地址组被]{lang="EN-US" style="font-family:宋体"}[PAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1594637962}[方式的]{lang="EN-US" style="font-family:宋体"}**[nat inbound]{lang="EN-US"}**[配置引用后，不能再被]{lang="EN-US" style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[方式的]{lang="EN-US" style="font-family:宋体"}**[nat inbound]{lang="EN-US"}**[配置引用，反之亦然。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在一个接口下，一个]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_83269_x5501_x140514758}[只能被一个]{lang="EN-US" style="font-family:宋体"}**[nat inbound]{lang="EN-US"}**[引用。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[add-route]{lang="EN-US"}**]{#struct_0_83269_x5501_x184450098}[参数不能应用在内网与外网地址重叠的组网场景中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{style="font-family:宋体"}]{#struct_0_83269_x5501_1834237640}**[add-route]{lang="EN-US"}**[参数，则有报文命中该配置时，设备会自动添加路由表项：目的地址为本次地址转换使用的地址组中的地址，出接口为本配置所在接口，下一跳地址为报文的源地址；如果没有指定]{style="font-family:宋体"}**[add-route]{lang="EN-US"}**[参数，则用户需要在设备上手工添加路由。由于自动添加路由表项速度较慢，通常建议手工添加路由。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口下可同时配置多条入方向地址转换。]{style="font-family:宋体"}]{#struct_0_83269_x5501_x2000111728}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370042865}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1676885344}[配置]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[，]{style="font-family:宋体"}[允许对]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn10]{lang="EN-US"}[内]{style="font-family:宋体"}[10.110.10.0/24]{lang="EN-US"}[网段的主机进行地址转换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_466496843}

[[\[Sysname\] acl basic 2001]{lang="EN-US"}]{#struct_0_83269_x5501_x866805590}

[[\[Sysname-acl-ipv4-basic-2001\] rule permit vpn-instance vpn10 source 10.110.10.0 0.0.0.255]{lang="EN-US"}]{#struct_0_83269_x5501_x525768490}

[[\[Sysname-acl-ipv4-basic-2001\] rule deny]{lang="EN-US"}]{#struct_0_83269_x5501_1130407513}

[[\[Sysname-acl-ipv4-basic-2001\] quit]{lang="EN-US"}]{#struct_0_83269_x5501_x2051361083}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1833926542}[配置]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] ip vpn-instance vpn10]{lang="EN-US"}]{#struct_0_83269_x5501_1461330867}

[[\[Sysname-vpn-instance-vpn10\] route-distinguisher 100:001]{lang="EN-US"}]{#struct_0_83269_x5501_x1370108401}

[[\[Sysname-vpn-instance-vpn10\] vpn-target 100:1 export-extcommunity]{lang="EN-US"}]{#struct_0_83269_x5501_x1261325060}

[[\[Sysname-vpn-instance-vpn10\] vpn-target 100:1 import-extcommunity]{lang="EN-US"}]{#struct_0_83269_x5501_1407856983}

[[\[Sysname-vpn-instance]{lang="FR"}[-vpn10]{lang="EN-US"}]{#struct_0_83269_x5501_1116736544}[\] quit]{lang="FR"}

[[\#  ]{lang="FR"}]{#struct_0_83269_x5501_1321463294}[配置地址]{style="font-family:宋体"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并添加地址组成员]{style="font-family:宋体"}[：]{style="font-family:宋体"}[202.110.10.10]{lang="EN-US"}[、]{style="font-family:宋体"}[202.110.10.11]{lang="EN-US"}[、]{style="font-family:宋体"}[202.110.10.12]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] nat address-group 1]{lang="EN-US"}]{#struct_0_83269_x5501_x1117082375}

[\[Sysname-address-group-1\] address 202.110.10.10 202.110.10.12]{lang="EN-US"}

[\[Sysname-address-group-1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1301398656}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置入方向动态地址转换，]{style="font-family:宋体"}[使用地址组]{style="font-family:宋体"}[1]{lang="EN-US"}[中的地址进行地址转换，在转换的时候不使用]{style="font-family:宋体"}[TCP/UDP]{lang="EN-US"}[的端口信息，且需要添加路由。]{style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_83269_x5501_x1584113578}

[[\[Sysname-GigabitEthernet1/0/1\] nat inbound 2001 address-group 1 vpn-instance vpn10 no-pat add-route]{lang="EN-US"}]{#struct_0_83269_x5501_x1370567156}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_260857346}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_1241162482}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat inbound]{lang="EN-US"}**]{#struct_0_83269_x5501_1894210169}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat no-pat]{lang="EN-US"}**]{#struct_0_83269_x5501_x1900586767}
:::

::: {#-406583154 .myid}
[]{#_Toc404786505}[]{#struct_0_83269_x5501_1179721818}[]{#_Toc363572623}

**NAT命令 \-- NAT配置命令 \-- nat log alarm**

------------------------------------------------------------------------

[**[nat log ]{lang="EN-US"}[alarm]{lang="EN-US"}**]{#struct_0_83269_x5501_691453964}[命令]{style="font-family:宋体"}[用来开启]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[告警信息日志功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo nat log ]{lang="EN-US"}[alarm]{lang="EN-US"}**]{#struct_0_83269_x5501_1179787354}[命令]{style="font-family:宋体"}[用来关闭]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[告警信息日志功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_673348530}

[**[nat log alarm]{lang="EN-US"}**]{#struct_0_83269_x5501_1180246107}

[**[undo nat log alarm]{lang="EN-US"}**]{#struct_0_83269_x5501_1180311643}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x920392660}

[[NAT444]{lang="EN-US"}]{#struct_0_83269_x5501_1180115035}[告警信息]{style="font-family:宋体"}[日志功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1742619047}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_1180180571}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x939231402}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1179983963}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1180049499}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x896055508}

[[在]{style="font-family:宋体"}[NAT444]{lang="EN-US"}]{#struct_0_83269_x5501_1179852891}[地址转换中，如果可为用户分配的公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口块或端口块中的端口都被占用，则该用户的后续连接由于没有可用的资源无法对其进行地址转换，相应的报文将被丢弃。为了监控公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口块资源的使用情况，可以通过开启]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[告警信息日志功能来对端口用满和资源用满两种情况记录告警信息日志。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[端口用满告警：在私网]{style="font-family:宋体"}]{#struct_0_83269_x5501_269294908}[IP]{lang="EN-US"}[地址对应的端口块中的所有端口都被占用的情况下，输出告警信息日志。对于端口块动态映射方式，如果配置了增量端口块分配，则当首次分配的端口块中的端口都被占用时，并不输出日志；只有当增量端口块中的端口也都被占用时，才会输出日志。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[资源用满告警：在]{style="font-family:宋体"}]{#struct_0_83269_x5501_1179918427}[NAT444]{lang="EN-US"}[端口块动态映射中，如果所有资源（公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口块）都被占用，则输出日志。]{style="font-family:宋体"}

[[只有开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_1179721819}[日志功能之后，]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[告警信息日志功能才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_691519500}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1179787355}[开启]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[告警信息日志功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_673414066}

[\[Sysname\] nat log alarm]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1180246104}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_1180311640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat log]{lang="EN-US"}**]{#struct_0_83269_x5501_x920458196}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[nat log enable]{lang="EN-US"}**]{#struct_0_83269_x5501_1180115032}
:::

::: {#827525385 .myid}
[]{#_Toc404786506}[]{#struct_0_83269_x5501_x772170224}

**NAT命令 \-- NAT配置命令 \-- nat log enable**

------------------------------------------------------------------------

[**[nat log enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x93847043}[命令用来开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}[日志功能。]{style="font-family:宋体"}

[**[undo nat log enable]{lang="EN-US"}**]{#struct_0_83269_x5501_1395253908}[用来关闭]{style="font-family:宋体"}[NAT]{lang="EN-US"}[日志功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_816839454}

[**[nat log enable ]{lang="EN-US"}**[\[ **acl** *acl-number* \] ]{lang="EN-US"}]{#struct_0_83269_x5501_x1370632692}

[**[undo nat log enable]{lang="EN-US"}**]{#struct_0_83269_x5501_58945310}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_732091350}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x14911212}[日志功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1653745555}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1507205725}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x587854909}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_323885017}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_x231077078}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370698228}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x2032232014}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_972745290}

[[必须开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_461126201}[日志功能，]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话日志功能（包括]{style="font-family:宋体"}[NAT]{lang="EN-US"}[新建会话、]{style="font-family:宋体"}[NAT]{lang="EN-US"}[删除会话和]{style="font-family:宋体"}[NAT]{lang="EN-US"}[活跃流的日志功能）、]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户日志功能（包括]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块分配和]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块回收的日志功能）和]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[告警信息日志功能才能生效。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**]{#struct_0_83269_x5501_x38664404}[参数只对]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话日志功能有效，对其他]{style="font-family:宋体"}[NAT]{lang="EN-US"}[日志功能无效。如果指定了]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，则只有符合]{style="font-family:宋体"}[ACL permit]{lang="EN-US"}[规则的数据流才触发输出]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话日志；如果没有指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，则表示对]{style="font-family:宋体"}[所有被]{style="font-family:宋体"}[NAT]{lang="EN-US"}[处理过的数据流]{style="font-family:宋体"}[都有可能]{style="font-family:宋体"}[触发]{style="font-family:宋体"}[输出]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[日志。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370763764}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_892356406}[开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}[日志功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x1817085258}

[\[Sysname\] ]{lang="EN-US"}[nat log enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_246514272}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_x381669346}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat log]{lang="EN-US"}**]{#struct_0_83269_x5501_x1433922317}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log alarm]{lang="EN-US"}**]{#struct_0_83269_x5501_1179787352}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log flow-active]{lang="EN-US"}**]{#struct_0_83269_x5501_1413708654}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log flow-begin]{lang="EN-US"}**]{#struct_0_83269_x5501_x2031834719}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log flow-end]{lang="EN-US"}**]{#struct_0_83269_x5501_1180246105}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log port-block-assign]{lang="EN-US"}**]{#struct_0_83269_x5501_996630762}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log port-block-withdraw]{lang="EN-US"}**]{#struct_0_83269_x5501_1180311641}
:::

::: {#-1632790221 .myid}
[]{#_Toc404786507}[]{#struct_0_83269_x5501_x1370829300}[]{#_Ref311205919}[]{#_Ref311205890}

**NAT命令 \-- NAT配置命令 \-- nat log flow-active**

------------------------------------------------------------------------

[**[nat log flow-active]{lang="EN-US"}**]{#struct_0_83269_x5501_1308178834}[命令]{style="font-family:宋体"}[用来开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}[活跃流日志功能，并设置生成活跃流日志的时间间隔]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[**[undo nat log flow-active]{lang="EN-US"}**]{#struct_0_83269_x5501_x1907701598}[命令]{style="font-family:
宋体"}[用来关闭]{style="font-family:宋体"}[NAT]{lang="EN-US"}[活跃流的日志功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1864466718}

[**[nat log flow-active ]{lang="EN-US"}***[time-value]{lang="EN-US"}*]{#struct_0_83269_x5501_1541607145}

[**[undo nat log flow-active]{lang="EN-US"}**]{#struct_0_83269_x5501_375258248}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x2089667659}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_993124133}[活跃流的日志功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1150139975}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1370894836}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1601523598}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1214395725}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_x844930277}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x459206226}

[*[time-value]{lang="EN-US"}*]{#struct_0_83269_x5501_x1012648381}[：表示触发输出]{style="font-family:宋体"}[NAT]{lang="EN-US"}[活跃流日志的时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1789151551}

[[对于一些长时间没有断开的]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1126175760}[会话]{style="font-family:宋体"}[（即活跃流），如果需要定期记录其连接情况，则可以通过活跃流日志功能来实现。]{style="font-family:宋体"}

[[开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1370960372}[活跃流日志功能后，]{style="font-family:宋体"}[对于]{style="font-family:宋体"}[NAT]{lang="EN-US"}[活跃流，每经过指定的时间间隔，设备就会记录一次]{style="font-family:宋体"}[NAT]{lang="EN-US"}[日志。]{style="font-family:宋体"}

[[需要注意]{style="font-family:宋体"}]{#struct_0_83269_x5501_1641230448}[的是，只有开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}[日志功能之后，活跃流日志功能才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1517206501}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1349925205}[开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}[活跃流日志功能，并设置]{style="font-family:宋体"}[输出]{style="font-family:宋体"}[NAT]{lang="EN-US"}[活跃流日志的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_1503913182}

[\[Sysname\] ]{lang="EN-US"}[nat log flow-active 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x767709649}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_783151405}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat log]{lang="EN-US"}**]{#struct_0_83269_x5501_x564647797}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x994946613}
:::

::: {#1227004607 .myid}
[]{#_Toc404786508}[]{#struct_0_83269_x5501_x1371025908}[]{#_Toc311387861}[]{#_Ref311205906}

**NAT命令 \-- NAT配置命令 \-- nat log flow-begin**

------------------------------------------------------------------------

[**[nat log flow-begin]{lang="EN-US"}**]{#struct_0_83269_x5501_x1719036653}[命令用来开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}[新建会话的日志功能，即]{style="font-family:宋体"}[新建]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话时，输出]{style="font-family:宋体"}[NAT]{lang="EN-US"}[日志]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo nat log flow-begin]{lang="EN-US"}**]{#struct_0_83269_x5501_x967149819}[命令用来关闭]{style="font-family:宋体"}[NAT]{lang="EN-US"}[新建会话的日志功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_80605317}

[**[nat log flow-begin]{lang="EN-US"}**]{#struct_0_83269_x5501_2125576558}

[**[undo nat log flow-begin]{lang="EN-US"}**]{#struct_0_83269_x5501_1830043215}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x983660107}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_1003701548}[新建会话的日志功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370042868}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x561140097}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1094836041}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_399389171}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_x16721369}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1570472342}

[[只有开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1512042389}[日志功能之后，]{style="font-family:宋体"}[NAT]{lang="EN-US"}[新建会话的日志功能]{style="font-family:宋体"}[才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1730395516}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_663735861}[开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}[新建]{style="font-family:宋体"}[会话]{style="font-family:宋体"}[的日志功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x1370108404}

[\[Sysname\] ]{lang="EN-US"}[nat log flow-begin]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x501810173}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_1693315556}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat log]{lang="EN-US"}**]{#struct_0_83269_x5501_1956624035}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x1038593440}
:::

::: {#828502091 .myid}
[]{#_Toc404786509}[]{#struct_0_83269_x5501_1934036390}

**NAT命令 \-- NAT配置命令 \-- nat log flow-end**

------------------------------------------------------------------------

[**[nat log flow-end]{lang="EN-US"}**]{#struct_0_83269_x5501_2097294300}[命令用来开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}[删除会话的日志功能。]{style="font-family:宋体"}

[**[undo nat log flow-end]{lang="EN-US"}**]{#struct_0_83269_x5501_190389846}[命令用来关闭]{style="font-family:宋体"}[NAT]{lang="EN-US"}[删除会话的日志功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1931200448}

[**[nat log flow-end]{lang="EN-US"}**]{#struct_0_83269_x5501_x1370567155}

[**[undo nat log flow-end]{lang="EN-US"}**]{#struct_0_83269_x5501_x1305226595}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_257690823}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_242582115}[删除会话的日志功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_589077239}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_299065107}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_861853654}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_176883610}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_893455973}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370632691}

[[只有开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x344339217}[日志功能之后，]{style="font-family:宋体"}[NAT]{lang="EN-US"}[删除会话的日志功能]{style="font-family:宋体"}[才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1764829793}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x700570993}[开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}[删除]{style="font-family:宋体"}[会话]{style="font-family:宋体"}[的日志功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x391319223}

[\[Sysname\] ]{lang="EN-US"}[nat log flow-end]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1034882131}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_200867146}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat log]{lang="EN-US"}**]{#struct_0_83269_x5501_x1488745400}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x1370698227}
:::

::: {#-649960165 .myid}
[]{#_Toc404786510}[]{#struct_0_83269_x5501_1180049497}[]{#_Toc363572628}

**NAT命令 \-- NAT配置命令 \-- nat log port-block-assign**

------------------------------------------------------------------------

[**[nat log ]{lang="EN-US"}[port-block-assign]{lang="EN-US"}**]{#struct_0_83269_x5501_1179852889}[命令]{style="font-family:宋体"}[用来开启端口块分配的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户]{style="font-family:宋体"}[日志功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo nat log ]{lang="EN-US"}[port-block-assign]{lang="EN-US"}**]{#struct_0_83269_x5501_269819197}[命令]{style="font-family:宋体"}[用来关闭端口块分配的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户]{style="font-family:宋体"}[日志功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1179918425}

[**[nat log port-block-assign]{lang="EN-US"}**]{#struct_0_83269_x5501_1179721817}

[**[undo nat log port-block-assign]{lang="EN-US"}**]{#struct_0_83269_x5501_691912716}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1179787353}

[[端口块分配]{style="font-family:宋体"}]{#struct_0_83269_x5501_1180246102}[的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户日志功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_996696298}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_1180311638}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x920982477}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1180115030}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1180180566}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x939165867}

[[端口块静态映射方式下，在某私网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_1179983958}[地址的第一个新建连接通过端口块进行地址转换时，如果开启了端口块分配]{style="font-family:宋体"}[的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户日志功能，则会输出日志。]{style="font-family:宋体"}

[[端口块动态映射方式下，在为某私网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_x504977280}[地址分配端口块或增量端口块时，如果开启了端口块分配]{style="font-family:宋体"}[的]{style="font-family:
宋体"}[NAT444]{lang="EN-US"}[用户日志功能，则会输出日志。]{style="font-family:宋体"}

[[只有开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_1180049494}[日志功能之后，端口块分配的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户]{style="font-family:宋体"}[日志功能才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1179852886}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_269229373}[开启端口块分配]{style="font-family:宋体"}[的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户日志功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_1179918422}

[\[Sysname\] nat log port-block-assign]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1179721814}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_691716108}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat log]{lang="EN-US"}**]{#struct_0_83269_x5501_1179787350}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log enable]{lang="EN-US"}**]{#struct_0_83269_x5501_1180246103}
:::

::: {#632527210 .myid}
[]{#_Toc404786511}[]{#struct_0_83269_x5501_996761834}[]{#_Toc363572629}

**NAT命令 \-- NAT配置命令 \-- nat log port-block-withdraw**

------------------------------------------------------------------------

[**[nat log ]{lang="EN-US"}[port-block-withdraw]{lang="EN-US"}**]{#struct_0_83269_x5501_1180311639}[命令]{style="font-family:宋体"}[用来开启端口块回收的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户]{style="font-family:宋体"}[日志功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo nat log ]{lang="EN-US"}[port-block-withdraw]{lang="EN-US"}**]{#struct_0_83269_x5501_1180115031}[命令]{style="font-family:宋体"}[用来关闭端口块回收的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户]{style="font-family:宋体"}[日志功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1742881191}

[**[nat log port-block-withdraw]{lang="EN-US"}**]{#struct_0_83269_x5501_1180180567}

[**[undo nat log port-block-withdraw]{lang="EN-US"}**]{#struct_0_83269_x5501_x939100331}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1179983959}

[[端口块]{style="font-family:宋体"}]{#struct_0_83269_x5501_1180049495}[回收的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户日志功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x896841940}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_1179852887}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1179918423}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_759992070}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1179721815}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1179787351}

[[端口块静态映射方式下，在某私网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_673151922}[地址的最后一个连接拆除时，如果开启了端口块]{style="font-family:宋体"}[回收的]{style="font-family:
宋体"}[NAT444]{lang="EN-US"}[用户日志功能，则会输出日志。]{style="font-family:宋体"}

[[端口块动态映射方式下，在释放端口块资源（并删除端口块表项）时，如果开启了端口块]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1548637249}[回收的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户日志功能，则会输出日志。]{style="font-family:宋体"}

[[只有开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1548571713}[日志功能之后，端口块回收的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户]{style="font-family:宋体"}[日志功能才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1462544851}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1548768321}[开启端口块回收]{style="font-family:宋体"}[的]{style="font-family:
宋体"}[NAT444]{lang="EN-US"}[用户日志功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x918681128}

[\[Sysname\] nat log port-block-withdraw ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1548702785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_x1548899393}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat log]{lang="EN-US"}**]{#struct_0_83269_x5501_x1468660489}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat log enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x1548833857}
:::

::: {#140482789 .myid}
[]{#_Toc404786512}[]{#struct_0_83269_x5501_x466148073}[]{#_Ref311207114}[]{#_Ref311206903}[]{#_Ref311193217}

**NAT命令 \-- NAT配置命令 \-- nat mapping-behavior**

------------------------------------------------------------------------

[**[nat mapping-behavior]{lang="FR"}**]{#struct_0_83269_x5501_x1222345756}[命令用来配置]{style="font-family:宋体"}[PAT]{lang="FR"}[方式出方向动态地址转换的模式。]{style="font-family:宋体"}

[**[undo nat mapping-behavior]{lang="EN-US"}**]{#struct_0_83269_x5501_1266316778}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1944719248}

[**[nat mapping-behavior]{lang="EN-US"}**[ **endpoint-independent** \[ **acl** *acl-number* \]]{lang="EN-US"}]{#struct_0_83269_x5501_x1878500116}

[**[undo nat mapping-behavior]{lang="EN-US"}**[ **endpoint-independent**]{lang="EN-US"}]{#struct_0_83269_x5501_x1942956361}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x564785561}

[[PAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1807783825}[出方向动态方式地址转换的模式为]{style="font-family:宋体"}[Address and Port-Dependent Mapping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370763763}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x673727535}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x275363419}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_283080378}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_600341557}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x309113617}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x1830585275}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，用于控制需要遵守指定地址转换模式的报文范围。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1709075078}

[[PAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1003080748}[方式出方向动态地址转换]{style="font-family:宋体"}[支持两种模式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Endpoint-Independent Mapping]{lang="EN-US"}]{#struct_0_83269_x5501_x1370829299}[（不关心对端地址和端口的转换模式）：只要是来自相同源地址和源端口号的报文，不论其目的地址是否相同，通过]{style="font-family:宋体"}[PAT]{lang="EN-US"}[映射后，其源地址和源端口号都被转换为同一个外部地址和端口号，该映射关系会被记录下来并生成一个]{style="font-family:宋体"}[EIM]{lang="EN-US"}[表项；并且]{style="font-family:宋体"}[NAT]{lang="EN-US"}[网关设备允许外部网络的主机通过该转换后的地址和端口来访问这些内部网络的主机。这种模式可以很好的支持位于不同]{style="font-family:宋体"}[NAT]{lang="EN-US"}[网关之后的主机间进行互访。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Address and Port-Dependent Mapping]{lang="EN-US"}]{#struct_0_83269_x5501_x1776345056}[（关心对端地址和端口的转换模式）：对于来自相同源地址和源端口号的报文，若其目的地址和目的端口号不同，由于相同的源地址和源端口号不要求被转换为相同的外部地址和端口号，所以通过]{style="font-family:宋体"}[PAT]{lang="EN-US"}[映射后，相同的源地址和源端口号通常会被转换成不同的外部地址和端口号。并且]{style="font-family:宋体"}[NAT]{lang="EN-US"}[网关设备只允许这些目的地址对应的外部网络的主机才可以通过该转换后的地址和端口来访问这些内部网络的主机。这种模式安全性好，但是不便于位于不同]{style="font-family:宋体"}[NAT]{lang="EN-US"}[网关之后的主机间进行互访。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_83269_x5501_367648219}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该配置只对出方向动态地址转换的]{style="font-family:宋体"}]{#struct_0_83269_x5501_x527296969}[PAT]{lang="EN-US"}[方式起作用。入方向动态地址转换]{style="font-family:宋体"}[的]{lang="EN-US" style="font-family:宋体"}[PAT]{lang="EN-US"}[方式的转换模式始终为]{lang="EN-US" style="font-family:宋体"}[ Address and Port-Dependent Mapping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{lang="EN-US" style="font-family:宋体"}**[acl]{lang="EN-US"}**]{#struct_0_83269_x5501_x1729947783}[参数]{style="font-family:宋体"}[，则表示只有符合]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[ permit]{lang="EN-US"}[规则]{style="font-family:宋体"}[的报文才采用]{lang="EN-US" style="font-family:宋体"}[Endpoint-Independent Mapping]{lang="EN-US"}[模式进行地址转换；如果没有配置]{lang="EN-US" style="font-family:宋体"}**[acl]{lang="EN-US"}**[参数]{style="font-family:宋体"}[，则表示所有的报文都采用]{lang="EN-US" style="font-family:宋体"}[Endpoint-Independent Mapping]{lang="EN-US"}[模式进行地址转换。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1184107405}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1598696156}[对所有报文都以]{style="font-family:宋体"}[Endpoint-Independent Mapping]{lang="EN-US"}[模式进行地址转换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_1540180988}

[[\[Sysname\] nat mapping-behavior endpoint-independent]{lang="EN-US"}]{#struct_0_83269_x5501_x1370894835}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x35439657}[仅对]{style="font-family:宋体"}[FTP]{lang="EN-US"}[和]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文才以]{style="font-family:宋体"}[Endpoint-Independent Mapping]{lang="EN-US"}[模式进行地址转换，其它报文采用]{style="font-family:宋体"}[Address and Port-Dependent Mapping]{lang="EN-US"}[模式进行地址转换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x30787955}

[[\[Sysname\] acl advanced 3000]{lang="EN-US"}]{#struct_0_83269_x5501_670174036}

[[\[Sysname-acl-ipv4-adv-3000\] rule permit tcp destination-port eq 80]{lang="EN-US"}]{#struct_0_83269_x5501_1927415131}

[[\[Sysname-acl-ipv4-adv-3000\] rule permit tcp destination-port eq 21]{lang="EN-US"}]{#struct_0_83269_x5501_x888154740}

[[\[Sysname-acl-ipv4-adv-3000\] quit]{lang="EN-US"}]{#struct_0_83269_x5501_x1169353009}

[[\[Sysname\] nat mapping-behavior endpoint-independent acl 3000]{lang="EN-US"}]{#struct_0_83269_x5501_x1025234270}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x898319049}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[nat outbound]{lang="EN-US"}**]{#struct_0_83269_x5501_x1370960371}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat eim]{lang="EN-US"}**]{#struct_0_83269_x5501_75146507}
:::

::: {#367937141 .myid}
[]{#_Toc404786513}[]{#struct_0_83269_x5501_x697174884}[]{#_Ref311206219}[]{#_Ref311193230}

**NAT命令 \-- NAT配置命令 \-- nat outbound**

------------------------------------------------------------------------

[**[nat outbound]{lang="EN-US"}**]{#struct_0_83269_x5501_x252446715}[命令用来配置出方向动态地址转换]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo nat outbound]{lang="EN-US"}**]{#struct_0_83269_x5501_x1222166810}[命令用来]{style="font-family:宋体"}[删除指定的出方向动态地址转换]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x317285207}

[[不存在动态地址转换配置。]{style="font-family:宋体"}]{#struct_0_83269_x5501_1190866892}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1562754846}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NO-PAT]{lang="EN-US"}]{#struct_0_83269_x5501_1236564930}[方式]{lang="EN-US" style="font-family:宋体"}

[**[nat outbound ]{lang="EN-US"}**[\[ *acl-number* \] **address-group** *group-number* \[ **vpn-instance** *vpn-instance-name* \] **no-pat** \[ **reversible** \] ]{lang="EN-US"}]{#struct_0_83269_x5501_x1371025907}

[**[undo nat outbound ]{lang="EN-US"}**[\[ *acl-number* \]]{lang="EN-US"}]{#struct_0_83269_x5501_1366077062}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PAT]{lang="EN-US"}]{#struct_0_83269_x5501_978813967}[方式]{lang="EN-US" style="font-family:
宋体"}

[**[nat outbound ]{lang="EN-US"}**[\[ *acl-number* \] \[ **address-group** *group-number* \] \[ **vpn-instance** *vpn-instance-name* \] \[ **port-preserved**]{lang="EN-US"}]{#struct_0_83269_x5501_x306748126}[ ]{lang="EN-US" style="font-size:10.0pt;
font-family:宋体;color:red"}[\]]{lang="EN-US"}

[**[undo nat outbound ]{lang="EN-US"}**[\[ *acl-number* \]]{lang="EN-US"}]{#struct_0_83269_x5501_x1686202785}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_604186825}

[[接口视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_396348462}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1621549512}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x1370042867}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_x514085930}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1181233036}

[*[acl-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x147782890}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。不指定该参数的情况下，不对转换对象进行限制。]{style="font-family:宋体"}

[**[address-group]{lang="EN-US"}***[ group-number]{lang="EN-US"}*]{#struct_0_83269_x5501_616704068}[：指定地址转换使用的地址组。]{style="font-family:宋体"}*[group-number]{lang="EN-US"}*[为地址组编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果不指定该参数，则直接使用该接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为转换后的地址，即实现]{style="font-family:宋体"}[Easy IP]{lang="EN-US"}[功能。]{style="font-family:宋体"}[Easy IP]{lang="EN-US"}[功能的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_83269_x5501_x1173670321}[：指定地址组中的地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[中的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示地址组中的地址不属于任何一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[no-pat]{lang="EN-US"}**]{#struct_0_83269_x5501_115261121}[：表示使用]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[方式进行转换，即转换时不使用报文的端口信息；如果未指定本参数，则表示使用]{style="font-family:宋体"}[PAT]{lang="EN-US"}[方式进行转换，即转换时使用报文的端口信息。]{style="font-family:宋体"}[PAT]{lang="EN-US"}[方式仅支持]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[查询报文，由于]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文没有端口的概念，我们将]{style="font-family:宋体"}[ICMP ID]{lang="EN-US"}[作为]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文的源端口。]{style="font-family:宋体"}

[**[reversible]{lang="EN-US"}**]{#struct_0_83269_x5501_x2099990477}[：表示允许反向地址转换。即，在内网用户主动向外网发起连接并成功触发建立地址转换表项的情况下，允许外网向该内网用户发起的连接使用已建立的地址转换表项进行目的地址转换。]{style="font-family:宋体"}

[**[port-preserved]{lang="EN-US"}**]{#struct_0_83269_x5501_x408500608}[：]{style="font-size:10.0pt;
font-family:宋体;color:black"}[PAT]{lang="EN-US"}[方式分配端口时尽量不转换端口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1370108403}

[[一般情况下，出方向]{style="font-family:宋体"}]{#struct_0_83269_x5501_x98525646}[动态地址转换]{style="font-family:宋体"}[配置在和外部网络连接的接口上。]{style="font-family:宋体"}[动态地址转换]{style="font-family:宋体"}[有两种转换方式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PAT]{lang="EN-US"}]{#struct_0_83269_x5501_1238838648}[方式：对于从内网到外网的报文，如果符合]{lang="EN-US" style="font-family:
宋体"}[ACL]{lang="EN-US"}[ permit]{lang="EN-US"}[规则]{style="font-family:宋体"}[，则使用地址组中的地址或该接口的地址（]{lang="EN-US" style="font-family:宋体"}[Easy IP]{lang="EN-US"}[方式）进行源地址转换，同时转换源端口（]{lang="EN-US" style="font-family:宋体"}[IP1/port1]{lang="EN-US"}[转换为]{lang="EN-US" style="font-family:宋体"}[IP2/port2]{lang="EN-US"}[）；如果]{lang="EN-US" style="font-family:宋体"}[同时]{style="font-family:宋体"}[配置了]{lang="EN-US" style="font-family:宋体"}[PAT]{lang="EN-US"}[方式下的地址转换模式为]{lang="EN-US" style="font-family:宋体"}[EIM]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Endpoint-Independent Mapping]{lang="EN-US"}[），则外网可以通过]{lang="EN-US" style="font-family:宋体"}[IP2/port2]{lang="EN-US"}[主动访问内网，]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[设备根]{lang="EN-US" style="font-family:宋体"}[据]{lang="EN-US" style="font-family:宋体"}[EIM]{lang="EN-US"}[表项转]{lang="EN-US" style="font-family:宋体"}[换]{style="font-family:宋体"}[目的地址和端口]{lang="EN-US" style="font-family:宋体"}[（]{style="font-family:宋体"}[IP2/port2]{lang="EN-US"}[转换为]{lang="EN-US" style="font-family:宋体"}[IP1/port1]{lang="EN-US"}[）]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NO-PAT]{lang="EN-US"}]{#struct_0_83269_x5501_945862895}[方式：对于从内网到外网的报文，如果符合]{style="font-family:宋体"}[ACL permit]{lang="EN-US"}[规则，则使用地址组中的地址进行源地址转换，不转换源端口（]{style="font-family:宋体"}[IP1]{lang="EN-US"}[转换为]{style="font-family:宋体"}[IP2]{lang="EN-US"}[）；如果同时配置了]{style="font-family:宋体"}**[reversible]{lang="EN-US"}**[，则允许外网通过]{style="font-family:宋体"}[IP2]{lang="EN-US"}[主动访问内网，对于此类报文，需要进行]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（提取报文的源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口和目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口，并将目的地址转换为]{style="font-family:宋体"}[IP1]{lang="EN-US"}[，然后将源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口和目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口互换去匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[），只有反向匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的报文才能进行转换（将目的地址]{style="font-family:宋体"}[IP2]{lang="EN-US"}[转换为]{style="font-family:宋体"}[IP1]{lang="EN-US"}[），否则不予转换。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_83269_x5501_1231611722}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个地址组被]{lang="EN-US" style="font-family:宋体"}]{#struct_0_83269_x5501_x39608260}**[nat]{lang="EN-US"}[ outbound]{lang="EN-US"}**[配置]{style="font-family:宋体"}[引用后，不能再被]{lang="EN-US" style="font-family:宋体"}**[nat]{lang="EN-US"}[ ]{lang="EN-US"}[in]{lang="EN-US"}[bound]{lang="EN-US"}**[引用。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个地址组被]{lang="EN-US" style="font-family:宋体"}[PAT]{lang="EN-US"}]{#struct_0_83269_x5501_x567657461}[方式的]{lang="EN-US" style="font-family:宋体"}**[nat]{lang="EN-US"}[ outbound]{lang="EN-US"}**[配置引用后，不能再被]{lang="EN-US" style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[方式的]{lang="EN-US" style="font-family:宋体"}**[nat]{lang="EN-US"}[ outbound]{lang="EN-US"}**[配置引用，反之亦然。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在一个接口下，一个]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_83269_x5501_859525572}[只能被一个]{lang="EN-US" style="font-family:宋体"}**[nat]{lang="EN-US"}[ outbound]{lang="EN-US"}**[引用。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口下可同时配置多条出方向地址转换。]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1749495738}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于同一接口下的出方向动态地址转换配置，指定了]{style="font-family:宋体"}]{#struct_0_83269_x5501_195516789}[ACL]{lang="EN-US"}[的配置的优先级高于未指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置的优先级；对于指定了]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的出方向动态地址转换配置，其生效优先级由]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号的大小决定，编号越大，优先级越高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1548899395}[PAT]{lang="EN-US"}[方式的]{style="font-family:宋体"}**[nat outbound]{lang="EN-US"}**[所引用的地址组中配置了端口范围和端口块参数，则将对匹配的报文进行]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块动态映射。]{style="font-family:宋体"}**[port-preserved]{lang="EN-US"}**[参数]{lang="EN-US" style="font-family:宋体"}[对]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块动态映射无效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1653738322}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1207528339}[配置]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[，]{style="font-family:宋体"}[允许对]{style="font-family:宋体"}[10.110.10.0/24]{lang="EN-US"}[网段的主机报文进行地址转换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_875930610}

[[\[Sysname\] acl basic 2001]{lang="EN-US"}]{#struct_0_83269_x5501_206078808}

[[\[Sysname-acl-ipv4-basic-2001\] rule permit source 10.110.10.0 0.0.0.255]{lang="EN-US"}]{#struct_0_83269_x5501_x1769102772}

[[\[Sysname-acl-ipv4-basic-2001\] rule deny]{lang="EN-US"}]{#struct_0_83269_x5501_1878012289}

[[\[Sysname-acl-ipv4-basic-2001\] quit]{lang="EN-US"}]{#struct_0_83269_x5501_x1699144139}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_2012795284}[配置地址组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并添加地址组成员：]{style="font-family:宋体"}[202.110.10.10]{lang="EN-US"}[、]{style="font-family:宋体"}[202.110.10.11]{lang="EN-US"}[、]{style="font-family:宋体"}[202.110.10.12]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] nat address-group 1]{lang="EN-US"}]{#struct_0_83269_x5501_399212390}

[\[Sysname-address-group-1\] address 202.110.10.10 202.110.10.12]{lang="EN-US"}

[\[Sysname-address-group-1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1302606295}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置出方向动态地址转换，]{style="font-family:宋体"}[允许对]{style="font-family:宋体"}[匹配]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[的报文]{style="font-family:宋体"}[使用地址组]{style="font-family:宋体"}[1]{lang="EN-US"}[中的地址进行地址转换，且在转换的时候使用]{style="font-family:宋体"}[TCP/UDP]{lang="EN-US"}[的端口信息。]{style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_83269_x5501_791278139}

[\[Sysname-GigabitEthernet1/0/1\] nat outbound 2001 address-group 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_871350058}[如果]{style="font-family:宋体"}[在接口]{style="font-family:宋体"}[GigabitEthernet1/1]{lang="EN-US"}[上]{style="font-family:宋体"}[不使用]{style="font-family:宋体"}[TCP/UDP]{lang="EN-US"}[的端口信息进行地址转换，可以使用如下配置。]{style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_83269_x5501_1973190502}

[\[Sysname-GigabitEthernet1/0/1\] nat outbound 2001 address-group 1 no-pat]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_195385717}[如果直接使用]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行地址转换，可以使用如下的配置。]{style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_83269_x5501_x1009096406}

[[\[Sysname-GigabitEthernet 1/0/1\] nat outbound 2001]{lang="EN-US"}]{#struct_0_83269_x5501_16875366}

[\[Sysname-GigabitEthernet 1/0/1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_2035477039}[内网]{style="font-family:宋体"}[10.110.10.0/24]{lang="EN-US"}[网段的主机使用地址组]{style="font-family:宋体"}[1]{lang="EN-US"}[中的地址作为转换后的地址访问外部网络。如果要在内网用户向外网主动发起访问之后，允许外网用户主动向]{style="font-family:宋体"}[10.110.10.0/24]{lang="EN-US"}[网段的主机发起访问，并利用已建立的地址转换表项进行反向地址转换，可以使用如下配置。]{style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_83269_x5501_737849192}

[[\[Sysname-GigabitEthernet1/0/1\] nat outbound 2001 address-group 1 no-pat reversible]{lang="EN-US"}]{#struct_0_83269_x5501_2076943872}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_195320181}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat eim]{lang="EN-US"}**]{#struct_0_83269_x5501_1571205303}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat outbound]{lang="EN-US"}**]{#struct_0_83269_x5501_2135593753}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[nat mapping-behavior]{lang="EN-US"}**]{#struct_0_83269_x5501_x1195344549}
:::

::: {#812119924 .myid}
[]{#_Toc404786514}[]{#struct_0_83269_x5501_1590853478}[]{#_Toc383423660}

**NAT命令 \-- NAT配置命令 \-- nat outbound ds-lite-b4**

------------------------------------------------------------------------

[**[nat outbound ds-lite-b4]{lang="EN-US"}**]{#struct_0_83269_x5501_x1837106726}[命令用来配置基于]{style="font-family:宋体"}[B4]{lang="EN-US"}[地址的]{style="font-family:宋体"}[DS-Lite NAT]{lang="EN-US"}[转换。]{style="font-family:宋体"}

[**[undo nat outbound ds-lite-b4]{lang="EN-US"}**]{#struct_0_83269_x5501_1196176423}[命令用来删除指定的]{style="font-family:
宋体"}[B4]{lang="EN-US"}[地址的]{style="font-family:宋体"}[DS-Lite NAT]{lang="EN-US"}[转换。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1527923138}

[**[nat outbound ds-lite-b4 ]{lang="EN-US"}***[ipv6-acl-number]{lang="EN-US"}*[ **address-group** *group-number*]{lang="EN-US"}]{#struct_0_83269_x5501_1821151370}

[**[undo nat outbound ds-lite-b4]{lang="EN-US"}**[ *ipv6-acl-number*]{lang="EN-US"}]{#struct_0_83269_x5501_1221961823}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1008510802}

[[不存在]{style="font-family:宋体"}[DS-Lite NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1911545017}[转换配置。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_728764336}

[[接口视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x2008291287}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x365461658}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x840657438}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x2140616058}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x959419929}

[*[ipv6-acl-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x514514232}[：用于匹配]{style="font-family:宋体"}[B4]{lang="EN-US"}[设备]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[address-group]{lang="EN-US"}***[ group-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x1559124758}[：指定地址转换使用的地址组。]{style="font-family:宋体"}*[group-number]{lang="EN-US"}*[为地址组编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。目前仅支持端口块动态映射方式的地址组，因此指定的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址组中必须配置端口块参数，否则配置不生效。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_955811015}

[[在使用]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}]{#struct_0_83269_x5501_x861584644}[隧道技术实现通过]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[网络连接]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[网络的组网环境下，基于]{style="font-family:宋体"}[B4]{lang="EN-US"}[地址的]{style="font-family:宋体"}[DS-Lite NAT]{lang="EN-US"}[转换配置在]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[网关设备连接外部网络的接口上，通常用于在]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[网关设备已知]{style="font-family:宋体"}[B4]{lang="EN-US"}[设备或]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[主机的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的情况下为]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[用户提供]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址转换。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1847849877}

[[ ]{lang="EN-US" style="font-size:10.0pt"}[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1285184582}[配置]{style="font-family:宋体"}[IPv6 ACL 2100]{lang="EN-US"}[，]{style="font-family:宋体"}[允许对]{style="font-family:宋体"}[2000::/64]{lang="EN-US"}[网段的主机报文进行地址转换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x374912585}

[\[Sysname\] acl ipv6 basic 2100]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2100\] rule permit source 2000::/64]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2100\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_59042850}[配置地址组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并添加地址组成员：]{style="font-family:宋体"}[202.110.10.10]{lang="EN-US"}[～]{style="font-family:宋体"}[202.110.10.12]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] nat address-group 1]{lang="EN-US"}]{#struct_0_83269_x5501_1208516454}

[\[Sysname-nat-address-group-1\] address 202.110.10.10 202.110.10.12]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1109593210}[配置地址组]{style="font-family:宋体"}[1]{lang="EN-US"}[的端口块参数，端口块大小为]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-nat-address-group-1\]]{lang="EN-US"}]{#struct_0_83269_x5501_x940003667}[ port-block block-size 256]{lang="EN-US"}

[\[Sysname-nat-address-group-1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x405169203}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置基于]{style="font-family:宋体"}[B4]{lang="EN-US"}[地址的]{style="font-family:宋体"}[DS-Lite NAT]{lang="EN-US"}[转换，]{style="font-family:宋体"}[允许对]{style="font-family:宋体"}[匹配]{style="font-family:宋体"}[IPv6 ACL 2100]{lang="EN-US"}[的报文]{style="font-family:宋体"}[使用地址组]{style="font-family:宋体"}[1]{lang="EN-US"}[中的地址进行地址转换。]{style="font-family:宋体"}

[[\[Sysname\] interface ethernet 1/1]{lang="EN-US"}]{#struct_0_83269_x5501_x334493102}

[\[Sysname-GigabitEthernet1/0/1\] nat outbound ds-lite-b4 2100 address-group 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1410094894}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat outbound]{lang="EN-US"}**]{#struct_0_83269_x5501_1250219912}
:::

::: {#1376359856 .myid}
[]{#_Toc404786515}[]{#struct_0_83269_x5501_17446693}[]{#_Toc363572632}

**NAT命令 \-- NAT配置命令 \-- nat outbound port-block-group**

------------------------------------------------------------------------

[**[nat outbound port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x250262134}[命令用来]{style="font-family:
宋体"}[配置]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块静态映射]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo nat outbound port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_17512229}[命令用来删除指定的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块静态映射配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_17315621}

[**[nat outbound port-block-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_83269_x5501_17381157}

[**[undo nat outbound port-block-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_83269_x5501_1887878744}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_17184549}

[[不存在]{style="font-family:宋体"}[NAT444]{lang="EN-US"}]{#struct_0_83269_x5501_17250085}[端口块静态映射配置。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1147746053}

[[接口视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_17053477}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_17119013}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_730497222}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_16922405}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_16987941}

[*[group-number]{lang="EN-US"}*]{#struct_0_83269_x5501_17446690}[：]{style="font-family:宋体"}[端口块组]{style="font-family:宋体"}[编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[。其中]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_17512226}

[[该配置在接口下引用指定的端口块组，根据端口块组内的配置数据，按照固定的算法为每个私网]{style="font-family:宋体"}]{#struct_0_83269_x5501_x989189088}[IP]{lang="PT-BR"}[地址分配一个静态端口块并创建静态端口块表项。]{style="font-family:宋体"}[当某]{style="font-family:宋体"}[私网]{style="font-family:宋体"}[IP]{lang="PT-BR"}[地址向公网发起连接时，通过该私网]{style="font-family:宋体"}[IP]{lang="PT-BR"}[地址查找静态端口块表项，使用表项中记录的公网]{style="font-family:宋体"}[IP]{lang="PT-BR"}[地址进行地址转换，并从对应的端口块中动态分配一个端口进行]{style="font-family:宋体"}[TCP/UDP]{lang="PT-BR"}[端口转换。]{style="font-family:宋体"}

[[一个接口下可以配置多条]{style="font-family:宋体"}]{#struct_0_83269_x5501_17315618}[基于不同端口块组的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块静态映射。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_17381154}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_17053474}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的出方向上配置基于端口组]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块静态映射]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_17315619}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] nat outbound port-block-group 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1463906112}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_17381155}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat outbound ]{lang="EN-US"}[port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_17184547}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat ]{lang="EN-US"}[port-block]{lang="EN-US"}**]{#struct_0_83269_x5501_960088016}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_17250083}
:::

::::: {#1032668127 .myid}
[]{#_Toc404786516}[]{#struct_0_83269_x5501_798937190}[]{#_Toc380069641}[]{#_Toc378256736}

**NAT命令 \-- NAT配置命令 \-- nat port-block synchronization enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NAT命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_83269_x5501_8981195}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_83269_x5501_1922871172}
:::

[ ]{lang="EN-US"}

[**[nat port-block synchronization enable]{lang="EN-US" style="color:black"}**]{#struct_0_83269_x5501_2101137958}[命令用来[开启]{style="color:black"}]{style="font-family:宋体"}[NAT444]{lang="EN-US" style="color:black"}[业务热备份功能]{style="font-family:宋体;
color:black"}[。]{style="font-family:宋体"}

[**[undo nat [port-block synchronization enable]{style="color:black"}]{lang="EN-US"}**]{#struct_0_83269_x5501_49902804}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_798871654}

[**[nat port-block synchronization enable]{lang="EN-US" style="color:black"}**]{#struct_0_83269_x5501_2138654297}

[**[undo nat [port-block synchronization enable]{style="color:black"}]{lang="EN-US"}**]{#struct_0_83269_x5501_x1055312279}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1284738555}

[[NAT444]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_x1756412}[业务热备份功能处于关闭状态。]{style="font-family:宋体;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_798412901}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_915156369}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_781575358}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1399491841}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x370482294}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_798347365}

[[在]{style="font-family:宋体;color:black"}]{#struct_0_83269_x5501_996337768}[业务热备份]{style="font-family:宋体;
color:black"}[环境中，通过开启]{style="font-family:宋体;color:black"}[NAT444]{lang="EN-US" style="color:black"}[业务热备份功能，可以实现主备切换后]{style="font-family:宋体;
color:black"}[动态]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块表项一致[。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x2048613828}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x920948046}[开启]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[多机备份功能]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_798543973}

[\[Sysname\] nat [port-block ]{style="color:
black"}synchronization enable]{lang="EN-US"}
:::::

::: {#1997370707 .myid}
[]{#_Toc404786517}[]{#struct_0_83269_x5501_17053475}[]{#_Toc363572633}

**NAT命令 \-- NAT配置命令 \-- nat port-block-group**

------------------------------------------------------------------------

[**[nat port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x1625198079}[命令用来创建一个]{style="font-family:宋体"}[NAT]{lang="EN-US"}[端口块组，并进入]{style="font-family:宋体"}[NAT]{lang="EN-US"}[端口块组视图。]{style="font-family:宋体"}

[**[undo nat port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_17119011}[命令用来删除指定的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[端口块组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_16922403}

[**[nat port-block-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_83269_x5501_16987939}

[**[undo nat port-block-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x20387042}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_17446688}

[[不存在]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_17512224}[端口块组]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1371526112}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_17315616}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_17381152}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_313900632}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_17184544}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_17250080}

[*[group-number]{lang="EN-US"}*]{#struct_0_83269_x5501_426232059}[：]{style="font-family:宋体"}[NAT]{lang="EN-US"}[端口块组编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[max_number]{lang="EN-US"}[。其中]{style="font-family:宋体"}[max_number]{lang="EN-US"}[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_17053472}

[[创建的]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x408619679}[端口块组用于配置]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块静态映射。]{style="font-family:宋体"}[一个端口块组中包含如下内容：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个或多个私网地址成员，通过]{lang="EN-US" style="font-family:宋体"}**[local-ip-address]{lang="EN-US"}**]{#struct_0_83269_x5501_16922400}[命令配置]{lang="EN-US" style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个或多个公网地址成员，通过]{lang="EN-US" style="font-family:宋体"}**[global-ip-pool]{lang="EN-US"}**]{#struct_0_83269_x5501_16987936}[命令配置]{lang="EN-US" style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[公网地址的端口范围，通过]{lang="EN-US" style="font-family:宋体"}**[port-range]{lang="EN-US"}**]{#struct_0_83269_x5501_17446689}[命令配置]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[端口块大小，通过]{lang="EN-US" style="font-family:宋体"}**[block-size]{lang="EN-US"}**]{#struct_0_83269_x5501_168810735}[命令配置]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[在进行]{style="font-family:宋体"}[NAT444]{lang="EN-US"}]{#struct_0_83269_x5501_17512225}[端口块静态映射时，系统根据相应端口块组的配置计算出私网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址到公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口块的静态映射关系，并创建静态端口块表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_17315617}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x316895040}[创建一个]{style="font-family:宋体"}[NAT]{lang="EN-US"}[端口块组，编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_83269_x5501_17381153}

[\[Sysname\]nat port-block-group 1]{lang="EN-US"}

[\[Sysname-port-block-group-1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_17184545}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[block-size]{lang="EN-US"}**]{#struct_0_83269_x5501_1342425040}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_17250081}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_17053473}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[global-ip-pool]{lang="EN-US"}**]{#struct_0_83269_x5501_17119009}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-ip-address]{lang="EN-US"}**]{#struct_0_83269_x5501_1547695457}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat outbound port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_16922401}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[port-range]{lang="EN-US"}**]{#struct_0_83269_x5501_16987937}
:::

::: {#-753794749 .myid}
[]{#_Toc404786518}[]{#struct_0_83269_x5501_1146590915}

**NAT命令 \-- NAT配置命令 \-- nat server**

------------------------------------------------------------------------

[**[nat server]{lang="EN-US"}**]{#struct_0_83269_x5501_269304628}[命令用来配置]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器，即定义内部服务器的外网地址和端口与内网地址和端口的映射表项。]{style="font-family:宋体"}

[**[undo nat server]{lang="EN-US"}**]{#struct_0_83269_x5501_427308393}[命令用来删除指定的内部服务器配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x338979682}

[[(1)[      ]{style="font:7.0pt "}]{lang="DA"}[普通内部服务器]{lang="EN-US" style="font-family:宋体"}]{#struct_0_83269_x5501_x1996483779}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[外网地址单一，未使用外网端口或外网端口单一]{style="font-family:宋体"}]{#struct_0_83269_x5501_195254645}

[**[nat server]{lang="DA"}**]{#struct_0_83269_x5501_783706313}[ **protocol** *pro-type* **global** { *global-address \|* **current-interface** \| **interface** *interface-type* *interface-number* } \[ *global-port* \] \[ **vpn-instance** *global-name* \] **inside** *local-address* \[ *local-port* \] \[ **vpn-instance** *local-name* \] ]{lang="DA"}[\[ **acl** *acl-number* \]]{lang="EN-US"}

[**[undo nat server]{lang="DA"}**]{#struct_0_83269_x5501_x1355583443}[ **protocol** *pro-type* **global** { *global-address \|* **current-interface** \| **interface** *interface-type* *interface-number* } \[ *global-port* \] \[ **vpn-instance** *global-name* \]]{lang="DA"}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[外网地址单一，外网端口连续]{style="font-family:宋体"}]{#struct_0_83269_x5501_x566519561}

[**[nat server]{lang="DA"}**]{#struct_0_83269_x5501_90239213}[ **protocol** *pro-type* **global** { *global-address \|* **current-interface** \| **interface** *interface-type* *interface-number* } *global-port1 global-port2* \[ **vpn-instance** *global-name* \] **inside** { { *local-address \| local-address1 local-address2* } *local-port* \| *local-address* *local-port*1 *local-port*2 } \[ **vpn-instance** *local-name* \] ]{lang="DA"}[\[ **acl** *acl-number* \]]{lang="EN-US"}

[**[undo nat server]{lang="DA"}**]{#struct_0_83269_x5501_x170681937}[ **protocol** *pro-type* **global** { *global-address \|* **current-interface** \| **interface** *interface-type* *interface-number* } *global-port1 global-port2* \[ **vpn-instance** *global-name* \] ]{lang="DA"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[外网地址连续，未使用外网端口或外网端口单一]{style="font-family:宋体"}]{#struct_0_83269_x5501_2060029475}

[**[nat server protocol]{lang="EN-US"}**[ *pro-type* **global** *global-address1 global-address2  *\[ *global-port* \] \[ **vpn-instance** *global-name* \] **inside** { *local-address* \| ]{lang="EN-US"}]{#struct_0_83269_x5501_211425045}*[local-address1 local-address2 ]{lang="DA"}*[} * *]{lang="EN-US"}[\[ *local-port* \]]{lang="EN-US"}[ ]{lang="EN-US"}[\[ **vpn-instance** *local-name* \] \[ **acl** *acl-number* \]]{lang="EN-US"}

[**[undo nat server protocol]{lang="EN-US"}**[ *pro-type* **global** *global-address1 global-address2* \[ *global-port* \] \[ **vpn-instance** *global-name* \] ]{lang="EN-US"}]{#struct_0_83269_x5501_1835006047}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[外网地址连续，外网端口单一]{style="font-family:宋体"}]{#struct_0_83269_x5501_195189109}

[**[nat server protocol]{lang="EN-US"}**[ *pro-type* **global** *global-address1 global-address2  global-port* \[ **vpn-instance** *global-name* \] **inside** ]{lang="EN-US"}]{#struct_0_83269_x5501_x1447055499}*[local-address]{lang="DA"}*[ *local-port*1 *local-port*2 ]{lang="DA"}[\[ **vpn-instance** *local-name* \] \[ **acl** *acl-number* \]]{lang="EN-US"}

[**[undo nat server protocol]{lang="EN-US"}**[ *pro-type* **global** *global-address1 global-address2  global-port* \[ **vpn-instance** *global-name* \]]{lang="EN-US"}]{#struct_0_83269_x5501_52618336}

[[(2)[      ]{style="font:7.0pt "}]{lang="DA"}[负载均衡内部服务器]{lang="EN-US" style="font-family:宋体"}]{#struct_0_83269_x5501_x1800625836}

[**[nat server protocol ]{lang="EN-US"}***[pro-type]{lang="EN-US"}***[ global ]{lang="EN-US"}**[{ { *global-address* \| **current-interface** \| **interface** *interface-type* *interface-number* } { *global-port* \| *global-port1 global-port2* } \| *global-address1 global-address2 global-port* } \[ **vpn-instance** *global-name* \] **inside server-group** *group-number* \[ **vpn-instance** *local-name* \] \[ **acl** *acl-number* \]]{lang="EN-US"}]{#struct_0_83269_x5501_x168561265}

[**[undo nat server protocol ]{lang="EN-US"}***[pro-type]{lang="EN-US"}***[ global ]{lang="EN-US"}**[{ { *global-address* \| **current-interface** \| **interface** *interface-type interface-number* } { *global-port* \| *global-port1 global-port2* } \| *global-address1 global-address2 global-port* } \[ **vpn-instance** *global-name* \]]{lang="EN-US"}]{#struct_0_83269_x5501_2141754818}

[[(3)[      ]{style="font:7.0pt "}]{lang="DA"}[基于]{style="font-family:宋体"}]{#struct_0_83269_x5501_226917077}[ACL]{lang="DA"}[的内部服务器]{style="font-family:宋体"}

[**[nat server global ]{lang="EN-US"}***[global-acl-number]{lang="EN-US"}***[ inside ]{lang="EN-US"}***[local-address]{lang="EN-US"}*[ \[ *local-port* \] \[ **vpn-instance** *local-name* \]]{lang="EN-US"}]{#struct_0_83269_x5501_x2076031261}

[**[undo nat server global ]{lang="EN-US"}***[global-acl-number]{lang="EN-US"}***[ inside ]{lang="EN-US"}***[local-address]{lang="EN-US"}*[ \[ *local-port* \] \[ **vpn-instance** *local-name* \]]{lang="EN-US"}]{#struct_0_83269_x5501_x640762472}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x110336823}

[[不存在内部服务器。]{style="font-family:宋体"}]{#struct_0_83269_x5501_179944308}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_195123573}

[[接口视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_2083315273}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x859066030}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x624544252}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_875376335}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1726160702}

[**[protocol]{lang="EN-US"}**[ *pro-type*]{lang="EN-US"}]{#struct_0_83269_x5501_25154655}[：指定协议类型。当协议类型不是]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议时，配置的内部服务器不带端口参数。]{style="font-family:宋体"}*[pro-type]{lang="EN-US"}*[可输入以下形式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[数字：取值范围为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_83269_x5501_x316255524}[～]{lang="EN-US" style="font-family:宋体"}[255]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[协议名称：取值包括]{style="font-family:宋体"}]{#struct_0_83269_x5501_x383045686}**[icmp]{lang="EN-US"}**[、]{style="font-family:宋体"}**[tcp]{lang="EN-US"}**[和]{style="font-family:宋体"}**[udp]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[global-address]{lang="EN-US"}*]{#struct_0_83269_x5501_195058037}[：内部服务器向外提供服务时对外公布的外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[global-address1]{lang="EN-US"}*]{#struct_0_83269_x5501_x1838668695}*[、]{style="font-family:宋体"}[global-address2]{lang="EN-US"}*[：外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围，所包含的地址数目不能超过]{style="font-family:宋体"}[256]{lang="FR"}[。]{style="font-family:宋体"}*[global-address1]{lang="EN-US"}*[表示起始地址，]{style="font-family:宋体"}*[global-address2]{lang="EN-US"}*[表示结束地址。]{style="font-family:宋体"}*[global-address2]{lang="EN-US"}*[必须大于]{style="font-family:宋体"}*[global-address1]{lang="EN-US"}*[。]{style="font-family:宋体"}

[**[global]{lang="EN-US"}***[ global-acl-number]{lang="EN-US"}*]{#struct_0_83269_x5501_1389716491}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。只有与指定的]{style="font-family:宋体"}[ACL permit]{lang="EN-US"}[规则匹配的报文才可以进行目的地址转换。]{style="font-family:宋体"}

[**[current-interface]{lang="EN-US"}**]{#struct_0_83269_x5501_x1637488980}[：使用当前接口的地址作为内部服务器的外网地址，即实现]{style="font-family:宋体"}[Easy IP]{lang="EN-US"}[方式的内部服务器。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x19821815}[：表示使用指定接口的地址作为内部服务器的外网地址，即实现]{style="font-family:宋体"}[Easy IP]{lang="EN-US"}[方式的内部服务器。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ ]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[接口类型和接口编号。目前只支持]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[global-port1]{lang="EN-US"}*]{#struct_0_83269_x5501_x2108456794}*[、]{style="font-family:宋体"}[global-port2]{lang="EN-US"}*[：外网端口范围，和内部主机的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围构成一一对应的关系。]{style="font-family:宋体"}*[global-port1]{lang="EN-US"}*[表示起始端口，]{style="font-family:宋体"}*[global-port2]{lang="EN-US"}*[表示结束端口。]{style="font-family:宋体"}*[global-port2]{lang="EN-US"}*[必须大于]{style="font-family:宋体"}*[global-port1]{lang="EN-US"}*[，且端口范围中的端口数目不能大于]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}[外网端口可输入以下形式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[数字：取值范围为]{style="font-family:宋体"}]{#struct_0_83269_x5501_1019263180}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。起始端口和结束端口均支持此形式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[协议名称：为]{style="font-family:宋体"}]{#struct_0_83269_x5501_995600270}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，例如]{style="font-family:宋体"}**[http]{lang="EN-US"}**[、]{style="font-family:宋体"}**[telnet]{lang="EN-US"}**[等。仅起始端口支持该形式。]{style="font-family:宋体"}

[*[local-address1]{lang="EN-US"}*]{#struct_0_83269_x5501_x686073501}[、]{style="font-family:宋体"}*[local-address2]{lang="EN-US"}*[：]{style="font-family:宋体"}[定义一组连续的内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围，和外网端口范围构成]{style="font-family:宋体"}[一一对应的关系。]{style="font-family:宋体"}*[local-address1]{lang="EN-US"}*[表示起始地址，]{style="font-family:宋体"}*[local-address2]{lang="EN-US"}*[表示结束地址。]{style="font-family:宋体"}*[local-address2]{lang="EN-US"}*[必须大于]{style="font-family:宋体"}*[local-address1]{lang="EN-US"}*[。该地址范围的数量必须和]{style="font-family:宋体"}*[global-port1]{lang="EN-US"}*[、]{style="font-family:宋体"}*[global-port2]{lang="EN-US"}*[定义的端口数量相同。]{style="font-family:宋体"}

[*[local-port]{lang="EN-US"}*]{#struct_0_83269_x5501_x1525624982}[：内部服务器的内网端口号，]{style="font-family:宋体"}[可输入以下形式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[数字：取值范围为]{style="font-family:宋体"}]{#struct_0_83269_x5501_196041077}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[（]{style="font-family:宋体"}[FTP]{lang="FR"}[数据端口号]{style="font-family:
宋体"}[20]{lang="FR"}[除外）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[协议名称：为]{style="font-family:宋体"}]{#struct_0_83269_x5501_85873477}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，例如]{style="font-family:宋体"}**[http]{lang="EN-US"}**[、]{style="font-family:宋体"}**[telnet]{lang="EN-US"}**[等。]{style="font-family:宋体"}

[*[global-port]{lang="EN-US"}*]{#struct_0_83269_x5501_x710031792}[：外网端口号，缺省值以及取值范围的要求和]{style="font-family:宋体"}*[local-port]{lang="EN-US"}*[的规定一致。]{style="font-family:宋体"}

[*[local-address]{lang="EN-US"}*]{#struct_0_83269_x5501_x1427284714}[：服务器的内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[global-name]{lang="EN-US"}*]{#struct_0_83269_x5501_128288901}[：对外公布的外网地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[global-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示对外公布的外网地址不属于任何一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[local-name]{lang="EN-US"}*]{#struct_0_83269_x5501_191055404}[：内部服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[local-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示内部服务器不属于任何一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[server-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x932849942}[：服务器在内网所属的服务器组。若指定了该参数，]{style="font-family:宋体"}[则表示要配置]{style="font-family:
宋体"}[一个负载分担内部服务器。]{style="font-family:宋体"}*[group-number]{lang="EN-US"}*[表示内部服务器组编号，不同设备的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x540404912}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}[若指定了该参数，则表示与指定的]{style="font-family:宋体"}[ACL permit]{lang="EN-US"}[规则匹配的报文才可以使用内部服务器的映射表进行地址转换。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_195975541}

[[通过该配置可以利用]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_1133108650}[设备将一些内部网络的服务器提供给外部网络使用，例如内部的]{style="font-family:宋体"}[Web]{lang="EN-US"}[服务器、]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器、]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务器、]{style="font-family:宋体"}[POP3]{lang="EN-US"}[服务器、]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器等。这些内部服务器可以位于普通的内网内，也可以位于]{style="font-family:宋体"}[MPLS VPN]{lang="EN-US"}[实例内。]{style="font-family:宋体"}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_2056763865}[内部服务器通常配置在]{style="font-family:宋体"}[NAT]{lang="EN-US"}[设备的外网侧接口上。外网]{style="font-family:宋体"}[用户可以通过]{style="font-family:宋体"}*[global-address]{lang="EN-US"}*[定义的外网地址和]{style="font-family:宋体"}*[global-port]{lang="EN-US"}*[定义的外网端口来访问内网地址和内网端口分别为]{style="font-family:宋体"}*[local-address]{lang="EN-US"}*[和]{style="font-family:宋体"}*[local-port]{lang="EN-US"}*[的内部服务器。]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器]{style="font-family:宋体"}[支持以下几种内网和外网的地址、端口映射关系。]{style="font-family:宋体"}

[[表1-18 ]{lang="EN-US"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x142165338}[内部服务器的地址与端口映射关系]{style="font-family:
黑体"}

[]{#table_struct_0_x740329913}[[外网]{style="font-family:黑体"}]{#struct_0_83269_x5501_2067313401}
:::

[[内网]{style="font-family:黑体"}]{#struct_0_83269_x5501_x975002503}

[[一个外网地址]{style="font-family:宋体"}]{#struct_0_83269_x5501_1105521361}

[[一个内网地址]{style="font-family:宋体"}]{#struct_0_83269_x5501_1341298652}

[[一个外网地址、一个端口号]{style="font-family:宋体"}]{#struct_0_83269_x5501_195516790}

[[一个内网地址、一个内网端口号]{style="font-family:宋体"}]{#struct_0_83269_x5501_302576821}

[[一个外网地址，]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_83269_x5501_1214238810}[个连续的外网端口号]{style="font-family:宋体"}

[[一个内网地址，一个内网端口]{style="font-family:宋体"}]{#struct_0_83269_x5501_x19486146}

[[N]{lang="EN-US"}]{#struct_0_83269_x5501_1666822668}[个连续的内网地址，一个内网端口号]{style="font-family:宋体"}

[[一个内网地址，]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_83269_x5501_195451254}[个连续的内网端口号]{style="font-family:宋体"}

[[N]{lang="EN-US"}]{#struct_0_83269_x5501_x1338361036}[个连续的外网地址]{style="font-family:宋体"}

[[一个内网地址]{style="font-family:宋体"}]{#struct_0_83269_x5501_543091408}

[[N]{lang="EN-US"}]{#struct_0_83269_x5501_x2135871332}[个连续的内网地址]{style="font-family:宋体"}

[[N]{lang="EN-US"}]{#struct_0_83269_x5501_1778904211}[个连续的外网地址连续，一个外网端口号]{style="font-family:宋体"}

[[一个内网地址，一个内网端口号]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1676671414}

[[N]{lang="EN-US"}]{#struct_0_83269_x5501_195385718}[个连续的内网地址，一个内网端口号]{style="font-family:宋体"}

[[一个内网地址，]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_83269_x5501_1557656532}[个连续的内网端口号]{style="font-family:宋体"}

[[一个外网地址，一个外网端口号]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1008375509}

[[一个内部服务器组]{style="font-family:宋体"}]{#struct_0_83269_x5501_522694022}

[[一个外网地址，]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_83269_x5501_203366867}[个连续的外网端口号]{style="font-family:宋体"}

[[N]{lang="EN-US"}]{#struct_0_83269_x5501_195320182}[个连续的外网地址，一个外网端口号]{style="font-family:宋体"}

[[外网地址（通过]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_83269_x5501_986497500}[进行匹配）]{style="font-family:宋体"}

[[一个内网地址]{style="font-family:宋体"}]{#struct_0_83269_x5501_x579586441}

[[一个内网地址、一个内网端口号]{style="font-family:宋体"}]{#struct_0_83269_x5501_6929925}

[ ]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_83269_x5501_1571205302}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口下允许配置的]{style="font-family:宋体"}]{#struct_0_83269_x5501_2135528217}**[nat server]{lang="EN-US"}**[命令个数与设备的型号有关。]{style="font-family:宋体"}[每个]{style="font-family:宋体"}**[nat server]{lang="EN-US"}**[命令下]{style="font-family:宋体"}[可以配置的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器数目为]{style="font-family:宋体"}*[global-port2]{lang="EN-US"}*[与]{style="font-family:宋体"}*[global-port1]{lang="EN-US"}*[的差值，即配置多少个外网端口就对应多少个]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备支持引用接口地址作为]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1966166636}[NAT]{lang="EN-US"}[内部服务器的外网地址（]{style="font-family:宋体"}[Easy IP]{lang="EN-US"}[方式）。如果配置关键字]{style="font-family:宋体"}**[current-interface]{lang="EN-US"}**[，表示外网地址使用的是当前接口的当前主地址；如果指定具体的接口，则只能指定]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口，外网地址使用的是配置的]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口的当前主地址。]{style="font-family:宋体"}[Easy IP]{lang="EN-US"}[功能的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1784294675}[Easy IP]{lang="EN-US"}[方式的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器使用了当前接口或其它接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为它的外网地址，因此强烈建议在配置了]{style="font-family:宋体"}[Easy IP]{lang="EN-US"}[方式的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器之后，其它]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器不要再配置该接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为它的外网地址，反之亦然。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_83269_x5501_195254646}*[pro-type]{lang="EN-US"}*[不是]{style="font-family:宋体"}[TCP]{lang="EN-US"}[（协议号为]{style="font-family:宋体"}[6]{lang="EN-US"}[）或]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（协议号为]{style="font-family:宋体"}[17]{lang="EN-US"}[）时，用户只能设置内部]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址与外部]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的一一对应的关系，无法设置端口号之间的映射。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于同一个接口下配置的]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1355583440}[NAT]{lang="EN-US"}[服务器，其协议类型、外网地址和外网端口号的组合必须是唯一的，否则认为是配置冲突。本规则同样适用于]{style="font-family:宋体"}[Easy IP]{lang="EN-US"}[方式的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[服务器，其外网地址为指定接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于同一个接口下配置的]{style="font-family:宋体"}]{#struct_0_83269_x5501_999564380}[Easy IP]{lang="EN-US"}[方式的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[服务器，其协议类型、接口名和外网端口的组合必须是唯一的，否则认为是配置冲突。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_83269_x5501_x508553150}[Easy IP]{lang="EN-US"}[方式的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[服务器，如果其引用的接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发生改变，导致跟现有的其它非]{style="font-family:宋体"}[Easy IP]{lang="EN-US"}[方式的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[服务器冲突，则]{style="font-family:宋体"}[Easy IP]{lang="EN-US"}[方式的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[服务器配置失效；如果接口地址又修改为不冲突的]{style="font-family:宋体"}[IP]{lang="EN-US"}[，或者之前与之冲突的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[服务器被删除，则]{style="font-family:宋体"}[Easy IP]{lang="EN-US"}[方式的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置重新生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x27231062}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x346750432}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器，]{style="font-family:宋体"}[指定局域网内部的]{style="font-family:宋体"}[Web]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}[10.110.10.10]{lang="EN-US"}[，希望外部通过]{style="font-family:宋体"}[http://202.110.10.10:8080]{lang="EN-US"}[可以访问]{style="font-family:宋体"}[Web]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x1138029877}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] nat server protocol tcp global 202.110.10.10 8080 inside 10.110.10.10 http]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_509259630}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器，]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[MPLS VPN vrf10]{lang="EN-US"}[内部的]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}[10.110.10.11]{lang="EN-US"}[，希望外部通过]{style="font-family:宋体"}[ftp://202.110.10.10]{lang="EN-US"}[可以访问]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_83269_x5501_1200622283}

[\[Sysname-GigabitEthernet1/0/1\] nat server protocol tcp global 202.110.10.10 21 inside 10.110.10.11 vpn-instance vrf10]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1383044027}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器，]{style="font-family:宋体"}[指定一个]{style="font-family:宋体"}[VPN vrf10]{lang="EN-US"}[内部的主机]{style="font-family:宋体"}[10.110.10.12]{lang="EN-US"}[，希望外部网络的主机可以利用]{style="font-family:宋体"}[ping 202.110.10.11]{lang="EN-US"}[命令]{style="font-family:宋体"}[ping]{lang="EN-US"}[通它。]{style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_83269_x5501_x1520366901}

[\[Sysname-GigabitEthernet1/0/1\] nat server protocol icmp global 202.110.10.11 inside 10.110.10.12 vpn-instance vrf10]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x374155962}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器，]{style="font-family:宋体"}[指定一个外部地址]{style="font-family:宋体"}[202.110.10.10]{lang="EN-US"}[，从端口]{style="font-family:宋体"}[1001]{lang="EN-US"}[～]{style="font-family:宋体"}[1100]{lang="EN-US"}[分别映射]{style="font-family:宋体"}[MPLS VPN vrf10]{lang="EN-US"}[内主机]{style="font-family:宋体"}[10.110.10.1]{lang="EN-US"}[～]{style="font-family:宋体"}[10.110.10.100]{lang="EN-US"}[的]{style="font-family:宋体"}[telnet]{lang="EN-US"}[服务。]{style="font-family:宋体"}[202.110.10.10:1001]{lang="EN-US"}[访问]{style="font-family:宋体"}[10.110.10.1]{lang="EN-US"}[，]{style="font-family:宋体"}[202.110.10:1002]{lang="EN-US"}[访问]{style="font-family:宋体"}[10.110.10.2]{lang="EN-US"}[，依此类推。]{style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_83269_x5501_2083315280}

[[\[Sysname-GigabitEthernet1/0/1\] nat server protocol tcp global 202.110.10.10 1001 1100 inside 10.110.10.1 10.110.10.100 telnet vpn-instance vrf10]{lang="EN-US"}]{#struct_0_83269_x5501_x859262627}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_226982613}[正确的服务器地址为]{style="font-family:宋体"}[10.0.0.172]{lang="EN-US"}[，用户配置的错误地址为]{style="font-family:宋体"}[192.168.0.0/24]{lang="EN-US"}[网段的地址，在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置基于]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的内部服务器对这部分用户的配置错误进行纠正。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_1801191912}

[\[Sysname\] acl advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 5 permit ip destination 192.168.0.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] nat server global 3000 inside 10.0.0.172]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1318521007}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_x926117913}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat server]{lang="EN-US"}**]{#struct_0_83269_x5501_x1656255429}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[nat server-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x1287181542}

::: {#-172844674 .myid}
[]{#_Toc404786519}[]{#struct_0_83269_x5501_x242613237}

**NAT命令 \-- NAT配置命令 \-- nat server-group**

------------------------------------------------------------------------

[**[nat server-group]{lang="EN-US"}**]{#struct_0_83269_x5501_195058038}[命令用来配置一个内部服务器组。]{style="font-family:宋体"}

[**[undo nat server-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x1838668682}[命令用来删除指定的内部服务器组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x2040839043}

[**[nat server-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x607380923}

[**[undo nat server-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x219156194}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1614396233}

[[不存在内部服务器组。]{style="font-family:宋体"}]{#struct_0_83269_x5501_1629023866}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_2059440566}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x733079278}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_196041078}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_85873488}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_57066407}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x973466705}

[*[group-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x1517896159}[：[[服务器组编号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{.FigureChar}]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_958840888}

[[一个内部服务器组中可以包括多个内部服务器组成员（通过]{style="font-family:宋体"}**[inside ip]{lang="EN-US"}**]{#struct_0_83269_x5501_x210047051}[命令配置）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x959035825}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x853628256}[配置一个内部服务器组，编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_195975542}

[[\[Sysname\] nat server-group 1]{lang="EN-US"}]{#struct_0_83269_x5501_1133108651}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_2056829401}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_x615168059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat server-group]{lang="EN-US"}**]{#struct_0_83269_x5501_2018473708}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[inside ip]{lang="EN-US"}**]{#struct_0_83269_x5501_x554591401}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat server]{lang="EN-US"}**]{#struct_0_83269_x5501_x1751679538}
:::

::::: {#1226113338 .myid}
[]{#_Toc404786520}[]{#struct_0_83269_x5501_x2061259079}[]{#_Toc371600470}[]{#_Toc351728017}[]{#_Toc357498976}

**NAT命令 \-- NAT配置命令 \-- nat service**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NAT命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_83269_x5501_667624276}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_83269_x5501_1783369523}
:::

[ ]{lang="EN-US"}

[**[nat service]{lang="EN-US"}**]{#struct_0_83269_x5501_217285582}[命令用来指定提供]{style="font-family:宋体"}[NAT]{lang="EN-US"}[处理的业务板。]{style="font-family:宋体"}

[**[undo nat service]{lang="EN-US"}**]{#struct_0_83269_x5501_1427073627}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1073704525}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_83269_x5501_x139010314}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[nat service slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_264274213}

[**[undo nat service slot]{lang="EN-US"}**]{#struct_0_83269_x5501_x1301809728}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_83269_x5501_x898525201}[模式：]{style="font-family:宋体"}

[**[nat service chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_1830358154}

[**[undo nat service chassis]{lang="EN-US"}**]{#struct_0_83269_x5501_667558740}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1783303987}

[[未指定提供]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_217220046}[处理的业务板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1427008091}

[[接口视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x139075850}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_264208677}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x1301875264}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x898590737}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1830292618}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x2061390151}[：指定单板所在的槽位号。]{lang="EN-US" style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备]{lang="EN-US" style="font-family:宋体"}[－]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:black"}[独立运行模式）]{lang="EN-US" style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_667493204}[：指定设备在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{lang="EN-US" style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{lang="EN-US" style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_83269_x5501_322451633}[：指定设备在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。]{lang="EN-US" style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。]{lang="EN-US" style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_1783238451}[：指定单板。]{lang="EN-US" style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{lang="EN-US" style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板报在的槽位号]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{lang="EN-US" style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－]{style="font-size:10.0pt;font-family:宋体;color:black"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_217154510}

[[对于支持本命令的设备，必须在配置了]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x4858122}[业务的接口上指定提供]{style="font-family:宋体"}[NAT]{lang="EN-US"}[处理的业务板。只有为接口指定了业务板，接口的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[功能才能生效。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_83269_x5501_398426405}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[一个接口上的]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1167657536}[NAT]{lang="EN-US"}[业务只能由一块业务板处理，该业务板可以是设备上的任意可提供]{style="font-family:宋体"}[NAT]{lang="EN-US"}[处理的业务板。通常，如果接口所在的板具有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[处理能力，那么建议将接口所在板指定为]{style="font-family:宋体"}[NAT]{lang="EN-US"}[业务板。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[如果要修改接口下指定的业务板，需要先恢复缺省情况再重新指定。]{style="font-family:宋体"}]{#struct_0_83269_x5501_x764373009}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[多个接口引用了同一个地址组或外网地址时，这些接口必须指定同一块业务板进行]{style="font-family:宋体"}]{#struct_0_83269_x5501_1964510346}[NAT]{lang="EN-US"}[处理。]{style="font-family:宋体"}[否则，可能会出现配置成功但实际不生效的情况，并且在配置恢复（由设备重启、软件升级等原因导致）时可能会造成配置丢失]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1387549477}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1927172423}[指定]{style="font-family:宋体"}[5]{lang="EN-US"}[号单板作为提供]{style="font-family:宋体"}[NAT]{lang="EN-US"}[处理的业务板。（分布式设备]{style="font-family:宋体"}[－]{style="font-size:10.0pt;
font-family:宋体;color:black"}[独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_1917456179}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] nat service slot 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_351372238}[指定]{style="font-family:宋体"}[5]{lang="EN-US"}[号成员设备作为提供]{style="font-family:宋体"}[NAT]{lang="EN-US"}[处理的业务板。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_1561160283}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname- GigabitEthernet1/0/1\] nat service slot 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x4923658}[指定]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[5]{lang="EN-US"}[号单板作为提供]{style="font-family:宋体"}[NAT]{lang="EN-US"}[处理的业务板。（分布式]{style="font-family:宋体"}[设备]{style="font-size:11.0pt;
font-family:宋体"}[－]{style="font-size:10.0pt;font-family:宋体;
color:black"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_398360869}

[\[Sysname\] interface gigabitethernet 1/3/0/1]{lang="EN-US"}

[\[Sysname- GigabitEthernet1/3/0/1\] nat service chassis 2 slot 5]{lang="EN-US"}
:::::

::::: {#2107084249 .myid}
[]{#_Toc404786521}[]{#struct_0_83269_x5501_1884070499}[]{#_Toc380589027}

**NAT命令 \-- NAT配置命令 \-- nat static-load-balance enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NAT命令.files/image001.png){#图片 1 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_83269_x5501_x495487127}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_83269_x5501_418028226}
:::

[ ]{lang="EN-US"}

[**[nat static-load-balance enable]{lang="EN-US"}**]{#struct_0_83269_x5501_1884004963}[命令用来[使能静态]{style="color:black"}]{style="font-family:宋体"}[NAT]{lang="EN-US" style="color:black"}[在多个]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[上进行负载分担的功能]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[**[undo nat static-load-balance enable]{lang="EN-US"}**]{#struct_0_83269_x5501_1879525860}[命令用来关闭[静态]{style="color:black"}]{style="font-family:宋体"}[NAT]{lang="EN-US" style="color:black"}[在多个]{style="font-family:宋体;
color:black"}[CPU]{lang="EN-US" style="color:black"}[上进行负载分担的功能]{style="font-family:宋体;color:black"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x580808145}

[**[nat static-load-balance enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x799235951}

[**[undo nat static-load-balance enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x658144432}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1914429542}

[[静态]{style="font-family:宋体;color:black"}[NAT]{lang="EN-US" style="color:black"}]{#struct_0_83269_x5501_813498137}[在多个]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[上进行负载分担的功能处于关闭状态]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_83269_x5501_8960821}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_356825467}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_695672178}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_2047119842}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_794841187}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1884201571}

[[使能本功能后，设备会将静态]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_281996368}[的处理分担到不同的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上，以均衡各个]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的负载。如果关闭本功能，则所有静态]{style="font-family:宋体"}[NAT]{lang="EN-US"}[都由主]{style="font-family:宋体"}[CPU]{lang="EN-US"}[来处理，可能会导致主]{style="font-family:宋体"}[CPU]{lang="EN-US"}[负载过重。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x844457598}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x2032022962}[使能静态]{style="font-family:宋体;color:black"}[NAT]{lang="EN-US" style="color:black"}[在多个]{style="font-family:宋体;
color:black"}[CPU]{lang="EN-US" style="color:black"}[上进行负载分担的功能]{style="font-family:宋体;color:black"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x577002308}

[\[Sysname\] nat static-load-balance enable]{lang="EN-US"}
:::::

::: {#1359631161 .myid}
[]{#_Toc404786522}[]{#struct_0_83269_x5501_x1174100092}[]{#_Toc374719625}

**NAT命令 \-- NAT配置命令 \-- nat static enable**

------------------------------------------------------------------------

[**[nat static enable]{lang="EN-US"}**]{#struct_0_83269_x5501_195516787}[命令用来开启接口上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[静态地址转换功能。]{style="font-family:宋体"}

[**[undo nat static enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x1653738312}[命令用来关闭接口上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[静态地址转换功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1207462803}

[**[nat static enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x2132405735}

[**[undo nat static enable]{lang="EN-US"}**]{#struct_0_83269_x5501_109398196}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_2042159853}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_702959714}[静态地址转换功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_566797600}

[[接口视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1027867294}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_195451251}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x1338361031}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_x1829561587}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_177536342}

[[接口下开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x224417342}[静态地址转换功能后，所有已配置的静态地址转换映射都会在该接口上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1209692991}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_2038562181}[配置内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.1]{lang="EN-US"}[到外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的出方向一对一静态地址转换，并且在]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[开启静态地址转换功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_1071051243}

[[\[Sysname\] nat static outbound 192.168.1.1 2.2.2.2]{lang="EN-US"}]{#struct_0_83269_x5501_x1661484944}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_83269_x5501_195385715}

[[\[Sysname-GigabitEthernet1/0/1\] nat static enable]{lang="EN-US"}]{#struct_0_83269_x5501_1557656527}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1008178902}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_x22034683}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nat static]{lang="EN-US"}**]{#struct_0_83269_x5501_620500932}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat static]{lang="EN-US"}**]{#struct_0_83269_x5501_1757028314}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[nat static net-to-net]{lang="EN-US"}**]{#struct_0_83269_x5501_x1225602583}
:::

::: {#-1869696753 .myid}
[]{#_Toc404786523}[]{#struct_0_83269_x5501_x730312866}

**NAT命令 \-- NAT配置命令 \-- nat static inbound**

------------------------------------------------------------------------

[**[nat static inbound]{lang="PT-BR"}**]{#struct_0_83269_x5501_x534590591}[命令用来配置入方向一对一静态地址转换映射。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **nat static**]{lang="EN-US"}]{#struct_0_83269_x5501_195320179}**[ inbound]{lang="PT-BR"}**[命令用来删除指定的入方向一对一静态地址转换映射。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1144238255}

[**[nat static inbound]{lang="EN-US"}***[ global-ip ]{lang="EN-US"}*[\[ **vpn-instance** *global-name* \] *local-ip* \[ **vpn-instance** *local-name* \] \[ **acl** *acl-number*[ \[ **reversible** \] \]]{style="color:black"}]{lang="EN-US"}]{#struct_0_83269_x5501_x812259085}

[**[undo]{lang="EN-US"}**[ **nat static inbound** *global-ip* \[ **vpn-instance** *global-name* \] ]{lang="EN-US"}]{#struct_0_83269_x5501_x852884944}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x541646691}

[[不存在任何地址转换映射。]{style="font-family:宋体"}]{#struct_0_83269_x5501_x388409866}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1629875021}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_1235356402}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1244081160}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_195254643}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_783706315}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1355583437}

[*[global-ip]{lang="EN-US"}*]{#struct_0_83269_x5501_1759406947}[：外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[global-name]{lang="EN-US"}*]{#struct_0_83269_x5501_1738500326}[：外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[global-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[的]{style="font-family:宋体"}[VPN]{lang="FR"}[实例名称，为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不属于任何一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[local-ip]{lang="EN-US"}*]{#struct_0_83269_x5501_x1099164551}[：内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ local-name]{lang="EN-US"}*]{#struct_0_83269_x5501_536885840}[：内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[local-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不属于任何一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x1461085048}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。本参数用于控制指定源地址的内网主机可以访问外网。]{style="font-family:宋体"}

[**[reversible]{lang="EN-US" style="color:black"}**]{#struct_0_83269_x5501_172281575}[：]{style="font-family:
宋体;color:black"}[表示从内网主动访问外网的报文必须通过]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配，才能使用该配置进行目的地址转换。]{style="font-family:宋体"}[该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_195189107}

[[对于从外网到内网的报文，将其源地址]{style="font-family:宋体"}*[global-ip]{lang="EN-US"}*]{#struct_0_83269_x5501_x1447055501}[转换为]{style="font-family:宋体"}*[local-ip]{lang="EN-US"}*[；]{style="font-family:宋体"}[对于从内网到外网的报文，将其目的地址]{style="font-family:宋体"}*[local-ip]{lang="EN-US"}*[转换为]{style="font-family:宋体"}*[global-ip]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_83269_x5501_x303153271}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定]{style="font-family:宋体"}]{#struct_0_83269_x5501_1339784255}[ACL]{lang="EN-US"}[，则所有从外网到内网的报文都可以使用该配置进行源地址转换；所有从内网到外网的报文都可以使用该配置进行目的地址转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果仅指定了]{style="font-family:宋体"}]{#struct_0_83269_x5501_348865107}[ACL]{lang="EN-US"}[，没有指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（即没有配置]{style="font-family:宋体"}**[reversible]{lang="EN-US" style="color:black"}**[），对于从外网到内网的报文，只有报文符合]{style="font-family:宋体"}[ACL permit]{lang="EN-US"}[规则，才能使用该配置进行源地址转换；对于从内网主动访问外网的报文，不能使用该配置进行目的地址转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果既指定了]{style="font-family:宋体"}]{#struct_0_83269_x5501_1566303186}[ACL]{lang="EN-US"}[，又指定了]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（即配置了]{style="font-family:宋体"}**[reversible]{lang="EN-US" style="color:black"}**[），对于外网到内网的报文，只有报文符合]{style="font-family:宋体"}[ACL permit]{lang="EN-US"}[规则，才能使用该配置进行源地址转换；对于从内网主动访问外网的报文，需要进行]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（提取报文的源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口和目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口，并根据配置转换目的地址，然后将源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口和目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口互换去匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[），只有反向匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的报文才能使用该配置进行转换，否则不予转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口下既配置了]{style="font-family:宋体"}]{#struct_0_83269_x5501_850637239}[NAT]{lang="EN-US"}[动态地址转换，又使能了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[静态地址转换，则优先使用静态地址转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备可支持配置多条入方向静态地址转换映射（包括]{lang="EN-US" style="font-family:宋体"}**[nat static inbound]{lang="EN-US"}**]{#struct_0_83269_x5501_1328501926}[和]{lang="EN-US" style="font-family:
宋体"}**[nat static inbound net-to-net]{lang="EN-US"}**[）。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1771526186}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1890411587}[配置外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[到]{style="font-family:宋体"}[内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.1]{lang="EN-US"}[的入方向静态地址转换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_195123571}

[\[Sysname\] nat static inbound 2.2.2.2 192.168.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_2083315275}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_x859459246}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat static]{lang="EN-US"}**]{#struct_0_83269_x5501_882516682}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[nat static enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x1714723756}
:::

::: {#1550445864 .myid}
[]{#_Toc404786524}[]{#struct_0_83269_x5501_x1998510167}

**NAT命令 \-- NAT配置命令 \-- nat static inbound net-to-net**

------------------------------------------------------------------------

[**[nat static inbound net-to-net]{lang="PT-BR"}**]{#struct_0_83269_x5501_x851011123}[命令用来配置入方向网段到网段的静态地址转换映射。]{style="font-family:
宋体"}

[**[undo nat static inbound net-to-net]{lang="PT-BR"}**]{#struct_0_83269_x5501_707296524}[命令用来删除指定的入方向网段到网段的静态地址转换映射。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_195058035}

[**[nat static inbound net-to-net ]{lang="EN-US"}***[global-start-address global-end-address ]{lang="EN-US"}*[\[ **vpn-instance** *global -name* \] **local** *local-network* { *mask-length* \| *mask* } \[ **vpn-instance** *local-name* \] \[ **acl** *acl-number*[ \[ **reversible** \] \]]{style="color:black"}]{lang="EN-US"}]{#struct_0_83269_x5501_x1838668693}

[**[undo nat static inbound net-to-net ]{lang="EN-US"}***[global-start-address global-end-address ]{lang="EN-US"}*[\[ **vpn-instance** *global -name* \]]{lang="EN-US"}]{#struct_0_83269_x5501_x474689566}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_155838800}

[[不存在任何地址转换映射。]{style="font-family:宋体"}]{#struct_0_83269_x5501_1435814411}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x52608602}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1702947009}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_665765421}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x1347275784}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_196041075}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_85873475}

[*[global-start-address global-end-address]{lang="FR"}*]{#struct_0_83269_x5501_x327694768}[：]{style="font-family:宋体"}[外网地址范围，]{style="font-family:宋体"}[所包含的地址数目不能超过]{style="font-family:宋体"}[255]{lang="FR"}[。]{style="font-family:宋体"}*[global-start-address]{lang="FR"}*[表示起始地址，]{style="font-family:宋体"}*[global-end-address]{lang="FR"}*[表示结束地址。]{style="font-family:宋体"}*[global-end-address]{lang="FR"}*[必须大于或等于]{style="font-family:宋体"}*[global-start-address]{lang="FR"}*[，]{style="font-family:宋体"}[如果]{style="font-family:宋体"}[二者]{style="font-family:宋体"}[相同]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则表示只有一个地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[global-name]{lang="EN-US"}*]{#struct_0_83269_x5501_x1131335888}[：外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[global-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[的]{style="font-family:宋体"}[VPN]{lang="FR"}[实例名称，为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不属于任何一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[local-network]{lang="PT-BR"}*]{#struct_0_83269_x5501_x1020306870}[：]{style="font-family:宋体"}[内网网段地址。]{style="font-family:宋体"}

[*[mask-length]{lang="PT-BR"}*]{#struct_0_83269_x5501_131636647}[：]{style="font-family:宋体"}[内网网络地址的掩码长度，取值范围为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="PT-BR"}*]{#struct_0_83269_x5501_x1156977027}[：内网网络地址掩码。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ local-name]{lang="EN-US"}*]{#struct_0_83269_x5501_x1626899709}[：内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[local-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不属于任何一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_83269_x5501_1233507150}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。本参数用于控制指定源地址的内网主机可以访问外网。]{style="font-family:宋体"}

[**[reversible]{lang="EN-US" style="color:black"}**]{#struct_0_83269_x5501_195975539}[：]{style="font-family:
宋体;color:black"}[表示从内网主动访问外网的报文必须通过]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配，才能使用该配置进行目的地址转换。[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="color:black"}]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x58532446}

[[外网网段通过起始地址和结束地址来指定，内网网段通过内网地址和掩码来指定。]{style="font-family:宋体"}]{#struct_0_83269_x5501_1629558542}

[[对于从外网到内网的报文，使用其源地址匹配]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1811163120}[外网地址，将源地址转换为内网地址；]{style="font-family:
宋体"}[对于从内网到外网的报文，使用其目的地址匹配]{style="font-family:宋体"}[内网地址，将目的地址转换为外网地址。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_83269_x5501_1963732143}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[外网结束地址不能大于外网起始地址和内网掩码所决定的网段中的最大]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1224655707}[IP]{lang="EN-US"}[地址。比如：内网地址配置为]{style="font-family:宋体"}[2.2.2.0]{lang="EN-US"}[，掩码为]{style="font-family:宋体"}[255.255.255.0]{lang="EN-US"}[，外网起始地址为]{style="font-family:宋体"}[1.1.1.100]{lang="EN-US"}[，则外网结束地址不应该大于]{style="font-family:宋体"}[1.1.1.0/24]{lang="EN-US"}[网段中可用的最大]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，即]{style="font-family:宋体"}[1.1.1.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定]{style="font-family:宋体"}]{#struct_0_83269_x5501_80824194}[ACL]{lang="EN-US"}[，则所有从外网到内网的报文都可以使用该配置进行源地址转换；所有从内网到外网的报文都可以使用该配置进行目的地址转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果仅指定了]{style="font-family:宋体"}]{#struct_0_83269_x5501_x812828611}[ACL]{lang="EN-US"}[，没有指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（即没有配置]{style="font-family:宋体"}**[reversible]{lang="EN-US" style="color:black"}**[），对于从外网到内网的报文，只有报文符合]{style="font-family:宋体"}[ACL permit]{lang="EN-US"}[规则，才能使用该配置进行源地址转换；对于从内网到外网的报文，不能使用该配置进行目的地址转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果既指定了]{style="font-family:宋体"}]{#struct_0_83269_x5501_1491236856}[ACL]{lang="EN-US"}[，又指定了]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（即配置了]{style="font-family:宋体"}**[reversible]{lang="EN-US" style="color:black"}**[），对于外网到内网的报文，只有报文符合]{style="font-family:宋体"}[ACL permit]{lang="EN-US"}[规则，才能使用该配置进行源地址转换；对于从内网到外网的报文，需要进行]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（提取报文的源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口和目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口，并根据配置转换目的地址，然后将源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口和目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口互换去匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[），只有反向匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的报文才能使用该配置进行转换，否则不予转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口下既配置了]{style="font-family:宋体"}]{#struct_0_83269_x5501_x856997336}[NAT]{lang="EN-US"}[动态地址转换，又使能了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[静态地址转换，则优先使用静态地址转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备支持配置]{lang="EN-US" style="font-family:宋体"}]{#struct_0_83269_x5501_195516788}[多条入方向]{style="font-family:宋体"}[静态地址转换映射（包括]{lang="EN-US" style="font-family:宋体"}**[nat static inbound]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:
宋体"}**[nat static inbound net-to-net]{lang="EN-US"}**[）。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1653738323}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_358555602}[配置外网网段]{style="font-family:宋体"}[202.100.1.0/24]{lang="EN-US"}[到内网网段]{style="font-family:宋体"}[192.168.1.0/24]{lang="EN-US"}[的入方向静态地址转换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x295741304}

[[\[Sysname\] nat static inbound net-to-net 202.100.1.1 202.100.1.255 local 192.168.1.0 24]{lang="EN-US"}]{#struct_0_83269_x5501_x204557907}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_242372372}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_1866433811}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat static]{lang="EN-US"}**]{#struct_0_83269_x5501_x2024165096}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[nat static enable]{lang="EN-US"}**]{#struct_0_83269_x5501_856290023}
:::

::: {#-2089986515 .myid}
[]{#_Toc404786525}[]{#struct_0_83269_x5501_195451252}[]{#_Ref311208999}

**NAT命令 \-- NAT配置命令 \-- nat static outbound**

------------------------------------------------------------------------

[**[nat static outbound]{lang="PT-BR"}**]{#struct_0_83269_x5501_x1338361034}[命令用来配置出方向一对一静态地址转换映射。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **nat static outbound**]{lang="EN-US"}]{#struct_0_83269_x5501_1705890822}[命令用来删除出方向一对一静态地址转换映射。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1382407453}

[**[nat static outbound ]{lang="EN-US"}***[local-ip]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **vpn-instance** *local-name* \] *global-ip* \[ **vpn-instance** *global-name* \] \[ **acl** *acl-number*[ \[ **reversible** \] \]]{style="color:black"}]{lang="EN-US"}]{#struct_0_83269_x5501_x1767107825}

[**[undo]{lang="EN-US"}**[ **nat static outbound** *local-ip* \[ **vpn-instance** *local-name* \] ]{lang="EN-US"}]{#struct_0_83269_x5501_x713948913}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1947039704}

[[不存在任何地址转换映射。]{style="font-family:宋体"}]{#struct_0_83269_x5501_368991561}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x152783634}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_255759582}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_195385716}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1557656530}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_x1008506581}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1973955191}

[*[local-ip]{lang="EN-US"}*]{#struct_0_83269_x5501_x1497525830}[：内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ local-name]{lang="EN-US"}*]{#struct_0_83269_x5501_x1793020876}[：内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[local-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不属于任何一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[global-ip]{lang="EN-US"}*]{#struct_0_83269_x5501_1443833675}[：外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[global-name]{lang="EN-US"}*]{#struct_0_83269_x5501_1598082616}[：外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[global-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[的]{style="font-family:宋体"}[VPN]{lang="FR"}[实例名称，为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不属于任何一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_83269_x5501_1885106039}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。本参数用于控制内网主机可以访问的目的地址。]{style="font-family:宋体"}

[**[reversible]{lang="EN-US" style="color:black"}**]{#struct_0_83269_x5501_195320180}[：]{style="font-family:
宋体;color:black"}[表示从外网主动访问内网的报文必须通过]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配，才能使用该配置进行目的地址转换]{style="font-family:宋体"}[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1571205304}

[[对于从内网到外网的报文，将其源地址]{style="font-family:宋体"}*[local-ip]{lang="EN-US"}*]{#struct_0_83269_x5501_2135397145}[转换为]{style="font-family:宋体"}*[global-ip]{lang="EN-US"}*[；]{style="font-family:宋体"}[对于从外网到内网的报文，将其目的地址]{style="font-family:宋体"}*[global-ip]{lang="EN-US"}*[转换为]{style="font-family:宋体"}*[local-ip]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_83269_x5501_x372856286}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定]{style="font-family:宋体"}]{#struct_0_83269_x5501_x595018067}[ACL]{lang="EN-US"}[，则所有从内网到外网的报文都可以使用该配置进行源地址转换；所有从外网到内网的报文都可以使用该配置进行目的地址转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果仅指定了]{style="font-family:宋体"}]{#struct_0_83269_x5501_x520716186}[ACL]{lang="EN-US"}[，没有指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（即没有配置]{style="font-family:宋体"}**[reversible]{lang="EN-US" style="color:black"}**[），对于从内网到外网的报文，只有报文符合]{style="font-family:宋体"}[ACL permit]{lang="EN-US"}[规则，才能使用该配置进行源地址转换；对于从外网主动访问内网的报文，不能使用该配置进行目的地址转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果既指定了]{style="font-family:宋体"}]{#struct_0_83269_x5501_x153675700}[ACL]{lang="EN-US"}[，又指定了]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（即配置了]{style="font-family:宋体"}**[reversible]{lang="EN-US" style="color:black"}**[），对于从内网到外网的报文，只有报文符合]{style="font-family:宋体"}[ACL permit]{lang="EN-US"}[规则，才能使用该配置进行源地址转换；对于从外网主动访问内网的报文，需要进行]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（提取报文的源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口和目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口，并根据配置转换目的地址，然后将源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口和目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口互换去匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[），只有反向匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的报文才能使用该配置进行转换，否则不予转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口下既配置了]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1690653756}[NAT]{lang="EN-US"}[动态地址转换，又使能了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[静态地址转换，则优先使用静态地址转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备可支持配置多条出方向]{lang="EN-US" style="font-family:宋体"}]{#struct_0_83269_x5501_612974775}[静态地址转换映射]{lang="EN-US" style="font-family:宋体"}[（包括]{lang="EN-US" style="font-family:宋体"}**[nat static outbound]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[nat static outbound net-to-net]{lang="EN-US"}**[）。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_195254644}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_783706312}[配置内网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.1]{lang="EN-US"}[到外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的出方向静态地址转换映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x1355583442}

[[\[Sysname\] nat static outbound 192.168.1.1 2.2.2.2]{lang="EN-US"}]{#struct_0_83269_x5501_x2132603502}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x649085615}[配置出方向静态地址转换映射，允许内网用户]{style="font-family:宋体"}[192.168.1.1]{lang="EN-US"}[访问外网网段]{style="font-family:宋体"}[3.3.3.0/24]{lang="EN-US"}[时，使用外网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_644133529}

[[\[Sysname\] acl advanced 3001]{lang="EN-US"}]{#struct_0_83269_x5501_168740836}

[[\[Sysname-acl-ipv4-adv-3001\] rule permit ip destination 3.3.3.0 0.0.0.255]{lang="EN-US"}]{#struct_0_83269_x5501_87544339}

[[\[Sysname-acl-ipv4-adv-3001\] quit]{lang="EN-US"}]{#struct_0_83269_x5501_1520023624}

[[\[Sysname\] nat static outbound 192.168.1.1 2.2.2.2 acl 3001]{lang="EN-US"}]{#struct_0_83269_x5501_195189108}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1447055498}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_1618702277}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat static]{lang="EN-US"}**]{#struct_0_83269_x5501_186391430}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[nat static enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x235264751}
:::

::: {#-1250383985 .myid}
[]{#_Toc404786526}[]{#struct_0_83269_x5501_x1868624000}

**NAT命令 \-- NAT配置命令 \-- nat static outbound net-to-net**

------------------------------------------------------------------------

[**[nat static outbound net-to-net]{lang="PT-BR"}**]{#struct_0_83269_x5501_1200521828}[命令用来配置出方向网段到网段的静态地址转换映射。]{style="font-family:
宋体"}

[**[undo nat static outbound net-to-net]{lang="PT-BR"}**]{#struct_0_83269_x5501_515151840}[命令用来删除出方向网段到网段的静态地址转换映射。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_354335050}

[**[nat static outbound net-to-net]{lang="EN-US"}**[ *local-start-address* *local-end-address* \[ **vpn-instance** *local-name* \] **global** *global-network* { *mask-length* \| *mask* } \[ **vpn-instance** *global-name* \] \[ **acl** *acl-number* [\[ **reversible** \] ]{style="color:black"}\]]{lang="EN-US"}]{#struct_0_83269_x5501_195123572}

[**[undo nat static outbound net-to-net]{lang="EN-US"}**[ *local-start-address* *local-end-address* \[ **vpn-instance** *local-name* \] ]{lang="EN-US"}]{#struct_0_83269_x5501_2083315274}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x859524782}

[[不存在任何地址转换映射。]{style="font-family:宋体"}]{#struct_0_83269_x5501_2118918150}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_343710766}

[[系统视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_1031188143}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x739722792}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_460966898}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_768521340}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_195058036}

[*[local-start-address local-end-address]{lang="FR"}*]{#struct_0_83269_x5501_x1838668696}[：]{style="font-family:宋体"}[内网地址范围，]{style="font-family:宋体"}[所包含的地址数目不能超过]{style="font-family:宋体"}[255]{lang="FR"}[。]{style="font-family:宋体"}*[local-start-address]{lang="FR"}*[ ]{lang="FR"}[表示起始地址，]{style="font-family:宋体"}*[local-end-address]{lang="FR"}*[表示结束地址。]{style="font-family:宋体"}*[local-end-address]{lang="FR"}*[必须大于或等于]{style="font-family:宋体"}*[local-start-address]{lang="FR"}*[，]{style="font-family:宋体"}[如果]{style="font-family:宋体"}[二者]{style="font-family:宋体"}[相同]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则表示只有一个地址。]{style="font-family:宋体"}

[*[global-network]{lang="PT-BR"}*]{#struct_0_83269_x5501_x71405039}[：外网网段地址。]{style="font-family:宋体"}

[*[mask-length]{lang="PT-BR"}*]{#struct_0_83269_x5501_x1696542287}[：外网网络]{style="font-family:宋体"}[地址的掩码长度，取值范围为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="PT-BR"}*]{#struct_0_83269_x5501_x1930904924}[：外网网络地址掩码。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x170634627}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。本参数用于控制内网主机可以访问的目的地址]{style="font-family:宋体"}

[**[reversible]{lang="EN-US" style="color:black"}**]{#struct_0_83269_x5501_878368043}[：]{style="font-family:
宋体;color:black"}[表示从外网主动访问内网的报文必须通过]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配，才能使用该配置进行目的地址转换]{style="font-family:宋体"}[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1093562155}

[[内网网段通过起始地址和结束地址来指定，外网网段通过外网地址和掩码来指定。]{style="font-family:宋体"}]{#struct_0_83269_x5501_196041076}

[[对于从内网到外网的报文，使用其源地址匹配]{style="font-family:宋体"}]{#struct_0_83269_x5501_85873478}[内网地址，将源地址转换为外网地址；]{style="font-family:
宋体"}[对于从外网到内网的报文，使用其目的地址匹配]{style="font-family:宋体"}[外网地址，将目的地址转换为内网地址。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_83269_x5501_10012240}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[内网结束地址不能大于内网起始地址和外网掩码所决定的网段中的最大]{style="font-family:宋体"}]{#struct_0_83269_x5501_x2133399909}[IP]{lang="EN-US"}[地址。比如：外网地址配置为]{style="font-family:宋体"}[2.2.2.0]{lang="EN-US"}[，掩码为]{style="font-family:宋体"}[255.255.255.0]{lang="EN-US"}[，内网起始地址为]{style="font-family:宋体"}[1.1.1.100]{lang="EN-US"}[，则内网结束地址不应该大于]{style="font-family:宋体"}[1.1.1.0/24]{lang="EN-US"}[网段中可用的最大]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，即]{style="font-family:宋体"}[1.1.1.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定]{style="font-family:宋体"}]{#struct_0_83269_x5501_100264960}[ACL]{lang="EN-US"}[，则所有从内网到外网的报文都可以使用该配置进行源地址转换；所有从外网到内网的报文都可以使用该配置进行目的地址转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果仅指定了]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1881653989}[ACL]{lang="EN-US"}[，没有指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（即没有配置]{style="font-family:宋体"}**[reversible]{lang="EN-US" style="color:black"}**[），对于从内网到外网的报文，只有报文符合]{style="font-family:宋体"}[ACL permit]{lang="EN-US"}[规则，才能使用该配置进行源地址转换；对于从外网主动访问内网的报文，不能使用该配置进行目的地址转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果既指定了]{style="font-family:宋体"}]{#struct_0_83269_x5501_x480402453}[ACL]{lang="EN-US"}[，又指定了]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（即配置了]{style="font-family:宋体"}**[reversible]{lang="EN-US" style="color:black"}**[），对于从内网到外网的报文，只有报文符合]{style="font-family:宋体"}[ACL permit]{lang="EN-US"}[规则，才能使用该配置进行源地址转换；对于从外网主动访问内网的报文，需要进行]{style="font-family:宋体"}[ACL]{lang="EN-US"}[反向匹配（提取报文的源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口和目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口，并根据配置转换目的地址，然后将源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口和目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口互换去匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[），只有反向匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的报文才能使用该配置进行转换，否则不予转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口下既配置了]{style="font-family:宋体"}]{#struct_0_83269_x5501_x204383305}[NAT]{lang="EN-US"}[动态地址转换，又使能了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[静态地址转换，则优先使用静态地址转换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备可支持配置多条出方向静态地址转换映射（包括]{lang="EN-US" style="font-family:宋体"}**[nat static outbound]{lang="EN-US"}**]{#struct_0_83269_x5501_x942310298}[和]{lang="EN-US" style="font-family:
宋体"}**[nat static outbound net-to-net]{lang="EN-US"}**[）。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_195975540}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1133108649}[配置内网网段]{style="font-family:宋体"}[192.168.1.0/24]{lang="EN-US"}[到外网网段]{style="font-family:宋体"}[2.2.2.0/24]{lang="EN-US"}[的出方向静态地址转换映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_2056305112}

[[\[Sysname\] nat static outbound net-to-net 192.168.1.1 192.168.1.255 global 2.2.2.0 24]{lang="EN-US"}]{#struct_0_83269_x5501_x1718759195}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_483773309}[配置出方向网段到网段的静态地址转换映射，允许内网]{style="font-family:宋体"}[192.168.1.0/24]{lang="EN-US"}[网段的用户访问外网网段]{style="font-family:宋体"}[3.3.3.0/24]{lang="EN-US"}[时，使用外网网段]{style="font-family:宋体"}[2.2.2.0/24]{lang="EN-US"}[中的地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_993883407}

[[\[Sysname\] acl advanced 3001]{lang="EN-US"}]{#struct_0_83269_x5501_x156999356}

[[\[Sysname-acl-ipv4-adv-3001\] rule permit ip destination 3.3.3.0 0.0.0.255]{lang="EN-US"}]{#struct_0_83269_x5501_1112482600}

[[\[Sysname-acl-ipv4-adv-3001\] quit]{lang="EN-US"}]{#struct_0_83269_x5501_x745923733}

[[\[Sysname\] nat static outbound net-to-net 192.168.1.1 192.168.1.255 global 2.2.2.0 24 acl 3001]{lang="EN-US"}]{#struct_0_83269_x5501_195516785}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1653738310}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat all]{lang="EN-US"}**]{#struct_0_83269_x5501_x44663389}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat static]{lang="EN-US"}**]{#struct_0_83269_x5501_x560816900}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[nat static enable]{lang="EN-US"}**]{#struct_0_83269_x5501_x1891312279}
:::

::: {#-436109135 .myid}
[]{#_Toc404786527}[]{#struct_0_83269_x5501_x433416292}[]{#_Toc363572641}

**NAT命令 \-- NAT配置命令 \-- port-block**

------------------------------------------------------------------------

[**[port-block]{lang="EN-US"}**]{#struct_0_83269_x5501_x433350756}[命令用来配置]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址组的端口块参数。]{style="font-family:宋体"}

[**[undo ]{lang="FR"}[port-block]{lang="EN-US"}**]{#struct_0_83269_x5501_x432892003}[命令用来删除]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址组的端口块参数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x432826467}

[**[port-block block-size]{lang="EN-US"}**[ *block-size* \[ **extended-block-number** *extended-block-number* \]]{lang="EN-US"}]{#struct_0_83269_x5501_x1473512993}

[**[undo port-block]{lang="EN-US"}**]{#struct_0_83269_x5501_x433023075}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x432957539}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x433154147}[地址组未配置端口块参数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x433088611}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_1957398150}[地址组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x433285219}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x433219683}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x749661658}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x433416291}

[**[block-size]{lang="EN-US"}***[ block-size]{lang="EN-US"}*]{#struct_0_83269_x5501_x433350755}[：端口块大小，即一个端口块中所包含的端口数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[。其中]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。同一]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址组内，该参数的值不能超过]{style="font-family:宋体"}**[port-range]{lang="EN-US"}**[参数的值。]{style="font-family:宋体"}

[**[extended-block-number ]{lang="EN-US"}***[extended-block-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x432892006}[：增量端口块数，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[5]{lang="EN-US"}[。当分配端口块中的端口资源耗尽（所有端口都被使用）时，如果对应的私网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址向公网发起新的连接，则无法从分配端口块中获取端口。此时，如果分配端口块的公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址组中配置了增量端口块数，则可以为对应的私网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行增量端口块分配。一个私网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址最多可同时占有]{style="font-family:宋体"}[1]{lang="EN-US"}[＋]{style="font-family:宋体"}*[extended-block-number]{lang="EN-US"}*[个端口块。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1602341965}

[[端口块动态映射方式下，配置出方向地址转换所引用的]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x432826470}[地址组中必须配置端口块参数。当某私网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址首次向公网发起连接时，从所匹配的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址组中获取一个公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，从获取的公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址中分配一个动态端口块并创建动态端口块表项（该私网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址后续向公网发起连接时，通过私网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址查找动态端口块表项），使用公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址转换，并从端口块中动态分配一个端口进行]{style="font-family:宋体"}[TCP/UDP]{lang="EN-US"}[端口转换。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x433023078}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x432957542}[配置]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址组]{style="font-family:宋体"}[2]{lang="EN-US"}[的端口块参数，端口块大小为]{style="font-family:宋体"}[256]{lang="EN-US"}[，增量端口块数为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x1852472029}

[\[Sysname\] nat address-group 2]{lang="EN-US"}

[\[Sysname-address-group-2\] port-block block-size 256 extended-block-number 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x433154150}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat address-group]{lang="EN-US"}**]{#struct_0_83269_x5501_x433088614}
:::

::: {#1893999324 .myid}
[]{#_Toc404786528}[]{#struct_0_83269_x5501_x433285222}[]{#_Toc363572642}

**NAT命令 \-- NAT配置命令 \-- port-range**

------------------------------------------------------------------------

[**[port-range]{lang="EN-US"}**]{#struct_0_83269_x5501_76913384}[命令用来配置公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的端口范围。]{style="font-family:宋体"}

[**[undo ]{lang="FR"}[port-range]{lang="EN-US"}**]{#struct_0_83269_x5501_x433219686}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x433416294}

[**[port-range]{lang="EN-US"}**[ *start-port-number end-port-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x433350758}

[**[undo port-range]{lang="EN-US"}**]{#struct_0_83269_x5501_x707730889}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x432892005}

[[公网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_83269_x5501_x432826469}[地址的端口范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x433023077}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x328116665}[地址组视图]{style="font-family:宋体"}[/NAT]{lang="EN-US"}[端口块组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x432957541}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x433154149}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_879366048}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x433088613}

[*[start-port-number end-port-number]{lang="EN-US"}*]{#struct_0_83269_x5501_x433285221}[：]{style="font-family:宋体"}[公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址端口的起始端口号和]{style="font-family:宋体"}[结束端口号]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[end-port-number]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[start-port-number]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x433219685}

[[在]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x749530586}[地址组（或]{style="font-family:宋体"}[NAT]{lang="EN-US"}[端口块组）视图下配置端口范围后，该]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址组（或]{style="font-family:宋体"}[NAT]{lang="EN-US"}[端口块组）内的所有公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址可用于地址转换的端口都必须位于所指定的端口范围之内。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x433416293}[端口块组内配置端口范围时，端口范围不能小于端口块大小。在]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址组内配置端口范围时，如果地址组配置了端口块参数，则端口范围也不能小于端口块大小。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x433350757}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1133191939}[配置]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址组]{style="font-family:宋体"}[1]{lang="EN-US"}[的公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址端口范围为]{style="font-family:宋体"}[1024]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_x1006919584}

[\[Sysname\] nat address-group 1]{lang="EN-US"}

[\[Sysname-address-group-1\] port-range 1024 65535]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1133257475}[配置]{style="font-family:宋体"}[NAT]{lang="EN-US"}[端口块组]{style="font-family:宋体"}[1]{lang="EN-US"}[的公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址端口范围为]{style="font-family:宋体"}[30001]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_83269_x5501_1133060867}

[\[Sysname\] nat port-block-group 1]{lang="EN-US"}

[\[Sysname-port-block-group-1\] port-range 30001 65535]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1133126403}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nat address-group]{lang="EN-US"}**]{#struct_0_83269_x5501_1132929795}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[nat port-block-group]{lang="EN-US"}**]{#struct_0_83269_x5501_121979962}
:::

::: {#4115366 .myid}
[]{#_Toc404786529}[]{#struct_0_83269_x5501_500354484}

**NAT命令 \-- NAT配置命令 \-- reset nat session**

------------------------------------------------------------------------

[**[reset nat session]{lang="EN-US"}**]{#struct_0_83269_x5501_1290790331}[命令用来删除]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_812079183}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_83269_x5501_139379198}

[**[reset nat ]{lang="SV"}**]{#struct_0_83269_x5501_195451249}[]{#_Hlt18739791}**[session]{lang="SV"}**

[[分布式设备]{style="font-family:宋体"}]{#struct_0_83269_x5501_617954113}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[reset nat session ]{lang="SV"}**]{#struct_0_83269_x5501_1102815775}[\[ **slot** ]{lang="SV"}*[slot-number]{lang="EN-US"}*[ \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_83269_x5501_x2072745490}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[reset nat session ]{lang="SV"}**]{#struct_0_83269_x5501_x939183500}[\[ **chassis**]{lang="SV"}[ *chassis-number* **slot** ]{lang="SV"}*[slot-number]{lang="EN-US"}*[ \[ **cpu** *cpu-number* \] \] ]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1704831317}

[[用户视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_480551995}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_491989120}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_901347871}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_83269_x5501_195385713}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1557656525}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x1008309974}[：删除指定单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果不指定该参数，则表示删除所有单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－独立运行模式]{style="font-family:宋体"}[）。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x1771320142}[：删除指定成员设备上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[如果不指定该参数，则表示删除所有成员设备上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_83269_x5501_x862093679}[：删除]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[如果不指定该参数，则表示删除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_83269_x5501_x355439063}[ *chassis-number* **slot** ]{lang="SV"}*[slot-number]{lang="EN-US"}*[：删除指定成员设备上指定单板的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果不指定该参数，则表示删除所有成员设备的所有单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_83269_x5501_x1265378206}[ *chassis-number* **slot** ]{lang="SV"}*[slot-number]{lang="EN-US"}*[：删除]{style="font-family:宋体"}[指定单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话，]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[如果不指定该参数，则表示删除所有单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_83269_x5501_1132733187}[：]{style="font-family:宋体"}[删除]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1222368564}

[[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x1835021760}[会话被删除之后，与其相关的]{style="font-family:宋体"}[NAT EIM]{lang="EN-US"}[表和]{style="font-family:宋体"}[NO-PAT]{lang="EN-US"}[表也会同时删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1245639383}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_195320177}[删除]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> reset nat session]{lang="EN-US"}]{#struct_0_83269_x5501_1144238265}

[[\#]{lang="EN-US"}]{#struct_0_83269_x5501_x812259086}[ ]{lang="EN-US" style="font-family:宋体"}[删除]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话。（分布式设备]{style="font-family:宋体"}[－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> reset nat session slot 2]{lang="EN-US"}]{#struct_0_83269_x5501_x852819408}

[[\#]{lang="EN-US"}]{#struct_0_83269_x5501_2121605962}[ ]{lang="EN-US" style="font-family:宋体"}[删除]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话。（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> reset nat session slot 2]{lang="EN-US"}]{#struct_0_83269_x5501_576571858}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_1648598670}[删除]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话。（分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> reset nat session chassis 1 slot 2]{lang="EN-US"}]{#struct_0_83269_x5501_x944904185}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x275497137}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display nat session]{lang="EN-US"}**]{#struct_0_83269_x5501_195254641}
:::

::: {#1055702076 .myid}
[]{#_Toc404786530}[]{#struct_0_83269_x5501_1611800981}[]{#_Toc380589025}[]{#_Toc377110450}[]{#_Toc377053893}

**NAT命令 \-- NAT配置命令 \-- reset nat static-load-balance**

------------------------------------------------------------------------

[**[reset nat static-load-balance]{lang="EN-US"}**]{#struct_0_83269_x5501_1541211172}[命令用来重新在多个]{style="font-family:
宋体"}[CPU]{lang="EN-US"}[上进行静态]{style="font-family:宋体"}[NAT]{lang="EN-US"}[（包括静态地址转换、]{style="font-family:宋体"}[NAT server]{lang="EN-US"}[和静态]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[）的负载分担。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x437339979}

[**[reset nat static-load-balance]{lang="EN-US"}**]{#struct_0_83269_x5501_x1409674634}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x73078581}

[[用户视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_1858444205}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x624078303}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x344514155}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_x920699192}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_606149396}

[[执行本命令后，设备会综合考虑当前的所有静态]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_x603024486}[配置（包括静态地址转换、]{style="font-family:宋体"}[NAT server]{lang="EN-US"}[和静态]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[的配置），重新将静态]{style="font-family:宋体"}[NAT]{lang="EN-US"}[的处理分担到不同的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上，以均衡各个]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的负载。]{style="font-family:宋体"}

[[需要注意的是，执行本命令后，会造成流量的暂时中断，请谨慎使用本命令。]{style="font-family:宋体"}]{#struct_0_83269_x5501_x1122647327}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x891345850}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x1641970790}[配置重新在多个]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上进行静态]{style="font-family:宋体"}[NAT]{lang="EN-US"}[的负载分担。]{style="font-family:宋体"}

[[\<Sysname\> reset nat static-load-balance]{lang="EN-US"}]{#struct_0_83269_x5501_x1654155926}
:::

::: {#-335866938 .myid}
[]{#_Toc404786531}[]{#struct_0_83269_x5501_268219968}[]{#_Toc380589026}

**NAT命令 \-- NAT配置命令 \-- reset nat dynamic-load-balance**

------------------------------------------------------------------------

[**[reset nat dynamic-load-balance]{lang="EN-US"}**]{#struct_0_83269_x5501_x474596774}[命令用来重新在多个]{style="font-family:
宋体"}[CPU]{lang="EN-US"}[上进行动态]{style="font-family:宋体"}[NAT]{lang="EN-US"}[（包括动态地址转换和动态]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[）的负载分担。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_83269_x5501_2056961541}

[**[reset nat dynamic-load-balance]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ ** a[ddress-group]{style="color:black"}**]{lang="EN-US"}]{#struct_0_83269_x5501_1358602920}**[ ]{lang="EN-US" style="color:black"}***[address-group-number ]{lang="EN-US" style="color:black"}*[\]]{lang="EN-US" style="color:blue"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x346997865}

[[用户视图]{style="font-family:宋体"}]{#struct_0_83269_x5501_412265722}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1164684042}

[[network-admin]{lang="EN-US"}]{#struct_0_83269_x5501_1241523698}

[[mdc-admin]{lang="EN-US"}]{#struct_0_83269_x5501_718720673}

[[【参数】]{style="font-family:黑体"}]{#struct_0_83269_x5501_1060325089}

[**[address-group ]{lang="EN-US" style="color:black"}***[address-group-number]{lang="EN-US" style="color:black"}*]{#struct_0_83269_x5501_x637822226}[：重新对指定地址池的动态]{style="font-family:
宋体;color:black"}[NAT]{lang="EN-US" style="color:black"}[进行负载分担。]{style="font-family:宋体;color:black"}*[address-group-number]{lang="EN-US" style="color:black"}*[为地址池的编号，]{style="font-family:
宋体;color:black"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[如果没有指定本参数，则重新对所有动态]{style="font-family:宋体;color:black"}[NAT]{lang="EN-US" style="color:black"}[进行负载分担。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_83269_x5501_x1875260338}

[[执行本命令后，设备会综合考虑当前所有的动态]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_83269_x5501_214020900}[配置（包括动态地址转换和动态]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[的配置）或指定地址池的动态]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置，重新将动态]{style="font-family:宋体"}[NAT]{lang="EN-US"}[的处理分担到不同的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上，以均衡各个]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的负载。]{style="font-family:宋体"}

[[需要注意的是，执行本命令后，会造成流量的暂时中断，请谨慎使用本命令。]{style="font-family:宋体"}]{#struct_0_83269_x5501_1762087046}

[[【举例】]{style="font-family:黑体"}]{#struct_0_83269_x5501_176849932}

[[\# ]{lang="EN-US"}]{#struct_0_83269_x5501_x582999284}[配置重新在多个]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上进行动态]{style="font-family:宋体"}[NAT]{lang="EN-US"}[的负载分担。]{style="font-family:宋体"}

[[\<Sysname\> reset nat dynamic-load-balance]{lang="EN-US"}]{#struct_0_83269_x5501_219485465}

[ ]{lang="EN-US"}
:::
