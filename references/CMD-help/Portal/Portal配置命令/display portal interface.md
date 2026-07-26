::: {#1903720998 .myid}
[]{#_Toc404792725}[]{#struct_0_17060_20103_1125776291}[]{#_Toc330201705}[]{#_Toc320893869}

**Portal \-- Portal配置命令 \-- display portal interface**

------------------------------------------------------------------------

[**[display portal interface]{lang="EN-US"}**]{#struct_0_17060_20103_x509195710}[命令用来显示指定接口上的]{style="font-family:
宋体"}[Portal]{lang="EN-US"}[配置信息和]{style="font-family:
宋体"}[Portal]{lang="EN-US"}[运行状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x838322204}

[**[display portal interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_17060_20103_x1145517208}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1170707798}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17060_20103_260095930}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x219533422}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x1852738389}

[[network-operator]{lang="EN-US"}]{#struct_0_17060_20103_875841795}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_x1397289485}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17060_20103_1126235043}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_166843989}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_17060_20103_x808836333}[：表示接口类型和接口编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_177527581}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x1357802726}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1206445635}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[配置信息和]{style="font-family:宋体"}[Portal]{lang="EN-US"}[运行状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display portal interface gigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_17060_20103_1126169507}

[ Portal information of GigabitEthernet1/0/1]{lang="EN-US"}

[     Nas id profile: aaa]{lang="EN-US"}

[     VSRP instance : instance1]{lang="EN-US"}

[     VSRP state    : Master]{lang="EN-US"}

[     Authorization : Strict checking]{lang="EN-US"}

[     ACL           : Enabled]{lang="EN-US"}

[     User profile  : Disabled]{lang="EN-US"}

[ IPv4:]{lang="EN-US"}

[     Portal status: Enabled]{lang="EN-US"}

[     Portal VSRP status: M_Delay]{lang="EN-US"}

[     Authentication type: Layer3]{lang="EN-US"}

[     Portal Web server: wbs]{lang="EN-US"}

[     Authentication domain: my-domain]{lang="EN-US"}

[     Pre-auth domain: abc]{lang="EN-US"}

[     Pre-auth IP pool: ab]{lang="EN-US"}

[     ]{lang="EN-US"}[BAS-IP: Not configured]{lang="EN-US"}

[     ]{lang="EN-US"}[User detection: Type: ICMP  Interval: 300s  Attempts: 5  Idle time: 180s]{lang="EN-US"}

[     ]{lang="EN-US"}[Action for sever detection:]{lang="EN-US"}

[         Server type    Server name                        Action]{lang="EN-US"}

[         Web server     wbs                                fail-permit]{lang="EN-US"}

[         Portal server  pts                                fail-permit]{lang="EN-US"}

[     Layer3 source network:]{lang="EN-US"}

[         IP address               Mask]{lang="EN-US"}

[         1.1.1.1                  255.255.0.0]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Destination ]{lang="EN-US"}[authentication subnet:]{lang="EN-US"}

[         IP address               Mask]{lang="EN-US"}

[         2.2.2.2                  255.255.255.0]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPv6:]{lang="EN-US"}

[     Portal status: enabled]{lang="EN-US"}

[     Portal VSRP status: M_Alone]{lang="EN-US"}

[     Authentication type: layer3]{lang="EN-US"}

[     Portal Web server: wbsv6]{lang="EN-US"}

[     Authentication domain: my-domain]{lang="EN-US"}

[     Pre-auth domain: abc]{lang="EN-US"}

[     Pre-auth IP pool: Not configured]{lang="EN-US"}

[     BAS-IPv6: Not configured]{lang="EN-US"}

[     ]{lang="EN-US"}[User detection: Type: ICMPv6  Interval: 300s   Attempts: 5   Idle time: 180s]{lang="EN-US"}

[     ]{lang="EN-US"}[Action for sever detection:]{lang="EN-US"}

[         Server type    Server name                        Action]{lang="EN-US"}

[         Web server     wbsv6                              fail-permit]{lang="EN-US"}

[         Portal server  ptsv6                              fail-permit]{lang="EN-US"}

[     Layer3 source network:]{lang="EN-US"}

[         IP address                                        Prefix length]{lang="EN-US"}

[         11::5                                             64]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Destination authentication subnet:]{lang="EN-US"}

[         IP address                                        Prefix length]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_1655393588}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1125710752}[显示接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[配置信息]{style="font-family:宋体"}[和]{style="font-family:宋体"}[Portal]{lang="EN-US"}[运行状态信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display portal interface vlan-interface 2]{lang="EN-US"}]{#struct_0_17060_20103_1125645216}

[ Portal information of Vlan-interface2]{lang="EN-US"}

[     Nas id profile: aaa]{lang="EN-US"}

[     VSRP instance : instance1]{lang="EN-US"}

[     VSRP status   : Master]{lang="EN-US"}

[     Authorization : Strict checking ]{lang="EN-US"}

[     ACL           : Enabled]{lang="EN-US"}

[     User profile  : Disabled]{lang="EN-US"}

[ IPv4:]{lang="EN-US"}

[     Portal status: Enabled]{lang="EN-US"}

[     Portal VSRP status: M_Delay]{lang="EN-US"}

[     Authentication type: Direct]{lang="EN-US"}

[     Portal Web server  : wbs]{lang="EN-US"}

[     Authentication domain: my-domain]{lang="EN-US"}

[     Pre-auth domain: abc]{lang="EN-US"}

[     Pre-auth IP pool: Not configured]{lang="EN-US"}

[     ]{lang="EN-US"}[BAS-IP: Not configured]{lang="EN-US"}

[     User detection: Type: ICMP  Interval: 300s  ]{lang="EN-US"}[Attempts: 5   Idle time: 180s]{lang="EN-US"}

[     Action for server detection:]{lang="EN-US"}

[         Server type    Server name                        Action]{lang="EN-US"}

[         Web server     wbs                                fail-permit]{lang="EN-US"}

[         Portal server  pts                                fail-permit]{lang="EN-US"}

[     Layer3 source network:]{lang="EN-US"}

[         IP address               Mask]{lang="EN-US"}

[         1.1.1.1                  255.255.0.0]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Destination ]{lang="EN-US"}[authentication subnet:]{lang="EN-US"}

[         IP address               Mask]{lang="EN-US"}

[         2.2.2.2                  255.255.255.0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ IPv6:]{lang="EN-US"}

[     portal status: Enabled]{lang="EN-US"}

[     Portal VSRP status: M_Alone]{lang="EN-US"}

[     Authentication type: Direct]{lang="EN-US"}

[     Portal Web server: wbsv6]{lang="EN-US"}

[     Authentication domain: my-domain]{lang="EN-US"}

[     Pre-auth domain: abc]{lang="EN-US"}

[     Pre-auth IP pool: Not configured]{lang="EN-US"}

[     BAS-IPv6:Not configured]{lang="EN-US"}

[     User detection: Type: ICMPv6  Interval: 300s  ]{lang="EN-US"}[Attempts: 5   Idle time: 180s]{lang="EN-US"}

[     ]{lang="EN-US"}[Action for server detection:]{lang="EN-US"}

[         Server type    Server name                        Action]{lang="EN-US"}

[         Web server     wbsv6                              fail-permit]{lang="EN-US"}

[         Portal server  ptsv6                              fail-permit]{lang="EN-US"}

[     Layer3 source network:]{lang="EN-US"}

[         IP address                                        Prefix length]{lang="EN-US"}

[         11::5                                             64]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Destination authentication subnet:]{lang="EN-US"}

[         IP address                                        Prefix length]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display portal interface]{lang="EN-US"}]{#struct_0_17060_20103_1058592204}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2008512765}[[字段]{style="font-family:黑体"}]{#struct_0_17060_20103_30554936}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17060_20103_x1634158779}

[[Portal information of interface]{lang="EN-US"}]{#struct_0_17060_20103_x1637769356}

[[接口上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1125579680}[信息]{style="font-family:宋体"}

[[NAS-ID profile]{lang="EN-US"}]{#struct_0_17060_20103_x1511549093}

[[接口上引用的]{style="font-family:宋体"}[NAS-ID profile]{lang="EN-US"}]{#struct_0_17060_20103_1670131600}

[[VSRP instance]{lang="EN-US"}]{#struct_0_17060_20103_983027814}

[[接口上引用的]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_17060_20103_x636102719}[实例名称]{style="font-family:宋体"}

[[VSRP state]{lang="EN-US"}]{#struct_0_17060_20103_982962278}

[[接口的]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_17060_20103_293747316}[状态，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_17060_20103_x1558872649}[：表示在该]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例中，本设备为主用设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_17060_20103_982634598}[：表示在该]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例中，本设备为备用设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_17060_20103_1678111810}[：表示在该]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例中，本设备不运行（在下面两种情况下设备会处于]{style="font-family:宋体"}[Down]{lang="EN-US"}[状态：一是当]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组处于]{style="font-family:宋体"}[init]{lang="EN-US"}[状态时，互相备份的两台设备在对应]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例中都处于无法运行状态；二是本端]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例不存在或者配置不完整）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_17060_20103_x316817333}[：表示接口上未引用]{lang="EN-US" style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例]{lang="EN-US" style="font-family:宋体"}

[[Authorization]{lang="EN-US"}]{#struct_0_17060_20103_982569062}

[[服务器下发给]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x2138091196}[用户的授权信息类型，包括]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[User profile]{lang="EN-US"}

[[Strict checking]{lang="EN-US"}]{#struct_0_17060_20103_982765670}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_898197520}[授权信息的严格检查模式是否开启]{style="font-family:宋体"}

[[IPv4]{lang="EN-US"}]{#struct_0_17060_20103_208489656}

[[IPv4 Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1797762267}[的相关信息]{style="font-family:宋体"}

[[IPv6]{lang="EN-US"}]{#struct_0_17060_20103_x629925048}

[[IPv6 Portal]{lang="EN-US"}]{#struct_0_17060_20103_1337566183}[的相关信息]{style="font-family:宋体"}

[[Portal status]{lang="EN-US"}]{#struct_0_17060_20103_x1786172598}

[[接口上]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x2141834316}[认证的运行状态，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_17060_20103_1125514144}[：]{lang="EN-US" style="font-family:宋体"}[Portal]{lang="EN-US"}[认证未使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_17060_20103_x93364019}[：]{lang="EN-US" style="font-family:宋体"}[Portal]{lang="EN-US"}[认证已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Authorized]{lang="EN-US"}]{#struct_0_17060_20103_x530521380}[：]{lang="EN-US" style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器或者]{lang="EN-US" style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器不可达，端口自动开放]{lang="EN-US" style="font-family:宋体"}

[[Portal VSRP status]{lang="EN-US"}]{#struct_0_17060_20103_982700134}

[[接口的]{style="font-family:宋体"}[Portal VSRP]{lang="EN-US"}]{#struct_0_17060_20103_983421030}[状态，包括如下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M_Initial]{lang="EN-US"}]{#struct_0_17060_20103_x826133787}[：主用设备的初始化状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M_Delay]{lang="EN-US"}]{#struct_0_17060_20103_983355494}[：主用设备的延迟状态（主用设备延迟一段时间后切换为主状态）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M_Alone]{lang="EN-US"}]{#struct_0_17060_20103_982896741}[：主用设备的单机状态（备份数据链路断开等原因，导致双机通信失败）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M_Hello]{lang="EN-US"}]{#struct_0_17060_20103_1860689463}[：主用设备处于和备用设备进行握手的状态（协商]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[状态和接口的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[使能状态）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M_Collect]{lang="EN-US"}]{#struct_0_17060_20103_728113991}[：主用设备处于等待备用设备发送]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户信息的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M_Sync]{lang="EN-US"}]{#struct_0_17060_20103_982831205}[：主用设备处于向备用设备发送]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户信息的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M_Synced]{lang="EN-US"}]{#struct_0_17060_20103_x2057749698}[：主用设备已经完成向备用设备备份]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B_Initial]{lang="EN-US"}]{#struct_0_17060_20103_983027813}[：备用设备的初始化状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B_Alone]{lang="EN-US"}]{#struct_0_17060_20103_x636102726}[：备用设备的单机状态（备份数据链路断开等原因，导致双机通信失败）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B_Hello]{lang="EN-US"}]{#struct_0_17060_20103_982962277}[：备用设备处于和主用设备进行握手的状态（协商]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[状态和接口的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[使能状态）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B_Report]{lang="EN-US"}]{#struct_0_17060_20103_293747317}[：备用设备处于向主用设备发送]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户信息的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B_Sync]{lang="EN-US"}]{#struct_0_17060_20103_982634597}[：备用设备处于接收主用设备发送]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户信息的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B_Synced]{lang="EN-US"}]{#struct_0_17060_20103_1678111801}[：备用设备已经完成]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户信息的备份]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_17060_20103_982569061}[：未运行]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[接口未使能]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_982765669}[或者未引用]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例时不显示该字段]{style="font-family:宋体"}

[[Authentication type]{lang="EN-US"}]{#struct_0_17060_20103_x787321376}

[[接口上配置的认证方式，包括以下取值：]{style="font-family:宋体"}]{#struct_0_17060_20103_x1333151428}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direct]{lang="EN-US"}]{#struct_0_17060_20103_1125972896}[：直接方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Redhcp]{lang="EN-US"}]{#struct_0_17060_20103_x95609864}[：二次地址方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Layer3]{lang="EN-US"}]{#struct_0_17060_20103_x1490577799}[：可]{lang="EN-US" style="font-family:宋体"}[跨三层路由方式]{style="font-family:宋体"}

[[Portal Web server]{lang="EN-US"}]{#struct_0_17060_20103_3068772}

[[接口上配置的]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_2005282054}[服务器的名称]{style="font-family:宋体"}

[[Authentication domain]{lang="EN-US"}]{#struct_0_17060_20103_x405721618}

[[接口上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1125907360}[强制认证域]{style="font-family:宋体"}

[[Pre-auth domain]{lang="EN-US"}]{#struct_0_17060_20103_1884554126}

[[接口上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_318470185}[认证前域，即]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证前用户使用的认证域，未指定则显示]{style="font-family:宋体"}[Not configured]{lang="EN-US"}

[[Pre-auth ip-pool]{lang="EN-US"}]{#struct_0_17060_20103_982700133}

[[为认证前的]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1266075140}[用户指定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址池名称]{style="font-family:宋体"}

[[BAS-IP]{lang="EN-US"}]{#struct_0_17060_20103_x108216800}

[[发送给]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x962995722}[认证服务器的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文的]{style="font-family:宋体"}[BAS-IP]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[BAS-IPv6]{lang="EN-US"}]{#struct_0_17060_20103_1896310958}

[[发送给]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1132746957}[认证服务器的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文的]{style="font-family:宋体"}[BAS-IPv6]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[User detection]{lang="EN-US"}]{#struct_0_17060_20103_1125841824}

[[接口上配置的用户在线状态探测配置，包括探测的方法（]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_17060_20103_1472636789}[、]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[、]{style="font-family:宋体"}[ND]{lang="EN-US"}[、]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[），探测周期和探测尝试次数，用户闲置的时间]{style="font-family:宋体"}

[[Action for server detection]{lang="EN-US"}]{#struct_0_17060_20103_1037824111}

[[服务器可达性探测功能对应的端口控制配置：]{style="font-family:宋体"}]{#struct_0_17060_20103_1689862566}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Server type]{lang="EN-US"}]{#struct_0_17060_20103_1125776288}[：服务器类型，包括]{lang="EN-US" style="font-family:宋体"}[Portal server]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[Web server]{lang="EN-US"}[，分别表示]{lang="EN-US" style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器和]{lang="EN-US" style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Server name]{lang="EN-US"}]{#struct_0_17060_20103_x508605887}[：服务器名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Action]{lang="EN-US"}]{#struct_0_17060_20103_x1645725518}[：对应的接口根据服务器探测结果所采取的动作，为不需要认证（]{style="font-family:宋体"}[fail-permit]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Layer3 source subnet]{lang="EN-US"}]{#struct_0_17060_20103_908473785}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1126235040}[源认证网段信息]{style="font-family:宋体"}

[[Destination authentication subnet]{lang="EN-US"}]{#struct_0_17060_20103_167040597}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x113798574}[目的认证网段认证信息]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_17060_20103_1126169504}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1655196980}[认证网段的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Mask]{lang="EN-US"}]{#struct_0_17060_20103_x1993447097}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x529723438}[认证网段的子网掩码]{style="font-family:宋体"}

[[Prefix length]{lang="EN-US"}]{#struct_0_17060_20103_1125710753}

[[Portal IPv6]{lang="EN-US"}]{#struct_0_17060_20103_x915917948}[认证网段的地址前缀长度]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1227179929}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal domain]{lang="EN-US"}**]{#struct_0_17060_20103_x1409135310}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal enable]{lang="EN-US"}**]{#struct_0_17060_20103_1551686440}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal free-all except destination]{lang="EN-US"}**]{#struct_0_17060_20103_500918568}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal ipv6 free-all except destination]{lang="EN-US"}**]{#struct_0_17060_20103_1996708310}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal ipv6 layer3 source]{lang="EN-US"}**]{#struct_0_17060_20103_x1823427723}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal layer3 source]{lang="EN-US"}**]{#struct_0_17060_20103_1125645217}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal web-server]{lang="EN-US"}**]{#struct_0_17060_20103_1058657740}

::: {#-1618259684 .myid}
[]{#_Toc404792726}[]{#struct_0_17060_20103_853931150}[]{#_Toc330201704}[]{#_Toc320893868}[]{#_Toc349831006}[]{#_Toc349831007}

**Portal \-- Portal配置命令 \-- display portal packet statistics**

------------------------------------------------------------------------

[**[display portal packet statistics]{lang="EN-US"}**]{#struct_0_17060_20103_623819369}[命令用来显示]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的报文统计信息，包括设备接收到]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器发送的报文以及设备发送给该]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的报文的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x996512809}

[**[display portal packet statistics]{lang="EN-US"}**[ \[ **server** *server-name* \]]{lang="EN-US"}]{#struct_0_17060_20103_1712078032}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_727427583}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17060_20103_x1633584879}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_288733889}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_1125579681}

[[network-operator]{lang="EN-US"}]{#struct_0_17060_20103_208424120}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_584113994}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17060_20103_x612545502}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_1777545294}

[**[server]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17060_20103_66884155}*[server-name]{lang="EN-US"}*[：]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_1033350611}

[[若不指定参数]{style="font-family:宋体"}**[server]{lang="EN-US"}**]{#struct_0_17060_20103_1125514145}[，则依次显示所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x93429555}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x635462939}[显示名字为]{style="font-family:宋体"}[pts]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display portal packet statistics server pts]{lang="EN-US"}]{#struct_0_17060_20103_1125972897}

[ Portal server :  pts]{lang="EN-US"}

[ Invalid packets: 0]{lang="EN-US"}

[ Pkt-Type                            Total    Drops    Errors]{lang="EN-US"}

[ REQ_CHALLENGE                       3        0        0]{lang="EN-US"}

[ ACK_CHALLENGE                       3        0        0]{lang="EN-US"}

[ REQ_AUTH                            3        0        0]{lang="EN-US"}

[ ACK_AUTH                            3        0        0]{lang="EN-US"}

[ REQ_LOGOUT                          1        0        0]{lang="EN-US"}

[ ACK_LOGOUT                          1        0        0]{lang="EN-US"}

[ AFF_ACK_AUTH                        3        0        0]{lang="EN-US"}

[ NTF_LOGOUT                          1        0        0]{lang="EN-US"}

[ REQ_INFO                            6        0        0]{lang="EN-US"}

[ ACK_INFO                            6        0        0]{lang="EN-US"}

[ NTF_USERDISCOVER                    0        0        0]{lang="EN-US"}

[ NTF_USERIPCHANGE                    0        0        0]{lang="EN-US"}

[ AFF_NTF_USERIPCHAN                  0        0        0]{lang="EN-US"}

[ ACK_NTF_LOGOUT                      1        0        0]{lang="EN-US"}

[ NTF_USER_HEARTBEAT                  2        0        0]{lang="EN-US"}

[ ACK_NTF_USER_HEARTBEAT              0        0        0]{lang="EN-US"}

[ NTF_CHALLENGE                       0        0        0]{lang="EN-US"}

[ NTF_USER_NOTIFY                     0        0        0]{lang="EN-US"}

[ AFF_NTF_USER_NOTIFY                 0        0        0]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display portal server statistics]{lang="EN-US"}]{#struct_0_17060_20103_x95675400}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2000479229}[[字段]{style="font-family:黑体"}]{#struct_0_17060_20103_x1050402752}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17060_20103_1504520465}

[[Portal server]{lang="EN-US"}]{#struct_0_17060_20103_264184644}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1125907361}[认证服务器名称]{style="font-family:宋体"}

[[Invalid packets]{lang="EN-US"}]{#struct_0_17060_20103_x108151264}

[[无效报文的数目]{style="font-family:宋体"}]{#struct_0_17060_20103_x1317509772}

[[Pkt-Type]{lang="EN-US"}]{#struct_0_17060_20103_1428332348}

[[报文的名称]{style="font-family:宋体"}]{#struct_0_17060_20103_x893510347}

[[Total]{lang="EN-US"}]{#struct_0_17060_20103_2145265162}

[[报文的总数]{style="font-family:宋体"}]{#struct_0_17060_20103_x1939875524}

[[Drops]{lang="EN-US"}]{#struct_0_17060_20103_1125841825}

[[丢弃报文数]{style="font-family:宋体"}]{#struct_0_17060_20103_1472702325}

[[Errors]{lang="EN-US"}]{#struct_0_17060_20103_x517661218}

[[错误报文数]{style="font-family:宋体"}]{#struct_0_17060_20103_x1248174524}

[[REQ_CHALLENGE]{lang="EN-US"}]{#struct_0_17060_20103_x490538463}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1125776289}[认证服务器向接入设备发送的]{style="font-family:宋体"}[challenge]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[ACK_CHALLENGE]{lang="EN-US"}]{#struct_0_17060_20103_x508671423}

[[接入设备对]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1963628996}[认证服务器]{style="font-family:宋体"}[challenge]{lang="EN-US"}[请求的响应报文]{style="font-family:宋体"}

[[REQ_AUTH]{lang="EN-US"}]{#struct_0_17060_20103_1725014253}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x2096012936}[认证服务器向接入设备发送的请求认证报文]{style="font-family:宋体"}

[[ACK_AUTH]{lang="EN-US"}]{#struct_0_17060_20103_2038305269}

[[接入设备对]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1126235041}[认证服务器认证请求的响应报文]{style="font-family:宋体"}

[[REQ_LOGOUT]{lang="EN-US"}]{#struct_0_17060_20103_166975061}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x9874583}[认证服务器向接入设备发送的下线请求报文]{style="font-family:宋体"}

[[ACK_LOGOUT]{lang="EN-US"}]{#struct_0_17060_20103_124961109}

[[接入设备对]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x634472394}[认证服务器下线请求的响应报文]{style="font-family:宋体"}

[[AFF_ACK_AUTH]{lang="EN-US"}]{#struct_0_17060_20103_1126169505}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1655262516}[认证服务器收到认证成功响应报文后向接入设备发送的确认报文]{style="font-family:宋体"}

[[NTF_LOGOUT]{lang="EN-US"}]{#struct_0_17060_20103_x1638450147}

[[接入设备发送给]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_420394684}[认证服务器，用户被强制下线的通知报文]{style="font-family:宋体"}

[[REQ_INFO]{lang="EN-US"}]{#struct_0_17060_20103_x1603172599}

[[信息询问报文]{style="font-family:宋体"}]{#struct_0_17060_20103_1221373705}

[[ACK_INFO]{lang="EN-US"}]{#struct_0_17060_20103_978162132}

[[信息询问的响应报文]{style="font-family:宋体"}]{#struct_0_17060_20103_x1375073936}

[[NTF_USERDISCOVER]{lang="EN-US"}]{#struct_0_17060_20103_x1603238135}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1343925045}[认证服务器向接入设备发送的发现新用户要求上线的通知报文]{style="font-family:宋体"}

[[NTF_USERIPCHANGE]{lang="EN-US"}]{#struct_0_17060_20103_x12065566}

[[接入设备向]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1795251253}[认证服务器发送的通知更改某个用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的通知报文]{style="font-family:宋体"}

[[AFF_NTF_USERIPCHAN]{lang="EN-US"}]{#struct_0_17060_20103_x407915505}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1603303671}[认证服务器通知接入设备对用户表项的]{style="font-family:宋体"}[IP]{lang="EN-US"}[切换已成功报文]{style="font-family:宋体"}

[[ACK_NTF_LOGOUT]{lang="EN-US"}]{#struct_0_17060_20103_x863349313}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x200281945}[认证服务器对强制下线通知的响应报文]{style="font-family:宋体"}

[[NTF_USER_HEARTBEAT ]{lang="EN-US"}]{#struct_0_17060_20103_x1462082217}

[[接入设备收到的从]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1603369207}[认证服务器发送的用户同步报文]{style="font-family:宋体"}

[[ACK_NTF_USER_HEARTBEAT ]{lang="EN-US"}]{#struct_0_17060_20103_x1733821601}

[[接入设备向]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_432101254}[认证服务器回应的用户同步响应报文]{style="font-family:宋体"}

[[NTF_HEARTBEAT]{lang="EN-US"}]{#struct_0_17060_20103_x1602910455}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_527145721}[认证服务器周期性向接入设备发送的服务器心跳报文]{style="font-family:宋体"}

[[NTF_CHALLENGE]{lang="EN-US"}]{#struct_0_17060_20103_1685023629}

[[接入设备向]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1323041496}[认证服务器发送的]{style="font-family:宋体"}[challenge]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[NTF_USER_NOTIFY]{lang="EN-US"}]{#struct_0_17060_20103_x1602975991}

[[接入设备向]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_982780386}[认证服务器发送的用户消息通知报文]{style="font-family:宋体"}

[[AFF_NTF_USER_NOTIFY]{lang="EN-US"}]{#struct_0_17060_20103_x1910722489}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_549315771}[认证服务器向接入设备发送的对]{style="font-family:宋体"}[NTF_USER_NOTIFY]{lang="EN-US"}[的确认报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1603041527}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_x887375352}**[packet ]{lang="EN-US"}[statistics]{lang="EN-US"}**

::: {#473556071 .myid}
[]{#_Toc404792727}[]{#struct_0_17060_20103_2125433749}[]{#_Toc330201701}

**Portal \-- Portal配置命令 \-- display portal rule**

------------------------------------------------------------------------

[**[display portal rule]{lang="EN-US"}**]{#struct_0_17060_20103_x1315535440}[命令用来显示指定接口上用于报文匹配的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[过滤规则信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1856379772}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17060_20103_x1018701536}

[**[display portal rule]{lang="EN-US"}**[ { **all** \| **dynamic** \| **static** } **interface** *interface-type interface-number* ]{lang="EN-US"}]{#struct_0_17060_20103_x1603107063}

[[分布式设备]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_17060_20103_x1494586237}[独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display portal rule ]{lang="EN-US"}**[{ **all** \| **dynamic** \| **static** } **interface** *interface-type interface-number* \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_17060_20103_1427963136}

[[分布式设备]{style="font-family:宋体"}[-IRF]{lang="EN-US"}]{#struct_0_17060_20103_x950961341}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display portal rule ]{lang="EN-US"}**[{ **all** \| **dynamic** \| **static** } **interface** *interface-type interface-number* \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_17060_20103_x951026877}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_2031849609}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17060_20103_x1502988337}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_2036210622}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x1870329770}

[[network-operator]{lang="EN-US"}]{#struct_0_17060_20103_x1602648311}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_x493062815}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17060_20103_1391410186}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_1398822961}

[**[all]{lang="EN-US"}**]{#struct_0_17060_20103_x1527353739}[：显示所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则信息，包括动态]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则和静态]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_17060_20103_x727583790}[：显示动态]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则信息，即用户通过]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证后设备上产生的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则，这类规则定义了允许指定源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的报文通过接口。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_17060_20103_544890640}[：显示静态]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则信息，即使能]{style="font-family:宋体"}[Portal]{lang="EN-US"}[后产生的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则，这类规则定义了在]{style="font-family:宋体"}[Portal]{lang="EN-US"}[功能开启后对接口上收到的报文的过滤动作。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_17060_20103_44594729}[：显示指定接口的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_17060_20103_x1602713847}[：显示指定单板上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若不指定该参数，则表示所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_17060_20103_1642919581}[：显示指定成员设备上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。若不指定该参数，则表示所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_17060_20103_x1108395638}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若不指定该参数，则表示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17060_20103_x950830270}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若不指定该参数，则表示所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17060_20103_1605001589}[：显示指定单板上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若不指定该参数，则表示所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_17060_20103_103543562}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号，只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_1836352555}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_1744174705}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x834703030}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[过滤规则的信息。]{style="font-family:宋体"}

[[\<Sysname\> display portal rule all interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_17060_20103_x1603369206}

[IPv4 portal rules on GigabitEthernet1/0/1:]{lang="EN-US"}

[Rule 1]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Permit]{lang="EN-US"}

[ Protocol            : Any]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP             : 0.0.0.0]{lang="EN-US"}

[    Mask           : 0.0.0.0]{lang="EN-US"}

[    Port           : Any]{lang="EN-US"}

[    MAC            : 0000-0000-0000]{lang="EN-US"}

[    Interface      : GigabitEthernet1/0/1]{lang="EN-US"}

[    ]{lang="EN-US"}[VLAN           : ]{lang="IT"}[Any]{lang="EN-US"}

[ Destination:]{lang="IT"}

[    IP             : 192.168.0.111]{lang="IT"}

[    Mask           : 255.255.255.255]{lang="IT"}

[    Port           : Any]{lang="IT"}

[ ]{lang="EN-US"}

[Rule 2]{lang="EN-US"}

[ Type                : Dynamic]{lang="EN-US"}

[ Action              : Permit]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP             : 2.2.2.2]{lang="EN-US"}

[    MAC            : 000d-88f8-0eab]{lang="EN-US"}

[    Interface      : GigabitEthernet1/0/1]{lang="EN-US"}

[    ]{lang="EN-US"}[VLAN           : ]{lang="IT"}[Any]{lang="EN-US"}

[ ]{lang="IT"}[Author ACL:]{lang="EN-US"}

[    Number         : 3001]{lang="EN-US"}

[ ]{lang="EN-US"}

[Rule 3]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Redirect]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP             : 0.0.0.0]{lang="EN-US"}

[    Mask           : 0.0.0.0]{lang="EN-US"}

[    ]{lang="EN-US"}[Interface      : ]{lang="IT"}[GigabitEthernet1/0/1]{lang="EN-US"}

[    VLAN           : ]{lang="IT"}[Any]{lang="EN-US"}

[    Protocol       : TCP]{lang="EN-US"}

[ Destination:]{lang="IT"}

[    IP             : 0.0.0.0]{lang="IT"}

[    ]{lang="IT"}[Mask           : 0.0.0.0]{lang="EN-US"}

[    Port           : 80]{lang="IT"}

[ ]{lang="EN-US"}

[Rule 4:]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Deny]{lang="EN-US"}

[ ]{lang="EN-US"}[Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP             : 0.0.0.0]{lang="EN-US"}

[    Mask           : 0.0.0.0]{lang="EN-US"}

[    Interface      : GigabitEthernet1/0/1]{lang="EN-US"}

[    VLAN           : Any]{lang="EN-US"}

[ Destination:]{lang="EN-US"}

[    IP             : 0.0.0.0]{lang="IT"}

[    ]{lang="IT"}[Mask           : 0.0.0.0]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPv6 portal rules on GigabitEthernet1/0/1:]{lang="EN-US"}

[Rule 1]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Permit]{lang="EN-US"}

[ Protocol            : Any]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP             : ::]{lang="EN-US"}

[    Prefix length  : 0]{lang="EN-US"}

[    Port           : Any]{lang="EN-US"}

[    MAC            : 0000-0000-0000]{lang="EN-US"}

[    Interface      : GigabitEthernet1/0/1]{lang="EN-US"}

[    VLAN           : Any]{lang="EN-US"}

[ Destination:]{lang="EN-US"}

[    IP             : 3000::1]{lang="EN-US"}

[    Prefix length  : 64]{lang="EN-US"}

[    Port           : Any]{lang="EN-US"}

[ ]{lang="EN-US"}

[Rule 2]{lang="EN-US"}

[ Type                : Dynamic]{lang="EN-US"}

[ Action              : Permit]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP              : 3000::1]{lang="EN-US"}

[    MAC             : 0015-e9a6-7cfe]{lang="EN-US"}

[    Interface       : GigabitEthernet1/0/1]{lang="EN-US"}

[    VLAN            : Any]{lang="EN-US"}

[ Author ACL:]{lang="EN-US"}

[    Number          : 3001]{lang="EN-US"}

[ ]{lang="EN-US"}

[Rule 3]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Redirect]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP              : ::]{lang="EN-US"}

[    Prefix length   : 0]{lang="EN-US"}

[    Interface       : GigabitEthernet1/0/1]{lang="EN-US"}

[    VLAN            : Any]{lang="EN-US"}

[    Protocol        : TCP]{lang="EN-US"}

[ Destination:]{lang="EN-US"}

[    IP              : ::]{lang="EN-US"}

[    Prefix length   : 0]{lang="EN-US"}

[    Port            : 80]{lang="EN-US"}

[ ]{lang="EN-US"}

[Rule 4:]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Deny]{lang="EN-US"}

[ ]{lang="EN-US"}[Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP             : ::]{lang="EN-US"}

[    Prefix length  : 0]{lang="EN-US"}

[    Interface      : GigabitEthernet1/0/1]{lang="EN-US"}

[    VLAN           : Any]{lang="EN-US"}

[ Destination:]{lang="EN-US"}

[    IP             : ::]{lang="IT"}

[    ]{lang="IT"}[Prefix length  : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Rule 5:]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Match pre-auth ACL]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    Interface      : GigabitEthernet1/0/1]{lang="EN-US"}

[Pre-auth ACL:]{lang="EN-US"}

[    Number          : 3002]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_995061754}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_132190774}[显示接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[过滤规则的信息。]{style="font-family:宋体"}

[[\<Sysname\> display portal rule all interface vlan-interface 100]{lang="EN-US"}]{#struct_0_17060_20103_x1603041526}

[IPv4 portal rules on Vlan-interface100:]{lang="EN-US"}

[Rule 1]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Permit]{lang="EN-US"}

[ Protocol            : Any]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP             : 0.0.0.0]{lang="EN-US"}

[    Mask           : 0.0.0.0]{lang="EN-US"}

[    Port           : Any]{lang="EN-US"}

[    MAC            : 0000-0000-0000]{lang="EN-US"}

[    Interface      : ]{lang="EN-US"}[Vlan-interface100]{lang="EN-US"}

[    ]{lang="EN-US"}[VLAN           : 100]{lang="IT"}

[ Destination:]{lang="IT"}

[    IP             : 192.168.0.111]{lang="IT"}

[    Mask           : 255.255.255.255]{lang="IT"}

[    Port           : Any]{lang="IT"}

[ ]{lang="EN-US"}

[Rule 2]{lang="EN-US"}

[ Type                : Dynamic]{lang="EN-US"}

[ Action              : Permit]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP             : 2.2.2.2]{lang="EN-US"}

[    MAC            : 000d-88f8-0eab]{lang="EN-US"}

[    Interface      : GigabitEthernet1/0/1]{lang="EN-US"}

[    ]{lang="EN-US"}[VLAN           : 100]{lang="IT"}

[ ]{lang="IT"}[Author ACL:]{lang="EN-US"}

[    Number         : 3001]{lang="EN-US"}

[ ]{lang="EN-US"}

[Rule 3]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Redirect]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP             : 0.0.0.0]{lang="EN-US"}

[    Mask           : 0.0.0.0]{lang="EN-US"}

[    ]{lang="EN-US"}[Interface      : ]{lang="IT"}[Vlan-interface100]{lang="EN-US"}

[    VLAN           : 100]{lang="IT"}

[    Protocol       : TCP]{lang="EN-US"}

[ Destination:]{lang="IT"}

[    IP             : 0.0.0.0]{lang="IT"}

[    ]{lang="IT"}[Mask           : 0.0.0.0]{lang="EN-US"}

[    Port           : 80]{lang="IT"}

[ ]{lang="EN-US"}

[Rule 4:]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Deny]{lang="EN-US"}

[ ]{lang="EN-US"}[Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP             : 0.0.0.0]{lang="EN-US"}

[    Mask           : 0.0.0.0]{lang="EN-US"}

[    Interface      : Vlan-interface100]{lang="EN-US"}

[    VLAN           : Any]{lang="EN-US"}

[ Destination:]{lang="EN-US"}

[    IP             : 0.0.0.0]{lang="IT"}

[    ]{lang="IT"}[Mask           : 0.0.0.0]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPv6 portal rules on Vlan-interface100:]{lang="EN-US"}

[Rule 1]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Permit]{lang="EN-US"}

[ Protocol            : Any]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP              : ::]{lang="EN-US"}

[    Prefix length   : 0]{lang="EN-US"}

[    Port            : Any]{lang="EN-US"}

[    MAC             : 0000-0000-0000]{lang="EN-US"}

[    Interface       : ]{lang="EN-US"}[Vlan-interface100]{lang="EN-US"}

[    VLAN            : ]{lang="EN-US"}[100]{lang="EN-US"}

[ Destination:]{lang="EN-US"}

[    IP               : 3000::1]{lang="EN-US"}

[    Prefix length    : 64]{lang="EN-US"}

[    Port             : Any]{lang="EN-US"}

[ ]{lang="EN-US"}

[Rule 2]{lang="EN-US"}

[ Type                : Dynamic]{lang="EN-US"}

[ Action              : Permit]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP              : 3000::1]{lang="EN-US"}

[    MAC             : 0015-e9a6-7cfe]{lang="EN-US"}

[    Interface       : GigabitEthernet1/0/1]{lang="EN-US"}

[    VLAN            : 100]{lang="EN-US"}

[ Author ACL:]{lang="EN-US"}

[    Number          : 3001]{lang="EN-US"}

[ ]{lang="EN-US"}

[Rule 3]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Redirect]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP              : ::]{lang="EN-US"}

[    Prefix length   : 0]{lang="EN-US"}

[    Interface       : ]{lang="EN-US"}[Vlan-interface100]{lang="EN-US"}

[    VLAN            : 100]{lang="EN-US"}

[    Protocol        : TCP]{lang="EN-US"}

[ Destination:]{lang="EN-US"}

[    IP              : ::]{lang="EN-US"}

[    Prefix length   : 0]{lang="EN-US"}

[    Port            : 80]{lang="EN-US"}

[ ]{lang="EN-US"}

[Rule 4:]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Deny]{lang="EN-US"}

[ ]{lang="EN-US"}[Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP             : ::]{lang="EN-US"}

[    Prefix length  : 0]{lang="EN-US"}

[    Interface      : Vlan-interface100]{lang="EN-US"}

[    VLAN           : 100]{lang="EN-US"}

[ Destination:]{lang="EN-US"}

[    IP             : ::]{lang="IT"}

[    ]{lang="IT"}[Prefix length  : 0]{lang="EN-US"}

[Author ACL:]{lang="EN-US"}

[    Number          : 3001]{lang="EN-US"}

[ ]{lang="EN-US"}

[Rule 5:]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Match pre-auth ACL]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    Interface      : Vlan-interface100]{lang="EN-US"}

[Pre-auth ACL:]{lang="EN-US"}

[    Number          : 3002]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display portal rule]{lang="EN-US"}]{#struct_0_17060_20103_x1603107062}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2001625187}[[字段]{style="font-family:黑体"}]{#struct_0_17060_20103_1234297118}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17060_20103_x702826613}

[[Rule]{lang="EN-US"}]{#struct_0_17060_20103_x139601124}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1602713846}[过滤规则编号。]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[过滤规则和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[过滤规则分别编号]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_17060_20103_x1603172601}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_865733170}[过滤规则的类型，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DE" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="DE"}]{#struct_0_17060_20103_x563230113}[：静态类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DE" style="font-size:10.0pt;font-family:Symbol"}[Dynamic]{lang="DE"}]{#struct_0_17060_20103_1118183586}[：动态类型]{style="font-family:宋体"}

[[Action]{lang="EN-US"}]{#struct_0_17060_20103_x384719059}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_263591117}[过滤规则的匹配动作，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_17060_20103_x1603238137}[：允许报文通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Redirect]{lang="EN-US"}]{#struct_0_17060_20103_181125631}[：重定向报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny]{lang="EN-US"}]{#struct_0_17060_20103_1241116316}[：拒绝报文通过]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Match pre-auth ACL]{lang="EN-US"}]{#struct_0_17060_20103_1884423054}[：匹配认证前域中的授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_17060_20103_x1620473834}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_37447538}[过滤规则的传输层协议，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Any]{lang="EN-US"}]{#struct_0_17060_20103_x959922369}[：不限制传输层协议类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TCP]{lang="EN-US"}]{#struct_0_17060_20103_x1603303673}[：]{style="font-family:宋体"}[TCP]{lang="EN-US"}[传输类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP]{lang="EN-US"}]{#struct_0_17060_20103_x2026148727}[：]{style="font-family:宋体"}[UDP]{lang="EN-US"}[传输类型]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_17060_20103_1196688841}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_2003481487}[过滤]{style="font-family:宋体"}[规则下发的状态，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="ES-AR" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="ES-AR"}]{#struct_0_17060_20103_x312308608}[：表示规则已生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="ES-AR" style="font-size:10.0pt;font-family:Symbol"}[Unactuated]{lang="ES-AR"}]{#struct_0_17060_20103_x1603369209}[：表示规则未生效]{lang="EN-US" style="font-family:宋体"}

[[Source]{lang="EN-US"}]{#struct_0_17060_20103_x571022187}

[[Portal]{lang="ES-AR"}]{#struct_0_17060_20103_x970790200}[过滤]{style="font-family:宋体"}[规则的源信息]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_17060_20103_x165805406}

[[源]{style="font-family:宋体"}]{#struct_0_17060_20103_1241671887}[IP]{lang="ES-AR"}[地址]{style="font-family:宋体"}

[[Mask]{lang="EN-US"}]{#struct_0_17060_20103_x1602910457}

[[源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_17060_20103_1689945135}[地址子网掩码]{style="font-family:宋体"}

[[Prefix length]{lang="EN-US"}]{#struct_0_17060_20103_x2099266222}

[[源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_17060_20103_1912587702}[地址前缀]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_17060_20103_1719367965}

[[源传输层端口号]{style="font-family:宋体"}]{#struct_0_17060_20103_x1602975993}

[[MAC]{lang="EN-US"}]{#struct_0_17060_20103_x180019028}

[[源]{style="font-family:宋体"}]{#struct_0_17060_20103_x130214965}[MAC]{lang="ES-AR"}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_17060_20103_x1256059009}

[[Portal]{lang="ES-AR"}]{#struct_0_17060_20103_x1603041529}[过滤]{style="font-family:宋体"}[规则应用的二层或三层接口]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_17060_20103_x2050174766}

[[源]{style="font-family:宋体"}]{#struct_0_17060_20103_x201651046}[VLAN]{lang="ES-AR"}

[[Protocol]{lang="EN-US"}]{#struct_0_17060_20103_x1481349565}

[[Portal]{lang="ES-AR"}]{#struct_0_17060_20103_x1603107065}[规则的协议类型]{style="font-family:宋体"}

[[Destination]{lang="EN-US"}]{#struct_0_17060_20103_1993812005}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x805343633}[规则的目的信息]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_17060_20103_x319062935}

[[目的]{style="font-family:宋体"}]{#struct_0_17060_20103_x1602648313}[IP]{lang="ES-AR"}[地址]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_17060_20103_x1655862229}

[[目的传输层端口号]{style="font-family:宋体"}]{#struct_0_17060_20103_x1598668124}

[[Mask]{lang="EN-US"}]{#struct_0_17060_20103_x907754801}

[[目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_17060_20103_x1602713849}[地址子网掩码]{style="font-family:宋体"}

[[Prefix length]{lang="EN-US"}]{#struct_0_17060_20103_x1652045687}

[[目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_17060_20103_1698842865}[地址前缀]{style="font-family:宋体"}

[[Author ACL]{lang="EN-US"}]{#struct_0_17060_20103_366374516}

[[Portal]{lang="EN-GB"}]{#struct_0_17060_20103_x1603238136}[用户认证后的授权]{style="font-family:宋体"}[ACL]{lang="EN-GB"}[，]{style="font-family:宋体"}[即]{style="font-family:宋体"}[AAA]{lang="EN-US"}[授权给用户的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，]{style="font-family:宋体"}[该字段仅在]{style="font-family:宋体"}[Type]{lang="EN-US"}[为]{style="font-family:宋体"}[Dynamic]{lang="EN-US"}[时才显示]{style="font-family:宋体"}

[[Pre-auth ACL]{lang="EN-US"}]{#struct_0_17060_20103_x797406134}

[[Portal]{lang="EN-GB"}]{#struct_0_17060_20103_x1209004195}[用户认证前的授权]{style="font-family:宋体"}[ACL]{lang="EN-GB"}[，该字段仅在]{style="font-family:宋体"}[Action]{lang="EN-GB"}[为]{style="font-family:宋体"}[Match pre-auth ACL]{lang="EN-US"}[时显示]{style="font-family:宋体"}

[[Number]{lang="EN-US"}]{#struct_0_17060_20103_1747209572}

[[授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_17060_20103_x178823795}[编号，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[未授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-1853837626 .myid}
[]{#_Toc404792728}[]{#struct_0_17060_20103_732854181}[]{#_Toc330201702}[]{#_Toc320893867}

**Portal \-- Portal配置命令 \-- display portal server**

------------------------------------------------------------------------

[**[display portal server]{lang="EN-US"}**]{#struct_0_17060_20103_189894227}[命令用来显示]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x635998637}

[**[display portal server]{lang="EN-US"}**[ \[ *server-name* \]]{lang="EN-US"}]{#struct_0_17060_20103_x1441757232}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1603303672}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17060_20103_702734628}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x797364021}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x2021459891}

[[network-operator]{lang="EN-US"}]{#struct_0_17060_20103_1439850826}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_x382987243}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17060_20103_1885971228}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1659966748}

[*[server-name]{lang="EN-US"}*]{#struct_0_17060_20103_x574108022}[：]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x404529883}

[[若不指定参数]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*]{#struct_0_17060_20103_x1603369208}[，则显示所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x2137106128}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_202656810}[显示]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[pts]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display portal server pts]{lang="EN-US"}]{#struct_0_17060_20103_x1640641446}

[Portal server: pts]{lang="EN-US"}

[  IP                    : 192.168.0.111]{lang="EN-US"}

[  VPN instance          : vpn1]{lang="EN-US"}

[  Port                  : 50100]{lang="EN-US"}

[  Server detection      : Timeout 60s  Action: log, trap]{lang="EN-US"}

[  User synchronization  : Timeout 200s]{lang="EN-US"}

[  Status                : Up]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display portal server]{lang="EN-US"}]{#struct_0_17060_20103_x1963774441}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1986924451}[[字段]{style="font-family:黑体"}]{#struct_0_17060_20103_x694395766}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17060_20103_1425179566}

[[Portal server]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_17060_20103_x1602910456}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1038938220}[认证服务器名称]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_17060_20103_x288113186}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1419653180}[认证服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_17060_20103_1402456884}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x923333468}[认证服务器所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}

[[该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_17060_20103_877944526}

[[Port]{lang="EN-US"}]{#struct_0_17060_20103_x1602975992}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1386064913}[认证服务器的监听端口]{style="font-family:宋体"}

[[Server detection]{lang="EN-US"}]{#struct_0_17060_20103_1303792093}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1030735284}[认证服务器可达性探测功能的参数，包括超时时间（单位：秒），以及探测到服务器状态变化后触发的动作（]{style="font-family:宋体"}[log]{lang="EN-US"}[、]{style="font-family:宋体"}[trap]{lang="EN-US"}[）]{style="font-family:宋体"}

[[User synchronization]{lang="EN-US"}]{#struct_0_17060_20103_221833738}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1884197724}[用户用户信息同步功能的参数，包括超时时间（单位：秒）]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_17060_20103_x1603041528}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_678708589}[认证服务器当前状态，其取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_17060_20103_966172922}[：服务器可达性探测功能未开启，可达状态未知]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_17060_20103_1719550291}[：服务器可达性探测功能已开启，探测结果为该服务器当前可达]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_17060_20103_x1619655544}[：服务器可达性探测功能已开启，探测结果为该服务器当前不可达]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1251170506}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal enable]{lang="EN-US"}**]{#struct_0_17060_20103_x1603107064}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal server]{lang="EN-US"}**]{#struct_0_17060_20103_427728064}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[server-detect]{lang="EN-US"}**]{#struct_0_17060_20103_188686410}[ (portal server view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[user-sync]{lang="EN-US"}**]{#struct_0_17060_20103_x627947306}

::: {#1183812578 .myid}
[]{#_Toc404792729}[]{#struct_0_17060_20103_x814510815}[]{#_Toc330201706}[]{#_Toc320893870}

**Portal \-- Portal配置命令 \-- display portal user**

------------------------------------------------------------------------

[**[display portal user]{lang="EN-US"}**]{#struct_0_17060_20103_266326655}[命令用来显示]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1155400357}

[**[display portal user]{lang="EN-US"}**[ { **all** \| **interface** *interface-type interface-number \|* **ip** *ip-address* \| **ipv6** *ipv6-address* \| **pre-auth** \[ **interface** { *interface-type interface-number* \| *interface-name* } \| **ip** *ip-address* \| **ipv6** *ipv6-address* \] } \[ **verbose** \]]{lang="EN-US"}]{#struct_0_17060_20103_x652467064}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1875656111}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17060_20103_x1602648312}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_1073021126}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_186826862}

[[network-operator]{lang="EN-US"}]{#struct_0_17060_20103_x1008619724}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_935132003}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17060_20103_617890623}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x88878136}

[**[pre-auth]{lang="EN-US"}**]{#struct_0_17060_20103_21346726}[：显示]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证前用户信息。若不指定该参数，则显示]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的信息。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_17060_20103_x844525837}[：显示所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**]{#struct_0_17060_20103_x2147094987}[ *interface-type interface-number*]{lang="EN-US"}[：显示指定接口上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:
宋体"}

[**[ip]{lang="EN-US"}**[ *ipv4-address*]{lang="EN-US"}]{#struct_0_17060_20103_x679421814}[：显示指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_17060_20103_473271780}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17060_20103_x1025400149}[：显示指定]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1602713848}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_17060_20103_x85961746}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_193053328}[显示所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的信息。]{style="font-family:宋体"}

[[\<Sysname\> display portal user all]{lang="EN-US"}]{#struct_0_17060_20103_x1603172603}

[Total portal users: 2]{lang="EN-US"}

[Username: abc]{lang="EN-US"}

[  Portal server: pts]{lang="EN-US"}

[  State: Online]{lang="EN-US"}

[  VPN instance: N/A]{lang="EN-US"}

[  MAC                IP                 VLAN   Interface]{lang="EN-US"}

[  000d-88f8-0eab     2.2.2.2            \--     GigabitEthernet1/0/1]{lang="EN-US"}

[  Authorization information:]{lang="EN-US"}

[    DHCP IP pool: ]{lang="EN-US"}[N/A]{lang="EN-US"}

[    User profile: abc (active)]{lang="EN-US"}

[    Session group profile: cd (inactive)]{lang="EN-US"}

[    ACL number: N/A]{lang="EN-US"}

[    Inbound CAR: N/A]{lang="EN-US"}

[    Outbound CAR: N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[Username: def]{lang="EN-US"}

[  Portal server: pts]{lang="EN-US"}

[  State: Online]{lang="EN-US"}

[  VPN instance: vpn1]{lang="EN-US"}

[  MAC                IP                 VLAN   Interface]{lang="EN-US"}

[  000d-88f8-0eac     3.3.3.3            \--     GigabitEthernet1/0/2]{lang="EN-US"}

[  Authorization information:]{lang="EN-US"}

[    DHCP IP pool: ]{lang="EN-US"}[N/A]{lang="EN-US"}

[    ]{lang="EN-US"}[User profile: N/A]{lang="EN-US"}

[    Session group profile: N/A]{lang="EN-US"}

[    ACL number: 3000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x679487350}[显示]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[50.50.50.3]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display portal user ip-address 50.50.50.3 verbose]{lang="EN-US"}]{#struct_0_17060_20103_x679946103}

[Basic]{lang="EN-US"}[：]{style="font-family:
宋体"}

[  Current IP address: 50.50.50.3]{lang="EN-US"}

[  Original IP address: 30.30.30.2]{lang="EN-US"}

[  Username: user1@hrss]{lang="EN-US"}

[  User ID: 0x28000002]{lang="EN-US"}

[  Access interface: eth3/2/2]{lang="EN-US"}

[  Service-VLAN/Customer-VLAN: -/-]{lang="EN-US"}

[  MAC address: 0000-0000-0001]{lang="EN-US"}

[  Domain: hrss]{lang="EN-US"}

[  VPN instance: 123]{lang="EN-US"}

[  Status: Online]{lang="EN-US"}

[  Portal server: test]{lang="EN-US"}

[  Portal authentication method: Direct]{lang="EN-US"}

[AAA:]{lang="EN-US"}

[ Realtime accounting interval: 60s, retry times: 3]{lang="EN-US"}

[  Idle-cut:180 sec, 10240 bytes]{lang="EN-US"}

[  Session duration: 500 sec, remaining: 300 sec]{lang="EN-US"}

[  Remaining traffic: 10240000 bytes]{lang="EN-US"}

[  Login time: 2014-01-19  2:42:3 UTC]{lang="EN-US"}

[  ITA policy name: test]{lang="EN-US"}

[  IP pool: abc]{lang="EN-US"}

[ACL&QoS&Multicast:]{lang="EN-US"}

[  Inbound CAR: CIR 64000bps PIR 640000bps]{lang="EN-US"}

[  Outbound CAR: CIR 64000bps PIR 640000bps]{lang="EN-US"}

[  ACL number:3000]{lang="EN-US"}[（]{style="font-family:宋体"}[inactive]{lang="EN-US"}[）]{style="font-family:宋体"}

[  User profile: portal (active)]{lang="EN-US"}

[  Session group profile: N/A]{lang="EN-US"}

[  Max multicast addresses: 4]{lang="EN-US"}

[  Multicast address list: 1.2.3.1, 1.34.33.1, 3.123.123.3, 4.5.6.7]{lang="EN-US"}

[2.2.2.2, 3.3.3.3, 4.4.4.4]{lang="EN-US"}

[Flow statistic:]{lang="EN-US"}

[  Uplink   packets/bytes: 7/546]{lang="EN-US"}

[  Downlink packets/bytes: 0/0]{lang="EN-US"}

[ITA:]{lang="EN-US"}

[  level-1 uplink   packets/bytes: 4/32]{lang="EN-US"}

[          downlink packets/bytes: 2/12]{lang="EN-US"}

[  level-2 uplink   packets/bytes: 0/0]{lang="EN-US"}

[          downlink packets/bytes: 0/0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x297066244}[应用]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x1603238139}[显示所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的信息。]{style="font-family:宋体"}

[[\<Sysname\> display portal user all]{lang="EN-US"}]{#struct_0_17060_20103_x1603303675}

[Total portal users: 2]{lang="EN-US"}

[Username: abc]{lang="EN-US"}

[  Portal server: pts]{lang="EN-US"}

[  State: Online]{lang="EN-US"}

[  VPN instance: N/A]{lang="EN-US"}

[  MAC                IP                 VLAN   Interface]{lang="EN-US"}

[  000d-88f8-0eab     2.2.2.2            100    Vlan-interface100]{lang="EN-US"}

[  Authorization information:]{lang="EN-US"}

[    DHCP IP pool: ]{lang="EN-US"}[N/A]{lang="EN-US"}

[    User profile: abc ]{lang="EN-US"}[（]{style="font-family:宋体"}[active]{lang="EN-US"}[）]{style="font-family:宋体"}

[    Session group profile: bcd (inactive)]{lang="EN-US"}

[    ACL number: N/A]{lang="EN-US"}

[    Inbound CAR: N/A]{lang="EN-US"}

[    Outbound CAR: N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[Username: def]{lang="EN-US"}

[  Portal server: pts]{lang="EN-US"}

[  State: Online]{lang="EN-US"}

[  VPN instance: vpn1]{lang="EN-US"}

[  MAC                IP                 VLAN   Interface]{lang="EN-US"}

[  000d-88f8-0eac     3.3.3.3            200    Vlan-interface200]{lang="EN-US"}

[  Authorization information:]{lang="EN-US"}

[    DHCP IP pool: ]{lang="EN-US"}[N/A]{lang="EN-US"}

[    ]{lang="EN-US"}[User profile: N/A]{lang="EN-US"}

[    Session group profile: N/A]{lang="EN-US"}

[    ]{lang="EN-US"}[ACL number: 3001]{lang="EN-US"}

[    Inbound CAR: CIR    3072 bps        PIR     3072 bps]{lang="EN-US"}

[    Outbound CAR: CIR    3072 bps        PIR     3072 bps]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x680077175}[显示所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证前用户的信息。]{style="font-family:宋体"}

[[\<Sysname\> display portal user pre-auth]{lang="EN-US"}]{#struct_0_17060_20103_x797471670}

[Total portal pre-auth users: 2]{lang="EN-US"}

[  MAC             IP                    VLAN    Interface]{lang="EN-US"}

[  000a-eb29-75f1  18.18.0.3             200     Route-Aggregation100]{lang="EN-US"}

[  State: Online]{lang="EN-US"}

[  VPN instance: N/A]{lang="EN-US"}

[  Authorization information:]{lang="EN-US"}

[    User profile: quew (active)]{lang="EN-US"}

[    Session group profile: pt1 (active)]{lang="EN-US"}

[    ACL number: 3000 (active)]{lang="EN-US"}

[    Inbound CAR: CIR    3072 bps        PIR     3072 bps]{lang="EN-US"}

[    Outbound CAR: CIR    3072 bps         PIR     3072 bps]{lang="EN-US"}

[ ]{lang="EN-US"}

[  MAC             IP                    VLAN    Interface]{lang="EN-US"}

[  000a-eb29-75f2  18.18.0.4             200     Route-Aggregation100]{lang="EN-US"}

[  State: Online]{lang="EN-US"}

[  VPN instance: N/A]{lang="EN-US"}

[  Authorization information:]{lang="EN-US"}

[    User profile: quew (active)]{lang="EN-US"}

[    Session group profile: pt1 (active)]{lang="EN-US"}

[    ACL number: 3000 (active)]{lang="EN-US"}

[    Inbound CAR: CIR    3072 bps        PIR     3072 bps]{lang="EN-US"}

[    Outbound CAR: CIR    3072 bps         PIR     3072 bp]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_368947600}[显示]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[50.50.50.3]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的详细信息。]{style="font-family:宋体"}

[[\<Sysname\>display portal user ip-address 50.50.50.3 verbose]{lang="EN-US"}]{#struct_0_17060_20103_x680142711}

[Basic:]{lang="EN-US"}

[  Current IP address: 50.50.50.3]{lang="EN-US"}

[  Original IP address: 30.30.30.2]{lang="EN-US"}

[  Username: user1@hrss]{lang="EN-US"}

[  User ID: 0x28000002]{lang="EN-US"}

[  Access interface: eth3/2/2]{lang="EN-US"}

[  Service-VLAN/Customer-VLAN: -/-]{lang="EN-US"}

[  MAC address: 0000-0000-0001]{lang="EN-US"}

[  Domain: hrss]{lang="EN-US"}

[  VPN instance: 123]{lang="EN-US"}

[  Status: Online]{lang="EN-US"}

[  Portal server: test]{lang="EN-US"}

[  Portal authentication method: Direct]{lang="EN-US"}

[AAA:]{lang="EN-US"}

[  Realtime accounting interval: 60s, retry times: 3]{lang="EN-US"}

[  Idle-cut:180 sec, 10240 bytes]{lang="EN-US"}

[  Session duration: 500 sec, remaining: 300 sec]{lang="EN-US"}

[  Remaining traffic: 10240000 bytes]{lang="EN-US"}

[  Login time: 2014-01-19  2:42:3 UTC]{lang="EN-US"}

[  ITA policy name: test]{lang="EN-US"}

[  IP pool: abc]{lang="EN-US"}

[ACL&QoS&Multicast:]{lang="EN-US"}

[  Inbound CAR: CIR 64000bps PIR 640000bps]{lang="EN-US"}

[  Outbound CAR: CIR 64000bps PIR 640000bps]{lang="EN-US"}

[  ACL number: 3000]{lang="EN-US"}[（]{style="font-family:宋体"}[inactive]{lang="EN-US"}[）]{style="font-family:宋体"}

[  User profile: portal (active)]{lang="EN-US"}

[  Session group profile: N/A]{lang="EN-US"}

[  Max multicast addresses: 4]{lang="EN-US"}

[  Multicast address list: 1.2.3.1, 1.34.33.1, 3.123.123.3, 4.5.6.7]{lang="EN-US"}

[                          2.2.2.2, 3.3.3.3, 4.4.4.4]{lang="EN-US"}

[Flow statistic:]{lang="EN-US"}

[  Uplink   packets/bytes: 7/546]{lang="EN-US"}

[  Downlink packets/bytes: 0/0]{lang="EN-US"}

[ITA:]{lang="EN-US"}

[  level-1 uplink   packets/bytes: 4/32]{lang="EN-US"}

[          downlink packets/bytes: 2/12]{lang="EN-US"}

[  level-2 uplink   packets/bytes: 0/0]{lang="EN-US"}

[          downlink packets/bytes: 0/0]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display portal user]{lang="EN-US"}]{#struct_0_17060_20103_1462249515}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1984272387}[[字段]{style="font-family:黑体"}]{#struct_0_17060_20103_x1749605424}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17060_20103_x690945723}

[[Total portal users]{lang="EN-US"}]{#struct_0_17060_20103_x613383076}

[[总计的]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1761637507}[用户数目]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_17060_20103_1857192902}

[[用户名]{style="font-family:宋体"}]{#struct_0_17060_20103_328350652}

[[Portal server]{lang="EN-US"}]{#struct_0_17060_20103_579677752}

[[用户认证所使用的]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_579350072}[认证服务器的名称]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_17060_20103_x1603369211}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x927318083}[用户的当前状态，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initialized]{lang="EN-US"}]{#struct_0_17060_20103_1403561431}[：初始化完成后的待认证状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Authenticating]{lang="EN-US"}]{#struct_0_17060_20103_x576284703}[：正在认证状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Author]{lang="EN-US"}]{#struct_0_17060_20103_1712247880}[i]{lang="EN-US"}[zing]{lang="EN-US"}[：正在授权状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_17060_20103_1579186681}[：在线状态]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_17060_20103_579284536}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_953459727}[用户所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[。若用户属于公网，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_17060_20103_579481144}

[[MAC]{lang="EN-US"}]{#struct_0_17060_20103_x986588082}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1536253957}[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_17060_20103_x1334483477}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_488038429}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_17060_20103_x1603041531}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1693878870}[用户所在的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_17060_20103_186881433}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_496706865}[用户接入的接口]{style="font-family:宋体"}

[[Authorization information]{lang="EN-US"}]{#struct_0_17060_20103_579612215}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_579546679}[用户的授权信息]{style="font-family:宋体"}

[[DHCP IP pool]{lang="EN-US"}]{#struct_0_17060_20103_x345624229}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_579743287}[用户的授权地址池名字。若无授权地址池，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[User profile]{lang="EN-US"}]{#struct_0_17060_20103_579677751}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_579481143}[用户的授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[名称。若未授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_17060_20103_x680339319}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_17060_20103_x680404855}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:宋体"}[User profile]{lang="EN-US"}

[[Session group profile]{lang="EN-US"}]{#struct_0_17060_20103_579415607}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_579612214}[用户的授权]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[名称。若未授权]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_17060_20103_x1918494886}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session group profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_17060_20103_x679421815}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session group profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:
  宋体"}[User profile]{lang="EN-US"}

[[ACL number]{lang="EN-US"}]{#struct_0_17060_20103_579546678}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x345624230}[用户的授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号。若未授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_17060_20103_473206244}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_17060_20103_x679487351}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}

[[Inbound CAR]{lang="EN-US"}]{#struct_0_17060_20103_x844067085}

[[授权的入方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_17060_20103_x849819301}[（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）。若未授权入方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Outbound CAR]{lang="EN-US"}]{#struct_0_17060_20103_1884816270}

[[授权的出方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_17060_20103_x468361307}[（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）。若未授权出方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display portal user verbose]{lang="EN-US"}]{#struct_0_17060_20103_448285066}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1933355889}[[字段]{style="font-family:黑体"}]{#struct_0_17060_20103_x1083230633}

[[描述]{style="font-family:黑体"}]{#struct_0_17060_20103_1213536974}

[[Current IP address]{lang="EN-US"}]{#struct_0_17060_20103_x1083296169}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x914105207}[用户当前的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Original IP address]{lang="EN-US"}]{#struct_0_17060_20103_794308587}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1083361705}[用户认证时的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_17060_20103_1738499880}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1083427241}[用户上线时使用的用户名]{style="font-family:宋体"}

[[User ID]{lang="EN-US"}]{#struct_0_17060_20103_1130240419}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x506325668}[用户]{style="font-family:宋体"}[ID ]{lang="EN-US"}

[[Access interface]{lang="EN-US"}]{#struct_0_17060_20103_x1083492777}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x300038715}[用户接入的接口]{style="font-family:宋体"}

[[Service-VLAN/Customer-VLAN]{lang="EN-US"}]{#struct_0_17060_20103_x1083558313}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1245214785}[用户所在的公网]{style="font-family:宋体"}[VLAN/]{lang="EN-US"}[私网]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示没有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[信息）]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_17060_20103_x1083623849}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17060_20103_955760257}[地址]{style="font-family:宋体"}

[[Domain]{lang="EN-US"}]{#struct_0_17060_20103_x1083689385}

[[用户认证时使用的]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_17060_20103_x182413562}[域名]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_17060_20103_x1082706345}

[[用户所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_17060_20103_x1345825049}[实例，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示用户属于公网]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_17060_20103_870749566}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1082771881}[用户的当前状态，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Authenticating]{lang="EN-US"}]{#struct_0_17060_20103_x662482635}[：正在认证状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Authorizing]{lang="EN-US"}]{#struct_0_17060_20103_x1083230634}[：正在授权状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Waiting_SetRule]{lang="EN-US"}]{#struct_0_17060_20103_x708777327}[：正在下发]{lang="EN-US" style="font-family:
  宋体"}[Portal]{lang="EN-US"}[规则状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_17060_20103_x1083296170}[：在线状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Waiting_Traffic]{lang="EN-US"}]{#struct_0_17060_20103_1008274630}[：正在等待用户流量状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stop Accounting]{lang="EN-US"}]{#struct_0_17060_20103_x1083361706}[：正在停止计费状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_17060_20103_x990383475}[：用户下线完成状态]{style="font-family:宋体"}

[[Portal server]{lang="EN-US"}]{#struct_0_17060_20103_x1083427242}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1598642936}[服务器名称]{style="font-family:宋体"}

[[Portal authentication method]{lang="EN-US"}]{#struct_0_17060_20103_x1549473385}

[[接入接口上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1083492778}[认证方式，包括如下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direct]{lang="EN-US"}]{#struct_0_17060_20103_103245812}[：直接方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Re-Dhcp]{lang="EN-US"}]{#struct_0_17060_20103_x1083558314}[：二次地址方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Layer3]{lang="EN-US"}]{#struct_0_17060_20103_2004729672}[：三层方式]{lang="EN-US" style="font-family:宋体"}

[[AAA]{lang="EN-US"}]{#struct_0_17060_20103_x1083623850}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x966488508}[用户的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[授权信息]{style="font-family:宋体"}

[[Realtime accounting interval]{lang="EN-US"}]{#struct_0_17060_20103_x1083689386}

[[授权的实时计费间隔和重传次数。若未授权，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_17060_20103_x585698089}

[[Idle-cut]{lang="EN-US"}]{#struct_0_17060_20103_x1082706346}

[[授权的闲置切断时长和流量。若未授权，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_17060_20103_x1749109576}

[[Session duration]{lang="EN-US"}]{#struct_0_17060_20103_x1082771882}

[[授权的会话时长以及剩余的会话时长。若未授权，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_17060_20103_2066400720}

[[Remaining traffic]{lang="EN-US"}]{#struct_0_17060_20103_x1083230631}

[[授权的剩余流量。若未授权，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_17060_20103_50737560}

[[Login time]{lang="EN-US"}]{#struct_0_17060_20103_x1083296167}

[[用户登录时间，即用户授权成功的时间，格式为设备时间，如：]{style="font-family:宋体"}[2023-1-19  2:42:30 UTC]{lang="EN-US"}]{#struct_0_17060_20103_248694207}

[[ITA policy name]{lang="EN-US"}]{#struct_0_17060_20103_1369342059}

[[授权的]{style="font-family:宋体"}[ITA]{lang="EN-US"}]{#struct_0_17060_20103_x1083361703}[（]{style="font-family:宋体"}[Intelligent Target Accounting]{lang="EN-US"}[，智能靶向计费）策略名称]{style="font-family:宋体"}

[[IP pool]{lang="EN-US"}]{#struct_0_17060_20103_x1393668002}

[[授权的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_17060_20103_x1083427239}[地址池名称。若未授权]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Inbound CAR]{lang="EN-US"}]{#struct_0_17060_20103_1486667387}

[[授权的入方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_17060_20103_x1083492775}[（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）。若未授权入方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Outbound CAR]{lang="EN-US"}]{#struct_0_17060_20103_862760699}

[[授权的出方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_17060_20103_x1083558311}[（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）。若未授权出方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[ACL number]{lang="EN-US"}]{#struct_0_17060_20103_x1886953097}

[[授权的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_17060_20103_x1083623847}[编号。若未授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_17060_20103_1762329311}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_17060_20103_x1083689383}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}

[[User profile]{lang="EN-US"}]{#struct_0_17060_20103_x988982616}

[[授权的]{style="font-family:宋体"}[User profile]{lang="EN-US"}]{#struct_0_17060_20103_x1082706343}[名称。若未授权]{style="font-family:宋体"}[User profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_17060_20103_2142573193}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_17060_20103_x1082771879}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:宋体"}[User profile]{lang="EN-US"}

[[Session group profile]{lang="EN-US"}]{#struct_0_17060_20103_x1019696035}

[[授权的]{style="font-family:宋体"}[Session group profile]{lang="EN-US"}]{#struct_0_17060_20103_x1083230632}[名称。若未授权]{style="font-family:宋体"}[Session group profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_17060_20103_x1515346381}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session group profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_17060_20103_x1083296168}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session group profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:
  宋体"}[User profile]{lang="EN-US"}

[[Max multicast addresses]{lang="EN-US"}]{#struct_0_17060_20103_x1083361704}

[[授权]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_172415939}[用户可加入的组播组的最大数目]{style="font-family:宋体"}

[[Multicast address list]{lang="EN-US"}]{#struct_0_17060_20103_x1083427240}

[[授权]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x435843522}[用户可加入的的组播组列表。若未授权组播组列表，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Flow statistic]{lang="EN-US"}]{#struct_0_17060_20103_x1083492776}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1266045226}[用户流量统计信息]{style="font-family:宋体"}

[[Uplink packets/bytes]{lang="EN-US"}]{#struct_0_17060_20103_x1083558312}

[[上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17060_20103_x1483668570}[字节数]{style="font-family:宋体"}

[[Downlink packets/bytes]{lang="EN-US"}]{#struct_0_17060_20103_x1083623848}

[[下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17060_20103_x610323684}[字节数]{style="font-family:宋体"}

[[ITA]{lang="EN-US"}]{#struct_0_17060_20103_x1083689384}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1748497503}[用户的]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务流量统计信息]{style="font-family:宋体"}

[[level-*n* uplink packets/bytes]{lang="EN-US"}]{#struct_0_17060_20103_x1082706344}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_17060_20103_1383058306}[的上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8 ]{lang="EN-US"}

[[level-n downlink packets/bytes]{lang="EN-US"}]{#struct_0_17060_20103_x1082771880}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_17060_20103_903601306}[的下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1023829522}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal enable]{lang="EN-US"}**]{#struct_0_17060_20103_x94853877}

::: {#1151501394 .myid}
[]{#_Toc404792730}[]{#struct_0_17060_20103_2130163210}[]{#_Toc330201703}

**Portal \-- Portal配置命令 \-- display portal web-server**

------------------------------------------------------------------------

[**[display portal web-server]{lang="EN-US"}**]{#struct_0_17060_20103_x1603107067}[命令用来显示]{style="font-family:
宋体"}[Portal Web]{lang="EN-US"}[服务器信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_831012591}

[**[display portal web-server]{lang="EN-US"}**]{#struct_0_17060_20103_804551837}[ \[ *server-name* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1391590929}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17060_20103_1134688900}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_1950202289}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x1065010155}

[[network-operator]{lang="EN-US"}]{#struct_0_17060_20103_742849220}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_1050346156}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17060_20103_x964925041}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1602648315}

[*[server-name]{lang="EN-US"}*]{#struct_0_17060_20103_1476305653}[：]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_1172935416}

[[若不指定参数]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*]{#struct_0_17060_20103_x1200320078}[，则显示所有]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1748297853}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_2139378936}[显示]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器]{style="font-family:宋体"}[wbs]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display portal web-server wbs]{lang="EN-US"}]{#struct_0_17060_20103_x1602713851}

[Portal Web server: wbs]{lang="EN-US"}

[    URL              : http://www.test.com/portal]{lang="EN-US"}

[    URL parameters   : userurl=http://www.test.com/welcome]{lang="EN-US"}

[                       userip=source-address]{lang="EN-US"}

[    VPN instance     : Not configured]{lang="EN-US"}

[    Server detection : Interval: 120s  Attempts: 5  Action: log, trap]{lang="EN-US"}

[    IPv4 status      : Up]{lang="EN-US"}

[    IPv6 status      : N/A]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display portal web-server]{lang="EN-US"}]{#struct_0_17060_20103_x1295880863}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1991485923}[[字段]{style="font-family:黑体"}]{#struct_0_17060_20103_1548717881}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17060_20103_559479925}

[[Portal Web server ]{lang="EN-US"}]{#struct_0_17060_20103_x137023777}

[[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_1101223495}[服务器名称]{style="font-family:宋体"}

[[URL]{lang="EN-US"}]{#struct_0_17060_20103_834318216}

[[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_362247246}[服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址以及携带的参数]{style="font-family:宋体"}

[[URL parameters]{lang="EN-US"}]{#struct_0_17060_20103_x1603172602}

[[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_1269017697}[服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[携带的参数信息]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_17060_20103_x2106555392}

[[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_x547106988}[服务器所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例名称]{style="font-family:宋体"}

[[Server detection]{lang="EN-US"}]{#struct_0_17060_20103_x20228832}

[[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_x1658612330}[服务器可达性探测功能的参数，包括探测间隔时间（单位：秒），探测尝试次数以及探测到服务器状态变化后的动作（]{style="font-family:宋体"}[log]{lang="EN-US"}[、]{style="font-family:宋体"}[trap]{lang="EN-US"}[）]{style="font-family:宋体"}

[[IPv4/IPv6 status]{lang="EN-US"}]{#struct_0_17060_20103_x1603238138}

[[Portal web]{lang="EN-US"}]{#struct_0_17060_20103_584410158}[服务器当前状态，其取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_17060_20103_1461299030}[：服务器可达性探测功能未开启，可达状态未知]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_17060_20103_1459430350}[：服务器可达性探测功能已开启，且探测结果为该服务器当前可达]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_17060_20103_131146888}[：服务器可达性探测功能已开启，且探测结果为该服务器当前不可达]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_18065793}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal enable]{lang="EN-US"}**]{#struct_0_17060_20103_x1603303674}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal web-server]{lang="EN-US"}**]{#struct_0_17060_20103_x103834426}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[server-detect]{lang="EN-US"}**]{#struct_0_17060_20103_x910048172}[ (portal web-server view)]{lang="EN-US"}

::: {#-1389047907 .myid}
[]{#_Toc404792731}[]{#struct_0_17060_20103_579350077}

**Portal \-- Portal配置命令 \-- display web-redirect rule**

------------------------------------------------------------------------

[**[display web-redirect rule]{lang="EN-US"}**]{#struct_0_17060_20103_579284541}[命令用来显示指定接口上的]{style="font-family:
宋体"}[Web]{lang="EN-US"}[重定向]{style="font-family:
宋体"}[过滤规则信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1762763794}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17060_20103_579481149}

[**[display web-redirect rule interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_17060_20103_1240781214}

[[分布式设备---独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17060_20103_579415613}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display web-redirect rule]{lang="EN-US"}**[ **interface** *interface-type interface-number* \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_17060_20103_x1892142912}

[[分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17060_20103_287478354}[设备：]{style="font-family:宋体"}

[**[display web-redirect rule]{lang="EN-US"}**[ **interface** *interface-type interface-number* \[ **chassis** *chassis-number * **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_17060_20103_580070973}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x65065725}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17060_20103_579612220}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1604821421}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x1428920812}

[[network-operator]{lang="EN-US"}]{#struct_0_17060_20103_579546684}

[[vd-admin]{lang="EN-US"}]{#struct_0_17060_20103_x683331226}

[[vd-operator]{lang="EN-US"}]{#struct_0_17060_20103_579743292}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x2014617864}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_17060_20103_579677756}[：显示指定接口的]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向过滤规则信息。]{style="font-family:宋体"}[interface-type interface-number]{lang="EN-US"}[为接口类型和接口编号。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_17060_20103_702069996}[：显示指定单板上指定接口的]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向过滤规则信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。若不指定该参数，则显示主用主控板上的]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向过滤规则信息。（分布式设备]{style="font-family:宋体"}[-]{lang="EN-US"}[独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_17060_20103_x1246612827}[：显示指定成员设备上指定接口的]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向过滤规则信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[若不指定该参数，则显示主用设备上的]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向过滤规则信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_17060_20103_x211565329}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上指定接口的]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向过滤规则信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若不指定该参数，则显示主用设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向过滤规则信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17060_20103_579350076}[：显示指定成员设备的指定单板上指定接口的]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向过滤规则，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。若不指定该参数，则显示全局主用主控板上的]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向过滤规则信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17060_20103_x963694515}[：显示指定单板上指定接口的]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向过滤规则，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。若不指定该参数，则显示全局主用主控板上的]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向过滤规则信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_1767065619}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_579284540}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1762763793}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向过滤规则。]{style="font-family:宋体"}

[[\<Sysname\> display web-redirect rule interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_17060_20103_579481148}

[IPv4 ]{lang="EN-US"}[web-redirect]{lang="EN-US"}[ rules on ]{lang="EN-US"}[GigabitEthernet1/0/1:]{lang="EN-US"}

[Rule 1:]{lang="EN-US"}

[ Type                : Dynamic]{lang="EN-US"}

[ Action              : Permit]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP             : 192.168.2.114]{lang="EN-US"}

[    VLAN           : Any]{lang="EN-US"}

[ ]{lang="EN-US"}

[Rule 2:]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Redirect]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    VLAN           : Any]{lang="EN-US"}

[    Protocol       : TCP]{lang="EN-US"}

[ Destination:]{lang="EN-US"}

[    Port           : 80]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPv6 ]{lang="EN-US"}[web-redirect]{lang="EN-US"}[ rules on ]{lang="EN-US"}[GigabitEthernet1/0/1:]{lang="EN-US"}

[Rule 1:]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Redirect]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    VLAN           : Any]{lang="EN-US"}

[    Protocol       : TCP]{lang="EN-US"}

[ Destination:]{lang="EN-US"}

[    Port           : 80]{lang="EN-US"}

[ ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_579415612}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x1892142911}[显示接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向过滤规则。]{style="font-family:宋体"}

[[\<Sysname\> display web-redirect rule interface vlan-interface 100]{lang="EN-US"}]{#struct_0_17060_20103_580070972}

[IPv4 ]{lang="EN-US"}[web-redirect]{lang="EN-US"}[ rules on vlan-interface 100:]{lang="EN-US"}

[Rule 1:]{lang="EN-US"}

[ Type                : Dynamic]{lang="EN-US"}

[ Action              : Permit]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    IP             : 192.168.2.114]{lang="EN-US"}

[    VLAN           : Any]{lang="EN-US"}

[ ]{lang="EN-US"}

[Rule 2:]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Redirect]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    VLAN           : Any]{lang="EN-US"}

[    Protocol       : TCP]{lang="EN-US"}

[ Destination:]{lang="EN-US"}

[    Port           : 80]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPv6 ]{lang="EN-US"}[web-redirect]{lang="EN-US"}[ rules on vlan-interface 100:]{lang="EN-US"}

[Rule 1:]{lang="EN-US"}

[ Type                : Static]{lang="EN-US"}

[ Action              : Redirect]{lang="EN-US"}

[ Status              : Active]{lang="EN-US"}

[ Source:]{lang="EN-US"}

[    VLAN           : Any]{lang="EN-US"}

[    Protocol       : TCP]{lang="EN-US"}

[ Destination:]{lang="EN-US"}

[    Port           : 80]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display web-redirect rule]{lang="EN-US"}]{#struct_0_17060_20103_x65065726}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1182677895}[[字段]{style="font-family:黑体"}]{#struct_0_17060_20103_2145696158}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17060_20103_2145630622}

[[Rule]{lang="EN-US"}]{#struct_0_17060_20103_1144534933}

[[Web]{lang="EN-US"}]{#struct_0_17060_20103_2145827230}[重定向规则编号]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_17060_20103_2145761694}

[[Web]{lang="EN-US"}]{#struct_0_17060_20103_2145434014}[重定向规则的类型，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DE" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="DE"}]{#struct_0_17060_20103_1967285614}[：静态类型。该类型的规则在]{style="font-family:宋体"}[Web]{lang="DE"}[重定向功能生效时生成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DE" style="font-size:10.0pt;font-family:Symbol"}[Dynamic]{lang="DE"}]{#struct_0_17060_20103_2145368478}[：动态类型。该类型的规则在用户访问重定向页面时生成]{style="font-family:宋体"}

[[Action]{lang="EN-US"}]{#struct_0_17060_20103_2145565086}

[[Web]{lang="EN-US"}]{#struct_0_17060_20103_2145499550}[重定向规则的匹配动作，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_17060_20103_1487163721}[：允许报文通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Redirect]{lang="EN-US"}]{#struct_0_17060_20103_2146220446}[：重定向报文]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_17060_20103_2145827229}

[[Web]{lang="EN-US"}]{#struct_0_17060_20103_2145761693}[重定向]{style="font-family:宋体"}[规则下发的状态，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="ES-AR" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="ES-AR"}]{#struct_0_17060_20103_x423515192}[：表示规则已生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="ES-AR" style="font-size:10.0pt;font-family:Symbol"}[Deactive]{lang="ES-AR"}]{#struct_0_17060_20103_2145434013}[：表示规则未生效]{lang="EN-US" style="font-family:宋体"}

[[Source]{lang="EN-US"}]{#struct_0_17060_20103_2145368477}

[[Web]{lang="EN-US"}]{#struct_0_17060_20103_2145565085}[重定向规则的源信息]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_17060_20103_398973343}

[[源]{style="font-family:宋体"}]{#struct_0_17060_20103_2145499549}[IP]{lang="ES-AR"}[地址]{style="font-family:宋体"}

[[Mask]{lang="EN-US"}]{#struct_0_17060_20103_2146220445}

[[源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_17060_20103_2146154909}[地址子网掩码]{style="font-family:宋体"}

[[Prefix length]{lang="EN-US"}]{#struct_0_17060_20103_2145696156}

[[源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_17060_20103_x1555661830}[地址前缀]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_17060_20103_2145630620}

[[源]{style="font-family:宋体"}]{#struct_0_17060_20103_2145827228}[VLAN]{lang="ES-AR"}[，如果未指定，显示为]{style="font-family:宋体"}[Any]{lang="ES-AR"}

[[Protocol]{lang="EN-US"}]{#struct_0_17060_20103_2145761692}

[[Web]{lang="EN-US"}]{#struct_0_17060_20103_2145434012}[重定向规则的传输层协议类型，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Any]{lang="EN-US"}]{#struct_0_17060_20103_x1389762769}[：不限制传输层协议类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="ES-AR" style="font-size:10.0pt;font-family:Symbol"}[TCP]{lang="EN-US"}]{#struct_0_17060_20103_x1389697233}[：]{style="font-family:宋体"}[TCP]{lang="EN-US"}[传输类型]{style="font-family:宋体"}

[[Destination]{lang="EN-US"}]{#struct_0_17060_20103_2145368476}

[[Web]{lang="EN-US"}]{#struct_0_17060_20103_2145565084}[重定向规则的目的信息]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_17060_20103_398907807}

[[目的传输层端口号，默认为]{style="font-family:宋体"}[80]{lang="EN-US"}]{#struct_0_17060_20103_2145499548}

[ ]{lang="EN-US"}

::: {#-839206969 .myid}
[]{#_Toc404792732}[]{#struct_0_17060_20103_x562596210}[]{#_Toc330201675}

**Portal \-- Portal配置命令 \-- ip**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**]{#struct_0_17060_20103_x2065703739}[命令用来指定]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ip]{lang="EN-US"}**]{#struct_0_17060_20103_1537682565}[命令用来删除指定的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x396034552}

[**[ip]{lang="EN-US"}***[ ipv4-address]{lang="EN-US"}*[ \[ **vpn-instance** *vpn-instance-name* \] \[ **key** {]{lang="EN-US"}]{#struct_0_17060_20103_591984552}[ ]{lang="EN-US"}**[cipher]{lang="DE"}**[ \| **simple**]{lang="DE"}[ ]{lang="DE"}[}]{lang="FR"}[ ]{lang="FR"}*[key-string]{lang="EN-US"}*[ \]]{lang="EN-US"}

[**[undo ip]{lang="EN-US"}**]{#struct_0_17060_20103_x1603369210}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_1801565272}

[[没有指定]{style="font-family:宋体"}]{#struct_0_17060_20103_1865116233}[Portal]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_17060_20103_4919118}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x802317924}[认证服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_629886676}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x1671551644}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_x121254790}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1020187071}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_17060_20103_x1602910458}[：]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**]{#struct_0_17060_20103_x232369166}*[ vpn-instance-name]{lang="EN-US"}*[：]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器位于公网中。]{style="font-family:宋体"}

[**[key]{lang="EN-US"}**]{#struct_0_17060_20103_562500213}[：与]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器通信时使用的共享密钥。设备与]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器交互的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文中会携带一个在该共享密钥参与下生成的验证字，该验证字用于接受方校验收到的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文的正确性。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_17060_20103_x1115419628}[：表示以密文方式设置共享密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_17060_20103_51014318}[：表示以明文方式设置共享密钥。]{style="font-family:宋体"}

[*[key-string]{lang="EN-US"}*]{#struct_0_17060_20103_x1602975994}[：设置的明文密钥或密文密钥，区分大小写。明文密钥为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串；密文密钥为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_579495859}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_17060_20103_1648468416}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[对应一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，因此一个]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器视图下只允许存在一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，后配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址（无论]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[）会覆盖已配置的。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同的]{style="font-family:宋体"}]{#struct_0_17060_20103_x532223958}[Portal]{lang="EN-US"}[认证服务器不允许]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的配置都相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_17060_20103_x504277368}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_1053970058}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1231168495}[指定]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[pts]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.111]{lang="EN-US"}[、共享密钥为明文]{style="font-family:宋体"}[portal]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x1603041530}

[\[Sysname\] portal server pts]{lang="EN-US"}

[\[Sysname-portal-server-pts\] ip 192.168.0.111 key simple portal]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1035004485}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal server]{lang="EN-US"}**]{#struct_0_17060_20103_235029159}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[portal server]{lang="EN-US"}**]{#struct_0_17060_20103_x1336171588}
:::

::: {#-488313789 .myid}
[]{#_Toc404792733}[]{#struct_0_17060_20103_x1215862320}[]{#_Toc330201676}

**Portal \-- Portal配置命令 \-- ipv6**

------------------------------------------------------------------------

[**[ipv6]{lang="EN-US"}**]{#struct_0_17060_20103_x1008231117}[命令用来指定]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ipv6]{lang="EN-US"}**]{#struct_0_17060_20103_x248362688}[命令用来删除指定的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_2129930175}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address* \[ **vpn-instance** *vpn-instance-name*\] \[ **key** {]{lang="EN-US"}]{#struct_0_17060_20103_x1603107066}[ ]{lang="EN-US"}**[cipher]{lang="DE"}***[ \| ]{lang="DE"}***[simple]{lang="DE"}***[ ]{lang="DE"}*[}]{lang="FR"}[ ]{lang="FR"}*[key-string]{lang="EN-US"}*[ \]]{lang="EN-US"}

[**[undo ipv6]{lang="EN-US"}**]{#struct_0_17060_20103_x735071350}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_750284048}

[[没有指定]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1532097693}[认证服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_1627063242}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x441413196}[认证服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1385784134}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x323648982}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_663463546}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_592031590}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_17060_20103_x1602648314}[：]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_17060_20103_x89778288}[：]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器位于公网中。]{style="font-family:宋体"}

[**[key]{lang="EN-US"}**]{#struct_0_17060_20103_1487551770}[：与]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器通信需要的共享密钥。设备与]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器交互的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文中会携带一个在该共享密钥参与下生成的验证字，该验证字用于接受方校验收到的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文的正确性。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_17060_20103_x1734481051}[：表示以密文方式设置共享密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_17060_20103_1852180499}[：表示以明文方式设置共享密钥。]{style="font-family:宋体"}

[*[key-string]{lang="EN-US"}*]{#struct_0_17060_20103_x1602713850}[：设置的明文密钥或密文密钥，区分大小写。明文密钥为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串；密文密钥为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_270203078}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_17060_20103_1031018352}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[对应一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，因此一个]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器视图下只允许存在一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，后配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址（无论]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[）会覆盖已配置的。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同的]{style="font-family:宋体"}]{#struct_0_17060_20103_x341788170}[Portal]{lang="EN-US"}[认证服务器不允许]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的配置都相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_17060_20103_1616623176}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x415455476}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_319141702}[指定]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[pts]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2000::1]{lang="EN-US"}[、共享密钥为明文]{style="font-family:宋体"}[portal]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x1979398840}

[\[Sysname\] portal server pts]{lang="EN-US"}

[\[Sysname-portal-server-pts\] ipv6 2000::1 key simple portal]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1010684853}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal server]{lang="EN-US"}**]{#struct_0_17060_20103_1852592666}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[portal server]{lang="EN-US"}**]{#struct_0_17060_20103_x564511950}
:::

::: {#1212291552 .myid}
[]{#_Toc404792734}[]{#struct_0_17060_20103_x2115267134}[]{#_Toc330201677}[]{#_Toc326065042}

**Portal \-- Portal配置命令 \-- port**

------------------------------------------------------------------------

[**[port]{lang="EN-US"}**]{#struct_0_17060_20103_319076166}[命令用来配置接入设备主动向]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器发送]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文时使用的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[**[undo port]{lang="EN-US"}**]{#struct_0_17060_20103_x780411979}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_608090507}

[**[port]{lang="EN-US"}**[ *port-id* ]{lang="EN-US"}]{#struct_0_17060_20103_x1529831012}

[**[undo port]{lang="EN-US"}**]{#struct_0_17060_20103_452717208}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_1434781625}

[[接入设备主动发送]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_319010630}[报文时使用的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[50100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_1923955010}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_908449001}[认证服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1768909675}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_1143406950}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_965445547}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_318945094}

[*[port-id]{lang="EN-US"}*]{#struct_0_17060_20103_x1133809800}[：设备向]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器主动发送]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文时使用的目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_1237034709}

[[本命令配置的端口号要和]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_406340271}[认证服务器上配置的监听]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文的端口号保持一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1137301372}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_319403846}[配置设备向]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[pts]{lang="EN-US"}[主动发送]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文时使用的目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[50000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x248992947}

[\[Sysname\] portal server pts]{lang="EN-US"}

[\[Sysname-portal-server-pts\] port 50000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1460328327}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal server]{lang="EN-US"}**]{#struct_0_17060_20103_613371902}
:::

::: {#-59299885 .myid}
[]{#_Toc404792735}[]{#struct_0_17060_20103_x1059772722}

**Portal \-- Portal配置命令 \-- portal { bas-ip \| bas-ipv6 }**

------------------------------------------------------------------------

[**[portal ]{lang="EN-US"}**[{ ]{lang="EN-US"}]{#struct_0_17060_20103_319338310}**[bas-ip ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[bas-ipv6]{lang="PT-BR"}**[ }]{lang="EN-US"}[命令用来设置发送给]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[BAS-IP]{lang="EN-US"}[或]{style="font-family:宋体"}[BAS-IPv6]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[**[undo portal ]{lang="EN-US"}**[{ ]{lang="EN-US"}]{#struct_0_17060_20103_x2096041479}**[bas-ip ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[bas-ipv6]{lang="PT-BR"}**[ }]{lang="EN-US"}[命令用来删除接口下指定的]{style="font-family:宋体"}[BAS-IP]{lang="EN-US"}[或]{style="font-family:宋体"}[BAS-IPv6]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x429808302}

[**[portal]{lang="PT-BR"}**[ { ]{lang="EN-US"}]{#struct_0_17060_20103_x528046412}**[bas-ip ]{lang="PT-BR"}***[ipv4-address]{lang="PT-BR"}*[ \| ]{lang="EN-US"}**[bas-ipv6 ]{lang="PT-BR"}***[ipv6-address]{lang="PT-BR"}*[ }]{lang="EN-US"}

[**[undo portal ]{lang="PT-BR"}**[{]{lang="EN-US"}]{#struct_0_17060_20103_x1840572610}**[ bas-ip \| bas-ipv6]{lang="PT-BR"}**[ }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1668187610}

[[对于响应类报文]{style="font-family:宋体"}]{#struct_0_17060_20103_1093599226}[IPv4 Portal]{lang="PT-BR"}[报文中的]{style="font-family:宋体"}[BAS-IP]{lang="PT-BR"}[属性为报文的源]{style="font-family:宋体"}[IP]{lang="PT-BR"}[地址]{style="font-family:宋体"}[，]{style="font-family:宋体"}[IPv6 Portal]{lang="PT-BR"}[报文中的]{style="font-family:宋体"}[BAS-IPv6]{lang="PT-BR"}[属性为报文源]{style="font-family:宋体"}[IPv6]{lang="PT-BR"}[地址。]{style="font-family:宋体"}

[[对于通知类报文]{style="font-family:宋体"}]{#struct_0_17060_20103_877608597}[IPv4 Portal]{lang="PT-BR"}[报文中的]{style="font-family:宋体"}[BAS-IP]{lang="PT-BR"}[属性为出接口的]{style="font-family:宋体"}[IP]{lang="PT-BR"}[地址]{style="font-family:宋体"}[，]{style="font-family:宋体"}[IPv6 Portal]{lang="PT-BR"}[报文中的]{style="font-family:宋体"}[BAS-IPv6]{lang="PT-BR"}[属性为出接口的]{style="font-family:宋体"}[IPv6]{lang="PT-BR"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_319272774}

[[接口视图]{style="font-family:宋体"} ]{#struct_0_17060_20103_x532822803}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x113324980}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_62432432}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_718388887}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_944749085}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_17060_20103_1702846709}[：接口发送]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文的]{style="font-family:宋体"}[BAS-IP]{lang="EN-US"}[属性值，应该为本机的地址，不能为全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址、全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址、]{style="font-family:宋体"}[D]{lang="EN-US"}[类地址、]{style="font-family:宋体"}[E]{lang="EN-US"}[类地址和环回地址。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_17060_20103_x2099573737}[：接口发送]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文的]{style="font-family:宋体"}[BAS-IPv6]{lang="EN-US"}[属性值，应该为本机的地址，不能为多播地址、全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址、本地链路地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1300165151}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备上运行]{style="font-family:宋体"}]{#struct_0_17060_20103_319207238}[Portal]{lang="EN-US"}[协议]{style="font-family:宋体"}[2.0]{lang="EN-US"}[版本时，主动发送给]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的报文（例如强制用户下线报文）中必须携带]{style="font-family:宋体"}[BAS-IP]{lang="EN-US"}[属性。设备上运行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[协议]{style="font-family:宋体"}[3.0]{lang="EN-US"}[版本时，主动发送给]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器必须携带]{style="font-family:宋体"}[BAS-IP]{lang="EN-US"}[或者]{style="font-family:宋体"}[BAS-IPv6]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置此命令后，设备主动发送的通知类]{style="font-family:宋体"}]{#struct_0_17060_20103_624322301}[Portal]{lang="EN-US"}[报文，其源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为配置的]{style="font-family:宋体"}[BAS-IP]{lang="EN-US"}[，否则为]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文出接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上使能了二次地址分配认证方式的]{style="font-family:宋体"}]{#struct_0_17060_20103_319665990}[Portal]{lang="EN-US"}[认证时，如果]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器上指定的设备]{style="font-family:宋体"}[IP]{lang="EN-US"}[不是]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文出接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则必须通过本命令配置相应的]{style="font-family:宋体"}[BAS-IP]{lang="EN-US"}[或]{style="font-family:宋体"}[BAS-IPv6]{lang="EN-US"}[属性，使其值与]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器上指定的设备]{style="font-family:宋体"}[IP]{lang="EN-US"}[一致，否则]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户无法认证成功。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_17060_20103_319600454}[H3C iMC]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的情况下，如果]{style="font-family:宋体"}[Portal]{lang="EN-US"}[服务器上指定的设备]{style="font-family:宋体"}[IP]{lang="EN-US"}[不是设备上]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文出接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则使能了]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证的接口上必须配置]{style="font-family:宋体"}[BAS-IP]{lang="EN-US"}[或者]{style="font-family:宋体"}[BAS-IPv6]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_742138515}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_2009906221}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_319141703}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文的]{style="font-family:宋体"}[BAS-IP]{lang="EN-US"}[属性值为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x1979398841}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] portal bas-ip 2.2.2.2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_1718198502}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_319076167}[配置接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[发送]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文的]{style="font-family:宋体"}[BAS-IP]{lang="EN-US"}[属性值为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x780411978}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname--Vlan-interface100\] portal bas-ip 2.2.2.2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_608156043}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_2011978021}**[interface]{lang="EN-US"}**
:::

::: {#1894213305 .myid}
[]{#_Toc404792736}[]{#struct_0_17060_20103_1883806769}[]{#_Toc330201684}

**Portal \-- Portal配置命令 \-- portal apply web-server**

------------------------------------------------------------------------

[**[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_319010631}[\[ **ipv6** \] ]{lang="EN-US"}**[apply]{lang="EN-US"}**[ ]{lang="EN-US"}**[web-server]{lang="EN-US"}**[命令用来在接口上引用]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器，设备会将]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[请求报文重定向到该]{style="font-family:宋体"}[Web]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[**[undo portal]{lang="EN-US"}**[ \[ **ipv6** \] **apply web-server**]{lang="EN-US"}]{#struct_0_17060_20103_1923955011}[命令用来取消接口上引用的]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_908383465}

[**[portal]{lang="EN-US"}**[ \[ **ipv6** \] **apply** **web-server** *server-name* \[ **fail-permit** \]]{lang="EN-US"}]{#struct_0_17060_20103_1468229745}

[**[undo portal ]{lang="EN-US"}**[\[ **ipv6** \] **apply** **web-server**]{lang="EN-US"}]{#struct_0_17060_20103_x1011801131}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_318945095}

[[接口上没有引用任何]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_x1133809801}[服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x329049232}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17060_20103_186391016}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_2116440743}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_534051108}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_1260955594}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_787388853}

[**[ipv6]{lang="EN-US"}**]{#struct_0_17060_20103_x450988114}[：表示]{style="font-family:宋体"}[IPv6 Portal Web]{lang="EN-US"}[服务器。若不指定该参数，则表示]{style="font-family:宋体"}[IPv4 Portal Web]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[*[server-name]{lang="EN-US"}*]{#struct_0_17060_20103_x1715562553}[：被引用的]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写，且必须已经存在。]{style="font-family:宋体"}

[**[fail-permit]{lang="EN-US"}**]{#struct_0_17060_20103_319403847}[：开启]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器不可达时的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户逃生功能，即设备探测到]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器不可达时取消接口的控制功能，允许用户不经过]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证即可自由访问网络。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x248992948}

[[一个接口上可以同时使能]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1460000647}[认证和]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[认证，因此也可以同时引用一个]{style="font-family:宋体"}[IPv4 Portal Web]{lang="EN-US"}[服务器和一个]{style="font-family:宋体"}[IPv6 Portal Web]{lang="EN-US"}[认证服务器。]{style="font-family:宋体"}

[[如果接口上同时开启了]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1231719813}[认证服务器逃生功能和]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器逃生功能，则当任意一个服务器不可达时，即放开接口控制，当两个服务器均恢复可达性后，再重新启动]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_1508328696}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x425342757}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_186182194}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上引用名称为]{style="font-family:宋体"}[wbs]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器作为用户认证时使用的]{style="font-family:宋体"}[Web]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x1253259421}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] portal apply web-server wbs]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x323896389}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_319338311}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上引用名称为]{style="font-family:宋体"}[wbs]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器作为用户认证时使用的]{style="font-family:宋体"}[Web]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x2096041478}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname--Vlan-interface100\] portal apply web-server wbs]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1995892243}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display portal interface]{lang="EN-US"}**]{#struct_0_17060_20103_x1960760387}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal fail-permit server]{lang="EN-US"}**]{#struct_0_17060_20103_581262635}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal web-server]{lang="EN-US"}**]{#struct_0_17060_20103_1109384736}
:::

::: {#863179697 .myid}
[]{#_Toc404792737}[]{#struct_0_17060_20103_2145827234}[]{#_Toc371518616}[]{#_Toc365963516}

**Portal \-- Portal配置命令 \-- portal authorization strict-checking**

------------------------------------------------------------------------

[**[portal authorization strict-checking]{lang="EN-US"}**]{#struct_0_17060_20103_2145761698}[命令用来开启]{style="font-family:宋体"}[Portal]{lang="EN-US"}[授权信息的严格检查模式。]{style="font-family:宋体"}

[**[undo authorizatio strict-checking]{lang="EN-US"}**]{#struct_0_17060_20103_x424236088}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1746331784}

[**[portal authorization]{lang="EN-US"}**[ { **acl** \| **user-profile** } **strict-checking**]{lang="EN-US"}]{#struct_0_17060_20103_2145434018}

[**[undo portal authorization ]{lang="EN-US"}**[{ **acl** \| **user-profile** } **strict-checking**]{lang="EN-US"}]{#struct_0_17060_20103_1966499182}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_2145368482}

[[缺省为非严格检查授权信息模式，当服务器下发的授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_17060_20103_1116396434}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[在设备上不存在或者设备下发]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[失败时，用户保持在线。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_2145565090}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17060_20103_398645662}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_2145499554}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_1487425865}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_1299889651}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_2146220450}

[**[acl]{lang="EN-US"}**]{#struct_0_17060_20103_252458768}[：表示开启对授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的严格检查。]{style="font-family:宋体"}

[**[user-profile]{lang="EN-US"}**]{#struct_0_17060_20103_2146154914}[：表示开启对授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的严格检查。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x2048105337}

[[接口上开启]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_2145696161}[授权信息的严格检查模式后**，**当服务器给用户下发的授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[在设备上不存在或者设备下发]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[失败时，设备将强制该用户下线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_1443596117}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_2145630625}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1144862613}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启对]{style="font-family:宋体"}[授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的严格检查模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_2145827233}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname--]{lang="EN-US"}[GigabitEthernet1/0/1]{lang="EN-US"}[\] ]{lang="EN-US"}[portal authoriztion acl strict-checking]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x372969655}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_2145761697}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上开启对]{style="font-family:宋体"}[授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的严格检查模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x423253048}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] portal authoriztion acl strict-checking]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_2145434017}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display portal interface]{lang="EN-US"}**]{#struct_0_17060_20103_1967089006}
:::

::: {#-713601002 .myid}
[]{#_Toc404792738}[]{#struct_0_17060_20103_1017640572}[]{#_Toc330201700}

**Portal \-- Portal配置命令 \-- portal delete-user**

------------------------------------------------------------------------

[**[portal delete-user]{lang="EN-US"}**]{#struct_0_17060_20103_x766245668}[命令用来强制]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户下线。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_671311778}

[**[portal delete-user ]{lang="EN-US"}**[{ *ipv4-address* \| **all** \| **interface** *interface-type interface-number* \| **ipv6** *ipv6-address* }]{lang="EN-US"}]{#struct_0_17060_20103_1939561441}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_319272775}

[[系统视图]{style="font-family:宋体"} ]{#struct_0_17060_20103_x532822802}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x113390516}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_3265085}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_x956921132}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_897089106}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_17060_20103_1781586687}[：]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_17060_20103_x1342480372}[：所有接口下的]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[用户和]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_17060_20103_x528770963}[：指定接口下的所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户，包括]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[用户和]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[用户。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:
宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_17060_20103_319207239}[：指定]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[用户的]{style="font-family:宋体"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_319665991}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1616525049}[强制]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户下线。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_735142478}

[\[Sysname\] portal delete-user 1.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x133744589}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display portal user]{lang="EN-US"}**]{#struct_0_17060_20103_1705513042}
:::

::: {#-700503352 .myid}
[]{#_Toc404792739}[]{#struct_0_17060_20103_1695723175}[]{#_Toc330201696}[]{#_Toc320893874}[]{#_Toc309735128}[]{#_Toc262736221}

**Portal \-- Portal配置命令 \-- portal domain**

------------------------------------------------------------------------

[**[portal ]{lang="EN-US"}**[\[ **ipv6** \]]{lang="EN-US"}]{#struct_0_17060_20103_319600455}[ ]{lang="EN-US"}**[domain]{lang="EN-US"}**[命令用于指定]{style="font-family:
宋体"}[Portal]{lang="EN-US"}[用户使用的认证域，使得所有从该接口上接入的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户强制使用该认证域。]{style="font-family:宋体"}

[**[undo portal]{lang="EN-US"}**]{#struct_0_17060_20103_742138514}[ ]{lang="EN-US"}[\[ **ipv6** \]]{lang="EN-US"}[ ]{lang="EN-US"}**[domain]{lang="EN-US"}**[命令用来删除指定的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户使用的认证域。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_319141700}

[**[portal]{lang="FR"}**]{#struct_0_17060_20103_x1979398838}[ ]{lang="FR"}[\[ **ipv6** \]]{lang="EN-US"}[ ]{lang="EN-US"}**[domain]{lang="FR"}**[ *domain-name*]{lang="FR"}

[**[undo portal]{lang="FR"}**]{#struct_0_17060_20103_x654913245}[ \[ **ipv6** \] **domain**]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_319919384}

[[未指定]{style="font-family:宋体"}]{#struct_0_17060_20103_x1391529409}[Portal]{lang="FR"}[用户使用的认证域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x783903466}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17060_20103_458215601}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1347531964}

[[network-admin]{lang="FR"}]{#struct_0_17060_20103_57194295}

[[mdc-admin]{lang="FR"}]{#struct_0_17060_20103_319076164}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x780411977}

[**[ipv6]{lang="FR"}**]{#struct_0_17060_20103_607697291}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv6 Portal]{lang="FR"}[用户使用的认证域。若不指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则表示指定]{style="font-family:宋体"}[IPv4 Portal]{lang="FR"}[用户使用的认证域。]{style="font-family:宋体"}

[*[domain-name]{lang="EN-US"}*]{#struct_0_17060_20103_x1621950114}[：]{style="font-family:宋体"}[ISP]{lang="EN-US"}[认证域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_706435046}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上可以同时指定]{lang="EN-US" style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}]{#struct_0_17060_20103_x101828121}[用户和]{lang="EN-US" style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[用户的认证域。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_17060_20103_319010628}**[ipv6]{lang="FR"}**[参数，则表示配置或者删除]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[用户使用的认证域。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x414697158}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_1762346877}[应用]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_188223377}[指定从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上接入的]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[用户使用认证域为]{style="font-family:宋体"}[my-domain]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_318945092}

[\[Sysname\] interface]{lang="EN-US"}[ gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname--]{lang="EN-US"}[GigabitEthernet1/0/1]{lang="EN-US"}[\] portal domain my-domain]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_17060_20103_x1133809806}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_2043603763}[指定从接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上接入的]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[用户使用认证域为]{style="font-family:宋体"}[my-domain]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x448740610}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname--Vlan-interface100\] portal domain my-domain]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1132523150}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_717985429}**[interface]{lang="EN-US"}**
:::

::: {#-1215771167 .myid}
[]{#struct_0_17060_20103_286191340}[]{#_Toc320893879}[]{#_Toc404792740}[]{#_Toc330201683}

**Portal \-- Portal配置命令 \-- portal enable**

------------------------------------------------------------------------

[**[portal]{lang="EN-US"}**[ \[ **ipv6** \] **enable**]{lang="EN-US"}]{#struct_0_17060_20103_x1275616301}[命令用来在接口上使能]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证，并指定认证方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **portal** \[ **ipv6** \] **enable**]{lang="EN-US"}]{#struct_0_17060_20103_x1052189724}[命令用来在指定接口上取消指定的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_319403844}

[**[portal]{lang="EN-US"}**[ **enable** **method** { **direct** \| **layer3** \| **redhcp** }]{lang="EN-US"}]{#struct_0_17060_20103_x248992945}

[**[portal]{lang="EN-US"}**[ **ipv6 enable** **method** { **direct** \| **layer3** }]{lang="EN-US"}]{#struct_0_17060_20103_x1460197255}

[**[undo]{lang="EN-US"}**[ **portal** \[ **ipv6** \] **enable**]{lang="EN-US"}]{#struct_0_17060_20103_442525884}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x959134725}

[[接口上没有使能]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1919885208}[认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1069522450}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17060_20103_x1207434343}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x883656827}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_319338308}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_242610689}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_1289764303}

[**[ipv6]{lang="EN-US"}**]{#struct_0_17060_20103_121260413}[：表示]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[认证。若不指定该参数，则表示]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[**[method]{lang="EN-US"}**]{#struct_0_17060_20103_1249695564}[：认证方式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[direct]{lang="EN-US"}**]{#struct_0_17060_20103_x1786518083}[：直接认证方式。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[layer3]{lang="EN-US"}**]{#struct_0_17060_20103_319272772}[：]{lang="EN-US" style="font-family:宋体"}[可跨]{style="font-family:宋体"}[三层认证方式。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[redhcp]{lang="EN-US"}**]{#struct_0_17060_20103_x532822809}[：二次地址分配认证方式。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x113980340}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使能]{lang="EN-US" style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1137782018}[功能之前，需要保证设备支持]{lang="EN-US" style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发功能。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 Portal]{lang="EN-US"}]{#struct_0_17060_20103_319207236}[认证不支持二次地址分配方式。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为保证以太网接口上的]{lang="EN-US" style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_624322287}[功能生效，请不要将使能]{lang="EN-US" style="font-family:宋体"}[Portal]{lang="EN-US"}[功能的以太网接口加入聚合组。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[允许在接口上同时使能]{lang="EN-US" style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}]{#struct_0_17060_20103_1402944732}[认证和]{lang="EN-US" style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[认证。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_319665988}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x722127118}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x1592030152}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[Portal]{lang="EN-US"}[认证，且指定为直接认证方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x537925232}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] portal enable method direct]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_430873585}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x1512286634}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[认证，且指定为直接认证方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x202665898}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname--Vlan-interface100\] portal enable method direct]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1194051406}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display portal interface]{lang="EN-US"}**]{#struct_0_17060_20103_319600452}
:::

::: {#-1546918298 .myid}
[]{#_Toc404792741}[]{#struct_0_17060_20103_742138517}[]{#_Toc330201688}

**Portal \-- Portal配置命令 \-- portal fail-permit server**

------------------------------------------------------------------------

[**[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_2009906219}[\[ **ipv6** \] **fail-permit** **server**]{lang="EN-US"}[命令用来开启]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器不可达时的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户逃生功能，即设备探测到]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器不可达时取消接口的控制功能，允许用户不经过]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证即可自由访问网络。]{style="font-family:宋体"}

[**[u]{lang="EN-US"}**]{#struct_0_17060_20103_x1110442155}**[ndo ]{lang="EN-US"}[portal]{lang="EN-US"}**[ \[ **ipv6**\] **fail-permit server**]{lang="EN-US"}[命令用来]{style="font-family:宋体"}[关闭指定的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器逃生功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x279245508}

[**[portal]{lang="EN-US"}**]{#struct_0_17060_20103_x1560518738}[ \[ **ipv6** \] ]{lang="EN-US"}**[fail-permit]{lang="EN-US"}[ server]{lang="EN-US"}[ ]{lang="EN-US"}***[server-name]{lang="EN-US"}*

[**[undo portal]{lang="EN-US"}**[ \[ **ipv6**\] **fail-permit server**]{lang="EN-US"}]{#struct_0_17060_20103_319141701}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1979398839}

[[设备探测到]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_2073970110}[认证服务器不可达时，不允许]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户逃生]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1390336196}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17060_20103_245276508}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_319076165}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x780411976}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_607762827}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_752841087}

[**[ipv6]{lang="EN-US"}**]{#struct_0_17060_20103_1602427248}[：表示]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[认证服务器。若不指定该参数，则表示]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[认证服务器。]{style="font-family:宋体"}

[*[server-name]{lang="EN-US"}*]{#struct_0_17060_20103_x721977038}[：]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_866553122}

[[如果接口上同时开启了]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_319010629}[认证服务器逃生功能和]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器逃生功能，则当任意一个服务器不可达时，立即放开接口控制；当两个服务器均恢复可达后，再重新启动接口的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证功能。重新启动接口的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证功能之后，未通过认证的用户需要通过认证之后才能访问网络资源，已通过认证的用户可继续访问网络资源。]{style="font-family:宋体"}

[[一个接口上，最多同时可以开启一个]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x414697157}[认证服务器逃生功能和一个]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器逃生功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_1762281341}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x590362452}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_318945093}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上启用]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[pts1]{lang="EN-US"}[不可达时的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户逃生功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x1133809807}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ]{lang="EN-US"}[portal ]{lang="EN-US"}[fail-permit]{lang="EN-US"}[ server pts1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_477519822}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_319403845}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上启用]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[ pts1]{lang="EN-US"}[不可达时的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户逃生功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x248992946}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname--Vlan-interface100\] portal ]{lang="EN-US"}[fail-permit]{lang="EN-US"}[ server pts1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1460393863}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_1788914960}**[interface]{lang="EN-US"}**
:::

::: {#-1150849115 .myid}
[]{#struct_0_17060_20103_369510588}[]{#_Toc404792742}[]{#_Toc330201694}[]{#_Toc326655115}

**Portal \-- Portal配置命令 \-- portal free-all except destination**

------------------------------------------------------------------------

[**[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_319338309}**[free-all except destination]{lang="EN-US"}**[命令用来配置]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[目的认证网段。]{style="font-family:宋体"}

[**[undo portal ]{lang="EN-US"}**]{#struct_0_17060_20103_319272773}**[free-all except destination]{lang="EN-US"}**[命令用来删除配置的]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[目的认证网段。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x532822808}

[**[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_x114045876}**[free-all except destination]{lang="EN-US"}**[ *ipv4-network-address* { *mask-length* \| *mask* }]{lang="EN-US"}

[**[undo portal ]{lang="EN-US"}**]{#struct_0_17060_20103_x857395321}**[free-all except destination]{lang="EN-US"}**[ \[ *ipv4-network-address* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1180128477}

[[没有配置]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}]{#struct_0_17060_20103_319207237}[目的网段认证，表示对访问任意目的网段的用户都进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_624322286}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17060_20103_1402944731}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x567610066}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x306830969}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_704442852}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1417425342}

[*[ipv4-network-address]{lang="EN-US"}*]{#struct_0_17060_20103_319665989}[：]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[认证网段地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_17060_20103_x722127119}[：子网掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_17060_20103_x1591964616}[：子网掩码，点分十进制格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_1842195193}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上仅要求]{style="font-family:宋体"}]{#struct_0_17060_20103_x1876040225}[Portal]{lang="EN-US"}[用户访问指定目的认证网段（除免认证规则中指定的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或网段）时才需要进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证，访问其它网段访问时不需要进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以通过多次执行本命令，配置多条目的认证网段。]{style="font-family:宋体"}]{#struct_0_17060_20103_330327465}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_17060_20103_319600453}**[undo]{lang="EN-US"}**[命令中不携带]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址参数，则表示删除所有制定的]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[目的认证网段。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[目的网段认证对二次地址分配认证方式的]{style="font-family:宋体"}]{#struct_0_17060_20103_319141698}[Portal]{lang="EN-US"}[认证不生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口上同时配置了源认证网段和目的认证网段，则源认证网段配置不会生效。]{style="font-family:宋体"}]{#struct_0_17060_20103_1176451549}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_864993252}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_679310673}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_319076162}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[Portal]{lang="EN-US"}[目的认证网段为]{style="font-family:宋体"}[11.11.11.0/24]{lang="EN-US"}[，仅允许访问]{style="font-family:宋体"}[11.11.11.0/24]{lang="EN-US"}[网段的用户触发]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证，其它目的网段可以直接访问。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x780411983}

[\[Sysname\] interface ]{lang="EN-US"}[gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname--]{lang="EN-US"}[GigabitEthernet1/0/1]{lang="EN-US"}[\] portal free-all except destination 11.11.11.0 24]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_607435148}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_318945090}[在接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[Portal]{lang="EN-US"}[目的认证网段为]{style="font-family:宋体"}[11.11.11.0/24]{lang="EN-US"}[，仅允许访问]{style="font-family:宋体"}[11.11.11.0/24]{lang="EN-US"}[网段的用户触发]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证，其它目的网段可以直接访问。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x1133809804}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname--Vlan-interface2\] portal free-all except destination 11.11.11.0 24]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1088564119}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_781770569}**[interface]{lang="EN-US"}**
:::

::: {#449936703 .myid}
[]{#_Toc404792743}[]{#struct_0_17060_20103_1294157988}[]{#_Toc330201681}

**Portal \-- Portal配置命令 \-- portal free-rule**

------------------------------------------------------------------------

[**[portal free-rule]{lang="EN-US"}**]{#struct_0_17060_20103_x1356346079}[命令用来配置基于]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[免认证规则。]{style="font-family:宋体"}

[**[undo portal free-rule]{lang="EN-US"}**]{#struct_0_17060_20103_x315081966}[命令用来删除指定的或所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[免认证规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x593273572}

[**[portal free-rule]{lang="EN-US"}**[ *rule-number* { **destination** **ip** { *ip-address* { *mask-length* \| *mask* } \| **any** } \[ **tcp** *tcp-port-number* \| **udp** *udp-port-number* \] \| **source** **ip** { *ip-address* { *mask-length* \| *mask* } \| **any** } \[ **tcp** *tcp-port-number* \| **udp** *udp-port-number* \] } \* \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_17060_20103_319403842}

[**[portal free-rule]{lang="EN-US"}**]{#struct_0_17060_20103_x248992943}[ *rule-number* { **destination** **ipv6** { *ipv6-address* *prefix-length* ]{lang="EN-US"}[\| **any** ]{lang="EN-US"}[} \[ **tcp** *tcp-port-numbe*r \| **udp** *udp-port-number* \] \| **source** **ipv6** { *ipv6-address prefix-length* ]{lang="EN-US"}[\| **any**]{lang="EN-US"}[ } \[ **tcp** *tcp-port-number* \| **udp** *udp-port-number* \] } \* \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}

[**[undo portal free-rule ]{lang="EN-US"}**]{#struct_0_17060_20103_x1460590471}[{ *rule-number* \| **all** }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x954886582}

[[不存在基于]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17060_20103_647182195}[地址的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[免认证规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1899322388}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17060_20103_319338306}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_242610675}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_2009808323}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_39697211}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_789756011}

[*[rule-number]{lang="EN-US"}*]{#struct_0_17060_20103_x1247920507}[：免认证规则编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[destination]{lang="EN-US"}**]{#struct_0_17060_20103_319272770}[：指定目的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**]{#struct_0_17060_20103_x532822807}[：指定源信息。]{style="font-family:宋体"}

[**[ip ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_17060_20103_x113062836}[：免认证规则的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[{ *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_17060_20103_319207234}[：免认证规则的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码。其中，]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[为子网掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[；]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[为子网掩码，点分十进制格式。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_17060_20103_624322289}[：免认证规则的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_17060_20103_1402944738}[：免认证规则的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}[ ]{lang="EN-US"}**]{#struct_0_17060_20103_x568068818}**[any]{lang="EN-US"}**[：]{style="font-family:宋体"}[任意]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6 ]{lang="EN-US"}**]{#struct_0_17060_20103_699300744}**[any]{lang="EN-US"}**[：]{style="font-family:宋体"}[任意]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**[ *tcp-port-number*]{lang="EN-US"}]{#struct_0_17060_20103_x443043905}[：免认证规则的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[udp]{lang="EN-US"}**[ *udp-port-number*]{lang="EN-US"}]{#struct_0_17060_20103_1658100687}[：免认证规则的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_17060_20103_19866857}[：所有免认证规则。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_17060_20103_x931296182}[：免认证规则生效的三层接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1925730630}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以同时指定源和目的参数，或者仅指定其中一个参数，后者表示另外一个地址不受限制。]{style="font-family:宋体"}]{#struct_0_17060_20103_319141699}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果免认证规则中同时配置了源端口号和目的端口号，则要求源和目的端口号所属的传输层协议类型保持一致。]{style="font-family:宋体"}]{#struct_0_17060_20103_1176451548}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[相同内容的免认证规则不能重复配置，否则提示免认证规则已存在或重复。]{style="font-family:宋体"}]{#struct_0_17060_20103_865058788}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[未指定三层接口的情况下，免认证规则对所有使能]{style="font-family:宋体"}]{#struct_0_17060_20103_x1936131917}[Portal]{lang="EN-US"}[的接口生效；指定三层接口的情况下，免认证规则只对指定的三层接口生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_588516879}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x2028879488}[配置一条基于]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[免认证规则：编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[、源地址为]{style="font-family:宋体"}[10.10.10.1/24]{lang="EN-US"}[、目的地址为]{style="font-family:宋体"}[20.20.20.1]{lang="EN-US"}[、目的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[23]{lang="EN-US"}[、生效接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。该规则表示在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上，]{style="font-family:宋体"}[10.10.10.1/24]{lang="EN-US"}[网段地址的用户不需要经过]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证即可以访问地址为]{style="font-family:宋体"}[20.20.20.1]{lang="EN-US"}[的主机在]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口]{style="font-family:宋体"}[23]{lang="EN-US"}[上提供的服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x1371522836}

[\[Sysname\] portal free-rule 1 destination ip 20.20.20.1 32 tcp 23 source ip 10.10.10.1 24 interface gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x616619232}[配置一条基于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[免认证规则：编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[、源地址为]{style="font-family:宋体"}[2000::1/64]{lang="EN-US"}[、目的地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[、目的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[23]{lang="EN-US"}[、生效接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。该规则表示在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上，]{style="font-family:宋体"}[2000::1/64]{lang="EN-US"}[网段地址的用户不需要经过]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证即可以访问目的地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[的主机在]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口]{style="font-family:宋体"}[23]{lang="EN-US"}[上提供的服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_319076163}

[\[Sysname\] portal free-rule 2 destination ipv6 2001::1 128 tcp 23 source ip 2000::1 64 interface gigabitethernet 1/0/1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x780411982}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display portal rule]{lang="EN-US"}**]{#struct_0_17060_20103_607500684}
:::

::: {#-833357395 .myid}
[]{#_Toc404792744}[]{#struct_0_17060_20103_x1107963104}[]{#_Toc330201682}

**Portal \-- Portal配置命令 \-- portal free-rule source**

------------------------------------------------------------------------

[**[portal free-rule source]{lang="EN-US"}**]{#struct_0_17060_20103_319010627}[命令用来配置基于源的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[免认证规则，这里的源可以是源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、源接口或者源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo portal free-rule]{lang="EN-US"}**]{#struct_0_17060_20103_x414697143}[命令用来删除免认证规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1762019198}

[**[portal free-rule]{lang="EN-US"}**[ *rule-number* **source** { **interface** *interface-type interface-number* \| **mac** *mac-address* \| **vlan** *vlan-id* } \*]{lang="EN-US"}]{#struct_0_17060_20103_x1352129657}

[**[undo portal free-rule ]{lang="EN-US"}**[{ *rule-number* \| **all** }]{lang="EN-US"}]{#struct_0_17060_20103_318945091}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1133809805}

[[没有配置基于源的]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_1640319236}[免认证规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_1162042728}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17060_20103_1776565508}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1537830348}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x2086700953}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_1411191671}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1873440658}

[*[rule-number]{lang="EN-US"}*]{#struct_0_17060_20103_x81673505}[：免认证规则编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_17060_20103_319403843}[：免认证规则的源接口。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:
宋体"}

[**[mac ]{lang="EN-US"}***[mac-address]{lang="EN-US"}*]{#struct_0_17060_20103_x248992944}[：免认证规则的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[的形式。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_17060_20103_x1460262791}[：免认证规则的源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_17060_20103_651719788}[：所有免认证规则。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_1791253473}

[[如果免认证规则中同时指定了源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17060_20103_x1210713312}[和二层源接口*，*则要求该接口属于对应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，否则该规则无效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1573469097}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_319338307}[配置一条]{style="font-family:宋体"}[Portal]{lang="EN-US"}[免认证规则：编号为]{style="font-family:宋体"}[3]{lang="EN-US"}[、源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1-1-1]{lang="EN-US"}[、源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[。]{style="font-family:宋体"}[该规则表示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1-1-1]{lang="EN-US"}[，属于]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[的]{style="font-family:宋体"}[用户不需要经过]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证即可以访问网络资源。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_242610676}

[\[Sysname\] portal free-rule 3 source mac 1-1-1 vlan 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_2009808322}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display portal rule]{lang="EN-US"}**]{#struct_0_17060_20103_39762747}
:::

::: {#1101145356 .myid}
[]{#_Toc404792745}[]{#struct_0_17060_20103_213027168}[]{#_Toc371518624}[]{#_Toc365963510}

**Portal \-- Portal配置命令 \-- portal { ipv4-max-user \| ipv6-max-user }**

------------------------------------------------------------------------

[**[portal]{lang="EN-US"}**[ { **ipv4-max-user** \| **ipv6-max-user** }]{lang="EN-US"}]{#struct_0_17060_20103_675845061}[命令用来配置每个接口下最大]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户数。]{style="font-family:宋体"}

[**[undo portal]{lang="EN-US"}**[ { **ipv4-max-user** \| **ipv6-max-user** }]{lang="EN-US"}]{#struct_0_17060_20103_x203684186}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_212830560}

[**[portal]{lang="EN-US"}**[ { **ipv4-max-user** \| **ipv6-max-user** } *max-number*]{lang="EN-US"}]{#struct_0_17060_20103_x383006485}

[**[undo portal]{lang="EN-US"}**[ { **ipv4-max-user** \| **ipv6-max-user** }]{lang="EN-US"}]{#struct_0_17060_20103_212896096}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x70572528}

[[每个接口下最大]{style="font-family:宋体"}]{#struct_0_17060_20103_213223776}[Portal]{lang="EN-US"}[用户数不受限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1402164607}

[[接口视图]{style="font-family:宋体"} ]{#struct_0_17060_20103_213289312}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_1284144175}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_212699487}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_183194531}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_212765023}

[*[max-number]{lang="EN-US"}*]{#struct_0_17060_20103_153495456}[：每个接口下允许的最大]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[用户数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967296]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_1297564045}

[[如果接口上配置的]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_212568415}[最大用户数小于当前接口上已经在线的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户数，则该配置可以执行成功，且在线]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户不受影响]{style="font-family:宋体"}[，但系统将不允许新的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户从该接口接入。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x107719366}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_212633951}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1658273838}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[最大]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[用户数为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_212961631}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[GigabitEthernet1/0/1]{lang="EN-US"}[\] portal ipv4-max-user 100]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x1976549780}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_213027167}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[最大]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[用户数为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_212830559}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname--Vlan-interface100\] ]{lang="EN-US"}[portal ipv4-max-user 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1956984590}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display portal interface]{lang="EN-US"}**]{#struct_0_17060_20103_212896095}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal max-user]{lang="EN-US"}**]{#struct_0_17060_20103_x70572527}
:::

::: {#1487940487 .myid}
[]{#struct_0_17060_20103_1837365106}[]{#_Toc404792746}[]{#_Toc330201695}

**Portal \-- Portal配置命令 \-- portal ipv6 free-all except destination**

------------------------------------------------------------------------

[**[portal]{lang="EN-US"}**[ **ipv6** ]{lang="EN-US"}]{#struct_0_17060_20103_319207235}**[free-all except destination]{lang="EN-US"}**[命令用来配置]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[目的网段认证。]{style="font-family:宋体"}

[**[undo portal]{lang="EN-US"}**[ **ipv6** ]{lang="EN-US"}]{#struct_0_17060_20103_319665987}**[free-all except destination]{lang="EN-US"}**[命令用来删除配置的]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[目的认证网段。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x722127105}

[**[portal ipv6 ]{lang="EN-US"}**]{#struct_0_17060_20103_x1592226759}**[free-all except destination]{lang="EN-US"}**[ *ipv6-network-address* *prefix-length*]{lang="EN-US"}

[**[undo portal ipv6 ]{lang="EN-US"}**]{#struct_0_17060_20103_278102974}**[free-all except destination]{lang="EN-US"}**[ \[ *ipv6-network-address* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_1798978223}

[[没有配置]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}]{#struct_0_17060_20103_319600451}[目的网段认证，表示对访问任意]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[目的网段的用户都进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_742138518}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17060_20103_2009906224}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1109590188}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_1191076185}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_x1594867237}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_1885225643}

[*[ipv6-network-address]{lang="EN-US"}*]{#struct_0_17060_20103_1431092927}[：]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[Portal]{lang="EN-US"}[认证网段地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_17060_20103_x1749352877}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1216814543}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上仅要求]{style="font-family:宋体"}]{#struct_0_17060_20103_1885160107}[Portal]{lang="EN-US"}[用户访问指定目的认证网段（除免认证规则中指定的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或网段）时才需要进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证，访问其它网段访问时不需要进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以通过多次执行本命令，配置多条目的认证网段。]{style="font-family:宋体"}]{#struct_0_17060_20103_1474066259}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_17060_20103_x1023545172}**[undo]{lang="EN-US"}**[命令中不携带]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址参数，则表示删除所有制定的]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[目的认证网段。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[目的网段认证对二次地址分配认证方式的]{style="font-family:宋体"}]{#struct_0_17060_20103_1885094571}[Portal]{lang="EN-US"}[认证不生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口上同时配置了源认证网段和目的认证网段，则源认证网段配置不会生效。]{style="font-family:宋体"}]{#struct_0_17060_20103_304171491}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_2069260556}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_1971537670}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1885487787}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[Portal]{lang="EN-US"}[目的认证网段为]{style="font-family:宋体"}[1::2/16]{lang="EN-US"}[，仅要求访问]{style="font-family:宋体"}[1::2/16]{lang="EN-US"}[网段的用户必须进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x2048731961}

[\[Sysname\] interface ]{lang="EN-US"}[gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname--]{lang="EN-US"}[GigabitEthernet1/0/1]{lang="EN-US"}[\] portal ipv6 free-all except destination 1::2 16]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_1464742526}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1885422251}[在接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[Portal]{lang="EN-US"}[目的认证网段为]{style="font-family:宋体"}[1::2/16]{lang="EN-US"}[，仅要求访问]{style="font-family:宋体"}[1::2/16]{lang="EN-US"}[网段的用户必须进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_1885356715}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname--Vlan-interface2\] portal ipv6 free-all except destination ]{lang="EN-US"}[1::2 16]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x501980980}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_146665934}**[interface]{lang="EN-US"}**
:::

::: {#1600849000 .myid}
[]{#_Toc404792747}[]{#struct_0_17060_20103_x68213943}[]{#_Toc330201693}

**Portal \-- Portal配置命令 \-- portal ipv6 layer3 source**

------------------------------------------------------------------------

[**[portal]{lang="EN-US"}**[ **ipv6** ]{lang="EN-US"}]{#struct_0_17060_20103_1885291179}**[layer3]{lang="EN-US"}**[ **source**]{lang="EN-US"}[命令用来配置]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[源认证网段，即接口上只允许在源认证网段范围内的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[用户报文才能触发]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证，否则丢弃。]{style="font-family:宋体"}

[**[undo portal]{lang="EN-US"}**[ **ipv6** ]{lang="EN-US"}]{#struct_0_17060_20103_x57742256}**[layer3]{lang="EN-US"}**[ **source**]{lang="EN-US"}[命令用来删除配置的]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[源认证网段。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1885749931}

[**[portal ipv6 ]{lang="EN-US"}**]{#struct_0_17060_20103_x1973139753}**[layer3 source ]{lang="EN-US"}***[ipv6-network-address]{lang="EN-US"}[ prefix-length]{lang="EN-US"}*

[**[undo portal ipv6 ]{lang="EN-US"}**]{#struct_0_17060_20103_x2131445449}**[layer3]{lang="EN-US"}**[ **source** \[ *ipv6-network-address* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_1513789014}

[[没有配置]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}]{#struct_0_17060_20103_1885684395}[源认证网段，]{style="font-family:宋体"}[表示对来自任意网段的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[用户都进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x84391517}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17060_20103_x1492929571}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1842006329}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x575667421}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_x2021897787}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_869844375}

[*[ipv6-network-address]{lang="EN-US"}*]{#struct_0_17060_20103_1885225644}[：]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[Portal]{lang="EN-US"}[源]{style="font-family:
宋体"}[认证网段地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_17060_20103_1431289535}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x230210153}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_17060_20103_1885160108}**[undo]{lang="EN-US"}**[命令中不携带]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址参数，则表示删除指定所有的]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[源认证网段。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[源认证网段仅对]{style="font-family:宋体"}]{#struct_0_17060_20103_1885029036}[Portal]{lang="EN-US"}[的可跨三层认证方式（]{style="font-family:宋体"}**[layer3]{lang="EN-US"}**[）生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口上同时配置了源认证网段和目的网段认证，则源认证网段配置不会生效。]{style="font-family:宋体"}]{#struct_0_17060_20103_1897547574}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_719309984}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x482335304}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1885487788}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置一条]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[Portal]{lang="EN-US"}[源认证网段为]{style="font-family:宋体"}[1::1/16]{lang="EN-US"}[，仅允许来自]{style="font-family:宋体"}[1::1/16]{lang="EN-US"}[网段的用户触发]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x2049321785}

[\[Sysname\] interface ]{lang="EN-US"}[gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname--]{lang="EN-US"}[GigabitEthernet1/0/1]{lang="EN-US"}[\] portal ipv6 layer3 source 1::1 16]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_17060_20103_x73405234}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1885422252}[在接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上配置一条]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[Portal]{lang="EN-US"}[源认证网段为]{style="font-family:宋体"}[1::1/16]{lang="EN-US"}[，仅允许来自]{style="font-family:宋体"}[1::1/16]{lang="EN-US"}[网段的用户触发]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_1885356716}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname--Vlan-interface2\] portal ipv6 layer3 source 1::1 16]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x501915444}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_x268486455}**[interface]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal ipv6 ]{lang="EN-US"}**]{#struct_0_17060_20103_x1722098455}**[free-all except destination]{lang="EN-US"}**
:::

::: {#612653415 .myid}
[]{#_Toc320893873}[]{#_Toc309735126}[]{#_Toc262736219}[]{#_Toc404792748}[]{#struct_0_17060_20103_x1739976856}[]{#_Toc330201691}

**Portal \-- Portal配置命令 \-- portal ipv6 user-detect**

------------------------------------------------------------------------

[**[portal ]{lang="EN-US"}[ipv6 ]{lang="EN-US"}**]{#struct_0_17060_20103_1785219750}**[user-detect]{lang="EN-US"}**[命令用来开启]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[用户在线探测功能。]{style="font-family:宋体"}

[**[undo portal user-detect]{lang="EN-US"}**]{#struct_0_17060_20103_x429963397}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1282777193}

[**[portal ipv6 user-detect type]{lang="EN-US"}**[ { **icmpv6** \| **nd** } \[ **retry** *retries* \] \[ **interval** *interval* \] \[ **idle** *time* \]]{lang="EN-US"}]{#struct_0_17060_20103_x1184147760}

[**[undo portal ipv6 user-detect]{lang="EN-US"}**]{#struct_0_17060_20103_x1198799073}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_1885291180}

[[接口上的]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}]{#struct_0_17060_20103_x57283513}[用户在线探测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_1618436310}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17060_20103_558165463}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x50841186}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_318662146}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_1802101715}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_608213095}

[**[type]{lang="EN-US"}**]{#struct_0_17060_20103_x1214424689}[：指定探测类型。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmpv6]{lang="EN-US"}**]{#struct_0_17060_20103_x1973205289}[：表示探测类型为]{style="font-family:
宋体"}[ICMPv6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nd]{lang="EN-US"}**]{#struct_0_17060_20103_1619036312}[：表示探测类型为]{style="font-family:
宋体"}[ND]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[retry]{lang="EN-US"}**[ *retries*]{lang="EN-US"}]{#struct_0_17060_20103_x770277217}[：探测次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_17060_20103_x366720796}[：探测间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1200]{lang="EN-US"}[，单位为秒，缺省]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[idle ]{lang="EN-US"}**]{#struct_0_17060_20103_x1755635344}*[time]{lang="EN-US"}*[：用户在线探测闲置时长，即闲置多长时间后发起探测，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒，缺省]{style="font-family:宋体"}[180]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_821994522}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[根据探测类型的不同，设备有以下两种探测机制：]{style="font-family:宋体"}]{#struct_0_17060_20103_1885684396}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[当探测类型为]{style="font-family:宋体"}]{#struct_0_17060_20103_482787774}[ICMPv6]{lang="EN-US"}[时，若设备发现一定时间（]{style="font-family:宋体"}**[idle]{lang="EN-US"}***[ time]{lang="EN-US"}*[）内接口上未收到某]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的报文，则会向该用户定期（]{style="font-family:宋体"}**[interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}[）发送探测报文。如果在指定探测次数（]{style="font-family:宋体"}**[retry]{lang="EN-US"}**[ *retries*]{lang="EN-US"}[）之内，设备收到了该用户的响应报文，则认为用户在线，且停止发送探测报文，重复这个过程，否则，强制其下线。]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[当探测类型为]{style="font-family:宋体"}]{#struct_0_17060_20103_x672225066}[ND]{lang="EN-US"}[时，若设备发现一定时间（]{style="font-family:宋体"}**[idle]{lang="EN-US"}**[ *time*]{lang="EN-US"}[）内接口上未收到某]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的报文，则会向该用户发送]{style="font-family:宋体"}[ND]{lang="EN-US"}[请求报文。设备定期（]{style="font-family:宋体"}**[interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}[）检测用户]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项是否被刷新过，如果在指定探测次数（]{style="font-family:宋体"}**[retry]{lang="EN-US"}**[ *retries*]{lang="EN-US"}[）内用户]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项被刷新过，则认为用户在线，且停止检测用户]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项，重复这个过程，否则，强制其下线。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请根据配置的认证方式选择合适的探测方法，如果配置了直接方式或者二次地址分配方式，则可以使用]{style="font-family:宋体"}]{#struct_0_17060_20103_1885029033}[ND]{lang="EN-US"}[或]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[探测方式，如果配置了可跨三层认证方式，则可以使用]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[探测方式，若配置了]{style="font-family:宋体"}[ND]{lang="EN-US"}[探测方式，则探测功能不生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户接入设备上配置了阻止]{style="font-family:宋体"}]{#struct_0_17060_20103_1897219894}[ICMPv6]{lang="EN-US"}[报文的防火墙策略，则接口上的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[探测方式可能会失败，从而导致接口上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户非正常下线。因此，若接口上需要使用]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[探测方式，请保证用户接入设备不会过滤掉]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x449101965}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x1585871520}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_935441251}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[用户在线探测功能：探测类型为]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[，发送探测报文的次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次，发送间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，闲置时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x1982834434}

[\[Sysname\] interface ]{lang="EN-US"}[gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname--]{lang="EN-US"}[GigabitEthernet1/0/1]{lang="EN-US"}[\] portal ipv6 user-detect type icmpv6 retry 5 interval 10 idle 300]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_1784527083}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1498666151}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上开启]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[用户在线探测功能：探测类型为]{style="font-family:宋体"}[ND]{lang="EN-US"}[，检测用户]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项的探测次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次，探测间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，闲置时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_1885487785}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname--Vlan-interface100\] portal ipv6 user-detect type nd retry 5 interval 10 idle 300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x2048600889}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_2098188124}**[interface]{lang="EN-US"}**
:::

::: {#-213796570 .myid}
[]{#_Toc404792749}[]{#struct_0_17060_20103_x1910397199}[]{#_Toc330201692}[]{#_Toc320893872}[]{#_Toc309735123}[]{#_Toc262736216}[]{#_Toc323397486}[]{#_Toc323397487}[]{#_Toc323397488}

**Portal \-- Portal配置命令 \-- portal layer3 source**

------------------------------------------------------------------------

[**[portal]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17060_20103_1885422249}**[layer3]{lang="EN-US"}**[ **source**]{lang="EN-US"}[命令用来配置]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[源认证网段，即接口上只允许在源认证网段范围内的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[用户报文才能触发]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证，否则丢弃。]{style="font-family:宋体"}

[**[undo portal]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17060_20103_x1255502412}**[layer3]{lang="EN-US"}**[ **source**]{lang="EN-US"}[命令用来删除配置的]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[源认证网段。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1885356713}

[**[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_x502112052}**[layer3 source ]{lang="EN-US"}***[ipv4-network-address]{lang="EN-US"}*[ { *mask-length* \| *mask* }]{lang="EN-US"}

[**[undo portal ]{lang="EN-US"}**]{#struct_0_17060_20103_x1941960797}**[layer3 ]{lang="EN-US"}[source]{lang="EN-US"}**[ \[ *ipv4-network-address* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1244671455}

[[没有配置]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}]{#struct_0_17060_20103_1885291177}[源认证网段，]{style="font-family:宋体"}[表示对来自任意网段的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[用户都进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x57349040}

[[接口视图]{style="font-family:宋体"} ]{#struct_0_17060_20103_1210122878}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x2072568877}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x479309129}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_683141293}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x944250805}

[*[ipv4-network-address]{lang="EN-US"}*]{#struct_0_17060_20103_1885749929}[：]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[Portal]{lang="EN-US"}[认证网段地址。]{style="font-family:
宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_17060_20103_x1973664042}[：子网掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_17060_20103_1628635100}[：子网掩码，点分十进制格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_1885684393}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_17060_20103_x84784733}**[undo]{lang="EN-US"}**[命令中不携带]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址参数，则表示删除指定所有的]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[源认证网段。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[源认证网段仅对]{style="font-family:宋体"}]{#struct_0_17060_20103_1885094570}[Portal]{lang="EN-US"}[的可跨三层认证方式（]{style="font-family:宋体"}**[layer3]{lang="EN-US"}**[）生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口上同时配置了源认证网段和目的网段认证，则源认证网段配置不会生效。]{style="font-family:宋体"}]{#struct_0_17060_20103_304105955}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x353938238}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_856856517}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1885029034}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置一条]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[Portal]{lang="EN-US"}[源认证网段为]{style="font-family:宋体"}[10.10.10.0/24]{lang="EN-US"}[，仅允许来自]{style="font-family:宋体"}[10.10.10.0/24]{lang="EN-US"}[网段的用户触发]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_1897416502}

[\[Sysname\] interface ]{lang="EN-US"}[gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname--]{lang="EN-US"}[GigabitEthernet1/0/1]{lang="EN-US"}[\] portal layer3 source 10.10.10.0 24]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_17060_20103_x833470113}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1885487786}[在接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上配置一条]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[Portal]{lang="EN-US"}[源认证网段为]{style="font-family:宋体"}[10.10.10.0/24]{lang="EN-US"}[，仅允许来自]{style="font-family:宋体"}[10.10.10.0/24]{lang="EN-US"}[网段的用户触发]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x2048666425}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname--Vlan-interface2\] portal layer3 source 10.10.10.0 24]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1134401534}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_2143868101}**[interface]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_1885422250}**[free-all except destination]{lang="EN-US"}**
:::

::: {#269368515 .myid}
[]{#_Toc404792750}[]{#struct_0_17060_20103_x1255961165}[]{#_Toc330201697}[]{#_Toc320893876}[]{#_Toc309735136}[]{#_Toc262736227}

**Portal \-- Portal配置命令 \-- portal max-user**

------------------------------------------------------------------------

[**[portal max-user]{lang="EN-US"}**]{#struct_0_17060_20103_x1281575937}[命令用来配置全局]{style="font-family:宋体"}[Portal]{lang="EN-US"}[最大用户数。]{style="font-family:宋体"}

[**[undo portal max-user]{lang="EN-US"}**]{#struct_0_17060_20103_512722045}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x213703911}

[**[portal max-user]{lang="EN-US"}**[ *max-number*]{lang="EN-US"}]{#struct_0_17060_20103_x1797229328}

[**[undo portal max-user]{lang="EN-US"}**]{#struct_0_17060_20103_x651936108}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x980666549}

[[全局]{style="font-family:宋体"}]{#struct_0_17060_20103_732507750}[Portal]{lang="EN-US"}[最大用户数不受限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_130393535}

[[系统视图]{style="font-family:宋体"} ]{#struct_0_17060_20103_1885356714}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x502046516}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_1972623796}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_859416935}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x2060887834}

[*[max-number]{lang="EN-US"}*]{#struct_0_17060_20103_x1253998674}[：系统中允许同时在线的最大]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户数。该参数的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_1450037032}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置的全局]{style="font-family:宋体"}]{#struct_0_17060_20103_x2020412203}[Portal]{lang="EN-US"}[最大用户数小于当前已经在线的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户数，则该命令可以执行成功，且在线]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户不受影响，但系统将不允许新的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户接入。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令指定的最大用户数是指]{style="font-family:宋体"}]{#struct_0_17060_20103_1885749930}[IPv4 Portal]{lang="EN-US"}[和]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[用户的总数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议所有使能]{style="font-family:宋体"}]{#struct_0_17060_20103_212633957}[Portal]{lang="EN-US"}[的接口上的最大]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[用户数和最大]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[用户数之和不超过全局最大]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户数配置为，否则会有部分]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户因为全局最大用户数已达到而无法上线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1973074217}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x316401622}[配置全局]{style="font-family:宋体"}[Portal]{lang="EN-US"}[最大用户数为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x372417020}

[\[Sysname\] portal max-user 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_579946888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_1722196812}**[user]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal]{lang="EN-US"}**[ { **ipv4-max-user** \| **ipv6-max-user** }]{lang="EN-US"}]{#struct_0_17060_20103_212961637}
:::

::: {#-2025799488 .myid}
[]{#_Toc404792751}[]{#struct_0_17060_20103_x2134141774}[]{#_Toc396313649}[]{#_Toc390431162}[]{#_Toc385938130}[]{#_Toc297724510}[]{#_Toc262736230}

**Portal \-- Portal配置命令 \-- portal nas-id-profile**

------------------------------------------------------------------------

[**[portal nas-id-profile]{lang="EN-US"}**]{#struct_0_17060_20103_2009373067}[命令用来指定接口引用的]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo portal nas-id-profile]{lang="EN-US"}**]{#struct_0_17060_20103_x1104240087}[命令用来删除接口引用的]{style="font-family:
宋体"}[NAS-ID Profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1264048917}

[**[portal nas-id-profile ]{lang="PT-BR"}**]{#struct_0_17060_20103_1268485476}*[profile-name]{lang="PT-BR"}*

[**[undo portal nas-id-profile]{lang="PT-BR"}**]{#struct_0_17060_20103_594741581}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1598433916}

[[未指定引用的]{style="font-family:宋体"}]{#struct_0_17060_20103_1288640594}[NAS-ID Profile]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_537556791}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17060_20103_2066246512}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_1698890412}

[[network-admin]{lang="PT-BR"}]{#struct_0_17060_20103_x791062619}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_17060_20103_1893874699}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1027003880}

[*[profile-name]{lang="PT-BR"}*]{#struct_0_17060_20103_x536371522}[：]{style="font-family:宋体"}[标识指定]{style="font-family:宋体"}[VLAN]{lang="PT-BR"}[和]{style="font-family:宋体"}[NAS-ID]{lang="PT-BR"}[绑定关系的]{style="font-family:宋体"}[Profile]{lang="PT-BR"}[名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:
宋体"}[31]{lang="PT-BR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_1165192628}

[[本命令引用的]{style="font-family:宋体"}]{#struct_0_17060_20103_x1911473782}[NAS-ID Profile]{lang="PT-BR"}[由命令]{style="font-family:宋体"}**[aaa nas-id profile]{lang="PT-BR"}**[配置]{style="font-family:宋体"}[，]{style="font-family:宋体"}[具体情况请参考]{style="font-family:宋体"}["]{style="font-family:宋体"}[安全命令参考]{style="font-family:宋体"}["]{style="font-family:宋体"}[中的]{style="font-family:宋体"}["]{style="font-family:宋体"}[AAA]{lang="PT-BR"}["]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[需要注意的是]{style="font-family:宋体"}]{#struct_0_17060_20103_x1828577965}[，]{style="font-family:宋体"}[如果接口上指定了]{style="font-family:宋体"}[NAS-ID Profile]{lang="PT-BR"}[，]{style="font-family:宋体"}[则此]{style="font-family:宋体"}[Profile]{lang="PT-BR"}[中定义的绑定关系优先使用]{style="font-family:宋体"}[；]{style="font-family:宋体"}[如果接口上未指定]{style="font-family:宋体"}[NAS-ID Profile]{lang="PT-BR"}[或指定的]{style="font-family:宋体"}[Profile]{lang="PT-BR"}[中没有找到匹配的绑定关系]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则使用设备名作为]{style="font-family:宋体"}[NAS-ID]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1289436514}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x853754168}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1370038334}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上指定名为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_1148162096}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname--GigabitEthernet1/0/1\] portal nas-id-profile aaa]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x1085187462}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x681719930}[在接口]{style="font-family:宋体"}[Vlan-interface 2]{lang="EN-US"}[上指定名为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_867177676}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] portal nas-id-profile aaa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1046743592}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aaa nas-id profile]{lang="EN-US"}**]{#struct_0_17060_20103_817409573}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#902139456 .myid}
[]{#_Toc404792752}[]{#struct_0_17060_20103_213027173}[]{#_Toc371518630}[]{#_Toc365963514}

**Portal \-- Portal配置命令 \-- portal nas-port-id format**

------------------------------------------------------------------------

[**[portal nas-port-id format]{lang="EN-US"}**]{#struct_0_17060_20103_x1280470084}[命令用来配置]{style="font-family:
宋体"}[NAS-Port-ID]{lang="EN-US"}[属性的格式。]{style="font-family:
宋体"}

[**[undo portal nas-port-id format]{lang="EN-US"}**]{#struct_0_17060_20103_212830565}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x383006490}

[**[portal nas-port-id format]{lang="EN-US"}**[ { **1** \| **2** \| **3** \| **4** }]{lang="EN-US"}]{#struct_0_17060_20103_212896101}

[**[undo portal nas-port-id format]{lang="EN-US"}**]{#struct_0_17060_20103_x1209689424}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_213223781}

[[NAS-Port-ID]{lang="EN-US"}]{#struct_0_17060_20103_x592860536}[的消息格式为格式]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_213289317}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17060_20103_1284144180}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_212699492}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x1773120600}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_212765028}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_212568420}

[**[1]{lang="EN-US"}**]{#struct_0_17060_20103_x1681697483}[：表示格式]{style="font-family:宋体"}[1]{lang="EN-US"}[，具体为]{style="font-family:宋体"}[{atm\|eth\|trunk}NAS_slot/NAS_subslot/NAS_port:XPI.XCI AccessNodeIdentifier/ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port\[:ANI_XPI.ANI_XCI\]]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2]{lang="EN-US"}**]{#struct_0_17060_20103_212633956}[：表示格式]{style="font-family:宋体"}[2]{lang="EN-US"}[，具体为]{style="font-family:宋体"}[SlotID/00/IfNO/VlanID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[3]{lang="EN-US"}**]{#struct_0_17060_20103_1220694100}[：表示格式]{style="font-family:宋体"}[3]{lang="EN-US"}[，具体为在格式]{style="font-family:宋体"}[2]{lang="EN-US"}[的内容后面添加]{style="font-family:宋体"}[Option82]{lang="EN-US"}[或者]{style="font-family:宋体"}[Option18]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[4]{lang="EN-US"}**]{#struct_0_17060_20103_x976789198}[：表示格式]{style="font-family:宋体"}[4]{lang="EN-US"}[，具体为"]{style="font-family:宋体"}[slot=\*\*;subslot=\*\*;port=\*\*;vlanid=\*\*;vlanid2=\*\*;]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_1658273837}

[[可通过本命令修改设备为]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_212961636}[用户发送的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文中填充的]{style="font-family:宋体"}[NAS-Port-ID]{lang="EN-US"}[属性的格式。]{style="font-family:宋体"}

[[不同厂商的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_17060_20103_x1976549779}[服务器要求不同的格式，通常中国电信的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器要求采用格式]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

#### [[1. ]{lang="EN-US"}[格式]{style="font-family:黑体"}[1]{lang="EN-US"}]{#struct_0_17060_20103_213027172} {#格式1 style="margin-left:0cm"}

[[{atm\|eth\|trunk}NAS_slot/NAS_subslot/NAS_port:XPI.XCI AccessNodeIdentifier/ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port\[:ANI_XPI.ANI_XCI\]]{lang="EN-US"}]{#struct_0_17060_20103_x1280470085}

[[各项含义如下：]{style="font-family:宋体"}]{#struct_0_17060_20103_212830564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[{atm\|eth\|trunk}]{lang="EN-US"}]{#struct_0_17060_20103_x383006489}[：]{lang="EN-US" style="font-family:宋体"}[BRAS]{lang="EN-US"}[端口类型，包括]{lang="EN-US" style="font-family:宋体"}[ATM]{lang="EN-US"}[接口、以太接口或]{lang="EN-US" style="font-family:宋体"}[trunk]{lang="EN-US"}[类型的以太网接口。]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NAS_slot]{lang="EN-US"}]{#struct_0_17060_20103_212896100}[：]{lang="EN-US" style="font-family:宋体"}[BRAS]{lang="EN-US"}[槽号，取值为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[31]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NAS_subslot]{lang="EN-US"}]{#struct_0_17060_20103_x1209689423}[：]{lang="EN-US" style="font-family:宋体"}[BRAS]{lang="EN-US"}[子槽号，取值为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[31]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NAS_Port]{lang="EN-US"}]{#struct_0_17060_20103_213223780}[：]{lang="EN-US" style="font-family:宋体"}[BRAS]{lang="EN-US"}[端口号，取值为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[XPI]{lang="EN-US"}]{#struct_0_17060_20103_x592860537}[：如果接口类型为]{style="font-family:宋体"}[atm]{lang="EN-US"}[，则]{style="font-family:宋体"}[XPI]{lang="EN-US"}[对应]{style="font-family:宋体"}[VPI]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[；如果接口类型为]{style="font-family:宋体"}[eth]{lang="EN-US"}[或]{style="font-family:宋体"}[trunk]{lang="EN-US"}[，则]{style="font-family:宋体"}[XPI]{lang="EN-US"}[对应]{style="font-family:宋体"}[PVLAN]{lang="EN-US"}[，]{style="font-family:宋体"}[XPI]{lang="EN-US"}[取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[XCI]{lang="EN-US"}]{#struct_0_17060_20103_213289316}[：如果接口类型为]{style="font-family:宋体"}[atm]{lang="EN-US"}[，则]{style="font-family:宋体"}[XCI]{lang="EN-US"}[对应]{style="font-family:宋体"}[VCI]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[；如果接口类型为]{style="font-family:宋体"}[eth]{lang="EN-US"}[或]{style="font-family:宋体"}[trunk]{lang="EN-US"}[，]{style="font-family:宋体"}[XCI]{lang="EN-US"}[对应于]{style="font-family:宋体"}[CVLAN]{lang="EN-US"}[，]{style="font-family:宋体"}[XCI]{lang="EN-US"}[取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AccessNodeIdentifier]{lang="EN-US"}]{#struct_0_17060_20103_1284144179}[：接入节点标识（例如]{lang="EN-US" style="font-family:宋体"}[DSLAM]{lang="EN-US"}[设备），为不超过]{lang="EN-US" style="font-family:宋体"}[50]{lang="EN-US"}[个字符的字符串，字符串中不能包括空格。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ANI_rack]{lang="EN-US"}]{#struct_0_17060_20103_1778783430}[：接入节点机架号（如支持紧耦合的]{style="font-family:
宋体"}[DSLAM]{lang="EN-US"}[设备），取值为]{style="font-family:
宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ANI_frame]{lang="EN-US"}]{#struct_0_17060_20103_x1638487747}[：接入节点机框号，取值为]{style="font-family:
宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ANI_slot]{lang="EN-US"}]{#struct_0_17060_20103_1778848966}[：接入节点槽号，取值为]{style="font-family:
宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ANI_subslot]{lang="EN-US"}]{#struct_0_17060_20103_x116486356}[：接入节点子槽号，取值为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[31]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ANI_port]{lang="EN-US"}]{#struct_0_17060_20103_1778652358}[：接入节点端口号，取值为]{style="font-family:
宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ANI_XPI.ANI_XCI]{lang="EN-US"}]{#struct_0_17060_20103_x514318857}[：可选项，主要用于携带]{style="font-family:宋体"}[CPE]{lang="EN-US"}[侧的业务信息，可用于标识未来的业务类型需求，如在多]{style="font-family:宋体"}[PVC]{lang="EN-US"}[应用场合下可标识具体的业务。其中，如果接口类型为]{style="font-family:宋体"}[atm]{lang="EN-US"}[，则]{style="font-family:宋体"}[ANI_XPI]{lang="EN-US"}[对应]{style="font-family:宋体"}[VPI]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，]{style="font-family:宋体"}[ANI_XCII]{lang="EN-US"}[对应]{style="font-family:宋体"}[VCI]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[；如果接口类型为]{style="font-family:宋体"}[eth]{lang="EN-US"}[或]{style="font-family:宋体"}[trunk]{lang="EN-US"}[，则]{style="font-family:宋体"}[ANI_XPI]{lang="EN-US"}[对应]{style="font-family:宋体"}[PVLAN]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[，则]{style="font-family:宋体"}[ANI_XCI]{lang="EN-US"}[对应]{style="font-family:宋体"}[CVLAN]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_17060_20103_1778717894}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[字符串之间用一个空格隔开，要求字符串中间不能有空格。花括号中的内容是必选的，]{style="font-family:宋体"}]{#struct_0_17060_20103_x1337230413}[\|]{lang="EN-US"}[表示并列的关系，多选一。]{style="font-family:宋体"}[\[\]]{lang="EN-US"}[表示可选项。对于某些设备没有机架、框、子槽的概念，相应位置应统一填]{style="font-family:宋体"}[0]{lang="EN-US"}[，对于无效的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[值都填]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如接口类型为]{lang="EN-US" style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_17060_20103_1779045574}[，则]{lang="EN-US" style="font-family:宋体"}[AccessNodeIdentifier]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ANI_rack]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ANI_frame]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ANI_slot]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ANI_subslot]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ANI_port]{lang="EN-US"}[域可统一填]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如运营商未使用]{style="font-family:宋体"}]{#struct_0_17060_20103_x2056023330}[SVLAN]{lang="EN-US"}[技术，则]{style="font-family:宋体"}[XPI=4096]{lang="EN-US"}[，]{style="font-family:宋体"}[XCI=VLAN]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如运营商未使用]{style="font-family:宋体"}]{#struct_0_17060_20103_1779111110}[VLAN]{lang="EN-US"}[技术区分用户（用户]{style="font-family:宋体"}[PC]{lang="EN-US"}[直连]{style="font-family:宋体"}[BAS]{lang="EN-US"}[端口），则]{style="font-family:宋体"}[XPI=4096]{lang="EN-US"}[，]{style="font-family:宋体"}[XCI=4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于接入节点设备（如]{style="font-family:宋体"}]{#struct_0_17060_20103_680050763}[DSLAM]{lang="EN-US"}[），按如上格式上报本接入节点的接入线路信息，对于与]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[设备相关的接入线路信息可统一填]{style="font-family:宋体"}[0]{lang="EN-US"}[，如：]{style="font-family:宋体"}

[["]{style="font-family:宋体"}]{#struct_0_17060_20103_1778914502}[0 0/0/0:4096.1234 guangzhou001/0/31/63/31/127"]{lang="EN-US"}

[[其含义是]{style="font-family:宋体"}]{#struct_0_17060_20103_273090123}[DSLAM]{lang="EN-US"}[节点标识为]{style="font-family:宋体"}[guangzhou001]{lang="EN-US"}[、]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的机架号为]{style="font-family:宋体"}[0]{lang="EN-US"}[（没有机架）、]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的框号为]{style="font-family:宋体"}[31]{lang="EN-US"}[、]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的槽号为]{style="font-family:宋体"}[63]{lang="EN-US"}[、]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的子槽号为]{style="font-family:宋体"}[31]{lang="EN-US"}[、]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的端口号为]{style="font-family:宋体"}[127]{lang="EN-US"}[、]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[号为]{style="font-family:宋体"}[1234]{lang="EN-US"}[，]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入线路信息为未知。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_17060_20103_1778980038}[BRAS]{lang="EN-US"}[设备，在获取接入节点设备（如]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[）的接入线路信息后，根据]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[的配置可透传接入线路信息，也可修改添加接入线路信息中与]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[设备相关的线路信息，形成完整的接入线路信息，如：]{style="font-family:宋体"}

[["]{lang="EN-US" style="font-family:宋体"}[eth  31/31/7:4096.1234 guangzhou001/0/31/63/31/127"]{lang="EN-US"}]{#struct_0_17060_20103_691745760}[。]{lang="EN-US" style="font-family:
宋体"}

[[示例：]{style="font-family:宋体"}]{#struct_0_17060_20103_1779307718}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[例]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_17060_20103_x501973969}[：]{lang="EN-US" style="font-family:宋体"}[NAS_PORT_ID ="atm 31/31/7:255.65535 0/0/0/0/0/0"]{lang="EN-US"}

[[含义：]{style="font-family:宋体"}[BRAS]{lang="EN-US"}]{#struct_0_17060_20103_1779373254}[设备的用户接口类型为]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口，]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[槽号为]{style="font-family:宋体"}[31]{lang="EN-US"}[，]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[子槽号为]{style="font-family:宋体"}[31]{lang="EN-US"}[，]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}[255]{lang="EN-US"}[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[例]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_257731015}[2]{lang="FR"}[：]{lang="EN-US" style="font-family:宋体"}[NAS_PORT_ID ="eth 31/31/7:1234.2345 0/0/0/0/0/0]{lang="FR"}["]{lang="EN-US" style="font-family:
宋体"}

[[含义：]{style="font-family:宋体"}[BRAS]{lang="EN-US"}]{#struct_0_17060_20103_1778783429}[设备的用户接口类型为以太接口，]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[槽号为]{style="font-family:宋体"}[31]{lang="EN-US"}[，]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[子槽号为]{style="font-family:宋体"}[31]{lang="EN-US"}[，]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[PVLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1234]{lang="EN-US"}[，]{style="font-family:宋体"}[CVLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2345]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[例]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x1638946498}[3]{lang="FR"}[：]{lang="EN-US" style="font-family:宋体"}[NAS_PORT_ID ="eth 31/31/7:4096.2345 0/0/0/0/0/0]{lang="FR"}["]{lang="EN-US" style="font-family:
宋体"}

[[含义：]{style="font-family:宋体"}[BRAS]{lang="EN-US"}]{#struct_0_17060_20103_1778848965}[设备的用户接口类型为以太接口，]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[槽号为]{style="font-family:宋体"}[31]{lang="EN-US"}[，]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[子槽号为]{style="font-family:宋体"}[31]{lang="EN-US"}[，]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2345]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[例]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_17060_20103_x116551892}[：]{lang="EN-US" style="font-family:宋体"}[NAS_PORT_ID ="eth  31/31/7:4096.2345 guangzhou001/1/31/63/31/127]{lang="EN-US"}["]{lang="EN-US" style="font-family:宋体"}

[[含义：]{style="font-family:宋体"}[BRAS]{lang="EN-US"}]{#struct_0_17060_20103_1778652357}[设备的用户接口类型为以太接口，]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[槽号为]{style="font-family:宋体"}[31]{lang="EN-US"}[，]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[子槽号为]{style="font-family:宋体"}[31, BRAS]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2345,]{lang="EN-US"}[接入节点]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的标识为]{style="font-family:宋体"}[guangzhou001]{lang="EN-US"}[，]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的机架号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的框号为]{style="font-family:宋体"}[31]{lang="EN-US"}[，]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的槽号为]{style="font-family:宋体"}[63]{lang="EN-US"}[，]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的子槽号为]{style="font-family:宋体"}[31]{lang="EN-US"}[，]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的端口号为]{style="font-family:宋体"}[127]{lang="EN-US"}[。]{style="font-family:宋体"}

#### [[2. ]{lang="EN-US"}[格式]{style="font-family:黑体"}[2]{lang="EN-US"}]{#struct_0_17060_20103_x514253321} {#格式2 style="margin-left:0cm"}

[[SlotID/00/IfNO/VlanID]{lang="EN-US"}]{#struct_0_17060_20103_1778717893}

[[各项含义如下：]{style="font-family:宋体"}]{#struct_0_17060_20103_x1337689165}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SlotID]{lang="EN-US"}]{#struct_0_17060_20103_1779045573}[：用户接入的槽位号，为两个字符的字符串。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IFNO]{lang="EN-US"}]{#struct_0_17060_20103_x2056088866}[：用户接入的接口编号，为]{style="font-family:宋体"}[3]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VlanID]{lang="EN-US"}]{#struct_0_17060_20103_1779111109}[：用户接入的]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，为]{lang="EN-US" style="font-family:宋体"}[9]{lang="EN-US"}[个字符的字符串。]{lang="EN-US" style="font-family:宋体"}

#### [[3. ]{lang="EN-US"}[格式]{style="font-family:黑体"}[3]{lang="EN-US"}]{#struct_0_17060_20103_x1151958895} {#格式3 style="margin-left:0cm"}

[[其格式为在格式]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_17060_20103_x1331126026}[的]{style="font-family:宋体"}[NAS-Port-ID]{lang="EN-US"}[内容后面添加用户]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文中指定]{style="font-family:宋体"}[Option]{lang="EN-US"}[的内容：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_17060_20103_x70996339}[用户，此处添加的是]{lang="EN-US" style="font-family:宋体"}[DHCP Option82]{lang="EN-US"}[的内容。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_17060_20103_595623218}[用户，此处添加的是]{lang="EN-US" style="font-family:宋体"}[DHCP Option18]{lang="EN-US"}[的内容。]{lang="EN-US" style="font-family:宋体"}

#### [[4. ]{lang="EN-US"}[格式]{style="font-family:黑体"}[4]{lang="EN-US"}]{#struct_0_17060_20103_x748674368} {#格式4 style="margin-left:0cm"}

[[其格式为"]{style="font-family:宋体"}[slot=\*\*;subslot=\*\*;port=\*\*;vlanid=\*\*;vlanid2=\*\*;]{lang="EN-US"}]{#struct_0_17060_20103_x733724891}["，具体情况如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于非]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17060_20103_1325731920}[接口，其格式为"]{lang="EN-US" style="font-family:宋体"}[slot=\*\*;subslot=\*\*;port=\*\*;vlanid=0;]{lang="EN-US"}["。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于只终结了一层]{lang="EN-US" style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_17060_20103_x1010522084}[的接口，其格式为"]{lang="EN-US" style="font-family:宋体"}[slot=\*\*;subslot=\*\*;port=\*\*;vlanid=\*\*;]{lang="EN-US"}["。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_680509516}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1778914501}[配置]{style="font-family:宋体"}[NAS-Port-ID]{lang="EN-US"}[属性的格式为]{style="font-family:宋体"}[format 1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_273155659}

[\[Sysname\] portal nas-port-id format 1]{lang="EN-US"}
:::

::: {#642037403 .myid}
[]{#_Toc404792753}[]{#struct_0_17060_20103_x978022669}

**Portal \-- Portal配置命令 \-- portal pre-auth domain**

------------------------------------------------------------------------

[**[portal]{lang="EN-US"}**[ \[ **ipv6** \] **pre-auth domain**]{lang="EN-US"}]{#struct_0_17060_20103_1619323599}[命令用来在接口上配置]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证前用户使用的认证域。]{style="font-family:宋体"}

[**[undo portal]{lang="EN-US"}**[ \[ **ipv6** \] **pre-auth domain**]{lang="EN-US"}]{#struct_0_17060_20103_x179525779}[命令用来删除接口上]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证前用户使用的认证域。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1233231820}

[**[portal]{lang="EN-US"}**[ \[ **ipv6** \] **pre-auth domain domain-name**]{lang="EN-US"}]{#struct_0_17060_20103_1806166945}

[**[undo portal]{lang="EN-US"}**[ \[ **ipv6** \] **pre-auth domain**]{lang="EN-US"}]{#struct_0_17060_20103_x1580724987}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_1750860686}

[[接口上未配置]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1610800112}[认证前用户使用的认证域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_656007322}

[[三层接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17060_20103_1629328405}[三层子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_524998874}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x1452616033}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_x500104990}

[[context-admin]{lang="EN-US"}]{#struct_0_17060_20103_2094187329}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x73285532}

[**[ipv6]{lang="EN-US"}**]{#struct_0_17060_20103_2053479441}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[用户使用的认证域。若不指定该参数，则表示指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[用户使用的认证域。]{style="font-family:宋体"}

[[domain-name]{lang="EN-US"}]{#struct_0_17060_20103_184776745}[：]{style="font-family:宋体"}[ISP]{lang="EN-US"}[认证域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[/]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"""、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[?]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["以及"]{style="font-family:宋体"}[@]{lang="EN-US"}["字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x561316749}

[[使能]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x342172512}[的接口上配置了认证前使用的认证域（简称为认证前域）时，在此接口上获取到]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的用户将被]{style="font-family:宋体"}[Portal]{lang="EN-US"}[授予指定认证前域内配置的相关授权属性（目前包括]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[、]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[和]{style="font-family:宋体"}[CAR]{lang="EN-US"}[），并根据授权信息获得相应的网络访问权限。若此用户后续触发了]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证，则认证成功之后会被]{style="font-family:宋体"}[AAA]{lang="EN-US"}[下发新的授权信息。用户下线之后，将被重新授予该认证前域中的授权属性。]{style="font-family:宋体"}

[[认证前域的配置只对采用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_17060_20103_x785569898}[或]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的用户生效。]{style="font-family:宋体"}

[[如果认证前域的域名发生变化，新的域名对所有认证前用户生效。]{style="font-family:宋体"}]{#struct_0_17060_20103_x781118316}

[[如果当前认证前域中的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_17060_20103_x163995763}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[、]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[和]{style="font-family:宋体"}[CAR]{lang="EN-US"}[授权配置发生变化，则新配置仅对新生成的认证前用户生效，已经存在的用户继续使用旧配置。]{style="font-family:宋体"}

[[需要注意的是，若认证前域中指定的授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_17060_20103_x1770821462}[不存在，或者]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中无任何规则，则表示不对用户的访问进行限制；若认证前域中指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中存在匹配源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、匹配源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、匹配所有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或匹配所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的规则，则该授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[下发后将会导致用户不能正常上线和下线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x236950077}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1125769971}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证前用户使用的认证域为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x1381307196}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] portal pre-auth domain abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_2130800900}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display portal interface]{lang="EN-US"}**]{#struct_0_17060_20103_1075709842}
:::

::: {#1331417621 .myid}
[]{#struct_0_17060_20103_1778980037}[]{#_Toc365963513}[]{#_Toc404792754}[]{#_Toc371518631}

**Portal \-- Portal配置命令 \-- portal pre-auth ip-pool**

------------------------------------------------------------------------

[**[portal ]{lang="EN-US"}**[\[ **ipv6** \] **pre-auth ip-pool**]{lang="EN-US"}]{#struct_0_17060_20103_692204512}[命令用来配置]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证前用户使用的地址池。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **portal** \[ **ipv6** \] **pre-auth ip-pool**]{lang="EN-US"}]{#struct_0_17060_20103_1779307717}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x502563793}

[**[portal]{lang="EN-US"}**[ \[ **ipv6** \] **pre-auth ip-pool** *pool-name*]{lang="EN-US"}]{#struct_0_17060_20103_1779373253}

[**[undo]{lang="EN-US"}**[ **portal** \[ **ipv6** \] **pre-auth ip-pool**]{lang="EN-US"}]{#struct_0_17060_20103_258058695}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_1778783428}

[[接口上未配置]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x1639012034}[认证前用户使用的地址池。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_1778848964}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17060_20103_x116617428}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_1778652356}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x514187785}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_1778717892}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1337623629}

[**[ipv6]{lang="EN-US"}**]{#struct_0_17060_20103_1779045572}[：表示]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[用户。若不指定该参数，则表示]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[*[pool-name]{lang="EN-US"}*]{#struct_0_17060_20103_x2056154402}[：表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址池的名字，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_1779111108}

[[在]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_680575052}[用户通过设备的子接口接入网络的组网环境中，当子接口上未配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，且用户需要通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[获取地址时，就必须通过本命令指定一个地址池，并在用户进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证之前为其分配一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址使其可以进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_17060_20103_1778914500}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[仅当接口使用直接认证方式的情况下，接口上为认证前的]{style="font-family:宋体"}]{#struct_0_17060_20103_273221195}[Portal]{lang="EN-US"}[用户指定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址池才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当使用接口上指定的]{style="font-family:宋体"}]{#struct_0_17060_20103_1778980036}[IP]{lang="EN-US"}[地址池为认证前的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址时，该指定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址池必须存在且配置完整，否则无法为]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，并导致用户无法进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_692138976}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_1779307716}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x502629329}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上为认证前的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_1779373252}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] portal pre-auth ip-pool abc]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_258124231}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1778783427}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上]{style="font-family:宋体"}[为认证前的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x1638553282}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname--Vlan-interface100\] portal pre-auth ip-pool abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1778848963}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp server ip-pool]{lang="EN-US"}**]{#struct_0_17060_20103_x116682964}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[业务]{style="font-family:宋体"}[/DHCP]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp pool]{lang="EN-US"}**]{#struct_0_17060_20103_1778652355}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[业务]{style="font-family:宋体"}[/DHCP]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display portal interface]{lang="EN-US"}**]{#struct_0_17060_20103_x514122249}
:::

::::: {#-849736037 .myid}
[]{#_Toc404792755}[]{#struct_0_17060_20103_1885684394}[]{#_Toc330201698}

**Portal \-- Portal配置命令 \-- portal roaming enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Portal命令.files/image001.png){width="62" height="26"}]{lang="EN-US"}]{#struct_0_17060_20103_x84325981}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17060_20103_1885225639}
:::

**[ ]{lang="EN-US"}**

[**[portal roaming enable]{lang="EN-US"}**]{#struct_0_17060_20103_1431486136}[命令用来使能]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户漫游功能。]{style="font-family:宋体"}

[**[undo portal roaming enable]{lang="EN-US"}**]{#struct_0_17060_20103_1885160103}[命令用来关闭]{style="font-family:
宋体"}[Portal]{lang="EN-US"}[用户漫游功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1474328403}

[**[portal roaming enable]{lang="EN-US"}**]{#struct_0_17060_20103_565809234}

[**[undo portal roaming enable]{lang="EN-US"}**]{#struct_0_17060_20103_1942301394}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_598521997}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_2119644780}[用户漫游功能处于关闭状态，即]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户上线后不能在所在的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内漫游。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1964848310}

[[系统视图]{style="font-family:宋体"} ]{#struct_0_17060_20103_603465470}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_1397498884}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_1885094567}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_304040420}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_473786732}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只对通过]{style="font-family:宋体"}]{#struct_0_17060_20103_1885487783}[VLAN]{lang="EN-US"}[接口上线的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户有效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果使能了]{style="font-family:宋体"}]{#struct_0_17060_20103_1885291175}[Portal]{lang="EN-US"}[用户漫游功能，则]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户上线后可以在使能]{style="font-family:宋体"}[Portal]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内漫游，即用户通过]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的任何二层端口都可以访问网络资源；否则用户只能通过认证成功的二层端口访问网络资源。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[有用户在线的情况下，不能配置此命令。]{style="font-family:宋体"}]{#struct_0_17060_20103_x57480112}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x441545111}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1756607327}[使能]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户漫游功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_1157821583}

[\[Sysname\] portal roaming enable]{lang="EN-US"}
:::::

::: {#1309295969 .myid}
[]{#_Toc404792756}[]{#struct_0_17060_20103_38711158}[]{#_Toc330201674}[]{#_Toc320893878}

**Portal \-- Portal配置命令 \-- portal server**

------------------------------------------------------------------------

[**[portal server]{lang="EN-US"}**]{#struct_0_17060_20103_x1624276262}[命令用来创建]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器，并进入]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器视图。]{style="font-family:宋体"}

[**[undo portal server]{lang="EN-US"}**]{#struct_0_17060_20103_1526377662}[命令用来删除指定的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1885749927}

[**[portal server ]{lang="EN-US"}***[server-name]{lang="EN-US"}*]{#struct_0_17060_20103_x1973532970}

[**[undo portal server ]{lang="EN-US"}***[server-name]{lang="EN-US"}*]{#struct_0_17060_20103_x532194456}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_1431703454}

[[没有配置任何]{style="font-family:宋体"}]{#struct_0_17060_20103_x1356297894}[Portal]{lang="EN-US"}[认证服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_100059250}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17060_20103_x152552943}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x116586184}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_541506492}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_1885684391}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x84653661}

[*[server-name]{lang="EN-US"}*]{#struct_0_17060_20103_2143245710}[：]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1829775037}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_145402798}[认证服务器视图用于配置]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的相关参数，包括服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口号，服务器所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，设备和服务器间通信的预共享密钥，服务器探测功能等。]{style="font-family:宋体"}

[[可以配置多个]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x676530996}[认证服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_1098646118}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x382451296}[创建名称为]{style="font-family:宋体"}[pts]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器，并进入]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_742701452}

[\[Sysname\] portal server pts]{lang="EN-US"}

[\[Sysname-portal-server-pts\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1885225640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display portal server]{lang="EN-US"}**]{#struct_0_17060_20103_1431027391}
:::

::: {#235063670 .myid}
[]{#_Toc404792757}[]{#struct_0_17060_20103_x582699199}[]{#_Toc330201690}[]{#_Toc320893871}

**Portal \-- Portal配置命令 \-- portal user-detect**

------------------------------------------------------------------------

[**[portal user-detect]{lang="EN-US"}**]{#struct_0_17060_20103_x2119494409}[命令用来开启]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[用户在线探测功能。]{style="font-family:宋体"}

[**[undo portal user-detect]{lang="EN-US"}**]{#struct_0_17060_20103_x826938183}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1127111011}

[**[portal user-detect type]{lang="EN-US"}**[ { **arp** \| **icmp** } \[ **retry** *retries*\] \[ **interval** *interval* \] \[ **idle** *time* \]]{lang="EN-US"}]{#struct_0_17060_20103_68702587}

[**[undo portal user-detect]{lang="EN-US"}**]{#struct_0_17060_20103_359497611}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1727776680}

[[接口上的]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}]{#struct_0_17060_20103_1885160104}[用户在线探测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_1474000723}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17060_20103_x1412549367}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_425672093}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_1664946288}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_1829113422}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_691638672}

[**[type]{lang="EN-US"}**]{#struct_0_17060_20103_x2073505739}[：指定探测类型。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp]{lang="EN-US"}**]{#struct_0_17060_20103_x1588319161}[：表示探测类型为]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp]{lang="EN-US"}**]{#struct_0_17060_20103_598961991}[：表示探测类型为]{style="font-family:
宋体"}[ICMP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[retry]{lang="EN-US"}**[ *retries*]{lang="EN-US"}]{#struct_0_17060_20103_1885094568}[：探测次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_17060_20103_303581668}[：探测间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1200]{lang="EN-US"}[，单位为秒，缺省]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[idle ]{lang="EN-US"}**]{#struct_0_17060_20103_1778983411}*[time]{lang="EN-US"}*[：用户在线探测闲置时长，即闲置多长时间后发起探测，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒，缺省]{style="font-family:宋体"}[180]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1638422407}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[根据探测类型的不同，设备有以下两种探测机制：]{style="font-family:宋体"}]{#struct_0_17060_20103_1885029032}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[当探测类型为]{style="font-family:宋体"}]{#struct_0_17060_20103_482460093}[ICMP]{lang="EN-US"}[时，若设备发现一定时间（]{style="font-family:宋体"}**[idle]{lang="EN-US"}***[ time]{lang="EN-US"}*[）内接口上未收到某]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的报文，则会向该用户定期（]{style="font-family:宋体"}**[interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}[）发送探测报文。如果在指定探测次数（]{style="font-family:宋体"}**[retry]{lang="EN-US"}**[ *retries*]{lang="EN-US"}[）之内，设备收到了该用户的响应报文，则认为用户在线，且停止发送探测报文，重复这个过程，否则，强制其下线。]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[当探测类型为]{style="font-family:宋体"}]{#struct_0_17060_20103_1015685030}[ARP]{lang="EN-US"}[时，若设备发现一定时间（]{style="font-family:宋体"}**[idle]{lang="EN-US"}**[ *time*]{lang="EN-US"}[）内接口上未收到某]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户的报文，则会向该用户发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求报文。设备定期（]{style="font-family:宋体"}**[interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}[）检测用户]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项是否被刷新过，如果在指定探测次数（]{style="font-family:宋体"}**[retry]{lang="EN-US"}**[ *retries*]{lang="EN-US"}[）内用户]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项被刷新过，则认为用户在线，且停止检测用户]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，重复这个过程，否则，强制其下线。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请根据配置的认证方式选择合适的探测方法，如果配置了直接方式或者二次地址分配方式，则可以使用]{style="font-family:宋体"}]{#struct_0_17060_20103_1885749928}[ARP]{lang="EN-US"}[或]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[探测方式，如果配置了可跨三层认证方式，则仅可以使用]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[探测方式，若配置了]{style="font-family:宋体"}[ARP]{lang="EN-US"}[探测方式，则探测功能不生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户接入设备上配置了阻止]{style="font-family:宋体"}]{#struct_0_17060_20103_x1973598506}[ICMP]{lang="EN-US"}[报文的防火墙策略，则接口上的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[探测方式可能会失败，从而导致接口上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户非正常下线。因此，若接口上需要使用]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[探测方式，请保证用户接入设备不会过滤掉]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x217354272}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_x159406929}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x2128660759}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户在线探测功能：探测类型为]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[，发送探测报文的次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次，发送间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，闲置时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_2099611496}

[\[Sysname\] interface ]{lang="EN-US"}[gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname--GigabitEthernet1/0/1\] portal user-detect type icmp retry 5 interval 10 idle 300]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_2002442188}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_890056367}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上开启]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户在线探测功能：探测类型为]{style="font-family:宋体"}[ARP]{lang="EN-US"}[，检测用户]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的探测次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次，探测间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，闲置时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_1885684392}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname--Vlan-interface100\] portal user-detect type arp retry 5 interval 10 idle 300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x84719197}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_x1380088479}**[interface]{lang="EN-US"}**
:::

::: {#971022064 .myid}
[]{#_Toc404792758}[]{#struct_0_17060_20103_x1159739289}[]{#_Toc330201678}

**Portal \-- Portal配置命令 \-- portal web-server**

------------------------------------------------------------------------

[**[portal web-server]{lang="EN-US"}**]{#struct_0_17060_20103_1988379758}[命令用来创建]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器，并进入]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器视图。]{style="font-family:宋体"}

[**[undo portal web-server]{lang="EN-US"}**]{#struct_0_17060_20103_x1330493611}[命令用来删除]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1151557888}

[**[portal web-server]{lang="EN-US"}**[ *server-name*]{lang="EN-US"}]{#struct_0_17060_20103_116241687}

[**[undo portal web-server]{lang="EN-US"}**[ *server-name*]{lang="EN-US"}]{#struct_0_17060_20103_x843657712}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_2014104200}

[[没有配置任何]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_x1057633617}[服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_1905120323}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17060_20103_x892001335}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x226709337}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_1344281329}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_x553535311}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_1562749793}

[*[server-name]{lang="EN-US"}*]{#struct_0_17060_20103_x1577311436}[：]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x843723248}

[[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_1617075410}[服务器是指]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证过程中向用户推送认证页面的]{style="font-family:宋体"}[Web]{lang="EN-US"}[服务器，也是设备强制重定向用户]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[请求报文时所指的]{style="font-family:宋体"}[Web]{lang="EN-US"}[服务器。]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器视图用于配置该]{style="font-family:宋体"}[Web]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址及配置设备重定向该]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址给用户时]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址所携带的参数，同时该视图还用于配置]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器探测等功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_760636150}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1376747165}[创建名称为]{style="font-family:宋体"}[wbs]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器，并进入]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x825984077}

[\[Sysname\] portal web-server wbs]{lang="EN-US"}

[\[Sysname-portal-websvr-wbs\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1320997044}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display portal web-server]{lang="EN-US"}**]{#struct_0_17060_20103_x1133297359}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_x1303843846}**[apply ]{lang="EN-US"}[web-server]{lang="EN-US"}**
:::

::: {#717485997 .myid}
[]{#_Toc404792759}[]{#struct_0_17060_20103_x1508004759}[]{#_Toc330201707}[]{#_Toc320893884}

**Portal \-- Portal配置命令 \-- reset portal packet statistics**

------------------------------------------------------------------------

[**[reset portal packet statistics]{lang="EN-US"}**]{#struct_0_17060_20103_x843788784}[命令用来清除]{style="font-family:
宋体"}[Portal]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1145391535}

[**[reset portal packet statistics]{lang="EN-US"}**]{#struct_0_17060_20103_1159773866}**[ ]{lang="EN-US"}**[\[ **server** *server-name* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x203897115}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17060_20103_1897615286}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_321173060}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_1020787910}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_1530314469}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_1179730643}

[*[server-name]{lang="EN-US"}*]{#struct_0_17060_20103_x843854320}[：]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x316784792}

[[若不指定参数]{style="font-family:宋体"}]{#struct_0_17060_20103_x843395568}**[server]{lang="EN-US"}**[，则清除所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x710429918}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x1446640934}[清除名字为]{style="font-family:宋体"}[st]{lang="EN-US"}[上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset portal packet statistics server pts ]{lang="EN-US"}]{#struct_0_17060_20103_1188940272}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1485670834}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[portal ]{lang="EN-US"}**]{#struct_0_17060_20103_x1606358955}**[packet ]{lang="EN-US"}[statistics]{lang="EN-US"}**
:::

::: {#1086392918 .myid}
[]{#_Toc309735145}[]{#_Toc262736235}[]{#_Toc404792760}[]{#struct_0_17060_20103_x13447860}[]{#_Toc330201685}[]{#_Toc320893880}[]{#_Toc323397280}[]{#_Toc323397281}[]{#_Toc323397282}[]{#_Toc323397283}[]{#_Toc323397284}[]{#_Toc323397285}[]{#_Toc323397286}[]{#_Toc323397287}[]{#_Toc323397288}[]{#_Toc323397289}[]{#_Toc323397290}[]{#_Toc323397291}[]{#_Toc323397292}[]{#_Toc323397293}[]{#_Toc323397294}[]{#_Toc323397295}[]{#_Toc323397296}[]{#_Toc323397297}[]{#_Toc323397298}[]{#_Toc323397299}[]{#_Toc323397300}[]{#_Toc323397301}[]{#_Toc323397302}[]{#_Toc323397303}[]{#_Toc323397304}[]{#_Toc323397305}[]{#_Toc323397306}[]{#_Toc323397307}[]{#_Toc323397308}[]{#_Toc323397309}[]{#_Toc323397310}[]{#_Toc323397311}[]{#_Toc323397312}[]{#_Toc323397313}[]{#_Toc323397356}[]{#_Toc323397357}[]{#_Toc323397358}[]{#_Toc323397359}[]{#_Toc323397360}[]{#_Toc323397361}[]{#_Toc323397362}[]{#_Toc323397363}[]{#_Toc323397364}[]{#_Toc323397365}[]{#_Toc323397366}[]{#_Toc323397367}[]{#_Toc323397368}[]{#_Toc323397369}[]{#_Toc323397370}[]{#_Toc323397371}[]{#_Toc323397372}[]{#_Toc323397373}[]{#_Toc323397374}[]{#_Toc323397375}[]{#_Toc323397376}[]{#_Toc323397377}[]{#_Toc323397378}[]{#_Toc323397379}[]{#_Toc323397380}[]{#_Toc323397381}[]{#_Toc323397382}[]{#_Toc323397383}[]{#_Toc323397384}[]{#_Toc323397385}[]{#_Toc323397386}[]{#_Toc323397387}[]{#_Toc323397388}[]{#_Toc323397389}[]{#_Toc323397390}[]{#_Toc323397391}[]{#_Toc323397392}[]{#_Toc323397393}[]{#_Toc323397394}[]{#_Toc323397395}[]{#_Toc323397396}[]{#_Toc323397397}[]{#_Toc323397398}[]{#_Toc323397399}[]{#_Toc323397400}[]{#_Toc323397401}[]{#_Toc323397402}[]{#_Toc323397403}[]{#_Toc323397404}[]{#_Toc323397405}[]{#_Toc323397406}[]{#_Toc323397407}[]{#_Toc323397408}[]{#_Toc323397409}[]{#_Toc323397410}[]{#_Toc323397411}[]{#_Toc323397412}[]{#_Toc323397413}[]{#_Toc323397414}[]{#_Toc323397415}[]{#_Toc323397416}[]{#_Toc323397465}[]{#_Toc323397466}[]{#_Toc323397467}[]{#_Toc323397468}[]{#_Toc323397469}[]{#_Toc323397470}[]{#_Toc323397471}[]{#_Toc323397472}[]{#_Toc323397473}[]{#_Toc323397474}[]{#_Toc323397475}[]{#_Toc323397476}[]{#_Toc323397477}[]{#_Toc323397478}[]{#_Toc323397479}

**Portal \-- Portal配置命令 \-- server-detect (portal server view)**

------------------------------------------------------------------------

[**[server-detect]{lang="EN-US"}**]{#struct_0_17060_20103_1530890091}[命令用来开启]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的可达性探测功能。开启]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的可达性探测功能后，设备会定期检测]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器发送的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文来判断服务器的可达状态。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_17060_20103_x40692709}**[server-detect]{lang="PT-BR"}**[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x843461104}

[**[server-detect]{lang="EN-US"}**]{#struct_0_17060_20103_816219625}[ \[ **timeout** *timeout* \] { **log \| trap** } \*]{lang="EN-US"}

[**[undo server-detect]{lang="PT-BR"}**]{#struct_0_17060_20103_x1781257959}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_831780868}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x843526640}[认证服务器的可达性探测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_1621710225}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x91868292}[认证服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_876276135}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x623844887}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_244789111}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_563718889}

[**[timeout ]{lang="EN-US"}***[timeout]{lang="EN-US"}*]{#struct_0_17060_20103_x794515242}[：探测超时时间，取值范围]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[60]{lang="EN-US"}[。]{style="font-family:宋体"}

[[{ **log \| trap** } **\***]{lang="EN-US"}]{#struct_0_17060_20103_x843592176}[：设备探测到]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[可达状态变化时，触发执行的操作。包括以下两种，且可同时选择多种。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[log]{lang="EN-US"}**]{#struct_0_17060_20103_1254172668}[：]{style="font-family:
宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[可达或者不可达的状态改变时，发送日志信息。日志信息中记录了]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[名以及该服务器状态改变前后的状态。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[trap]{lang="EN-US"}**]{#struct_0_17060_20103_x200655938}[：]{style="font-family:
宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[可达或者不可达的状态改变时，向网管服务器发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息。]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息中记录了]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[名以及该服务器的当前状态。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_870463656}

[[只有在支持]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x686348672}[服务器心跳功能（目前仅]{style="font-family:宋体"}[iMC]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器支持）的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的配合下，本功能才有效。]{style="font-family:宋体"}

[[若设备在指定的探测超时时间（]{style="font-family:宋体"}**[timeout]{lang="EN-US"}**[ *timeout*]{lang="EN-US"}]{#struct_0_17060_20103_x1111515191}[）内收到]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文，且验证其正确，则认为此次探测成功且服务器可达，否则认为此次服务器不可达。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_719540438}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_493686951}[开启对]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[pts]{lang="EN-US"}[的探测功能，探测超时时间为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒，若服务器状态改变，则发送日志信息和]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x2000277778}

[\[Sysname\] portal server pts]{lang="EN-US"}

[\[Sysname-portal-server-pts\] server-detect timeout 600 log trap]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x843133424}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal server]{lang="EN-US"}**]{#struct_0_17060_20103_x1524786130}
:::

::: {#-819508152 .myid}
[]{#_Toc404792761}[]{#struct_0_17060_20103_1895677585}[]{#_Toc330201687}

**Portal \-- Portal配置命令 \-- server-detect (portal web-server view)**

------------------------------------------------------------------------

[**[server-detect]{lang="EN-US"}**]{#struct_0_17060_20103_1982975246}[命令用来开启]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器的可达性探测功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_17060_20103_x591479466}**[server-detect]{lang="PT-BR"}**[命令用来]{style="font-family:宋体"}[恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x241562441}

[**[server-detect]{lang="EN-US"}**[ \[ **interval** *interval* \] \[ **retry** ]{lang="EN-US"}]{#struct_0_17060_20103_1894262781}*[retries]{lang="EN-US"}[ ]{lang="EN-US"}*[\] { **log** \| **trap** } \*]{lang="EN-US"}

[**[undo server-detect]{lang="PT-BR"}**]{#struct_0_17060_20103_1596026801}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1036303902}

[[当前]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_1530693650}[服务器的可达性探测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x843198960}

[[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_1243985309}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_1759372510}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_1752906748}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_x1707906997}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x134062367}

[**[interval]{lang="EN-US"}**]{#struct_0_17060_20103_x377763101}*[ interval]{lang="EN-US"}*[：进行探测尝试的时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[1200]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[retry]{lang="EN-US"}**]{#struct_0_17060_20103_1540978493}*[ retries]{lang="EN-US"}*[：连续探测失败的最大次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[3]{lang="EN-US"}[。若连续探测失败数目达到此值，则认为服务器不可达。]{style="font-family:宋体"}

[[{ **log \| trap** ]{lang="EN-US"}[}]{lang="EN-US"}]{#struct_0_17060_20103_x2007373939}**[ \*]{lang="EN-US"}**[：]{style="font-family:
宋体"}[Portal Web]{lang="EN-US"}[服务器可达状态的变化时，可触发执行的操作。包括以下两种，且可同时选择多种。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[log]{lang="EN-US"}**]{#struct_0_17060_20103_326479155}[：]{style="font-family:
宋体"}[Portal Web]{lang="EN-US"}[服务器可达或者不可达的状态改变时，发送日志信息。日志信息中记录了]{style="font-family:宋体"}[Portal ]{lang="EN-US"}[Web]{lang="EN-US"}[服务器名以及该服务器状态改变前后的状态。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[trap]{lang="EN-US"}**]{#struct_0_17060_20103_x843657711}[：]{style="font-family:
宋体"}[Portal Web]{lang="EN-US"}[服务器可达或者不可达的状态改变时，向网管服务器发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息。]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息中记录了]{style="font-family:宋体"}[Portal ]{lang="EN-US"}[Web]{lang="EN-US"}[服务器名以及该服务器的当前状态。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_2014038664}

[[该探测方法可由设备独立完成，不需要]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_x843723247}[服务器端的任何配置来配合。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_1616878802}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x28399372}[配置对]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器]{style="font-family:宋体"}[wbs]{lang="EN-US"}[的探测功能，每次探测间隔时间为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒，若连续二次探测均失败，则发送服务器不可达的日志信息和]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x1785671502}

[\[Sysname\] portal web-server wbs]{lang="EN-US"}

[\[Sysname-portal-websvr-wbs\] server-detect interval 600 retry 2 log trap]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1734314061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal web-server]{lang="EN-US"}**]{#struct_0_17060_20103_1888583034}
:::

::: {#-1384273943 .myid}
[]{#_Toc404792762}[]{#struct_0_17060_20103_1194328627}[]{#_Toc330201679}

**Portal \-- Portal配置命令 \-- url**

------------------------------------------------------------------------

[**[url]{lang="EN-US"}**]{#struct_0_17060_20103_x626084870}[命令用来指定]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo url]{lang="EN-US"}**]{#struct_0_17060_20103_x36229626}[命令用来删除指定的]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x843788783}

[**[url]{lang="EN-US"}**[ *url-string*]{lang="EN-US"}]{#struct_0_17060_20103_x1145850287}

[**[undo url]{lang="EN-US"}**]{#struct_0_17060_20103_x932172603}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_1809697606}

[[没有指定]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_1373340025}[服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_619263276}

[[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_x131706682}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_x494863992}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_484886751}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_x843854319}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x316194971}

[*[url-string]{lang="EN-US"}*]{#struct_0_17060_20103_27632769}[：]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1142489266}

[[本命令指定的]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_17060_20103_x843461103}[是可用标准]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[或者]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[协议访问的]{style="font-family:宋体"}[URL]{lang="EN-US"}[，它以]{style="font-family:宋体"}[http://]{lang="EN-US"}[或者]{style="font-family:宋体"}[https://]{lang="EN-US"}[开头。如果该]{style="font-family:宋体"}[URL]{lang="EN-US"}[未以]{style="font-family:宋体"}[http://]{lang="EN-US"}[或者]{style="font-family:宋体"}[https://]{lang="EN-US"}[开头，则缺省认为是以]{style="font-family:宋体"}[http://]{lang="EN-US"}[开头。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_816547305}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x695547201}[配置]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器]{style="font-family:宋体"}[wbs]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[为]{style="font-family:宋体"}[http://www.test.com/portal]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x1266050400}

[\[Sysname\] portal web-server wbs]{lang="EN-US"}

[\[Sysname-portal-websvr-wbs\] url http://www.test.com/portal]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1339896057}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display portal web-server]{lang="EN-US"}**]{#struct_0_17060_20103_1124281056}
:::

::: {#-2144197787 .myid}
[]{#_Toc404792763}[]{#struct_0_17060_20103_x2085246784}[]{#_Toc330201680}

**Portal \-- Portal配置命令 \-- url-parameter**

------------------------------------------------------------------------

[**[url-parameter]{lang="EN-US"}**]{#struct_0_17060_20103_x843592175}[命令用来配置设备重定向给用户的]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[中携带的参数信息。]{style="font-family:宋体"}

[**[undo url-parameter]{lang="EN-US"}**]{#struct_0_17060_20103_1254107132}[命令用来删除配置的]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器]{style="font-family:宋体"}[URL]{lang="EN-US"}[携带的参数信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1003156660}

[**[url-parameter ]{lang="EN-US"}***[param-name ]{lang="EN-US"}*[{ **original-url** \| **source-address** \| **source-mac** \| **value** *expression* }]{lang="EN-US"}]{#struct_0_17060_20103_2040794371}

[**[undo url-parameter ]{lang="EN-US"}***[param-name]{lang="EN-US"}*]{#struct_0_17060_20103_x843133423}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1525113810}

[[未配置]{style="font-family:宋体"}]{#struct_0_17060_20103_x843198959}[设备重定向给用户的]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[中携带的参数信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x843657714}

[[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_2014235272}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_501962286}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x991949901}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_1717767447}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x642483878}

[*[param-name]{lang="EN-US"}*]{#struct_0_17060_20103_x1257923399}[：]{style="font-family:宋体"}[URL]{lang="EN-US"}[参数名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[URL]{lang="EN-US"}[参数名对应的参数内容由]{style="font-family:宋体"}*[param-name]{lang="EN-US"}*[后的参数指定。]{style="font-family:宋体"}

[**[original-url]{lang="EN-US"}**]{#struct_0_17060_20103_x144571965}[：用户初始访问的]{style="font-family:宋体"}[Web]{lang="EN-US"}[页面的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[source-address]{lang="EN-US"}**]{#struct_0_17060_20103_x1552120372}[：用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[source-mac]{lang="EN-US"}**]{#struct_0_17060_20103_x843723250}[：用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[value ]{lang="EN-US"}***[expression]{lang="EN-US"}*]{#struct_0_17060_20103_1616551123}[：自定义字符串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_749965288}

[[可以通过多次执行本命令配置多条参数信息。]{style="font-family:宋体"}]{#struct_0_17060_20103_1291932867}

[[对于同一个参数名]{style="font-family:宋体"}*[param-name]{lang="EN-US"}*]{#struct_0_17060_20103_1264086610}[后的参数设置，最后配置的生效。]{style="font-family:宋体"}

[[该命令用于配置用户访问]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_x843395570}[服务器时，要求携带的一些参数，比较常用的是要求携带用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、用户原始访问的]{style="font-family:宋体"}[URL]{lang="EN-US"}[信息。用户也可以手工指定，携带一些特定的字符信息。配置完成后，在设备给用户强制重定向]{style="font-family:宋体"}[URL]{lang="EN-US"}[时会携带这些参数，例如配置]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[为：]{style="font-family:宋体"}[http://www.test.com/portal]{lang="EN-US"}[，若同时配置如下两个参数信息：]{style="font-family:宋体"}**[url-parameter]{lang="EN-US"}**[ **userip** **source-address**]{lang="EN-US"}[和]{style="font-family:
宋体"}**[url-parameter]{lang="EN-US"}**[ **userurl** **value** **http://www.test.com/welcome**]{lang="EN-US"}[，则设备给源]{style="font-family:
宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的用户重定向时回应的]{style="font-family:宋体"}[URL]{lang="EN-US"}[格式即为：]{style="font-family:宋体"}[http://www.test.com/portal?userip=1.1.1.1&userurl= http://www.test.com/welcome]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x709905629}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x843526642}[为设备重定向给用户的]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器]{style="font-family:宋体"}[wbs]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[中配置两个参数]{style="font-family:宋体"}[userip]{lang="EN-US"}[和]{style="font-family:宋体"}[userurl]{lang="EN-US"}[，其值分别为用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和自定义字符串]{style="font-family:宋体"}[http://www.test.com/welcome]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_1621841297}

[\[Sysname\] portal web-server wbs]{lang="EN-US"}

[\[Sysname-portal-websvr-wbs\] url-parameter userip source-address]{lang="EN-US"}

[\[Sysname-portal-websvr-wbs\] url-parameter userurl value http://www.test.com/welcome]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1646745733}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display portal web-server]{lang="EN-US"}**]{#struct_0_17060_20103_1385532691}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[url]{lang="EN-US"}**]{#struct_0_17060_20103_x1345679966}
:::

::: {#1867035541 .myid}
[]{#_Toc404792764}[]{#struct_0_17060_20103_x1784226969}[]{#_Toc330201686}[]{#_Toc320893881}[]{#_Toc240343131}

**Portal \-- Portal配置命令 \-- user-sync**

------------------------------------------------------------------------

[**[user-sync]{lang="EN-US"}**]{#struct_0_17060_20103_x843592178}[命令用来配置开启]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户信息同步功能。配置此功能后，设备会响应并周期性地检测指定的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[发来的用户同步报文，以保持设备与该服务器上在线用户信息的一致性。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[user-sync]{lang="EN-US"}**]{#struct_0_17060_20103_1253779452}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x511290126}

[**[user-sync timeout]{lang="EN-US"}**[ *timeout*]{lang="EN-US"}]{#struct_0_17060_20103_x843133426}

[**[undo user-sync]{lang="EN-US"}**]{#struct_0_17060_20103_x1524917202}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1537618793}

[[当前]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_17060_20103_x843198962}[认证服务器的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户信息同步功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_1244116381}

[[Portal]{lang="EN-US"}]{#struct_0_17060_20103_2043643917}[认证服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_1925628669}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x2009343888}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_x1099163116}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x892341427}

[**[timeout ]{lang="EN-US"}***[timeout]{lang="EN-US"}*]{#struct_0_17060_20103_x843657713}[：检测用户同步报文的时间间隔，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[18000]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[1200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_2014169736}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在支持]{style="font-family:宋体"}]{#struct_0_17060_20103_1629300861}[Portal]{lang="EN-US"}[用户心跳功能（目前仅]{style="font-family:宋体"}[iMC]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器支持）的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器的配合下，本功能才有效。为了实现该功能，还需要在]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器上选择支持用户心跳功能，且服务器上配置的用户心跳间隔要小于等于设备上配置的检测超时时间。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在设备上删除]{style="font-family:宋体"}]{#struct_0_17060_20103_x843723249}[Portal]{lang="EN-US"}[认证服务器时将会同时删除该服务器的用户信息同步功能配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对同一服务器多次执行用户信息同步功能的配置时，新的配置将覆盖原有的配置。]{style="font-family:宋体"}]{#struct_0_17060_20103_x843788785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于设备上多余的用户信息，即在检测用户同步报文的时间间隔]{style="font-family:宋体"}]{#struct_0_17060_20103_x1145457071}*[timeout]{lang="EN-US"}*[到达后被判定为]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器上已不存在的用户信息，设备会在]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*[后的某时刻将其删除掉。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果服务器同步过来的用户信息在设备上不存在，则设备会将这些用户的]{style="font-family:宋体"}]{#struct_0_17060_20103_x519474907}[IP]{lang="EN-US"}[地址封装在用户心跳回应报文中发送给服务器，由服务器删除多余的用户。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x323312376}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_x843854321}[配置对]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[pts]{lang="EN-US"}[的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户信息同步功能，检测用户同步报文的时间间隔为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒，如果设备中的某用户信息在]{style="font-family:宋体"}[600]{lang="EN-US"}[秒内未在该]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证服务器]{style="font-family:宋体"}[发送的同步报文中出现，设备将强制该用户下线。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x316719256}

[\[Sysname\] portal server pts]{lang="EN-US"}

[\[Sysname-portal-server-pts\] user-sync timeout 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x787741958}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal server]{lang="EN-US"}**]{#struct_0_17060_20103_574601642}
:::

::: {#1715388964 .myid}
[]{#_Toc404792765}[]{#struct_0_17060_20103_x843395569}[]{#_Toc323397499}[]{#_Toc323397500}[]{#_Toc323397501}[]{#_Toc323397502}[]{#_Toc323397503}[]{#_Toc323397504}[]{#_Toc323397505}[]{#_Toc323397506}[]{#_Toc323397507}[]{#_Toc323397508}[]{#_Toc323397509}[]{#_Toc323397510}[]{#_Toc323397511}[]{#_Toc323397512}[]{#_Toc323397513}[]{#_Toc323397514}[]{#_Toc323397515}[]{#_Toc323397516}[]{#_Toc323397517}[]{#_Toc323397518}[]{#_Toc323397519}[]{#_Toc323397520}[]{#_Toc323397521}[]{#_Toc323397522}[]{#_Toc323397523}[]{#_Toc323397524}[]{#_Toc323397525}[]{#_Toc323397526}[]{#_Toc323397527}[]{#_Toc323397528}[]{#_Toc323397529}[]{#_Toc323397530}[]{#_Toc323397531}[]{#_Toc323397532}[]{#_Toc323397533}[]{#_Toc323397534}[]{#_Toc323397535}[]{#_Toc323397536}[]{#_Toc323397537}[]{#_Toc323397538}[]{#_Toc323397539}[]{#_Toc323397540}[]{#_Toc323397541}[]{#_Toc323397542}[]{#_Toc323397543}[]{#_Toc323397544}[]{#_Toc323397545}[]{#_Toc323397546}[]{#_Toc323397547}[]{#_Toc323397548}[]{#_Toc323397549}[]{#_Toc323397550}[]{#_Toc323397551}[]{#_Toc323397552}[]{#_Toc323397553}[]{#_Toc323397554}[]{#_Toc323397555}[]{#_Toc323397556}[]{#_Toc323397557}[]{#_Toc323397558}[]{#_Toc323397559}[]{#_Toc323397560}[]{#_Toc323397561}[]{#_Toc323397562}[]{#_Toc323397563}[]{#_Toc323397564}[]{#_Toc323397565}[]{#_Toc323397566}[]{#_Toc323397567}[]{#_Toc323397568}[]{#_Toc323397569}[]{#_Toc323397570}[]{#_Toc323397571}[]{#_Toc323397572}[]{#_Toc323397573}[]{#_Toc323397574}[]{#_Toc323397575}[]{#_Toc323397576}[]{#_Toc323397577}[]{#_Toc323397578}[]{#_Toc323397579}[]{#_Toc323397580}[]{#_Toc323397581}[]{#_Toc323397582}[]{#_Toc323397583}[]{#_Toc323397584}[]{#_Toc323397585}[]{#_Toc323397586}[]{#_Toc323397587}[]{#_Toc323397588}[]{#_Toc323397589}[]{#_Toc323397590}[]{#_Toc323397591}[]{#_Toc323397592}[]{#_Toc323397593}[]{#_Toc323397594}[]{#_Toc323397595}[]{#_Toc323397596}[]{#_Toc323397597}[]{#_Toc323397598}[]{#_Toc323397599}[]{#_Toc323397600}[]{#_Toc323397601}[]{#_Toc323397602}[]{#_Toc323397603}[]{#_Toc323397604}[]{#_Toc323397605}[]{#_Toc323397606}[]{#_Toc323397607}[]{#_Toc323397608}[]{#_Toc323397609}[]{#_Toc323397610}[]{#_Toc323397611}[]{#_Toc323397612}[]{#_Toc323397613}[]{#_Toc323397614}[]{#_Toc323397615}[]{#_Toc323397616}[]{#_Toc323397617}[]{#_Toc323397618}[]{#_Toc323397619}[]{#_Toc323397620}[]{#_Toc323397621}[]{#_Toc323397622}[]{#_Toc323397623}[]{#_Toc323397624}[]{#_Toc323397625}[]{#_Toc323397626}[]{#_Toc323397627}[]{#_Toc323397628}[]{#_Toc323397629}[]{#_Toc323397630}[]{#_Toc323397631}[]{#_Toc323397632}[]{#_Toc323397633}[]{#_Toc323397634}[]{#_Toc323397635}[]{#_Toc323397636}[]{#_Toc323397637}[]{#_Toc323397638}[]{#_Toc323397639}[]{#_Toc323397640}[]{#_Toc323397641}[]{#_Toc323397642}[]{#_Toc323397643}[]{#_Toc323397644}[]{#_Toc323397645}[]{#_Toc323397646}[]{#_Toc323397647}[]{#_Toc323397648}[]{#_Toc323397649}[]{#_Toc323397650}

**Portal \-- Portal配置命令 \-- vpn-instance**

------------------------------------------------------------------------

[**[vpn-instance]{lang="EN-US"}**]{#struct_0_17060_20103_x710364382}[命令用来配置]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_17060_20103_88057023}[命令用来取消配置的]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1562717117}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_17060_20103_x1660451930}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_17060_20103_1484454314}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x2042803879}

[[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_x2076062170}[服务器位于公网中。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1051384987}

[[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_x843461105}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_816154089}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_1935633671}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_1668647277}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_1129743297}

[[v*pn-instance-name*]{lang="EN-US"}]{#struct_0_17060_20103_1117950281}[：]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_1738671110}

[[一个]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}]{#struct_0_17060_20103_832151614}[服务器只能属于一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_391930858}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_485663010}[配置]{style="font-family:宋体"}[Portal Web]{lang="EN-US"}[服务器]{style="font-family:宋体"}[wbs]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_x843526641}

[\[Sysname\] portal web-server wbs]{lang="EN-US"}

[\[Sysname-portal-websvr-wbs\] vpn-instance abc]{lang="EN-US"}
:::

::::: {#-391247292 .myid}
[]{#_Toc404792766}[]{#struct_0_17060_20103_x1600680886}

**Portal \-- Portal配置命令 \-- web-redirect track**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[ ]{lang="EN-US"}]{#struct_0_17060_20103_x274107609}[![说明](Portal命令.files/image002.png){#图片 1 width="62" height="25"}]{lang="EN-US"}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17060_20103_1445611779}
:::

[ ]{lang="EN-US"}

[**[web-redirect track]{lang="EN-US"}**]{#struct_0_17060_20103_1458747432}[命令用来开启]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向]{style="font-family:宋体"}[Track]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo web-redirect track]{lang="EN-US"}**]{#struct_0_17060_20103_x1368656778}[命令用来关闭]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向]{style="font-family:宋体"}[Track]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1252314801}

[**[web-redirect track interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_17060_20103_756961992}

[**[undo web-redirect track]{lang="EN-US"}**]{#struct_0_17060_20103_1855785188}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1072505439}

[[Web]{lang="EN-US"}]{#struct_0_17060_20103_1128202469}[重定向]{style="font-family:宋体"}[Track]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_761535834}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17060_20103_57446425}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_943934053}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_x721669303}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_427694860}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_1351121379}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_17060_20103_231387226}[：表示监视指定接口的状态或网络信号信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_x88338836}

[[本命令用来开启]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_17060_20103_499228599}[重定向]{style="font-family:宋体"}[Track]{lang="EN-US"}[功能，监视指定接口的状态或网络信号信息。]{style="font-family:宋体"}

[[如果监视的指定接口状态为]{style="font-family:宋体"}[Down]{lang="EN-US"}]{#struct_0_17060_20103_x2317898}[或以太网通道接口（]{style="font-family:宋体"}[Eth-channel]{lang="EN-US"}[）的网络信号为]{style="font-family:宋体"}[2G]{lang="EN-US"}[信号、无信号，当用户访问互联网时，为其推出不可达页面。之后，用户不能访问外网资源。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_17060_20103_1245852694}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[目前只支持对以太网通道接口（]{lang="EN-US" style="font-family:宋体"}[Eth-channel]{lang="EN-US"}]{#struct_0_17060_20103_x1244516062}[）网络信号信息的监视，不支持监视其他类型的接口。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Web]{lang="EN-US"}]{#struct_0_17060_20103_x1320565446}[重定向]{lang="EN-US" style="font-family:
宋体"}[Track]{lang="EN-US"}[功能，目前只支持]{lang="EN-US" style="font-family:
宋体"}[IPv4]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使能]{lang="EN-US" style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_17060_20103_695396708}[重定向]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[功能时，]{lang="EN-US" style="font-family:宋体"}[Web]{lang="EN-US"}[重定向功能指定的]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[页面必须配置在本机上的。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_x392177682}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1277663797}[在接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[下开启]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向]{style="font-family:宋体"}[Track]{lang="EN-US"}[功能，监视上行接口]{style="font-family:宋体"}[Eth-channel2/0:0]{lang="EN-US"}[的网络信号信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_594585959}

[\[Sysname\] interface vlan 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] web-redirect track interface eth-channel 2/0:0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1998605012}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display web-redirect rule]{lang="EN-US"}**]{#struct_0_17060_20103_301446715}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[web-redirect url]{lang="EN-US"}**]{#struct_0_17060_20103_2050519493}
:::::

::: {#-1432915098 .myid}
[]{#_Toc404792767}[]{#struct_0_17060_20103_1778848969}[]{#_Toc371518645}[]{#_Toc365963515}

**Portal \-- Portal配置命令 \-- web-redirect url**

------------------------------------------------------------------------

[**[web-redirect url]{lang="EN-US"}**]{#struct_0_17060_20103_1778652361}[命令用来配置]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向功能。]{style="font-family:宋体"}

[**[undo web-redirect]{lang="EN-US"}**]{#struct_0_17060_20103_x513860108}[命令用来关闭]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_1778717897}

[**[web-redirect]{lang="EN-US"}**[ \[ **ipv6** \] **url** *url-string* \[ **interval** *interval* \]]{lang="EN-US"}]{#struct_0_17060_20103_x1337427021}

[**[undo web-redirect]{lang="EN-US"}**[ \[ **ipv6** \]]{lang="EN-US"}]{#struct_0_17060_20103_1779045577}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17060_20103_1779111113}

[[Web]{lang="EN-US"}]{#struct_0_17060_20103_679854155}[重定功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17060_20103_1778914505}

[[接口视图]{style="font-family:宋体"} ]{#struct_0_17060_20103_273417803}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17060_20103_1778980041}

[[network-admin]{lang="EN-US"}]{#struct_0_17060_20103_692335587}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17060_20103_1779307721}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17060_20103_x502432722}

[**[ipv6]{lang="EN-US"}**]{#struct_0_17060_20103_1779373257}[：表示]{style="font-family:宋体"}[IPv6 Web]{lang="EN-US"}[重定向功能。若不指定该参数，则表示]{style="font-family:宋体"}[IPv4 Web]{lang="EN-US"}[重定向功能。]{style="font-family:宋体"}

[**[url]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17060_20103_257796551}*[url-string]{lang="EN-US"}*[：]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向的地址，即用户的]{style="font-family:宋体"}[Web]{lang="EN-US"}[访问请求被重定向的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[个字符的字符串，必须是以]{style="font-family:宋体"}[http://]{lang="PT-BR"}[或者]{style="font-family:宋体"}[https://]{lang="PT-BR"}[开头的完整]{style="font-family:宋体"}[URL]{lang="PT-BR"}[路径。]{style="font-family:宋体"}

[**[interval]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17060_20103_1375498903}*[interval]{lang="EN-US"}*[：对用户访问的]{style="font-family:宋体"}[Web]{lang="EN-US"}[页面进行重定向的周期，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒，缺省为]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17060_20103_1375564439}

[[接口上配置了]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_17060_20103_x322238769}[重定向功能后，当该接口上接入的用户初次通过]{style="font-family:宋体"}[Web]{lang="EN-US"}[页面访问外网时，设备会将用户的初始访问页面重定向到指定的]{style="font-family:宋体"}[URL]{lang="EN-US"}[页面，之后用户才可以正常访问外网，经过一定时长（]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[）后，设备又可以对用户要访问的网页或者正在访问的网页重定向到指定的]{style="font-family:宋体"}[URL]{lang="EN-US"}[页面。]{style="font-family:宋体"}

[[如果设备支持以太网通道接口（]{style="font-family:宋体"}[Eth-channel]{lang="EN-US"}]{#struct_0_17060_20103_x81716648}[），则接口下可以同时开启]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向功能和]{style="font-family:宋体"}[Portal]{lang="EN-US"}[功能，否则当接口下同时开启]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向功能和]{style="font-family:宋体"}[Portal]{lang="EN-US"}[功能时，]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向功能失效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17060_20103_113146932}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17060_20103_1375433367}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1640278300}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv4 Web]{lang="EN-US"}[重定向功能：]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向地址为]{style="font-family:宋体"}[http://192.0.0.1]{lang="EN-US"}[，]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向周期为]{style="font-family:宋体"}[3600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_1375761047}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[GigabitEthernet1/0/1]{lang="EN-US"}[\] web-redirect url http://192.0.0.1 interval 3600]{lang="EN-US"}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[]{lang="EN-US"}]{#struct_0_17060_20103_x1845772273}[[交换应用]{lang="EN-US" style="font-family:宋体"}]{.ItemStepChar}

[[\# ]{lang="EN-US"}]{#struct_0_17060_20103_1375826583}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv4 Web]{lang="EN-US"}[重定向功能：]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向地址为]{style="font-family:宋体"}[http://192.0.0.1]{lang="EN-US"}[，]{style="font-family:宋体"}[Web]{lang="EN-US"}[重定向周期为]{style="font-family:宋体"}[3600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17060_20103_1375629975}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname--Vlan-interface100\] web-redirect url http://192.0.0.1 interval 3600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17060_20103_x1784079541}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display web-redirect rule]{lang="EN-US"}**]{#struct_0_17060_20103_1375695511}
:::
