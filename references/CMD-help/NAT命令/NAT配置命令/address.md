
**NAT命令 \-- NAT配置命令 \-- address**

------------------------------------------------------------------------

**[address**]命令用来添加一个地址组成员。

**[undo address**]命令用来删除一个地址组成员。

【命令】

**[address ***start-address end-address*]

**[undo address ***start-address end-address*]

【缺省情况】

不存在地址组成员。

【视图】

NAT地址组视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

*[start-address end-address*]：地址组成员的起始IP地址和结束IP地址。*end-address*必须大于或等于*start-address*，如果*start-address*和*end-address*相同，则表示只有一个地址。

【使用指导】

一个NAT地址组是多个地址组成员的集合。当需要对到达外部网络的数据报文进行地址转换时，报文的源地址将被转换为地址组成员中的某个地址。

需要注意的是：

·一个地址组成员所包含的地址数目不能超过256。

·各地址组成员的IP地址段不能互相重叠。

·在多形态防火墙设备上，配置的所有地址组成员包含的地址总数不能少于安全引擎（或安全插卡）的数量。

【举例】

\# 在NAT地址组2中添加两个地址组成员。

\<Sysname\> system-view

Sysname nat address-group 2

Sysname-address-group-2 address 10.1.1.1 10.1.1.15

Sysname-address-group-2 address 10.1.1.20 10.1.1.30

【相关命令】

·**nat address-group**

**NAT命令 \-- NAT配置命令 \-- block-size**

------------------------------------------------------------------------

**[block-size**]命令用来设置端口块大小。

**[undo**]**block-size**命令用来将端口块大小恢复为默认值。

【命令】

**[block-size** *block-size*]

**[undo** **block-size**]

【缺省情况】

一个端口块中包含256个端口。

【视图】

NAT端口块组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[block-size*]：端口块大小，即一个端口块中所包含的端口数，取值范围为1～*max_number*。其中*max_number*的取值与设备的型号有关，请以设备的实际情况为准。

【使用指导】

在一个端口块组中，需要根据私网IP地址个数，以及公网IP地址个数及其端口范围，确定一个合理的端口块大小值。端口块大小值不能超过公网地址的端口范围值。

【举例】

\# 配置端口块组1的端口块大小为1024。

\<Sysname\> system-view

Sysname nat port-block-group 1

Sysname-port-block-group-1 block-size 1024

【相关命令】

·**nat port-block-group**

**NAT命令 \-- NAT配置命令 \-- display nat all**

------------------------------------------------------------------------

**[display nat all**]命令用来显示所有的NAT配置信息。

【命令】

**[display nat all**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示所有的NAT配置信息。（集中式设备）

\<Sysname\> display nat all

NAT address group information:

  Totally 5 NAT address groups.

  Address group 1:

    Port range: 1-65535

    Address information:

      Start address         End address

      202.110.10.10         202.110.10.15

  Address group 2:

    Port range: 1-65535

    Address information:

      Start address         End address

      202.110.10.20         202.110.10.25

      202.110.10.30         202.110.10.35

  Address group 3:

    Port range: 1024-65535

    Address information:

      Start address         End address

      202.110.10.40         202.110.10.50

  Address group 4:

    Port range: 10001-65535

    Port block size: 500

    Extended block number: 1

    Address information:

      Start address         End address

      202.110.10.60         202.110.10.65

  Address group 6:

    Port range: 1-65535

    Address information:

      Start address         End address

      \-\--                   \-\--

NAT server group information:

  Totally 3 NAT server groups.

  Group Number        Inside IP             Port        Weight

  1                   192.168.0.26          23          100

                      192.168.0.27          23          500

  2                   \-\--                   \-\--         \-\--

  3                   192.168.0.26          69          100

NAT inbound information:

  Totally 1 NAT inbound rules.

  Interface: GigabitEthernet1/0/2

    ACL: 2038         Address group: 2      Add route: Y

    NO-PAT:Y         Reversible: N

    VPN instance: vpn_nat

    Config status: Active

NAT outbound information:

  Totally 2 NAT outbound rules.

  Interface: GigabitEthernet1/0/1

    ACL: 2036         Address group: 1      Port-preserved: Y

    NO-PAT: N         Reversible: N

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: address group, and ACL.

  Interface: GigabitEthernet1/0/1

    ACL: 2037         Address group: 1      Port-preserved: N

    NO-PAT: Y         Reversible: Y

    VPN instance: vpn_nat

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: ACL.

NAT internal server information:

  Totally 4 internal servers.

  Interface: GigabitEthernet1/0/3

    Protocol: 6(TCP)

    Global IP/port: 50.1.1.1/23

    Local IP/port : 192.168.10.15/23

    ACL           : 2000

    Config status : Active

  Interface: GigabitEthernet1/0/4

    Protocol: 6(TCP)

    Global IP/port: 50.1.1.1/23-30

    Local IP/port : 192.168.10.15-192.168.10.22/23

    Global VPN    : vpn1

    Local VPN     : vpn3

    Config status : Active

  Interface: GigabitEthernet1/0/4

    Protocol: 255(Reserved)

    Global IP/port: 50.1.1.100/\-\--

    Local IP/port : 192.168.10.150/\-\--

    Global VPN    : vpn2

    Local VPN     : vpn4

    ACL           : 3000

    Config status : Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, and ACL.

  Interface: GigabitEthernet1/0/5

    Protocol: 17(UDP)

    Global IP/port: 50.1.1.2/23

    Local IP/port : server group 1

                    1.1.1.1/21            (Connections: 10)

                    192.168.100.200/80    (Connections: 20)

    Global VPN    : vpn1

    Local VPN     : vpn3

    Config status : Active

Static NAT mappings:

  Totally 2 inbound static NAT mappings.

  Net-to-net:

    Global IP    : 2.2.2.1 -- 2.2.2.255

    Local IP     : 1.1.1.0

    Netmask      : 255.255.255.0

    Global VPN   : vpn2

    Local VPN    : vpn1

    ACL          : 3000

    Reversible   : Y

    Config status: Active

  IP-to-IP:

    Global IP    : 5.5.5.5

    Local IP     : 4.4.4.4

    Global VPN   : vpn3

    Local VPN    : vpn4

    ACL          : 2001

    Reversible   : Y

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, global VPN, and ACL.

  Totally 2 outbound static NAT mappings.

  Net-to-net:

    Local IP     : 1.1.1.1 - 1.1.1.255

    Global IP    : 2.2.2.0

    Netmask      : 255.255.255.0

    Local VPN    : vpn1

    Global VPN   : vpn2

    ACL          : 3000

    Reversible   : Y

    Config status: Active

  IP-to-IP:

    Local IP     : 4.4.4.4

    Global IP    : 5.5.5.5

    Local VPN    : vpn1

    Global VPN   : vpn2

    ACL:         : 2001

    Reversible   : Y

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: ACL.

Interfaces enabled with static NAT:

  Totally 2 interfaces enabled with static NAT.

  Interface: GigabitEthernet1/0/2

    Config status: Active

  Interface: GigabitEthernet1/0/3

    Config status: Active

NAT DNS mappings:

  Totally 2 NAT DNS mappings.

  Domain name  : www.server.com

  Global IP    : 6.6.6.6

  Global port  : 23

  Protocol     : TCP(6)

  Config status: Active

  Domain name  : www.service.com

  Global IP    : \-\--

  Global port  : 12

  Protocol     : TCP(6)

  Config status: Inactive

  Reasons for inactive status:

    The following items don\'t exist or aren\'t effective: interface IP address.

NAT logging:

  Log enable          : Enabled(ACL 2000)

  Flow-begin          : Disabled

  Flow-end            : Disabled

  Flow-active         : Enabled(10 minutes)

  Port-block-assign   : Disabled

  Port-block-withdraw : Disabled

  Alarm               : Disabled

NAT hairpinning:

  Totally 2 interfaces enabled with NAT hairpinning.

  Interface: GigabitEthernet1/0/1

    Config status: Active

  Interface: GigabitEthernet1/0/2

    Config status: Active

NAT mapping behavior:

  Mapping mode : Endpoint-Independent

  ACL          : 2050

  Config status: Active

NAT ALG:

  DNS        : Enabled

  FTP        : Disabled

  H323       : Enabled

  ICMP-ERROR : Enabled

  ILS        : Enabled

  MGCP       : Enabled

  NBT        : Enabled

  PPTP       : Enabled

  RSH        : Enabled

  RTSP       : Enabled

  SCCP       : Enabled

  SIP        : Disabled

  SQLNET     : Enabled

  TFTP       : Enabled

  XDMCP      : Enabled

NAT port block group information:

  Totally 3 NAT port block groups.

  Port block group 1:

    Port range: 1-65535

    Block size: 256

    Local IP address information:

      Start address        End address          VPN instance

      172.16.1.1           172.16.1.254         \-\--

      192.168.1.1          192.168.1.254        vpna

      192.168.3.1          192.168.3.254        vpna

    Global IP pool information:

      Start address        End address

      201.1.1.1            201.1.1.10

      201.1.1.21           201.1.1.25

  Port block group 2:

    Port range: 10001-30000

    Block size: 500

    Local IP address information:

      Start address        End address          VPN instance

      10.1.1.1             10.1.10.255          vpnb

    Global IP pool information:

      Start address        End address

      202.10.10.101        202.10.10.120

  Port block group 3:

    Port range: 1-65535

    Block size: 256

    Local IP address information:

      Start address        End address          VPN instance

      \-\--                  \-\--                  \-\--

    Global IP pool information:

      Start address        End address

      \-\--                  \-\--

NAT outbound port block group information:

  Totally 2 outbound port block group items.

  Interface: GigabitEthernet1/0/2

    Port block group: 2

    Config status   : Active

  Interface: GigabitEthernet1/0/2

    Port block group: 10

    Config status   : Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: port block group.

\# 显示所有的NAT配置信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display nat all

NAT address group information:

  Totally 5 NAT address groups.

  Address group 1:

    Port range: 1-65535

    Address information:

      Start address         End address

      202.110.10.10         202.110.10.15

  Address group 2:

    Port range: 1-65535

    Address information:

      Start address         End address

      202.110.10.20         202.110.10.25

      202.110.10.30         202.110.10.35

  Address group 3:

    Port range: 1024-65535

    Address information:

      Start address         End address

      202.110.10.40         202.110.10.50

  Address group 4:

    Port range: 10001-65535

    Port block size: 500

    Extended block number: 1

    Address information:

      Start address         End address

      202.110.10.60         202.110.10.65

  Address group 6:

    Port range: 1-65535

    Address information:

      Start address         End address

      \-\--                   \-\--

NAT server group information:

  Totally 3 NAT server groups.

  Group Number        Inside IP             Port        Weight

  1                   192.168.0.26          23          100

                      192.168.0.27          23          500

  2                   \-\--                   \-\--         \-\--

  3                   192.168.0.26          69          100

NAT inbound information:

  Totally 1 NAT inbound rules.

  Interface: GigabitEthernet1/0/1

    ACL: 2038         Address group: 2      Add route: Y

    NO-PAT: Y         Reversible: N

    VPN instance: vpn_nat

    Service card: Slot 2

    Config status: Active

    Global flow-table status: Active

NAT outbound information:

  Totally 2 NAT outbound rules.

  Interface: GigabitEthernet1/0/2

    ACL: 2036         Address group: 1      Port-preserved: Y

    NO-PAT: N         Reversible: N

    Service card: \-\--

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: address group, and ACL.

      Service card not specified.

    Global flow-table status: Active

  Interface: GigabitEthernet1/0/2

    ACL: 2037         Address group: 1      Port-preserved: N

    NO-PAT: Y         Reversible: Y

    VPN instance: vpn_nat

    Service card: \-\--

    Config status: Inactive

    Reasons for inactive status:

      Service card not specified.

    Global flow-table status: Active

NAT internal server information:

  Totally 4 internal servers.

  Interface: GigabitEthernet1/0/3

    Protocol: 6(TCP)

    Global IP/port: 50.1.1.1/23

    Local IP/port : 192.168.10.15/23

    ACL           : 2000

    Service card  : Slot 2

    Config status : Active

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/0/4

    Protocol: 6(TCP)

    Global IP/port: 50.1.1.1/23-30

    Local IP/port : 192.168.10.15-192.168.10.22/23

    Global VPN    : vpn1

    Local VPN     : vpn3

    Service card  : Slot 2

    Config status : Active

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/0/4

    Protocol: 255(Reserved)

    Global IP/port: 50.1.1.100/\-\--

    Local IP/port : 192.168.10.150/\-\--

    Global VPN    : vpn2

    Local VPN     : vpn4

    ACL           : 3000

    Service card  : Slot 2

    Config status : Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, and ACL.

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/0/5

    Protocol: 17(UDP)

    Global IP/port: 50.1.1.2/23

    Local IP/port : server group 1

                    192.168.0.26/23       (Connections: 10)

                    192.168.0.27/23       (Connections: 20)

    Global VPN    : vpn1

    Local VPN     : vpn3

    Service card  : Slot 2

    Config status : Active

    Global flow-table status: Active

    Local flow-table status: Active

Static NAT mappings:

  Totally 2 inbound static NAT mappings.

  Net-to-net:

    Global IP    : 2.2.2.1 -- 2.2.2.255

    Local IP     : 1.1.1.0

    Netmask      : 255.255.255.0

    Global VPN   : vpn2

    Local VPN    : vpn1

    ACL          : 2000

    Reversible   : Y

    Config status: Active

    Global flow-table status: Active

    Local flow-table status: Active

  IP-to-IP:

    Global IP    : 5.5.5.5

    Local IP     : 4.4.4.4

    Global VPN   : vpn3

    Local VPN    : vpn4

    ACL          : 2001

    Reversible   : Y

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, global VPN, and ACL.

    Global flow-table status: Active

    Local flow-table status: Active

  Totally 2 outbound static NAT mappings.

  Net-to-net:

    Local IP     : 1.1.1.1 - 1.1.1.255

    Global IP    : 2.2.2.0

    Netmask      : 255.255.255.0

    Local VPN    : vpn1

    Global VPN   : vpn2

    ACL          : 2000

    Reversible   : Y

    Config status: Active

    Global flow-table status: Active

    Local flow-table status: Active

  IP-to-IP:

    Local IP     : 4.4.4.4

    Global IP    : 5.5.5.5

    Local VPN    : vpn1

    Global VPN   : vpn2

    ACL:         : 2001

    Reversible   : Y

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: ACL.

    Global flow-table status: Active

    Local flow-table status: Active

Interfaces enabled with static NAT:

  Totally 2 interfaces enabled with static NAT.

  Interface: GigabitEthernet1/0/4

    Service card : Slot 2

    Config status: Active

  Interface: GigabitEthernet1/0/6

    Service card : \-\--

    Config status: Inactive

    Reasons for inactive status:

      Service card not specified.

NAT DNS mappings:

  Totally 2 NAT DNS mappings.

  Domain name  : www.server.com

  Global IP    : 6.6.6.6

  Global port  : 23

  Protocol     : TCP(6)

  Config status: Active

  Domain name  : www.service.com

  Global IP    : \-\--

  Global port  : 12

  Protocol     : TCP(6)

  Config status: Inactive

  Reasons for inactive status:

    The following items don\'t exist or aren\'t effective: interface IP address.

NAT logging:

  Log enable          : Enabled(ACL 2000)

  Flow-begin          : Disabled

  Flow-end            : Disabled

  Flow-active         : Enabled(10 minutes)

  Port-block-assign   : Disabled

  Port-block-withdraw : Disabled

  Alarm               : Disabled

NAT hairpinning:

  Totally 2 interfaces enabled with NAT hairpinning.

  Interface: GigabitEthernet1/0/4

    Service card : Slot 2

    Config status: Active

  Interface: GigabitEthernet1/0/6

    Service card : Slot 2

    Config status: Active

NAT mapping behavior:

  Mapping mode : Endpoint-Independent

  ACL          : 2050

  Config status: Active

NAT ALG:

  DNS        : Enabled

  FTP        : Enabled

  H323       : Enabled

  ICMP-ERROR : Enabled

  ILS        : Enabled

  MGCP       : Enabled

  NBT        : Enabled

  PPTP       : Enabled

  RTSP       : Enabled

  RSH        : Enabled

  SCCP       : Enabled

  SIP        : Enabled

  SQLNET     : Enabled

  TFTP       : Enabled

  XDMCP      : Disabled

NAT port block group information:

  Totally 3 NAT port block groups.

  Port block group 1:

    Port range: 1-65535

    Block size: 256

    Local IP address information:

      Start address        End address          VPN instance

      172.16.1.1           172.16.1.254         \-\--

      192.168.1.1          192.168.1.254        vpna

      192.168.3.1          192.168.3.254        vpna

    Global IP pool information:

      Start address        End address

      201.1.1.1            201.1.1.10

      201.1.1.21           201.1.1.25

  Port block group 2:

    Port range: 10001-30000

    Block size: 500

    Local IP address information:

      Start address        End address          VPN instance

      10.1.1.1             10.1.10.255          vpnb

    Global IP pool information:

      Start address        End address

      202.10.10.101        202.10.10.120

  Port block group 3:

    Port range: 1-65535

    Block size: 256

    Local IP address information:

      Start address        End address          VPN instance

      \-\--                  \-\--                  \-\--

    Global IP pool information:

      Start address        End address

      \-\--                  \-\--

NAT outbound port block group information:

Totally 2 outbound port block group items.

  Interface: GigabitEthernet1/0/2

    Port block group: 2

    Config status   : Active

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/0/2

    Port block group: 10

    Config status   : Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: port block group.

    Global flow-table status: Active

    Local flow-table status: Active

\# 显示所有的NAT配置信息。（分布式设备－IRF模式）

\<Sysname\> display nat all

NAT address group information:

  Totally 5 NAT address groups.

  Address group 1:

    Port range: 1-65535

    Address information:

      Start address         End address

      202.110.10.10         202.110.10.15

  Address group 2:

    Port range: 1-65535

    Address information:

      Start address         End address

      202.110.10.20         202.110.10.25

      202.110.10.30         202.110.10.35

  Address group 3:

    Port range: 1024-65535

    Address information:

      Start address         End address

      202.110.10.40         202.110.10.50

  Address group 4:

    Port range: 10001-65535

    Port block size: 500

    Extended block number: 1

    Address information:

      Start address         End address

      202.110.10.60         202.110.10.65

  Address group 6:

    Port range: 1-65535

    Address information:

      Start address         End address

      \-\--                   \-\--

NAT server group information:

  Totally 3 NAT server groups.

  Group Number        Inside IP             Port        Weight

  1                   192.168.0.26          23          100

                      192.168.0.27          23          500

  2                   \-\--                   \-\--         \-\--

  3                   192.168.0.26          69          100

NAT inbound information:

  Totally 1 NAT inbound rules.

  Interface: GigabitEthernet1/3/0/1

    ACL: 2038         Address group: 2      Add route: Y

    NO-PAT: Y         Reversible: N

    VPN instance: vpn_nat

    Service card: Chassis 2 Slot 5

    Config status: Active

    Global flow-table status: Active

NAT outbound information:

  Totally 2 NAT outbound rules.

  Interface: GigabitEthernet1/3/0/2

    ACL: 2036         Address group: 1      Port-preserved: Y

    NO-PAT: N         Reversible: N

    Service card: \-\--

    Config status: Inactive

    Reasons for inactive status:

      Service card not specified.

    Global flow-table status: Active

  Interface: GigabitEthernet1/3/0/2

    ACL: 2037         Address group: 1      Port-preserved: N

    NO-PAT: Y         Reversible: Y

    VPN instance: vpn_nat

    Service card: \-\--

    Config status: Inactive

    Reasons for inactive status:

      Service card not specified.

    Global flow-table status: Active

NAT internal server information:

  Totally 4 internal servers.

  Interface: GigabitEthernet1/3/0/3

    Protocol: 6(TCP)

    Global IP/port: 50.1.1.1/23

    Local IP/port : 192.168.10.15/23

    ACL           : 2000

    Service card  : Chassis 2 Slot 5

    Config status : Active

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/3/0/4

    Protocol: 6(TCP)

    Global IP/port: 50.1.1.1/23-30

    Local IP/port : 192.168.10.15-192.168.10.22/23

    Global VPN    : vpn1

    Local VPN     : vpn3

    Service card  : Chassis 2 Slot 5

    Config status : Active

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/3/0/4

    Protocol: 255(Reserved)

    Global IP/port: 50.1.1.100/\-\--

    Local IP/port : 192.168.10.150/\-\--

    Global VPN    : vpn2

    Local VPN     : vpn4

    ACL           : 3000

    Service card  : Chassis 2 Slot 5

    Config status : Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, and ACL.

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/3/0/5

    Protocol: 17(UDP)

    Global IP/port: 50.1.1.2/23

    Local IP/port : server group 1

                    192.168.0.26/23       (Connections: 10)

                    192.168.0.27/23       (Connections: 20)

    Global VPN    : vpn1

    Local VPN     : vpn3

    Service card  : Chassis 2 Slot 5

    Config status : Active

    Global flow-table status: Active

    Local flow-table status: Active

Static NAT mappings:

  Totally 2 inbound static NAT mappings.

  Net-to-net:

    Global IP : 2.2.2.1 -- 2.2.2.255

    Local IP  : 1.1.1.0

    Netmask   : 255.255.255.0

    Global VPN: vpn2

    Local VPN : vpn1

    ACL       : 2000

    Reversible: Y

    Config status: Active

    Global flow-table status: Active

    Local flow-table status: Active

  IP-to-IP:

    Global IP : 5.5.5.5

    Local IP  : 4.4.4.4

    Global VPN: vpn3

    Local VPN : vpn4

    ACL       : 2001

    Reversible: Y

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, global VPN, and ACL.

    Global flow-table status: Active

    Local flow-table status: Active

  Totally 2 outbound static NAT mappings.

  Net-to-net:

    Local IP  : 1.1.1.1 - 1.1.1.255

    Global IP : 2.2.2.0

    Netmask   : 255.255.255.0

    Local VPN : vpn1

    Global VPN: vpn2

    ACL       : 2000

    Reversible: Y

    Config status: Active

    Global flow-table status: Active

    Local flow-table status: Active

  IP-to-IP:

    Local IP  : 4.4.4.4

    Global IP : 5.5.5.5

    Local VPN : vpn1

    Global VPN: vpn2

    ACL:      : 2001

    Reversible: Y

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: ACL.

    Global flow-table status: Active

    Local flow-table status: Active

Interfaces enabled with static NAT:

  Totally 2 interfaces enabled with static NAT.

  Interface: GigabitEthernet1/3/0/4

    Service card : Chassis 2 Slot 5

    Config status: Active

  Interface: GigabitEthernet1/3/0/6

    Service card : \-\--

    Config status: Inactive

    Reasons for inactive status:

      Service card not specified.

NAT DNS mappings:

  Totally 2 NAT DNS mappings.

  Domain name  : www.server.com

  Global IP    : 6.6.6.6

  Global port  : 23

  Protocol     : TCP(6)

  Config status: Active

  Domain name  : www.service.com

  Global IP    : \-\--

  Global port  : 12

  Protocol     : TCP(6)

  Config status: Inactive

  Reasons for inactive status:

    The following items don\'t exist or aren\'t effective: interface IP address.

NAT logging:

  Log enable          : Enabled(ACL 2000)

  Flow-begin          : Disabled

  Flow-end            : Disabled

  Flow-active         : Enabled(10 minutes)

  Port-block-assign   : Disabled

  Port-block-withdraw : Disabled

  Alarm               : Disabled

NAT hairpinning:

  Totally 2 interfaces enabled with NAT hairpinning.

  Interface: GigabitEthernet1/3/0/1

    Service card : Chassis 2 Slot 5

    Config status: Active

  Interface: GigabitEthernet1/3/0/2

    Service card : Chassis 2 Slot 5

    Config status: Active

NAT mapping behavior:

  Mapping mode : Endpoint-Independent

  ACL          : 2050

  Config status: Active

NAT ALG:

  DNS        : Enabled

  FTP        : Enabled

  H323       : Enabled

  ICMP-ERROR : Enabled

  ILS        : Enabled

  MGCP       : Enabled

  NBT        : Enabled

  PPTP       : Enabled

  RTSP       : Enabled

  RSH        : Enabled

  SCCP       : Enabled

  SIP        : Enabled

  SQLNET     : Enabled

  TFTP       : Enabled

  XDMCP      : Disabled

NAT port block group information:

  Totally 3 NAT port block groups.

  Port block group 1:

    Port range: 1-65535

    Block size: 256

    Local IP address information:

      Start address        End address          VPN instance

      172.16.1.1           172.16.1.254         \-\--

      192.168.1.1          192.168.1.254        vpna

      192.168.3.1          192.168.3.254        vpna

    Global IP pool information:

      Start address        End address

      201.1.1.1            201.1.1.10

      201.1.1.21           201.1.1.25

  Port block group 2:

    Port range: 10001-30000

    Block size: 500

    Local IP address information:

      Start address        End address          VPN instance

      10.1.1.1             10.1.10.255          vpnb

    Global IP pool information:

      Start address        End address

      202.10.10.101        202.10.10.120

  Port block group 3:

    Port range: 1-65535

    Block size: 256

    Local IP address information:

      Start address        End address          VPN instance

      \-\--                  \-\--                  \-\--

    Global IP pool information:

      Start address        End address

      \-\--                  \-\--

NAT outbound port block group information:

Totally 2 outbound port block group items.

  Interface: GigabitEthernet1/3/0/2

    Port block group: 2

    Config status   : Active

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/3/0/2

    Port block group: 10

    Config status   : Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: port block group.

    Global flow-table status: Active

    Local flow-table status: Active

上述显示信息是目前所有NAT配置信息的集合。由于部分NAT配置（**nat address-group**、**nat server-group**、**nat inbound**、**nat outbound**、**nat server**、**nat static**、**nat static net-to-net**、**nat static enable**、**nat dns-map**、**nat log**、**nat port-block-group**和**nat outbound port-block-group**）有自己独立的显示命令，且此处显示信息的格式与各命令对应的显示信息的格式相同的，所以此处不对这些配置的显示字段的含义进行写详细解释，如有需要，请参考各独立的显示命令。下面的表格将给出相关显示命令的参见信息并仅解释**nat hairpin enable**、**nat mapping-behavior**和**nat alg**配置的显示字段的含义。

表1-1 display nat all命令显示信息描述表

字段

描述

NAT address group information

NAT地址组的配置信息，详细字段解释请参见"[表]1-2(?212897139#_Ref332718363)"

NAT server group information

NAT内部服务器组的配置信息，详细字段解释请参见"[表]1-13(?-2052594180#_Ref334106521)"

NAT inbound information:

入方向动态地址转换的配置信息，详细字段解释请参见" 表1-5(?-1724764660#_Ref334104209)"

NAT outbound information

出方向动态地址转换的配置信息，详细字段解释请参见" 表1-8(?-1864024100#_Ref334105167)"

NAT internal server information

NAT内部服务器的配置信息，详细字段解释请参见"[表]1-12(?-347761546#_Ref334105524)"

Static NAT mappings

静态地址转换的配置信息，详细字段解释请参见" 表1-15(?1118470241#_Ref334167313)"

NAT DNS mappings

NAT DNS mapping的配置信息，详细字段解释请参见"[表]1-3(?-891847204#_Ref334101543)"

NAT logging

NAT日志功能的配置信息，详细字段解释请参见"[表]1-6(?-463444198#_Ref334104166)"

NAT hairpinning

NAT hairpin功能

Totally *n* interfaces enabled NAT hairpinning

当前有*n*个接口使能NAT hairpin功能

Interface

使能NAT hairpin功能的接口

Service card

显示提供NAT处理的业务板。如果接口下没有指定业务板，则显示为"\-\--"

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Config status

显示NAT hairpin配置的状态

·Active：生效

·Inactive：不生效

Reasons for inactive status

当Config status字段为Inactive时，显示NAT hairpin配置不生效的原因

·Service card not specified：没有指定提供NAT处理的业务板

NAT mapping behavior

PAT方式下的地址转换模式

·Endpoint-Independent：表示不关心对端地址和端口

·Address and Port-Dependent：表示关心对端地址和端口

ACL

引用的ACL编号。如果没有配置，则显示"\-\--"

Config status

显示NAT mapping behavior配置的状态

·Active：生效

·Inactive：不生效

Reasons for inactive status

当Config status字段为Inactive时，显示NAT mapping behavior配置不生效的原因

·The following items don\'t exist or aren\'t effective: ACL：引用的ACL不存在

Global flow-table status

针对Global地址下发流表的状态

·Active：生效

·Inactive：不生效

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Local  flow-table status

针对Local地址下发流表的状态

·Active：生效

·Inactive：不生效

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Reasons for flow-table inactive status

当下发流表的状态为Inactive时，显示流表不生效的原因

其中，Not enough resources are available to complete the operation表示因为资源不足导致下发流表失败

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

NAT ALG

各协议的NAT ALG功能开启信息

NAT port block group information

NAT端口块组的配置信息，详细字段解释请参见"[表]1-11(?-367314176#_Ref363572644)"

NAT outbound port block group information

NAT444端口块静态映射的配置信息，详细字段解释请参见"[表]1-9(?1628387509#_Ref363572645)"

**NAT命令 \-- NAT配置命令 \-- display nat address-group**

------------------------------------------------------------------------

**[display nat address-group**]命令用来显示NAT地址组配置信息。

【命令】

**[display nat address-group** [ *group-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator**

【参数】

*[group-number*]**：**地址组编号，取值范围为[0～]*max_number*。其中*max_number*的取值与设备的型号有关，请以设备的实际情况为准。如果不设置该值，则显示所有地址组。

【举例】

\# 显示所有地址组的配置信息。

\<Sysname\> display nat address-group

NAT address group information:

  Totally 5 NAT address groups.

  Address group 1:

    Port range: 1-65535

    Address information:

      Start address         End address

      202.110.10.10         202.110.10.15

  Address group 2:

    Port range: 1-65535

    Address information:

      Start address         End address

      202.110.10.20         202.110.10.25

      202.110.10.30         202.110.10.35

  Address group 3:

    Port range: 1024-65535

    Address information:

      Start address         End address

      202.110.10.40         202.110.10.50

  Address group 4:

    Port range: 10001-65535

    Port block size: 500

    Extended block number: 1

    Address information:

      Start address         End address

      202.110.10.60         202.110.10.65

  Address group 6:

    Port range: 1-65535

    Address information:

      Start address         End address

      \-\--                   \-\--

\# 显示指定地址组的配置信息。

\<Sysname\> display nat address-group 1

  Address group 1:

    Port range: 1-65535

    Address information:

      Start address         End address

      202.110.10.10         202.110.10.15

表1-2 display nat address-group命令显示信息描述表

字段

描述

NAT address group information

NAT地址组信息

Totally *n* NAT address groups

当前有*n*个地址组

Address group

地址组编号

Port range

地址的端口范围

Block size

端口块大小。如果没有配置，则不显示

Extended block number

增量端口块数。如果没有配置，则不显示

Address information

地址组成员信息

Start address

地址组成员的起始地址。如果没有配置，则显示"\-\--"

End address

地址组成员的结束地址。如果没有配置，则显示"\-\--"

【相关命令】

·**nat address-group**

**NAT命令 \-- NAT配置命令 \-- display nat dns-map**

------------------------------------------------------------------------

**[display nat dns-map**]命令用来显示NAT DNS mapping配置信息。

【命令】

**[display nat dns-map**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator**

【举例】

\# 显示所有NAT DNS mapping的配置信息。

\<Sysname\> display nat dns-map

NAT DNS mapping information:

  Totally 2 NAT DNS mappings.

  Domain name  : www.server.com

  Global IP    : 6.6.6.6

  Global port  : 23

  Protocol     : TCP(6)

  Config status: Active

  Domain name  : www.service.com

  Global IP    : \-\--

  Global port  : 12

  Protocol     : TCP(6)

  Config status: Inactive

  Reasons for inactive status:

    The following items don\'t exist or aren\'t effective: interface IP address.

表1-3 display nat dns-map命令显示信息描述表

字段

描述

NAT DNS mapping information

NAT DNS mapping配置信息

Totally *n* NAT DNS mappings

当前有*n*条DNS mapping配置

Domain name

DNS域名

Global IP

外网地址。如果配置使用的是Easy IP方式，则此处显示指定的接口的地址。"\-\--"表示接口下没有配置外网地址

Global port

外网端口号

Protocol

协议名称以及协议编号

Config status

显示DNS mapping配置的状态

·Active：生效

·Inactive：不生效

Reasons for inactive status

当Config status字段为Inactive时，显示DNS mapping配置不生效的原因

·The following items don\'t exist or aren\'t effective: interface IP address：引用的接口没有配置IP地址

【相关命令】

·**nat dns-map**

**NAT命令 \-- NAT配置命令 \-- display nat eim**

------------------------------------------------------------------------

**[display nat eim**]命令用来显示NAT EIM表项信息。

【命令】

集中式设备：

**[display nat eim**]

分布式设备－独立运行模式/集中式IRF设备：

**[display nat eim ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display nat eim ****chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator**

【参数】

**[slot ***slot-number*]：显示指定单板上的EIM表项信息，*slot-number*表示单板所在的槽位号。若不指定该参数，则表示显示所有单板上的EIM表项信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的EIM表项信息，*slot-number*表示设备在IRF中的成员编号。若不指定该参数，则表示显示所有成员设备上的EIM表项信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的EIM表项信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则表示显示所有成员设备/PEX上的EIM表项信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的EIM表项信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。若不指定该参数，则表示显示所有成员设备的所有单板上的EIM表项信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的EIM表项信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若不指定该参数，则表示显示所有单板上的EIM表项信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的EIM表项信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

EIM表项是报文在进行Endpoint-Independent Mapping方式的PAT转换时创建的，它记录了内网和外网的转换关系（内网地址和端口\<\--\>NAT地址和端口），该表项有以下两个作用：

·保证后续来自相同源地址和源端口的新建连接与首次连接使用相同的转换关系。

·允许外网主机向NAT地址和端口发起的新建连接根据EIM表项进行反向地址转换。

【举例】

\# 显示NAT EIM表项的信息。（集中式设备）

\<Sysname\> display nat eim

Local  IP/port: 192.168.100.100/1024

Global IP/port: 200.100.1.100/2048

Local  VPN: vpn1

Global VPN: vpn2

Protocol: TCP(6)

Local  IP/port: 192.168.100.200/2048

Global IP/port: 200.100.1.200/4096

Protocol: UDP(17)

Total entries found: 2

\# 显示1号单板上的NAT EIM表项信息。（分布式设备－独立运行模式）

\<Sysname\> display nat eim slot 1

Slot 1:

Local  IP/port: 192.168.100.100/1024

Global IP/port: 200.100.1.100/2048

Local  VPN: vpn1

Global VPN: vpn2

Protocol: TCP(6)

Local  IP/port: 192.168.100.200/2048

Global IP/port: 200.100.1.200/4096

Protocol: UDP(17)

Total entries found: 2

\# 显示1号成员设备上的NAT EIM表项信息。（集中式IRF设备）

\<Sysname\> display nat eim slot 1

Slot 1:

Local  IP/port: 192.168.100.100/1024

Global IP/port: 200.100.1.100/2048

Local  VPN: vpn1

Global VPN: vpn2

Protocol: TCP(6)

Local  IP/port: 192.168.100.200/2048

Global IP/port: 200.100.1.200/4096

Protocol: UDP(17)

Total entries found: 2

\# 显示1号成员设备的1号单板上的NAT EIM表项信息。（分布式设备－IRF模式）

\<Sysname\> display nat eim chassis 1 slot 0

Slot 0 in chassis 1:

Local  IP/port: 192.168.100.100/1024

Global IP/port: 200.100.1.100/2048

Local  VPN: vpn1

Global VPN: vpn2

Protocol: TCP(6)

Local  IP/port: 192.168.100.200/2048

Global IP/port: 200.100.1.200/4096

Protocol: UDP(17)

Total entries found: 2

\# 显示1号单板的0号CPU上的NAT EIM表项信息。（分布式设备－独立运行模式）

\<Sysname\> display nat eim slot 1 cpu 0

CPU 0 on slot 1:

Local  IP/port: 192.168.100.100/1024

Global IP/port: 200.100.1.100/2048

Local  VPN: vpn1

Global VPN: vpn2

Protocol: TCP(6)

Local  IP/port: 192.168.100.200/2048

Global IP/port: 200.100.1.200/4096

Protocol: UDP(17)

Total entries found: 2

\# 显示1号成员设备上的0号CPU的NAT EIM表项信息。（集中式IRF设备）

\<Sysname\> display nat eim slot 1 cpu 0

CPU 0 on slot 1:

Local  IP/port: 192.168.100.100/1024

Global IP/port: 200.100.1.100/2048

Local  VPN: vpn1

Global VPN: vpn2

Protocol: TCP(6)

Local  IP/port: 192.168.100.200/2048

Global IP/port: 200.100.1.200/4096

Protocol: UDP(17)

Total entries found: 2

\# 显示1号成员设备的1号单板的0号CPU上的NAT EIM表项信息。（分布式设备－IRF模式）

\<Sysname\> display nat eim chassis 1 slot 1 cpu 0

CPU 0 on slot 1 in chassis 1:

Local  IP/port: 192.168.100.100/1024

Global IP/port: 200.100.1.100/2048

Local  VPN: vpn1

Global VPN: vpn2

Protocol: TCP(6)

Local  IP/port: 192.168.100.200/2048

Global IP/port: 200.100.1.200/4096

Protocol: UDP(17)

Total entries found: 2

表1-4 display nat eim命令显示信息描述表

字段

描述

Local IP/port

内网IP地址/端口号

Global IP/port

外网IP地址/端口号

Local VPN

内网地址所属的MPLS L3VPN的VPN实例名称。如果不属于任何VPN，则不显示该字段

Global VPN

外网地址所属的MPLS L3VPN的VPN实例名称。如果不属于任何VPN，则不显示该字段

Protocol

协议名称以及协议编号

Total entries found

当前查找到的EIM表项的个数

【相关命令】

·**nat mapping-behavior**

·**nat outbound**

**NAT命令 \-- NAT配置命令 \-- display nat inbound**

------------------------------------------------------------------------

**[display nat inbound**]命令用来显示NAT入方向动态地址转换的配置信息。

【命令】

**[display nat inbound**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator**

【举例】

\# 显示NAT入接口动态地址转换的配置信息。（集中式设备）

\<Sysname\> display nat inbound

NAT inbound information:

  Totally 2 NAT inbound rules.

  Interface: GigabitEthernet1/0/2

    ACL: 2038         Address group: 2      Add route: Y

    NO-PAT: Y         Reversible: N

    VPN instance: vpn1

    Config status: Active

Interface: GigabitEthernet1/0/3

    ACL: 2037         Address group: 1      Add route: Y

    NO-PAT: Y         Reversible: N

    VPN instance: vpn2

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, and ACL.

\# 显示NAT入接口动态地址转换的配置信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display nat inbound

NAT inbound information:

  Totally 2 NAT inbound rules.

  Interface: GigabitEthernet1/0/2

    ACL: 2038         Address group: 2      Add route: Y

    NO-PAT: Y         Reversible: N

    VPN instance: vpn1

    Service card: Slot 5

    Config status: Active

    Global flow-table status: Active

Interface: GigabitEthernet1/0/3

    ACL: 2037         Address group: 1      Add route: Y

    NO-PAT: Y         Reversible: N

    VPN instance: vpn2

    Service card: \-\--

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, and ACL.

      Service card not specified.

Global flow-table status: Active

\# 显示NAT入接口动态地址转换的配置信息。（分布式设备－IRF模式设备）

\<Sysname\> display nat inbound

NAT inbound information:

  Totally 2 NAT inbound rules.

  Interface: GigabitEthernet1/3/0/2

    ACL: 2038         Address group: 2      Add route: Y

    NO-PAT: Y         Reversible: N

    VPN instance: vpn1

    Service card: Chassis 2 slot 5

    Config status: Active

    Global flow-table status: Active

Interface: GigabitEthernet1/3/0/3

    ACL: 2037         Address group: 1      Add route: Y

    NO-PAT: Y         Reversible: N

    VPN instance: vpn2

    Service card: \-\--

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, and ACL.

      Service card not specified.

    Global flow-table status: Active

表1-5 display nat inbound命令显示信息描述表

字段

描述

NAT inbound information

NAT入方向动态地址转换的配置信息

Totally *n* NAT inbound rules

当前存在*n*条入入方向动态地址转换配置

Interface

入方向动态地址转换配置所在的接口

ACL

引用的ACL编号

Address group

入方向动态地址转换使用的地址组

Add route

是否添加路由。若其值为"Y"，则表示有报文命中此项入接口动态地址转换配置时，设备会自动添加一条路由；否则，不添加

NO-PAT

是否使用NO-PAT方式进行地址转换。若其值为"Y"，则表示使用NO-PAT方式；若其值为"N"，则表示使用PAT方式

Reversible

是否允许反向地址转换。若其值为"Y"，则表示在某方向上发起的连接已成功建立地址转换表项的情况下，允许反方向发起的连接使用已建立的地址转换表项进行地址转换；否则，不允许

VPN instance

地址组所属的MPLS L3VPN的VPN实例名称。如果不属于任何VPN，则不显示该字段

Service card

显示提供NAT处理的业务板。如果接口下没有指定业务板，则显示为"\-\--"

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Config status

显示NAT配置的状态

·Active：生效

·Inactive：不生效

Reasons for inactive status

当Config status字段为Inactive时，显示NAT入方向动态地址转换的配置不生效的原因

·The following items don\'t exist or aren\'t effective: local VPN, address group, and ACL：配置中地址组所属的VPN实例、地址组、ACL不存在或不生效

·Service card not specified：没有指定提供NAT处理业务板

Global flow-table status

针对Global地址下发流表的状态

·Active：生效

·Inactive：不生效

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Reasons for flow-table inactive status

当下发流表的状态为Inactive时，显示流表不生效的原因

其中，Not enough resources are available to complete the operation表示因为资源不足导致下发流表失败

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

【相关命令】

·**nat inbound**

**NAT命令 \-- NAT配置命令 \-- display nat log**

------------------------------------------------------------------------

**[display nat log**]命令用来显示NAT日志功能的配置信息。

【命令】

**[display nat log**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator**

【举例】

\# 显示NAT日志功能的配置信息。

\<Sysname\> display nat log

NAT logging:

  Log enable          : Enabled(ACL 2000)

  Flow-begin          : Disabled

  Flow-end            : Disabled

  Flow-active         : Enabled(10 minutes)

  Port-block-assign   : Disabled

  Port-block-withdraw : Disabled

  Alarm               : Disabled

表1-6 display nat log命令显示信息描述表

字段

描述

NAT logging

NAT日志功能的配置信息

Log enable

NAT日志开关的开启情况。如果NAT日志开关处于开启状态，且指定了ACL，则同时显示指定的ACL编号

Flow-begin

NAT会话新建日志开关的开启情况

Flow-end

NAT会话删除日志开关的开启情况

Flow-active

NAT活跃流日志开关的开启情况以及阈值信息。如果NAT活跃流日志开关处于开启状态，则同时显示配置的生成活跃流日志的时间间隔（单位为分）

Port-block-assign

端口块分配的NAT444用户日志开关的开启情况

Port-block-withdraw

端口块回收的NAT444用户日志开关的开启情况

Alarm

NAT444告警信息日志开关的开启情况

【相关命令】

·**nat log enable**

·**nat log flow-active**

·**nat log flow-begin**

**NAT命令 \-- NAT配置命令 \-- display nat no-pat**

------------------------------------------------------------------------

**[display nat no-pat**]命令用来显示NAT NO-PAT表项信息。

【命令】

集中式设备：

**[display nat no-pat**]

分布式设备－独立运行模式/集中式IRF设备：

**[display nat no-pat ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display nat no-pat ****chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator**

【参数】

**[slot ***slot-number*]：显示指定单板上的NO-PAT表项信息，*slot-number*表示单板所在的槽位号。若不指定该参数，则表示显示所有单板上的NO-PAT表项信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的NO-PAT表项信息，*slot-number*表示设备在IRF中的成员编号。若不指定该参数，则表示显示所有成员设备上的NO-PAT表项信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的NO-PAT表项信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则表示显示所有成员设备/PEX上的NO-PAT表项信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的NO-PAT表项信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。若不指定该参数，则表示显示所有成员设备的所有单板上的NO-PAT表项信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的NO-PAT表项信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若不指定该参数，则表示显示所有单板上的NO-PAT表项信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的NO-PAT表项信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

NO-PAT表项记录了动态分配的一对一地址映射关系，该表项有两个作用：

·保证后续同方向的新连接使用与第一个连接相同的地址转换关系。

·反方向的新连接可以使用NO-PAT表进行地址转换。

**[nat inbound**]和**nat outbound**配置的NO-PAT方式在转换报文地址之后都需要创建NO-PAT表。这两种配置创建的NO-PAT表类型不同，不能互相使用，因此分成两类进行显示。

【举例】

\# 显示NAT NO-PAT表项。（集中式设备）

\<Sysname\> display nat no-pat

Global  IP: 200.100.1.100

Local   IP: 192.168.100.100

Global VPN: vpn2

Local  VPN: vpn1

Reversible: N

Type      : Inbound

Local   IP: 192.168.100.200

Global  IP: 200.100.1.200

Reversible: Y

Type      : Outbound

Total entries found: 2

\# 显示1号单板上的NAT NO-PAT表项。（分布式设备－独立运行模式）

\<Sysname\> display nat no-pat slot 1

Slot 1:

Global  IP: 200.100.1.100

Local   IP: 192.168.100.100

Global VPN: vpn2

Local  VPN: vpn1

Reversible: N

Type      : Inbound

Local   IP: 192.168.100.200

Global  IP: 200.100.1.200

Reversible: Y

Type      : Outbound

Total entries found: 2

\# 显示1号成员设备的NAT NO-PAT表项。（集中式IRF设备）

\<Sysname\> display nat no-pat slot 1

Slot 1:

Global  IP: 200.100.1.100

Local   IP: 192.168.100.100

Global VPN: vpn2

Local  VPN: vpn1

Reversible: N

Type      : Inbound

Local   IP: 192.168.100.200

Global  IP: 200.100.1.200

Reversible: Y

Type      : Outbound

Total entries found: 2

\# 显示1号成员设备的1号单板上的NAT NO-PAT表项。（分布式设备－IRF模式）

\<Sysname\> display nat no-pat chassis 1 slot 1

Slot 1 in chassis 1:

Global  IP: 200.100.1.100

Local   IP: 192.168.100.100

Global VPN: vpn2

Local  VPN: vpn1

Reversible: N

Type      : Inbound

Local   IP: 192.168.100.200

Global  IP: 200.100.1.200

Reversible: Y

Type      : Outbound

Total entries found: 2

\# 显示1号单板的0号CPU上的NAT NO-PAT表项。（分布式设备－独立运行模式）

\<Sysname\> display nat no-pat slot 1 cpu 0

CPU 0 on slot 1:

Global  IP: 200.100.1.100

Local   IP: 192.168.100.100

Global VPN: vpn2

Local  VPN: vpn1

Reversible: N

Type      : Inbound

Local   IP: 192.168.100.200

Global  IP: 200.100.1.200

Reversible: Y

Type      : Outbound

Total entries found: 2

\# 显示1号成员设备的0号CPU的NAT NO-PAT表项。（集中式IRF设备）

\<Sysname\> display nat no-pat slot 1 cpu 0

CPU 0 on slot 1:

Global  IP: 200.100.1.100

Local   IP: 192.168.100.100

Global VPN: vpn2

Local  VPN: vpn1

Reversible: N

Type      : Inbound

Local   IP: 192.168.100.200

Global  IP: 200.100.1.200

Reversible: Y

Type      : Outbound

Total entries found: 2

\# 显示1号成员设备的1号单板的0号CPU上的NAT NO-PAT表项。（分布式设备－IRF模式）

\<Sysname\> display nat no-pat chassis 1 slot 1 cpu 0

CPU 0 on slot 1 in chassis 1:

Global  IP: 200.100.1.100

Local   IP: 192.168.100.100

Global VPN: vpn2

Local  VPN: vpn1

Reversible: N

Type      : Inbound

Local   IP: 192.168.100.200

Global  IP: 200.100.1.200

Reversible: Y

Type      : Outbound

Total entries found: 2

表1-7 display nat no-pat命令显示信息描述表

字段

描述

Local IP

内网IP地址

Global IP

外网IP地址

Local VPN

内网地址所属的MPLS L3VPN的实例名称。如果不属于任何VPN，则该行不显示

Global VPN

外网地址所属的MPLS L3VPN的实例名称。如果不属于任何VPN，则该行不显示

Reversible

是否允许反向地址转换。若其值为"Y"，则表示在某方向上发起的连接已成功建立地址转换表项的情况下，允许反方向发起的连接使用已建立的地址转换表项进行地址转换

Type

NO-PAT表项类型

Inbound：入方向动态地址转换过程中创建的NO-PAT表项

Outbound：出方向动态地址转换过程中创建的NO-PAT表项

Total entries found

当前查找到的NO-PAT表项的个数

【相关命令】

·**nat inbound**

·**nat outbound**

**NAT命令 \-- NAT配置命令 \-- display nat outbound**

------------------------------------------------------------------------

**[display nat outbound**]命令用来显示出方向动态地址转换的配置信息。

【命令】

**[display nat outbound**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator**

【举例】

\# 显示出方向动态地址转换的配置信息。（集中式设备）

\<Sysname\> display nat outbound

NAT outbound information:

  Totally 2 NAT outbound rules.

  Interface: GigabitEthernet1/0/1

    ACL: 2036         Address group: 1      Port-preserved: Y

    NO-PAT: N         Reversible: N

    Config status: Active

  Interface: GigabitEthernet1/0/1

    ACL: 2037         Address group: \-\--    Port-preserved: N

    NO-PAT: Y         Reversible: Y

    VPN instance: vpn_nat

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: global VPN, and ACL

  Interface: GigabitEthernet1/0/1

    DS-Lite B4 ACL: 2100         Address group: 0      Port-preserved: N

    NO-PAT: N         Reversible: N

    Config status: Active

\# 显示出方向动态地址转换的配置信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display nat outbound

NAT outbound information:

  Totally 2 NAT outbound rules.

  Interface: GigabitEthernet1/0/1

    ACL: 2036         Address group: 1      Port-preserved: Y

    NO-PAT: N         Reversible: N

    Service card: Slot 5

    Config status: Active

    Global flow-table status: Active

  Interface: GigabitEthernet1/0/2

    ACL: 2037         Address group: 2      Port-preserved: N

    NO-PAT: Y         Reversible: Y

    VPN instance: vpn_nat

    Service card: Slot 5

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: global VPN, and ACL.

      Service card not specified.

    Global flow-table status: Active

  Interface: GigabitEthernet1/0/1

    DS-Lite B4 ACL: 2100         Address group: 0      Port-preserved: N

    NO-PAT: N         Reversible: N

    Service card: Slot 5

    Config status: Active

\# 显示出方向动态地址转换的配置信息。（分布式设备－IRF模式）

\<Sysname\> display nat outbound

NAT outbound information:

  Totally 2 NAT outbound rules.

  Interface: GigabitEthernet1/3/0/1

    ACL: 2036         Address group: 1      Port-preserved: Y

    NO-PAT: N         Reversible: N

    Service card: Chassis 2 Slot 5

    Config status: Active

    Global flow-table status: Active

  Interface: GigabitEthernet1/3/0/2

    ACL: 2037         Address group: 1      Port-preserved: N

    NO-PAT: Y         Reversible: Y

    VPN instance: vpn_nat

    Service card: \-\--

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: global VPN, and ACL.

      Service card not specified.

    Global flow-table status: Active

  Interface: GigabitEthernet3/0/1

    DS-Lite B4 ACL: 2100         Address group: 0      Port-preserved: N

    NO-PAT: N         Reversible: N

    Service card: Chassis 2 Slot 5

    Config status: Active

表1-8 display nat outbound命令显示信息描述表

字段

描述

NAT outbound information

出方向动态地址转换的配置信息

Totally *n* NAT outbound rules

当前存在*n*条出方向动态地址转换

Interface

出方向动态地址转换配置所在的接口

ACL

引用的IPv4 ACL编号。如果没有配置，则显示"\-\--"

DS-Lite B4 ACL

DS-Lite B4引用的IPv6 ACL编号

Address group

出方向动态地址转换使用的地址组。如果没有配置，则显示"\-\--"

Port-preserved

PAT方式下，是否尽量不转换端口

NO-PAT

是否使用NO-PAT方式进行转换。若其值为"N"，则表示使用PAT方式

Reversible

是否允许反向地址转换。若其值为"Y"，则表示在某方向上发起的连接已成功建立地址转换表项的情况下，允许反方向发起的连接使用已建立的地址转换表项进行地址转换

VPN instance

地址组所属的MPLS L3VPN的VPN实例名称。如果不属于任何VPN，则不显示该字段

Service card

显示提供NAT处理的业务板。如果接口下没有指定业务板，则显示为"\-\--"

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Config status

显示配置的状态

·Active：生效

·Inactive：不生效

Reasons for inactive status

当Config status字段为Inactive时，显示配置不生效的原因

·The following items don\'t exist or aren\'t effective: global VPN, interface IP address, address group, and ACL：配置中地址组所属的VPN实例、接口地址、地址组、ACL不存在或不生效

·Service card not specified：没有指定提供NAT处理的业务板

·NAT address conflicts：NAT地址冲突

Global flow-table status

针对Global地址下发流表的状态

·Active：生效

·Inactive：不生效

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Reasons for flow-table inactive status

当下发流表状态为Inactive时，显示流表不生效的原因

其中，Not enough resources are available to complete the operation表示因为资源不足导致下发流表失败

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

【相关命令】

·**nat outbound**

**NAT命令 \-- NAT配置命令 \-- display nat outbound port-block-group**

------------------------------------------------------------------------

**[display nat outbound port-block-group**]命令用来显示NAT444端口块静态映射的配置信息。

【命令】

**[display nat outbound port-block-group**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示NAT444端口块静态映射的配置信息。

\<Sysname\> display nat outbound port-block-group

NAT outbound port block group information:

  Totally 2 outbound port block group items.

  Interface: GigabitEthernet1/0/2

    Port block group: 2

    Config status   : Active

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/0/2

    Port block group: 10

    Config status   : Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: port block group.

    Global flow-table status: Active

    Local flow-table status: Active

表1-9 display nat outbound port-block-group 命令显示信息描述表

字段

描述

NAT outbound port block group information

NAT444端口块静态映射的配置信息

Totally *n*outbound port block group items

当前存在*n*条NAT444端口块静态映射配置

Interface

NAT444端口块静态映射配置所在的接口

Port block group

端口块组编号

Config status

显示配置的状态

·Active：生效

·Inactive：不生效

Reasons for inactive status

当Config status字段为Inactive时，显示配置不生效的原因

·The following items don\'t exist or aren\'t effective: port block group：配置中端口块组不存在或不生效

Global flow-table status

针对Global地址下发流表的状态

·Active：生效

·Inactive：不生效

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Local  flow-table status

针对Local地址下发流表的状态

·Active：生效

·Inactive：不生效

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Reasons for flow-table inactive status

当下发流表的状态为Inactive时，显示流表不生效的原因

其中，Not enough resources are available to complete the operation表示因为资源不足导致下发流表失败

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

【相关命令】

l**nat outbound port-block-group**

**NAT命令 \-- NAT配置命令 \-- display nat port-block**

------------------------------------------------------------------------

**[display nat port-block**]命令用来显示端口块表项。

【命令】

集中式设备：

**[display nat port-block **{ **dynamic** [ **ds-lite-b4**  \| **static** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display nat port-block **{ **dynamic** [ **ds-lite-b4**  \| **static** }  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display nat port-block **{ **dynamic** [ **ds-lite-b4**  \| **static** } ]**chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dynamic**]：显示动态端口块表项。

**[ds-lite-b4**]：显示基于DS-Lite B4地址的端口块表项。

**[static**]：显示静态端口块表项。

**[slot ***slot-number*]：显示指定单板上的端口块表项信息，*slot-number*表示单板所在的槽位号。若不指定该参数，则表示显示所有单板上的端口块表项信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的端口块表项信息，*slot-number*表示设备在IRF中的成员编号。若不指定该参数，则表示显示所有成员设备上的端口块表项信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的端口块表项信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则表示显示所有成员设备/PEX上的端口块表项信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的端口块表项信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。若不指定该参数，则表示显示所有成员设备的所有单板上的端口块表项信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的端口块表项信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若不指定该参数，则表示显示所有单板上的端口块表项信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的端口块表项信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示静态端口块表项。

\<Sysname\> display nat port-block static

Static port-block mapping tables:

Local VPN     Local IP         Global IP        Port block   Connections

\-\--           100.100.100.111  202.202.100.101  10001-10256  0

\-\--           100.100.100.112  202.202.100.101  10257-10512  0

\-\--           100.100.100.113  202.202.100.101  10513-10768  0

vpn012345678  100.100.100.113  202.202.100.101  10769-11024  0

901234567890

1234567

Total entries found: 4

\# 显示动态端口块表项。

\<Sysname\> display nat port-block dynamic

Dynamic port-block mapping tables:

Local VPN     Local IP         Global IP        Port block   Connections

\-\--           101.1.1.12       192.168.135.201  10001-11024  1

Total entries found: 1

\# 显示基于DS-Lite B4地址的端口块表项。

\<Sysname\> display nat port-block dynamic ds-lite-b4

Local VPN     DS-Lite B4 addr  Global IP        Port block   Connections

\-\--           2000::2          192.168.135.201  10001-11024  1

Total entries found: 1

表1-10 display nat port-block 命令显示信息描述表

字段

描述

Static port-block mapping tables

静态端口块表项信息

Dynamic port-block mapping tables

动态端口块表项信息

Local VPN

私网IP地址所属VPN，"\-\--"表示不属于任何VPN

Local IP

私网IP地址

DS-Lite B4 addr

DS-Lite B4设备的IPv6地址

Global IP

公网IP地址

Port block

端口块（起始端口-结束端口）

Connections

当前使用本端口块中的端口建立的连接数

**NAT命令 \-- NAT配置命令 \-- display nat port-block-group**

------------------------------------------------------------------------

**[display nat port-block-group**]命令用来显示NAT端口块组配置信息。

【命令】

**[display nat port-block-group** [ *group-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-number*]：端口块组编号，取值范围为0～*max_number*。其中*max_number*的取值与设备的型号有关，请以设备的实际情况为准。如果不设置该值，则显示所有端口块组的配置信息。

【举例】

\# 显示所有端口块组的配置信息。

\<Sysname\> display nat port-block-group

NAT port block group information:

  Totally 3 NAT port block groups.

  Port block group 1:

    Port range: 1-65535

    Block size: 256

    Local IP address information:

      Start address        End address          VPN instance

      172.16.1.1           172.16.1.254         \-\--

      192.168.1.1          192.168.1.254        vpna

      192.168.3.1          192.168.3.254        vpna

    Global IP pool information:

      Start address        End address

      201.1.1.1            201.1.1.10

      201.1.1.21           201.1.1.25

  Port block group 2:

    Port range: 10001-30000

    Block size: 500

    Local IP address information:

      Start address        End address          VPN instance

      10.1.1.1             10.1.10.255          vpnb

    Global IP pool information:

      Start address        End address

      202.10.10.101        202.10.10.120

  Port block group 3:

    Port range: 1-65535

    Block size: 256

    Local IP address information:

      Start address        End address          VPN instance

      \-\--                  \-\--                  \-\--

    Global IP pool information:

      Start address        End address

      \-\--                  \-\--

\# 显示端口块组1的配置信息。

\<Sysname\> display nat port-block-group 1

  Port block group 1:

    Port range: 1-65535

    Block size: 256

    Local IP address information:

      Start address        End address          VPN instance

      172.16.1.1           172.16.1.254         \-\--

      192.168.1.1          192.168.1.254        vpna

      192.168.3.1          192.168.3.254        vpna

    Global IP pool information:

      Start address        End address

      201.1.1.1            201.1.1.10

      201.1.1.21           201.1.1.25

表1-11 display nat port-block-group 命令显示信息描述表

字段

描述

NAT port block group information

NAT端口块组信息

Totally *n* NAT port block groups

当前有*n*个端口块组

Port block group *m*

端口块组编号*m*

Port range

公网地址的端口范围

Block size

端口块大小

Local IP address information

私网IP地址成员信息

Global IP pool information

公网IP地址成员信息

Start address

私网/公网IP地址成员的起始IP地址。如果没有配置，则显示"\-\--"

End address

私网/公网IP地址成员的成员结束IP地址。如果没有配置，则显示"\-\--"

VPN instance

私网IP地址成员所属的VPN。如果没有配置，则显示"\-\--"

【相关命令】

·**nat port-block-group**

**NAT命令 \-- NAT配置命令 \-- display nat server**

------------------------------------------------------------------------

**[display nat server**]命令用来显示NAT内部服务器的配置信息。

【命令】

**[display nat server**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator**

【举例】

\# 显示NAT内部服务器的信息。（集中式设备）

\<Sysname\> display nat server

NAT internal server information:

  Totally 4 internal servers.

  Interface: GigabitEthernet1/0/3

    Protocol: 6(TCP)

    Global IP/port: 50.1.1.1/23

    Local IP/port : 192.168.10.15/23

    Config status : Active

  Interface: GigabitEthernet1/0/4

    Protocol: 6(TCP)

    Global IP/port: 50.1.1.1/23-30

    Local IP/port : 192.168.10.15-192.168.10.22/23

    Global VPN    : vpn1

    Local VPN     : vpn3

    Config status : Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN.

  Interface: GigabitEthernet1/0/4

    Protocol: 255(Reserved)

    Global IP/port: 50.1.1.100/\-\--

    Local IP/port : 192.168.10.150/\-\--

    Global VPN    : vpn2

    Local VPN     : vpn4

    Config status : Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: interface IP address.

  Interface: GigabitEthernet1/0/5

    Protocol: 17(UDP)

    Global IP/port: 50.1.1.2/23

    Local IP/port : server group 1

                    1.1.1.1/21            (Connections: 10)

                    192.168.100.200/80    (Connections: 20)

    Global VPN    : vpn1

    Local VPN     : vpn3

    Config status : Active

\# 显示NAT内部服务器的信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display nat server

NAT internal server information:

  Totally 4 internal servers.

  Interface: GigabitEthernet1/0/3

    Protocol: 6(TCP)

    Global IP/port: 50.1.1.1/23

    Local IP/port : 192.168.10.15/23

    Service card  : \-\--

    Config status : Inactive

    Reasons for inactive status:

      Service card not specified.

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/0/4

    Protocol: 6(TCP)

    Global IP/port: 50.1.1.1/23-30

    Local IP/port : 192.168.10.15-192.168.10.22/23

    Global VPN    : vpn1

    Local VPN     : vpn3

    Service card  : \-\--

    Config status : Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN.

      Service card not specified.

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/0/4

    Protocol: 255(Reserved)

    Global IP/port: 50.1.1.100/\-\--

    Local IP/port : 192.168.10.150/\-\--

    Global VPN    : vpn2

    Local VPN     : vpn4

    Service card  : Slot 5

    Config status : Active

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/0/5

    Protocol: 17(UDP)

    Global IP/port: 50.1.1.2/23

    Local IP/port : server group 1

                    1.1.1.1/21            (Connections: 10)

                    192.168.100.200/80    (Connections: 20)

    Global VPN    : vpn1

    Local VPN     : vpn10

    Service card  : Slot 5

    Config status : Active

    Global flow-table status: Active

    Local flow-table status: Active

\# 显示NAT内部服务器的信息。（分布式设备－IRF模式）

\<Sysname\> display nat server

NAT internal server information:

  Totally 4 internal servers.

  Interface: GigabitEthernet1/3/0/3

    Protocol: 6(TCP)

    Global IP/port: 50.1.1.1/23

    Local IP/port : 192.168.10.15/23

    Service card  : \-\--

    Config status : Inactive

    Reasons for inactive status:

      Service card not specified.

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/3/0/4

    Protocol: 6(TCP)

    Global IP/port: 50.1.1.1/23-30

    Local IP/port : 192.168.10.15-192.168.10.22/23

    Global VPN    : vpn1

    Local VPN     : vpn3

    Service card  : \-\--

    Config status : Inactive

    Reasons for inactive status:

      Service card not specified.

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/3/0/4

    Protocol: 255(Reserved)

    Global IP/port: 50.1.1.100/\-\--

    Local IP/port : 192.168.10.150/\-\--

    Global VPN    : vpn2

    Local VPN     : vpn4

    Service card  : Chassis 2 Slot 5

    Config status : Active

    Global flow-table status: Active

    Local flow-table status: Active

  Interface: GigabitEthernet1/3/0/5

    Protocol: 17(UDP)

    Global IP/port: 50.1.1.2/23

    Local IP/port : server group 1

                    1.1.1.1/21            (Connections: 10)

                    192.168.100.200/80    (Connections: 20)

    Global VPN    : vpn1

    Local VPN     : vpn3

    Service card  : Chassis 2 Slot 5

    Config status : Active

    Global flow-table status: Active

    Local flow-table status: Active

表1-12 display nat server命令显示信息描述表

字段

描述

NAT internal server information

NAT内部服务器的配置信息

Totally *n* internal servers

当前存在*n*条内部服务器配置

Interface

内部服务器配置所在的接口

Protocol

内部服务器的协议编号以及协议名称

Global IP/port

内部服务器的外网地址/端口号

·Global IP可以是单个地址，也可以是一个连续的地址段。如果使用Easy IP方式，则此处显示指定的接口的地址；如果接口下没有配置地址，则Global IP显示为"\-\--"

·port可以是单个端口，也可以是一个连续的端口段。如果指定的协议没有端口的概念，则port显示为"\-\--"

Local IP/port

对于普通内部服务器，显示服务器的内网地址/端口号

·Local IP可以是单个地址，也可以是一个连续的地址段

·port可以是单个端口，也可以是一个连续的端口段。如果指定的协议没有端口的概念，则port显示为"\-\--"

对于负载分担内部服务器，显示内部服务器组编号以及服务器组成员的IP地址、端口和连接数

Global VPN

外网地址所属的MPLS L3VPN的VPN实例名称。如果不属于任何VPN，则不显示该字段

Local VPN

内网地址所属的MPLS L3VPN的VPN实例名称。 如果不属于任何VPN，则不显示该字段

ACL

引用的ACL编号。如果没有配置，则不显示该字段

Service card

显示提供NAT处理的业务板。如果接口下没有指定业务板，则显示为"\-\--"

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Config status

显示配置的状态

·Active：生效

·Inactive：不生效

Reasons for inactive status

当Config status字段为Inactive时，显示配置不生效的原因

·The following items don\'t exist or aren\'t effective: local VPN, global VPN, interface IP address, server group, and ACL：配置中内网地址所属的VPN实例、外网地址所属的VPN实例、接口地址、服务器组、ACL不存在或不生效

·Service card not specified：没有指定提供NAT处理的业务板

·Server configuration conflicts：NAT内部服务器配置冲突

·NAT address conflicts：NAT地址冲突

Global flow-table status

针对Global地址下发流表的状态

·Active：生效

·Inactive：不生效

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Local  flow-table status

针对Local地址下发流表的状态

·Active：生效

·Inactive：不生效

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Reasons for flow-table inactive status

当下发流表的状态为Inactive时，显示流表不生效的原因

其中，Not enough resources are available to complete the operation表示因为资源不足导致下发流表失败

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

【相关命令】

·**nat server**

**NAT命令 \-- NAT配置命令 \-- display nat server-group**

------------------------------------------------------------------------

**[display nat server-group**]命令用来显示NAT内部服务器组的配置信息。

【命令】

**[display nat server-group ** *group-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator**

【参数】

*[group-number*]：NAT内部服务器组编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果不设置该值，则显示所有内部服务器组。

【举例】

\# 显示所有NAT内部服务器组的配置信息。

\<Sysname\> display nat server-group

NAT server group information:

  Totally 3 NAT server groups.

  Group Number        Inside IP             Port        Weight

  1                   192.168.0.26          23          100

                      192.168.0.27          23          500

  2                   \-\--                   \-\--         \-\--

  3                   192.168.0.26          69          100

\# 显示指定NAT内部服务器组的配置信息。

\<Sysname\> display nat server-group 1

  Group Number        Inside IP             Port        Weight

  1                   192.168.0.26          23          100

                      192.168.0.27          23          500

表1-13 display nat server-group命令显示信息描述表

字段

描述

NAT server group information

NAT内部服务器组信息

Totally *n* NAT server groups

当前有*n*个内部服务器组

Group Number

内部服务器组编号

Inside IP

内部服务器组成员在内网的IP地址。如果没有配置，则显示"\-\--"

Port

内部服务器组成员在内网的端口。如果没有配置，则显示"\-\--"

Weight

内部服务器组成员的权重值。如果没有配置，则显示"\-\--"

【相关命令】

·**nat server-group**

**NAT命令 \-- NAT配置命令 \-- display nat session**

------------------------------------------------------------------------

**[display nat session**]命令用来显示NAT会话，即经过NAT地址转换处理的会话。

【命令】

集中式设备：

**[display nat session **[[ { **source-ip** *source-ip* \| **destination-ip** *destination-ip* } \* ]] **vpn-instance** *vpn-name* ]  **verbose**

分布式设备－独立运行模式/集中式IRF设备：

**[display nat session **[[ { **source-ip** *source-ip* \| **destination-ip** *destination-ip* } \*]  **vpn-instance** *vpn -name* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]

分布式设备－IRF模式：

**[display nat session **[[ { **source-ip** *source-ip* \| **destination-ip** *destination-ip* } \* ]] **vpn-instance** *vpn -name* ] \**chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator**

【参数】

**[source-ip** *source-ip*]：显示指定源地址的会话。*source-ip*表示源地址，该地址必须是创建会话的报文的源地址。

**[destination-ip** *destination-ip*]：显示指定目的地址的会话。*destination-ip*表示目的地址，该地址必须是创建会话的报文的目的地址。

**[vpn-instance**]* vpn-name*：显示指定目的VPN的会话。*vpn-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。该VPN必须是报文中携带的VPN。如果不指定该参数，则显示目的IP不属于任何VPN的会话。

**[slot ***slot-number*]：显示指定单板上的NAT会话，*slot-number*表示单板所在的槽位号。若不指定该参数，则显示所有单板上的NAT会话（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的NAT会话，*slot-number*表示设备在IRF中的成员编号。若不指定该参数，则显示所有成员设备上的NAT会话。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的NAT会话，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则表示显示所有成员设备/PEX上的NAT会话。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的NAT会话，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。若不指定该参数，则显示所有成员设备的所有单板上的NAT会话。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的NAT会话，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若不指定该参数，则表示显示所有单板上的NAT会话。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的NAT会话，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[verbose**]：显示NAT会话的详细信息。如果不配置则显示会话的概要信息。

【使用指导】

如果不指定任何参数，则显示所有的NAT会话。

【举例】

\# 显示NAT会话的详细信息。（集中式设备）

\<Sysname\> display nat session verbose

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.10/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 1

\# 显示1号单板上NAT会话的详细信息。（分布式设备－独立运行模式）

\<Sysname\> display nat session slot 1 verbose

Slot 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 1

\# 显示1号成员设备上NAT会话的详细信息。（集中式IRF设备）

\<Sysname\> display nat session slot 1 verbose

Slot 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 1

\# 显示1号成员设备上1号单板的NAT会话的详细信息。（分布式设备－IRF模式）

\<Sysname\> display nat session chassis 1 slot 1 verbose

Slot 1 in chassis 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 1

\# 显示1号单板的0号CPU上NAT会话的详细信息。（分布式设备－独立运行模式）

\<Sysname\> display nat session slot 1 cpu 0 verbose

CPU 0 on slot 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 1

\# 显示1号成员设备的0号CPU上NAT会话的详细信息。（集中式IRF设备）

\<Sysname\> display nat session slot 1 cpu 1verbose

CPU 0 on slot 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 1

\# 显示1号成员设备上1号单板的0号CPU上NAT会话的详细信息。（分布式设备－IRF模式）

\<Sysname\> display nat session chassis 1 slot 1 cpu 0 verbose

CPU 0 on slot 1 in chassis 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 1

表1-14 display nat session命令显示信息描述表

字段

描述

Initiator

发起方的会话信息

Responder

响应方的会话信息

Source IP/port

源IP地址/端口号

Destination IP/port

目的IP地址/端口号

DS-Lite tunnel peer

DS-Lite隧道对端地址。会话不属于任何DS-Lite隧道时，本字段显示为"-"

VPN instance/VLAN ID/VLL ID

会话所属的MPLS L3VPN/二层转发时会话所属的VLAN ID/二层转发时会话所属的INLINE。如果未指定则显示"-/-/-"

Protocol

传输层协议类型，包括：DCCP、ICMP、Raw IP 、SCTP、TCP、UDP、UDP-Lite

Inbound interface

报文的入接口

Source security zone

源安全域，即入接口所属的安全域。若接口不属于任何安全域，则显示为"-"

该参数的支持情况与设备的型号有关，请以设备的实际情况为准

State

会话状态

Application

应用层协议类型，取值包括：FTP、DNS等，OTHER表示未知协议类型，其对应的端口为非知名端口

Start time

会话创建时间

TTL

会话剩余存活时间，单位为秒

Initiator-\>Responder

发起方到响应方的报文数、报文字节数

Responder-\>Initiator

响应方到发起方的报文数、报文字节数

Total sessions found

当前查找到的会话表总数

【相关命令】

·**reset nat session**

**NAT命令 \-- NAT配置命令 \-- display nat static**

------------------------------------------------------------------------

**[display nat static**]命令用来显示NAT静态地址转换的配置信息。

【命令】

**[display nat static**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator**

【举例】

\# 显示NAT静态地址转换的配置信息。（集中式设备）

\<Sysname\> display nat static

Static NAT mappings:

  Totally 2 inbound static NAT mappings.

  Net-to-net:

    Global IP    : 1.1.1.1 - 1.1.1.255

    Local IP     : 2.2.2.0

    Netmask      : 255.255.255.0

    Global VPN   : vpn2

    Local VPN    : vpn1

    ACL          : 2000

    Reversible   : Y

    Config status: Active

  IP-to-IP:

    Global IP    : 5.5.5.5

    Local IP     : 4.4.4.4

    Global VPN   : vpn2

    Local VPN    : vpn1

    ACL          : 2000

    Reversible   : Y

   Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, global VPN, and ACL.

Totally 2 outbound static NAT mappings.

  Net-to-net:

    Local IP     : 1.1.1.1 - 1.1.1.255

    Global IP    : 2.2.2.0

    Netmask      : 255.255.255.0

    Local VPN    : vpn1

    Global VPN   : vpn2

    ACL          : 2000

    Reversible   : Y

    Config status: Active

  IP-to-IP:

    Local IP     : 4.4.4.4

    Global IP    : 5.5.5.5

    Local VPN    : vpn1

    Global VPN   : vpn2

    ACL:         : 2001

    Reversible   : Y

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, and global VPN.

Interfaces enabled with static NAT:

  Totally 2 interfaces enabled with static NAT.

  Interface: GigabitEthernet1/0/2

    Config status: Active

  Interface: GigabitEthernet1/0/3

    Config status: Active

\# 显示NAT静态地址转换的配置信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display nat static

Static NAT mappings:

  Totally 2 inbound static NAT mappings.

  Net-to-net:

    Global IP    : 1.1.1.1 - 1.1.1.255

    Local IP     : 2.2.2.0

    Netmask      : 255.255.255.0

    Global VPN   : vpn2

    Local VPN    : vpn1

    ACL          : 2000

    Reversible   : Y

    Config status: Active

    Global flow-table status: Active

    Local flow-table status: Active

  IP-to-IP:

    Global IP   : 5.5.5.5

    Local IP     : 4.4.4.4

    Global VPN   : vpn3

    Local VPN    : vpn4

    ACL          : 2001

    Reversible   : Y

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, global VPN, and ACL.

    Global flow-table status: Active

    Local flow-table status: Active

Totally 2 outbound static NAT mappings.

  Net-to-net:

    Local IP     : 1.1.1.1 - 1.1.1.255

    Global IP    : 2.2.2.0

    Netmask      : 255.255.255.0

    Local VPN    : vpn1

    Global VPN   : vpn2

    ACL          : 2000

    Reversible   : Y

    Config status: Active

    Global flow-table status: Active

    Local flow-table status: Active

  IP-to-IP:

    Local IP     : 4.4.4.4

    Global IP    : 5.5.5.5

    Local VPN    : vpn4

    Global VPN   : vpn3

    ACL:         : 2000

    Reversible   : Y

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, and global VPN.

    Global flow-table status: Active

    Local flow-table status: Active

Interfaces enabled with static NAT:

  Totally 2 interfaces enabled with static NAT.

  Interface: GigabitEthernet1/0/2

    Service card : Slot 5

    Config status: Active

  Interface: GigabitEthernet1/0/3

    Service card : \-\--

    Config status: Inactive

    Reasons for inactive status:

      Service card not specified.

\# 显示NAT静态地址转换的配置信息。（分布式设备－IRF模式）

\<Sysname\> display nat static

Static NAT mappings:

  Totally 2 inbound static NAT mappings.

  Net-to-net:

    Global IP    : 1.1.1.1 - 1.1.1.255

    Local IP     : 2.2.2.0

    Netmask      : 255.255.255.0

    Global VPN   : vpn2

    Local VPN    : vpn1

    ACL          : 2000

    Reversible   : Y

    Config status: Active

    Global flow-table status: Active

    Local flow-table status: Active

  IP-to-IP:

    Global IP    : 5.5.5.5

    Local IP     : 4.4.4.4

    Global VPN   : vpn3

    Local VPN    : vpn4

    ACL          : 2001

    Reversible   : Y

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, global VPN, and ACL.

    Global flow-table status: Active

    Local flow-table status: Active

Totally 2 outbound static NAT mappings.

  Net-to-net:

    Local IP     : 1.1.1.1 - 1.1.1.255

    Global IP    : 2.2.2.0

    Netmask      : 255.255.255.0

    Local VPN    : vpn1

    Global VPN   : vpn2

    ACL          : 2000

    Reversible   : Y

    Config status: Active

    Global flow-table status: Active

    Local flow-table status: Active

  IP-to-IP:

    Local IP     : 4.4.4.4

    Global IP    : 5.5.5.5

    Local VPN    : vpn4

    Global VPN   : vpn3

    ACL:         : 2000

    Reversible   : Y

    Config status: Inactive

    Reasons for inactive status:

      The following items don\'t exist or aren\'t effective: local VPN, and global VPN.

    Global flow-table status: Active

    Local flow-table status: Active

Interfaces enabled with static NAT:

  Totally 2 interfaces enabled with static NAT.

  Interface: GigabitEthernet1/3/0/2

    Service card : Chassis 2 Slot 5

    Config status: Active

  Interface: GigabitEthernet1/3/0/3

    Service card : Chassis 2 Slot 5

    Config status: Active

表1-15 display nat static命令显示信息描述表

字段

描述

Static NAT mappings

静态地址转换的配置信息

Totally *n* inbound static NAT mappings

当前存在*n*条入方向静态地址转换的配置

Totally *n* outbound static NAT mappings

当前存在*n*条出方向静态地址转换的配置

Net-to-net

网段到网段的静态地址转换映射

IP-to-IP

IP到IP的静态地址转换映射

Local IP

内网IP地址或地址范围

Global IP

外网IP地址或地址范围

Netmask

IP地址掩码

Local VPN

内网地址所属的MPLS L3VPN的VPN实例名称。如果不属于任何VPN，则不显示该字段

Global VPN

外网地址所属的MPLS L3VPN的VPN实例名称。如果不属于任何VPN，则不显示该字段

ACL

引用的ACL编号。如果没有配置，则不显示该字段

Reversible

是否允许反向地址转换。若其值为"Y"，则表示在某方向上发起的连接已成功建立地址转换表项的情况下，允许反方向发起的连接使用已建立的地址转换表项进行地址转换

如果没有配置，则不显示该字段

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Interfaces enabled with static NAT

静态地址转换在接口下的使能情况

Totally *n* interfaces enabled with static NAT

当前有*n*个接口使能了静态地址转换

Interface

使能静态地址转换功能的接口

Service card

显示提供NAT服务的业务板。如果接口下没有指定业务板，则显示为"\-\--"

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Config status

显示配置的状态

·Active：生效

·Inactive：不生效

Reasons for inactive status

当Config status字段为Inactive时，显示配置不生效的原因

·The following items don\'t exist or aren\'t effective: local VPN, global VPN, and ACL：配置中内网地址所属的VPN实例、外网地址所属的VPN实例、ACL不存在或不存在

·Service card not specified：没有指定提供NAT服务的业务板

·NAT address conflicts：NAT地址冲突

Global flow-table status

针对Global地址下发流表的状态

·Active：生效

·Inactive：不生效

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Local  flow-table status

针对Local地址下发流表的状态

·Active：生效

·Inactive：不生效

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Reasons for flow-table inactive status

当下发流表的状态为Inactive时，显示流表不生效的原因

其中，Not enough resources are available to complete the operation表示因为资源不足导致下发流表失败

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

【相关命令】

·**nat static**

·**nat static net-to-net**

·**nat static enable**

**NAT命令 \-- NAT配置命令 \-- display nat statistics**

------------------------------------------------------------------------

**[display nat statistics**]命令用来显示NAT统计信息。

【命令】

集中式设备：

**[display nat** **statistics** [ **summary** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display nat** **statistics** [ **summary**   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display nat** **statistics** [ **summary**  ]**chassis** *chassis-number* **slot** *slot-number* **cpu** *cpu-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator**

【参数】

**[summary**]：显示NAT统计信息的摘要信息。不指定该参数时，显示NAT统计信息的详细信息。

**[slot ***slot-number*]：显示指定单板上的NAT统计信息，*slot-number*表示单板所在的槽位号。若不指定该参数，则显示所有单板上的NAT统计信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的NAT统计信息，*slot-number*表示设备在IRF中的成员编号。若不指定该参数，则显示所有成员设备上的NAT统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的NAT统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则表示显示所有成员设备/PEX上的NAT统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的NAT统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。若不指定该参数，则显示所有成员设备的所有单板上的NAT统计信息。（分布式设备-IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的NAT统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若不指定该参数，则表示显示所有单板上的NAT统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的NAT统计信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示所有NAT统计信息的详细信息。（集中式设备）

\<Sysname\> display nat statistics

  Total session entries: 100

  Total EIM entries: 1

  Total inbound NO-PAT entries: 0

  Total outbound NO-PAT entries: 0

  Total static port block entries: 10

  Total dynamic port block entries: 15

  Active static port block entries: 0

  Active dynamic port block entries: 0

\# 显示所有NAT统计信息的详细信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display nat statistics

Slot 1:

  Total session entries: 100

  Total EIM entries: 1

  Total inbound NO-PAT entries: 0

  Total outbound NO-PAT entries: 0

  Total static port block entries: 10

  Total dynamic port block entries: 15

  Active static port block entries: 0

  Active dynamic port block entries: 0

\# 显示所有NAT统计信息的详细信息。（分布式设备－IRF模式）

\<Sysname\> display nat statistics

Slot 1 in chassis 1:

  Total session entries: 100

  Total EIM entries: 1

  Total inbound NO-PAT entries: 0

  Total outbound NO-PAT entries: 0

  Total static port block entries: 10

  Total dynamic port block entries: 15

  Active static port block entries: 0

  Active dynamic port block entries: 0

\# 显示所有NAT统计信息的详细信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display nat statistics

CPU 0 on slot 1:

  Total session entries: 100

  Total EIM entries: 1

  Total inbound NO-PAT entries: 0

  Total outbound NO-PAT entries: 0

  Total static port block entries: 10

  Total dynamic port block entries: 15

  Active static port block entries: 0

  Active dynamic port block entries: 0

\# 显示所有NAT统计信息的详细信息。（分布式设备－IRF模式）

\<Sysname\> display nat statistics

CPU 0 on slot 1 in chassis 1:

  Total session entries: 100

  Total EIM entries: 1

  Total inbound NO-PAT entries: 0

  Total outbound NO-PAT entries: 0

  Total static port block entries: 10

  Total dynamic port block entries: 15

  Active static port block entries: 0

  Active dynamic port block entries: 0

表1-16 display nat statistics命令显示信息描述表

字段

描述

Total session entries

NAT会话表项个数

Total EIM entries

EIM表项个数

Total inboundNO-PAT entries

入方向的NO-PAT表项个数

Total outboundNO-PAT entries

出方向的NO-PAT表项个数

Total static port block entries

当前配置创建的静态端口块表项个数

Total dynamic port block entries

当前配置可创建的动态端口块表项个数，即可分配的动态端口块总数，包括已分配的端口块和尚未分配的端口块

Active static port block entries

当前正在使用的静态端口块表项个数

Active dynamic port block entries

当前已创建的动态端口块表项个数，即已分配的动态端口块个数

\# 显示所有NAT统计信息的概要信息。（集中式设备）

\<Sysname\> display nat statistics summary

EIM: Total EIM entries.

SPB: Total static port block entries.

DPB: Total dynamic port block entries.

ASPB: Active static port block entries.

ADPB: Active dynamic port block entries.

Sessions  EIM       SPB       DPB       ASPB      ADPB

100       1         10        15        0         0

\# 显示所有NAT统计信息的概要信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display nat statistics summary

EIM: Total EIM entries.

SPB: Total static port block entries.

DPB: Total dynamic port block entries.

ASPB: Active static port block entries.

ADPB: Active dynamic port block entries.

Slot Sessions  EIM       SPB       DPB       ASPB      ADPB

2    0         0         0         1572720   0         0

\# 显示所有NAT统计信息的概要信息。（分布式设备－IRF模式）

\<Sysname\> display nat statistics summary

EIM: Total EIM entries.

SPB: Total static port block entries.

DPB: Total dynamic port block entries.

ASPB: Active static port block entries.

ADPB: Active dynamic port block entries.

Chassis Slot Sessions  EIM       SPB       DPB       ASPB      ADPB

1       2    0         0         0         1572720   0         0

\# 显示所有NAT统计信息的概要信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display nat statistics summary

EIM: Total EIM entries.

SPB: Total static port block entries.

DPB: Total dynamic port block entries.

ASPB: Active static port block entries.

ADPB: Active dynamic port block entries.

Slot CPU Sessions  EIM       SPB       DPB       ASPB      ADPB

2    1   0         0         0         1572720   0         0

\# 显示所有NAT统计信息的概要信息。（分布式设备－IRF模式）

\<Sysname\> display nat statistics summary

EIM: Total EIM entries.

SPB: Total static port block entries.

DPB: Total dynamic port block entries.

ASPB: Active static port block entries.

ADPB: Active dynamic port block entries.

Chassis Slot CPU Sessions  EIM       SPB       DPB       ASPB      ADPB

1       2    1   0         0         0         1572720   0         0

表1-17 display nat statistics summary命令显示信息描述表

字段

描述

Chassis

IRF成员编号（分布式设备－IRF模式）

Slot

单板所在的槽位号（分布式设备－独立运行模式）

IRF中的成员编号（集中式IRF设备）

CPU

CPU编号

Sessions

NAT会话表项个数

EIM

EIM表项个数

SPB

当前配置创建的静态端口块表项个数

DPB

当前配置可创建的动态端口块表项个数，即可分配的动态端口块总数，包括已分配的端口块和尚未分配的端口块

ASPB

当前正在使用的静态端口块表项个数

ADPB

当前已创建的动态端口块表项个数，即已分配的动态端口块个数

**NAT命令 \-- NAT配置命令 \-- global-ip-pool**

------------------------------------------------------------------------

**[global-ip-pool**]命令用来添加一个公网地址成员。

**[undo**]**global-ip-pool**命令用来删除一个公网地址成员。

【命令】

**[global-ip-pool***start-address* *end-address*]

**[undo**]**global-ip-pool***start-address*

【缺省情况】

不存在公网地址成员。

【视图】

NAT端口块组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[start-address end-address*]：公网地址成员的起始IP地址和结束IP地址。*end-address*必须大于或等于*start-address*；如果*start-address*和*end-address*相同，则表示只有一个地址。

【使用指导】

在NAT444端口块静态映射中，端口基于公网地址成员的IP地址为私网地址成员的IP地址分配端口块。一个公网IP地址可对应的端口块个数，由端口块组配置的公网地址端口范围和端口块大小决定（端口范围除以端口块大小）。

需要注意的是：

·一个端口块组内，可以配置多个公网地址成员，但各公网地址成员之间的IP地址不能重叠。

·不同端口块组间的公网地址成员的IP地址可以重叠，但要保证在有地址重叠时端口范围不重叠。

【举例】

\# 在端口块组1中添加一个公网地址成员，IP地址从202.10.1.1到202.10.1.10。

\<Sysname\> system-view

Sysname nat port-block-group 1

Sysname-port-block-group-1 global-ip-pool 202.10.1.1 202.10.1.10

【相关命令】

·**nat port-block-group**

**NAT命令 \-- NAT配置命令 \-- inside ip**

------------------------------------------------------------------------

**[inside ip**]命令用来添加一个内部服务器组成员。

**[undo inside ip**]命令用来删除一个内部服务器组成员。

【命令】

**[inside ip*** inside-ip* **port** *port-number* [ **weight** *weight-value* ]]

**[undo inside**] **ip** *inside-ip* **port** *port-number*

【缺省情况】

内部服务器组内没有内部服务器组成员。

【视图】

内部服务器组视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

*[inside-ip*]：内部服务器组成员的IP地址。

**[port** *port-number*]：内部服务器组成员提供服务的端口号，取值范围为1～65535（FTP数据端口号20除外）。

**[weight **]*weight-value*：内部服务器组成员的权重。*weight-value*表示权值，取值范围为1～1000，缺省为100。

【使用指导】

内部服务器组成员按照权重比例对外提供服务，权重值越大的内部服务器组成员对外提供服务的比重越大。

【举例】

\# 为内部服务器组1添加一个内部服务器组成员，其IP地址为10.1.1.2，服务端口号为30。

\<Sysname\> system-view

Sysname nat server-group 1

Sysname-nat-server-group-1 inside ip 10.1.1.2 port 30

【相关命令】

·**nat server-group**

**NAT命令 \-- NAT配置命令 \-- local-ip-address**

------------------------------------------------------------------------

**[local-ip-address**]命令用来添加一个私网地址成员。

**[undo **]**local-ip-address**命令用来删除一个私网地址成员。

【命令】

**[local-ip-address ***start-address* *end-address* [ **vpn-instance** *vpn-instance-name* ]]

**[undo** **local-ip-address** *start-address* [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

不存在私网地址成员。

【视图】

NAT端口块组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[start-address end-address*]：私网地址成员的起始IP地址和结束IP地址。*end-address*必须大于或等于*start-address*；如果*start-address*和*end-address*相同，则表示只有一个地址。

**[vpn-instance*** vpn-instance-name*]：私网地址成员所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示私网地址成员不属于任何一个VPN。

【使用指导】

私网地址成员的IP地址作为端口块的使用者，基于端口块组配置的公网地址成员的IP地址为其分配端口块。在一个端口块组内，一个私网IP地址只分配一个端口块。

需要注意的是：

·一个端口块组内，可以配置多个私网地址成员，但各私网地址成员之间的IP地址不能重叠。

·不同端口块组间的私网地址成员的IP地址可以重叠。

·如果一个端口块组中的私网地址总数超过可分配的端口块总数（端口范围除以端口块大小），则在进行NAT444端口块静态映射时，超出部分的私网地址将无法分配到端口块。

【举例】

\# 在端口块组1中添加一个私网地址成员，IP地址从172.16.1.1到172.16.1.255，所属VPN为vpn1。

\<Sysname\> system-view

Sysname nat port-block-group 1

Sysname-port-block-group-1 local-ip-address 172.16.1.1 172.16.1.255 vpn-instance vpn1

【相关命令】

·**nat port-block-group**

**NAT命令 \-- NAT配置命令 \-- nat address-group**

------------------------------------------------------------------------

**[nat address-group**]命令用来创建一个地址组，并进入地址组视图。

**[undo nat address-group**]命令用来删除指定的地址组。

【命令】

**[nat address-group ***group-number*]

**[undo nat address-group ***group-number*]

【缺省情况】

不存在地址组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

*[group-number*]：地址组编号，取值范围为0～*max_number*。其中*max_number*的取值与设备的型号有关，请以设备的实际情况为准。

【使用指导】

一个地址组是多个地址组成员的集合，各个地址组成员通过**address**命令配置。当需要对数据报文进行动态地址转换时，其源地址将被转换为地址组成员中的某个地址。

【举例】

\# 创建一个地址组，编号为1。

\<Sysname\> system-view

Sysname nat address-group 1

【相关命令】

·**address**

·**display nat address-group**

·**display nat all**

·**nat inbound**

·**nat outbound**

**NAT命令 \-- NAT配置命令 \-- nat alg**

------------------------------------------------------------------------

**[nat alg**]命令用来开启指定或所有协议类型的NAT ALG功能。

**[undo nat alg**]命令用来关闭指定或所有协议类型的NAT ALG功能。

【命令】

**[nat alg**[\| **ils** \| **mgcp** \| **nbt** \| **pptp** \| **rsh** \| ]**rtsp**[ \| **sccp**  \|]**sip**[\| **sqlnet** \| ]**tftp **[\| ]**xdmcp** }

**[undo nat alg**[\| **ils** \| **mgcp** \| **nbt** \| **pptp** \| **rsh** \| ]**rtsp**[ \| **sccp**  \| ]**sip**[\| **sqlnet** \| ]**tftp**[\| ]**xdmcp** }

【缺省情况】]

所有协议类型的]NAT ALG功能均处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

**[all**]：所有可指定的协议的ALG功能。

**[dns**]：表示DNS协议的ALG功能。

**[ftp**]：表示FTP协议的ALG功能。

**[h323**]：表示H323协议的ALG功能。

**[icmp-error**]：表示ICMP差错控制报文的ALG功能。

**[ils**]：表示ILS（Internet Locator Service，互联网定位服务）协议的ALG功能。

**[mgcp**]：表示MGCP（Media Gateway Control Protocol，媒体网关控制协议）协议的ALG功能。

**[nbt**]：表示NBT（NetBIOS over TCP/IP，基于TCP/IP的网络基本输入输出系统）协议的ALG功能。

**[pptp**]：表示PPTP（Point-to-Point Tunneling Protocol，点到点隧道协议）协议的ALG功能。

**[rsh**]：表示RSH（Remote Shell，远程外壳）协议的ALG功能。

**[rtsp**]：表示RTSP（Real Time Streaming Protocol，实时流协议）协议的ALG功能。

**[sccp**]：表示SCCP（Skinny Client Control Protocol，瘦小客户端控制协议）协议的ALG功能。

**[sip**]：表示SIP（Session Initiation Protocol，会话初始协议）协议的ALG功能。

**[sqlnet**]：表示SQLNET协议的ALG功能。

**[tftp**]：表示TFTP协议的ALG功能。

**[xdmcp**]：表示XDMCP（X Display Manager Control Protocol，X显示监控）协议的ALG功能。

【使用指导】

ALG（ApplicationLevelGateway，应用层网关）主要完成对应用层报文的解析和处理。通常情况下，NAT只对报文头中的IP地址和端口信息进行转换，不对应用层数据载荷中的字段进行分析和处理。然而对于一些应用层协议，它们的报文的数据载荷中可能包含IP地址或端口信息，这些载荷信息也必须进行有效的转换，否则可能导致功能不正常。

例如，FTP应用由数据连接和控制连接共同完成，而数据连接使用的地址和端口由控制连接协商报文中的载荷信息决定，这就需要ALG利用NAT的相关转换配置来完成载荷信息的转换，以保证后续数据连接的正确建立。

【举例】

\# 开启FTP协议的ALG功能。

\<Sysname\> system-view

Sysname nat alg ftp

【相关命令】

·**display nat all**

**NAT命令 \-- NAT配置命令 \-- nat dns-map**

------------------------------------------------------------------------

**[nat dns-map**]命令用来配置一条域名到内部服务器的映射。

**[undo nat dns-map**]命令用来删除一条域名到内部服务器的映射。

【命令】

**[nat dns-map domain **]*domain-name*** protocol ***pro-type* **[interface ***interface-type* *interface-number* *[\|]*** ip ***global-ip *}** port ***global-port*

**[undo nat dns-map domain **]*domain-name*

【缺省情况】]

不存在域名到内部服务器的映射。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

**[domain ***domain-name*]：指定内部服务器的合法域名。*domain-name*表示内部服务器的域名，由"."分隔的字符串组成（如aabbcc.com），每个字符串的长度不超过63个字符，包括"."在内的总长度不超过253个字符。不区分大小写，字符串中可以包含字母、数字、"-"、"\_"或"."。

**[protocol ***pro-type*]：指定内部服务器的协议类型。*pro-type*表示具体的协议类型，取值为**tcp**或**udp**。

**[interface*** interface-type interface-number*]：表示使用指定接口的地址作为内部服务器的外网地址。*interface-type**interface-number*表示接口类型和接口编号。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip ***global-ip*]：指定内部服务器提供给外部网络访问的IP地址。*global-ip*表示外网IP地址。

**[port ***global-port*]：指定内部服务器提供给外部网络访问的服务端口号，可输入的形式如下：

·数字：取值范围为1～65535。

·协议名称：为1～15个字符的字符串，例如**ftp**、**telnet**等。

【使用指导】

NAT的DNS mapping功能需要和内部服务器配合使用，主要应用于DNS服务器在外网，应用服务器在内网（在NAT设备上有对应的**natserver**配置），内网用户需要通过域名访问内网应用服务器的场景。NAT设备对来自外网的DNS响应报文进行DNSALG处理时，由于载荷中只包含域名和应用服务器的外网IP地址（不包含传输协议类型和端口号），当接口上存在多条NAT服务器配置且使用相同的外网地址而内网地址不同时，DNSALG仅使用IP地址来匹配内部服务器可能会得到错误的匹配结果。因此需要借助DNS mapping的配置，指定域名与应用服务器的外网IP地址、端口和协议的映射关系，由域名获取应用服务器的外网IP地址、端口和协议，进而（在当前NAT接口上）精确匹配内部服务器配置获取应用服务器的内网IP地址。

设备可支持配置多条域名到内部服务器的映射。

【举例】

\# 某公司内部对外提供Web服务，内部服务器的域名为www.server.com，对外的IP地址为202.112.0.1，服务端口号为12345。配置一条域名到内部服务器的映射，使得公司内部用户可以通过域名访问内部Web服务器。

\<Sysname\> system-view

Sysname nat dns-map domain www.server.com protocol tcp ip 202.112.0.1 port 12345

【相关命令】

·**display nat all**

·**display nat dns-map**

·**nat server**

**NAT命令 \-- NAT配置命令 \-- nat hairpin enable**

------------------------------------------------------------------------

**[nat hairpin enable**]命令用来使能NAThairpin功能。

**[undo nat hairpin enable**]用来关闭NAThairpin功能。

【命令】

**[nat hairpin enable**]

**[undo nat hairpin enable**]

【缺省情况】

NAThairpin功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin**

【使用指导】

NAT hairpin功能用于满足位于内网侧的用户之间或用户与服务器之间通过NAT地址进行访问的需求，需要与内部服务器（**nat server**）、出方向动态地址转换（**nat outbound**）或出方向静态地址转换（**nat static outbound**）配合工作。使能NAT hairpin的内网侧接口上会对报文同时进行源地址和目的地址的转换。

【举例】

\# 在GigabitEthernet1/0/1接口下开启NAThairpin功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat hairpin enable

【相关命令】

·**display nat all**

**NAT命令 \-- NAT配置命令 \-- nat inbound**

------------------------------------------------------------------------

**[nat inbound**]命令用来配置入方向动态地址转换。

**[undo nat inbound**]命令用来删除指定的入方向动态地址转换。

【命令】

**[nat inbound ***acl-number ***address-group** *group-number* [ **vpn-instance** *vpn-instance-name*   **no-pat** [ **reversible**   **add-route**  ]]]

**[undo** **nat inbound** *acl-number*]

【缺省情况】

不存在入方向动态地址转换配置。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

*[acl-number*]：ACL编号，取值范围为2000～3999。

**[address-group** *group-number*]：指定地址转换使用的地址组。*group-number*为地址组编号，取值范围与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance ***vpn-instance-name*]：指定地址组中的地址所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示地址组中的地址不属于任何一个VPN。

**[no-pat**]：表示使用NO-PAT方式进行转换，即转换时不使用报文的端口信息。如果未指定本参数，则表示使用PAT方式进行转换，即转换时使用报文的端口信息。PAT方式仅支持TCP、UDP和ICMP查询报文，由于ICMP报文没有端口的概念，我们将ICMP ID作为ICMP报文的源端口。

**[reversible**]：表示允许反向地址转换。即，在外网用户主动向内网发起连接并成功触发建立地址转换表项的情况下，允许内网向该外网用户发起的连接使用已建立的地址转换表项进行目的地址转换。

**[add-route**]：为转换后的地址添加路由表，其目的地址是转换后的地址，出接口为进行地址转换的接口，下一跳为该报文转换前的源地址。

【使用指导】

从配置了入方向地址转换的接口接收到的符合ACL permit规则的报文，会使用地址组*group-number*中的地址进行源地址转换。

入方向地址转换有两种转换方式：

·PAT方式：对于从外网到内网的报文，如果符合ACL，则使用地址组中的地址进行源地址转换，同时转换源端口（IP1/port1转换为IP2/port2）。

·NO-PAT方式：对于从外网到内网的报文，如果符合ACL，则使用地址组中的地址进行源地址转换，不转换源端口（IP1转换为IP2）；如果用户配置了**reversible**，则允许内网通过IP2主动访问外网，对于此类访问报文，需要进行ACL反向匹配（提取报文的源地址/端口和目的地址/端口，并将目的地址转换为IP1，然后将源地址/端口和目的地址/端口互换去匹配ACL），只有反向匹配ACL的报文才能进行转换（将目的地址IP2转换为IP1），否则不予转换。

**[nat inbound**]命令通常与**nat****outbound**、**nat****server**或**nat****static**配合使用，用于支持在外网侧口上对报文同时进行源和目的转换，即双向NAT。

需要注意的是：

·一个地址组被**nat inbound**配置引用后，就不能再被**nat outbound**配置引用。

·一个地址组被PAT方式的**nat inbound**配置引用后，不能再被NO-PAT方式的**nat inbound**配置引用，反之亦然。

·在一个接口下，一个ACL只能被一个**nat inbound**引用。

·**add-route**参数不能应用在内网与外网地址重叠的组网场景中。

·如果指定了**add-route**参数，则有报文命中该配置时，设备会自动添加路由表项：目的地址为本次地址转换使用的地址组中的地址，出接口为本配置所在接口，下一跳地址为报文的源地址；如果没有指定**add-route**参数，则用户需要在设备上手工添加路由。由于自动添加路由表项速度较慢，通常建议手工添加路由。

·一个接口下可同时配置多条入方向地址转换。

【举例】

\# 配置ACL 2001，允许对VPN实例vpn10内10.110.10.0/24网段的主机进行地址转换。

\<Sysname\> system-view

Sysname acl basic 2001

Sysname-acl-ipv4-basic-2001 rule permit vpn-instance vpn10 source 10.110.10.0 0.0.0.255

Sysname-acl-ipv4-basic-2001 rule deny

Sysname-acl-ipv4-basic-2001 quit

\# 配置MPLS L3VPN的VPN实例vpn10。

Sysname ip vpn-instance vpn10

Sysname-vpn-instance-vpn10 route-distinguisher 100:001

Sysname-vpn-instance-vpn10 vpn-target 100:1 export-extcommunity

Sysname-vpn-instance-vpn10 vpn-target 100:1 import-extcommunity

Sysname-vpn-instance-vpn10 quit

\#  配置地址组1，并添加地址组成员：202.110.10.10、202.110.10.11、202.110.10.12。

Sysname nat address-group 1

Sysname-address-group-1 address 202.110.10.10 202.110.10.12

Sysname-address-group-1 quit

\# 在接口GigabitEthernet1/0/1上配置入方向动态地址转换，使用地址组1中的地址进行地址转换，在转换的时候不使用TCP/UDP的端口信息，且需要添加路由。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat inbound 2001 address-group 1 vpn-instance vpn10 no-pat add-route

【相关命令】

·**display nat all**

·**display nat inbound**

·**display nat no-pat**

**NAT命令 \-- NAT配置命令 \-- nat log alarm**

------------------------------------------------------------------------

**[nat log alarm**]命令用来开启NAT444告警信息日志功能。

**[undo nat log alarm**]命令用来关闭NAT444告警信息日志功能。

【命令】

**[nat log alarm**]

**[undo nat log alarm**]

【缺省情况】

NAT444告警信息日志功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在NAT444地址转换中，如果可为用户分配的公网IP地址、端口块或端口块中的端口都被占用，则该用户的后续连接由于没有可用的资源无法对其进行地址转换，相应的报文将被丢弃。为了监控公网IP地址和端口块资源的使用情况，可以通过开启NAT444告警信息日志功能来对端口用满和资源用满两种情况记录告警信息日志。

·端口用满告警：在私网IP地址对应的端口块中的所有端口都被占用的情况下，输出告警信息日志。对于端口块动态映射方式，如果配置了增量端口块分配，则当首次分配的端口块中的端口都被占用时，并不输出日志；只有当增量端口块中的端口也都被占用时，才会输出日志。

·资源用满告警：在NAT444端口块动态映射中，如果所有资源（公网IP地址、端口块）都被占用，则输出日志。

只有开启NAT日志功能之后，NAT444告警信息日志功能才能生效。

【举例】

\# 开启NAT444告警信息日志功能。

\<Sysname\> system-view

Sysname nat log alarm

【相关命令】

·**display nat all**

·**display nat log**

·**nat log enable**

**NAT命令 \-- NAT配置命令 \-- nat log enable**

------------------------------------------------------------------------

**[nat log enable**]命令用来开启NAT日志功能。

**[undo nat log enable**]用来关闭NAT日志功能。

【命令】

**[nat log enable ** **acl** *acl-number* ]

**[undo nat log enable**]

【缺省情况】

NAT日志功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

**[acl ***acl-number*]：指定ACL编号，取值范围为2000～3999。

【使用指导】

必须开启NAT日志功能，NAT会话日志功能（包括NAT新建会话、NAT删除会话和NAT活跃流的日志功能）、NAT444用户日志功能（包括NAT444端口块分配和NAT444端口块回收的日志功能）和NAT444告警信息日志功能才能生效。

**[acl**]参数只对NAT会话日志功能有效，对其他NAT日志功能无效。如果指定了ACL，则只有符合ACL permit规则的数据流才触发输出NAT会话日志；如果没有指定ACL，则表示对所有被NAT处理过的数据流都有可能触发输出NAT会话日志。

【举例】

\# 开启NAT日志功能。

\<Sysname\> system-view

Sysname nat log enable

【相关命令】

·**display nat all**

·**display nat log**

·**nat log alarm**

·**nat log flow-active**

·**nat log flow-begin**

·**nat log flow-end**

·**nat log port-block-assign**

·**nat log port-block-withdraw**

**NAT命令 \-- NAT配置命令 \-- nat log flow-active**

------------------------------------------------------------------------

**[nat log flow-active**]命令用来开启NAT活跃流日志功能，并设置生成活跃流日志的时间间隔。

**[undo nat log flow-active**]命令用来关闭NAT活跃流的日志功能。

【命令】

**[nat log flow-active ***time-value*]

**[undo nat log flow-active**]

【缺省情况】

NAT活跃流的日志功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

*[time-value*]：表示触发输出NAT活跃流日志的时间间隔，取值范围为10～120，单位为分钟。

【使用指导】

对于一些长时间没有断开的NAT会话（即活跃流），如果需要定期记录其连接情况，则可以通过活跃流日志功能来实现。

开启NAT活跃流日志功能后，对于NAT活跃流，每经过指定的时间间隔，设备就会记录一次NAT日志。

需要注意的是，只有开启NAT日志功能之后，活跃流日志功能才能生效。

【举例】

\# 开启NAT活跃流日志功能，并设置输出NAT活跃流日志的时间间隔为10分钟。

\<Sysname\> system-view

Sysname nat log flow-active 10

【相关命令】

·**display nat all**

·**display nat log**

·**nat log enable**

**NAT命令 \-- NAT配置命令 \-- nat log flow-begin**

------------------------------------------------------------------------

**[nat log flow-begin**]命令用来开启NAT新建会话的日志功能，即新建NAT会话时，输出NAT日志。

**[undo nat log flow-begin**]命令用来关闭NAT新建会话的日志功能。

【命令】

**[nat log flow-begin**]

**[undo nat log flow-begin**]

【缺省情况】

NAT新建会话的日志功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin**

【使用指导】

只有开启NAT日志功能之后，NAT新建会话的日志功能才能生效。

【举例】

\# 开启NAT新建会话的日志功能。

\<Sysname\> system-view

Sysname nat log flow-begin

【相关命令】

·**display nat all**

·**display nat log**

·**nat log enable**

**NAT命令 \-- NAT配置命令 \-- nat log flow-end**

------------------------------------------------------------------------

**[nat log flow-end**]命令用来开启NAT删除会话的日志功能。

**[undo nat log flow-end**]命令用来关闭NAT删除会话的日志功能。

【命令】

**[nat log flow-end**]

**[undo nat log flow-end**]

【缺省情况】

NAT删除会话的日志功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin**

【使用指导】

只有开启NAT日志功能之后，NAT删除会话的日志功能才能生效。

【举例】

\# 开启NAT删除会话的日志功能。

\<Sysname\> system-view

Sysname nat log flow-end

【相关命令】

·**display nat all**

·**display nat log**

·**nat log enable**

**NAT命令 \-- NAT配置命令 \-- nat log port-block-assign**

------------------------------------------------------------------------

**[nat log port-block-assign**]命令用来开启端口块分配的NAT444用户日志功能。

**[undo nat log port-block-assign**]命令用来关闭端口块分配的NAT444用户日志功能。

【命令】

**[nat log port-block-assign**]

**[undo nat log port-block-assign**]

【缺省情况】

端口块分配的NAT444用户日志功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

端口块静态映射方式下，在某私网IP地址的第一个新建连接通过端口块进行地址转换时，如果开启了端口块分配的NAT444用户日志功能，则会输出日志。

端口块动态映射方式下，在为某私网IP地址分配端口块或增量端口块时，如果开启了端口块分配的NAT444用户日志功能，则会输出日志。

只有开启NAT日志功能之后，端口块分配的NAT444用户日志功能才能生效。

【举例】

\# 开启端口块分配的NAT444用户日志功能。

\<Sysname\> system-view

Sysname nat log port-block-assign

【相关命令】

·**display nat all**

·**display nat log**

·**nat log enable**

**NAT命令 \-- NAT配置命令 \-- nat log port-block-withdraw**

------------------------------------------------------------------------

**[nat log port-block-withdraw**]命令用来开启端口块回收的NAT444用户日志功能。

**[undo nat log port-block-withdraw**]命令用来关闭端口块回收的NAT444用户日志功能。

【命令】

**[nat log port-block-withdraw**]

**[undo nat log port-block-withdraw**]

【缺省情况】

端口块回收的NAT444用户日志功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

端口块静态映射方式下，在某私网IP地址的最后一个连接拆除时，如果开启了端口块回收的NAT444用户日志功能，则会输出日志。

端口块动态映射方式下，在释放端口块资源（并删除端口块表项）时，如果开启了端口块回收的NAT444用户日志功能，则会输出日志。

只有开启NAT日志功能之后，端口块回收的NAT444用户日志功能才能生效。

【举例】

\# 开启端口块回收的NAT444用户日志功能。

\<Sysname\> system-view

Sysname nat log port-block-withdraw

【相关命令】

·**display nat all**

·**display nat log**

·**nat log enable**

**NAT命令 \-- NAT配置命令 \-- nat mapping-behavior**

------------------------------------------------------------------------

**[nat mapping-behavior**]命令用来配置PAT方式出方向动态地址转换的模式。

**[undo nat mapping-behavior**]命令用来恢复缺省情况。

【命令】

**[nat mapping-behavior** **endpoint-independent** [ **acl** *acl-number* ]]

**[undo nat mapping-behavior** **endpoint-independent**]

【缺省情况】

PAT出方向动态方式地址转换的模式为Address and Port-Dependent Mapping。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

**[acl ***acl-number*]：指定ACL编号，用于控制需要遵守指定地址转换模式的报文范围。*acl-number*的取值范围为2000～3999。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

PAT方式出方向动态地址转换支持两种模式：

·Endpoint-Independent Mapping（不关心对端地址和端口的转换模式）：只要是来自相同源地址和源端口号的报文，不论其目的地址是否相同，通过PAT映射后，其源地址和源端口号都被转换为同一个外部地址和端口号，该映射关系会被记录下来并生成一个EIM表项；并且NAT网关设备允许外部网络的主机通过该转换后的地址和端口来访问这些内部网络的主机。这种模式可以很好的支持位于不同NAT网关之后的主机间进行互访。

·Address and Port-Dependent Mapping（关心对端地址和端口的转换模式）：对于来自相同源地址和源端口号的报文，若其目的地址和目的端口号不同，由于相同的源地址和源端口号不要求被转换为相同的外部地址和端口号，所以通过PAT映射后，相同的源地址和源端口号通常会被转换成不同的外部地址和端口号。并且NAT网关设备只允许这些目的地址对应的外部网络的主机才可以通过该转换后的地址和端口来访问这些内部网络的主机。这种模式安全性好，但是不便于位于不同NAT网关之后的主机间进行互访。

需要注意的是：

·该配置只对出方向动态地址转换的PAT方式起作用。入方向动态地址转换的PAT方式的转换模式始终为 Address and Port-Dependent Mapping。

·如果配置了**acl**参数，则表示只有符合ACL permit规则的报文才采用Endpoint-Independent Mapping模式进行地址转换；如果没有配置**acl**参数，则表示所有的报文都采用Endpoint-Independent Mapping模式进行地址转换。

【举例】

\# 对所有报文都以Endpoint-Independent Mapping模式进行地址转换。

\<Sysname\> system-view

Sysname nat mapping-behavior endpoint-independent

\# 仅对FTP和HTTP报文才以Endpoint-Independent Mapping模式进行地址转换，其它报文采用Address and Port-Dependent Mapping模式进行地址转换。

\<Sysname\> system-view

Sysname acl advanced 3000

Sysname-acl-ipv4-adv-3000 rule permit tcp destination-port eq 80

Sysname-acl-ipv4-adv-3000 rule permit tcp destination-port eq 21

Sysname-acl-ipv4-adv-3000 quit

Sysname nat mapping-behavior endpoint-independent acl 3000

【相关命令】

·**nat outbound**

·**display nat eim**

**NAT命令 \-- NAT配置命令 \-- nat outbound**

------------------------------------------------------------------------

**[nat outbound**]命令用来配置出方向动态地址转换。

**[undo nat outbound**]命令用来删除指定的出方向动态地址转换。

【缺省情况】

不存在动态地址转换配置。

【命令】

·NO-PAT方式

**[nat outbound ** *acl-number* ] **address-group** *group-number*  **vpn-instance** *vpn-instance-name*  **no-pat**  **reversible**

**[undo nat outbound ** *acl-number* ]

·PAT方式

**[nat outbound ** *acl-number* ]  **address-group** *group-number*   **vpn-instance** *vpn-instance-name*   **port-preserved**

**[undo nat outbound ** *acl-number* ]

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

*[acl-number*]：ACL编号，取值范围为2000～3999。不指定该参数的情况下，不对转换对象进行限制。

**[address-group*** group-number*]：指定地址转换使用的地址组。*group-number*为地址组编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果不指定该参数，则直接使用该接口的IP地址作为转换后的地址，即实现Easy IP功能。Easy IP功能的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance ***vpn-instance-name*]：指定地址组中的地址所属的VPN。*vpn-instance-name*表示MPLS L3VPN中的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示地址组中的地址不属于任何一个VPN。

**[no-pat**]：表示使用NO-PAT方式进行转换，即转换时不使用报文的端口信息；如果未指定本参数，则表示使用PAT方式进行转换，即转换时使用报文的端口信息。PAT方式仅支持TCP、UDP和ICMP查询报文，由于ICMP报文没有端口的概念，我们将ICMP ID作为ICMP报文的源端口。

**[reversible**]：表示允许反向地址转换。即，在内网用户主动向外网发起连接并成功触发建立地址转换表项的情况下，允许外网向该内网用户发起的连接使用已建立的地址转换表项进行目的地址转换。

**[port-preserved**]：PAT方式分配端口时尽量不转换端口。

【使用指导】

一般情况下，出方向动态地址转换配置在和外部网络连接的接口上。动态地址转换有两种转换方式：

·PAT方式：对于从内网到外网的报文，如果符合ACL permit规则，则使用地址组中的地址或该接口的地址（Easy IP方式）进行源地址转换，同时转换源端口（IP1/port1转换为IP2/port2）；如果同时配置了PAT方式下的地址转换模式为EIM（Endpoint-Independent Mapping），则外网可以通过IP2/port2主动访问内网，NAT设备根据EIM表项转换目的地址和端口（IP2/port2转换为IP1/port1）。

·NO-PAT方式：对于从内网到外网的报文，如果符合ACL permit规则，则使用地址组中的地址进行源地址转换，不转换源端口（IP1转换为IP2）；如果同时配置了**reversible**，则允许外网通过IP2主动访问内网，对于此类报文，需要进行ACL反向匹配（提取报文的源地址/端口和目的地址/端口，并将目的地址转换为IP1，然后将源地址/端口和目的地址/端口互换去匹配ACL），只有反向匹配ACL的报文才能进行转换（将目的地址IP2转换为IP1），否则不予转换。

需要注意的是：

·一个地址组被**nat outbound**配置引用后，不能再被**natinbound**引用。

·一个地址组被PAT方式的**nat outbound**配置引用后，不能再被NO-PAT方式的**nat outbound**配置引用，反之亦然。

·在一个接口下，一个ACL只能被一个**nat outbound**引用。

·一个接口下可同时配置多条出方向地址转换。

·对于同一接口下的出方向动态地址转换配置，指定了ACL的配置的优先级高于未指定ACL的配置的优先级；对于指定了ACL的出方向动态地址转换配置，其生效优先级由ACL编号的大小决定，编号越大，优先级越高。

·如果PAT方式的**nat outbound**所引用的地址组中配置了端口范围和端口块参数，则将对匹配的报文进行NAT444端口块动态映射。**port-preserved**参数对NAT444端口块动态映射无效。

【举例】

\# 配置ACL 2001，允许对10.110.10.0/24网段的主机报文进行地址转换。

\<Sysname\> system-view

Sysname acl basic 2001

Sysname-acl-ipv4-basic-2001 rule permit source 10.110.10.0 0.0.0.255

Sysname-acl-ipv4-basic-2001 rule deny

Sysname-acl-ipv4-basic-2001 quit

\# 配置地址组1，并添加地址组成员：202.110.10.10、202.110.10.11、202.110.10.12。

Sysname nat address-group 1

Sysname-address-group-1 address 202.110.10.10 202.110.10.12

Sysname-address-group-1 quit

\# 在接口GigabitEthernet1/0/1上配置出方向动态地址转换，允许对匹配ACL 2001的报文使用地址组1中的地址进行地址转换，且在转换的时候使用TCP/UDP的端口信息。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat outbound 2001 address-group 1

Sysname-GigabitEthernet1/0/1 quit

\# 如果在接口GigabitEthernet1/1上不使用TCP/UDP的端口信息进行地址转换，可以使用如下配置。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat outbound 2001 address-group 1 no-pat

Sysname-GigabitEthernet1/0/1 quit

\# 如果直接使用接口GigabitEthernet1/0/1接口的IP地址进行地址转换，可以使用如下的配置。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet 1/0/1 nat outbound 2001

Sysname-GigabitEthernet 1/0/1 quit

\# 内网10.110.10.0/24网段的主机使用地址组1中的地址作为转换后的地址访问外部网络。如果要在内网用户向外网主动发起访问之后，允许外网用户主动向10.110.10.0/24网段的主机发起访问，并利用已建立的地址转换表项进行反向地址转换，可以使用如下配置。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat outbound 2001 address-group 1 no-pat reversible

【相关命令】

·**display nat eim**

·**display nat outbound**

·**nat mapping-behavior**

**NAT命令 \-- NAT配置命令 \-- nat outbound ds-lite-b4**

------------------------------------------------------------------------

**[nat outbound ds-lite-b4**]命令用来配置基于B4地址的DS-Lite NAT转换。

**[undo nat outbound ds-lite-b4**]命令用来删除指定的B4地址的DS-Lite NAT转换。

【命令】

**[nat outbound ds-lite-b4 ***ipv6-acl-number* **address-group** *group-number*]

**[undo nat outbound ds-lite-b4** *ipv6-acl-number*]

【缺省情况】

不存在DS-Lite NAT转换配置。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-acl-number*]：用于匹配B4设备IPv6地址的IPv6 ACL编号，取值范围为2000～2999。

**[address-group*** group-number*]：指定地址转换使用的地址组。*group-number*为地址组编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。目前仅支持端口块动态映射方式的地址组，因此指定的NAT地址组中必须配置端口块参数，否则配置不生效。

【使用指导】

在使用DS-Lite隧道技术实现通过IPv6网络连接IPv4网络的组网环境下，基于B4地址的DS-Lite NAT转换配置在NAT444网关设备连接外部网络的接口上，通常用于在NAT444网关设备已知B4设备或DS-Lite主机的IPv6地址的情况下为DS-Lite用户提供NAT地址转换。

【举例】

\# 配置IPv6 ACL 2100，允许对2000::/64网段的主机报文进行地址转换。

\<Sysname\> system-view

Sysname acl ipv6 basic 2100

Sysname-acl-ipv6-basic-2100 rule permit source 2000::/64

Sysname-acl-ipv6-basic-2100 quit

\# 配置地址组1，并添加地址组成员：202.110.10.10～202.110.10.12。

Sysname nat address-group 1

Sysname-nat-address-group-1 address 202.110.10.10 202.110.10.12

\# 配置地址组1的端口块参数，端口块大小为256。

Sysname-nat-address-group-1 port-block block-size 256

Sysname-nat-address-group-1 quit

\# 在接口GigabitEthernet1/0/1上配置基于B4地址的DS-Lite NAT转换，允许对匹配IPv6 ACL 2100的报文使用地址组1中的地址进行地址转换。

Sysname interface ethernet 1/1

Sysname-GigabitEthernet1/0/1 nat outbound ds-lite-b4 2100 address-group 1

【相关命令】

·**display nat outbound**

**NAT命令 \-- NAT配置命令 \-- nat outbound port-block-group**

------------------------------------------------------------------------

**[nat outbound port-block-group**]命令用来配置NAT444端口块静态映射。

**[undo nat outbound port-block-group**]命令用来删除指定的NAT444端口块静态映射配置。

【命令】

**[nat outbound port-block-group** *group-number*]

**[undo nat outbound port-block-group** *group-number*]

【缺省情况】

不存在NAT444端口块静态映射配置。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-number*]：端口块组编号，取值范围为0～*max_number*。其中*max_number*的取值与设备的型号有关，请以设备的实际情况为准。

【使用指导】

该配置在接口下引用指定的端口块组，根据端口块组内的配置数据，按照固定的算法为每个私网IP地址分配一个静态端口块并创建静态端口块表项。当某私网IP地址向公网发起连接时，通过该私网IP地址查找静态端口块表项，使用表项中记录的公网IP地址进行地址转换，并从对应的端口块中动态分配一个端口进行TCP/UDP端口转换。

一个接口下可以配置多条基于不同端口块组的NAT444端口块静态映射。

【举例】

\# 在接口GigabitEthernet1/0/1的出方向上配置基于端口组1的NAT444端口块静态映射。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat outbound port-block-group 1

【相关命令】

·**display nat all**

·**display nat outbound port-block-group**

·**display nat port-block**

·**nat port-block-group**

**NAT命令 \-- NAT配置命令 \-- nat port-block synchronization enable**

------------------------------------------------------------------------

![说明](NAT命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[nat port-block synchronization enable**]命令用来[开启]NAT444业务热备份功能。

**[undo nat [port-block synchronization enable]**]命令用来恢复缺省情况。

【命令】

**[nat port-block synchronization enable**]

**[undo nat [port-block synchronization enable]**]

【缺省情况】

NAT444业务热备份功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在业务热备份环境中，通过开启NAT444业务热备份功能，可以实现主备切换后动态NAT444端口块表项一致[。]

【举例】

\# 开启NAT444多机备份功能。

\<Sysname\> system-view

Sysname nat port-block synchronization enable

**NAT命令 \-- NAT配置命令 \-- nat port-block-group**

------------------------------------------------------------------------

**[nat port-block-group**]命令用来创建一个NAT端口块组，并进入NAT端口块组视图。

**[undo nat port-block-group**]命令用来删除指定的NAT端口块组。

【命令】

**[nat port-block-group** *group-number*]

**[undo nat port-block-group** *group-number*]

【缺省情况】

不存在NAT端口块组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-number*]：NAT端口块组编号，取值范围为0～max_number。其中max_number的取值与设备的型号有关，请以设备的实际情况为准。

【使用指导】

创建的NAT端口块组用于配置NAT444端口块静态映射。一个端口块组中包含如下内容：

·一个或多个私网地址成员，通过**local-ip-address**命令配置。

·一个或多个公网地址成员，通过**global-ip-pool**命令配置。

·公网地址的端口范围，通过**port-range**命令配置。

·端口块大小，通过**block-size**命令配置。

在进行NAT444端口块静态映射时，系统根据相应端口块组的配置计算出私网IP地址到公网IP地址、端口块的静态映射关系，并创建静态端口块表项。

【举例】

\# 创建一个NAT端口块组，编号为1。

\<Sysname\>system-view

Sysnamenat port-block-group 1

Sysname-port-block-group-1

【相关命令】

·**block-size**

·**display nat all**

·**display nat port-block-group**

·**global-ip-pool**

·**local-ip-address**

·**nat outbound port-block-group**

·**port-range**

**NAT命令 \-- NAT配置命令 \-- nat server**

------------------------------------------------------------------------

**[nat server**]命令用来配置NAT内部服务器，即定义内部服务器的外网地址和端口与内网地址和端口的映射表项。

**[undo nat server**]命令用来删除指定的内部服务器配置。

【命令】

(1)普通内部服务器

·外网地址单一，未使用外网端口或外网端口单一

**[nat server**  **protocol** *pro-type* **global** { *global-address \|* **current-interface** \| **interface** *interface-type* *interface-number* } [ *global-port* ]  **vpn-instance** *global-name*  **inside** *local-address*  *local-port*   **vpn-instance** *local-name*  ] **acl** *acl-number*

**[undo nat server**  **protocol** *pro-type* **global** { *global-address \|* **current-interface** \| **interface** *interface-type* *interface-number* } [ *global-port* ]  **vpn-instance** *global-name* ]

·外网地址单一，外网端口连续

**[nat server**  **protocol** *pro-type* **global** { *global-address \|* **current-interface** \| **interface** *interface-type* *interface-number* } *global-port1 global-port2* [ **vpn-instance** *global-name* ] **inside** { { *local-address \| local-address1 local-address2* } *local-port* \| *local-address* *local-port*1 *local-port*2 }  **vpn-instance** *local-name*  ] **acl** *acl-number*

**[undo nat server**  **protocol** *pro-type* **global** { *global-address \|* **current-interface** \| **interface** *interface-type* *interface-number* } *global-port1 global-port2* [ **vpn-instance** *global-name* ] ]

·外网地址连续，未使用外网端口或外网端口单一

**[nat server protocol** *pro-type* **global** *global-address1 global-address2  *[ *global-port*   **vpn-instance** *global-name*  **inside** ]*local-address1 local-address2 *} * * *local-port* ] **vpn-instance** *local-name*   **acl** *acl-number*

**[undo nat server protocol** *pro-type* **global** *global-address1 global-address2* [ *global-port*   **vpn-instance** *global-name*  ]]

·外网地址连续，外网端口单一

**[nat server protocol** *pro-type* **global** *global-address1 global-address2  global-port* [ **vpn-instance** *global-name*  **inside** ]]*local-address* *local-port*1 *local-port*2  **vpn-instance** *local-name*   **acl** *acl-number*

**[undo nat server protocol** *pro-type* **global** *global-address1 global-address2  global-port* [ **vpn-instance** *global-name* ]]

(2)负载均衡内部服务器

**[nat server protocol ***pro-type*** global **[{ { *global-address* \| **current-interface** \| **interface** *interface-type* *interface-number* } { *global-port* \| *global-port1 global-port2* } \| *global-address1 global-address2 global-port* } [ **vpn-instance** *global-name* ] **inside server-group** *group-number*  **vpn-instance** *local-name*   **acl** *acl-number* ]]

**[undo nat server protocol ***pro-type*** global **[{ { *global-address* \| **current-interface** \| **interface** *interface-type interface-number* } { *global-port* \| *global-port1 global-port2* } \| *global-address1 global-address2 global-port* } [ **vpn-instance** *global-name* ]]]

(3)基于ACL的内部服务器

**[nat server global ***global-acl-number*** inside ***local-address* [ *local-port*   **vpn-instance** *local-name* ]]

**[undo nat server global ***global-acl-number*** inside ***local-address* [ *local-port*   **vpn-instance** *local-name* ]]

【缺省情况】

不存在内部服务器。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

**[protocol** *pro-type*]：指定协议类型。当协议类型不是TCP、UDP协议时，配置的内部服务器不带端口参数。*pro-type*可输入以下形式：

·数字：取值范围为1～255。

·协议名称：取值包括**icmp**、**tcp**和**udp**。

*[global-address*]：内部服务器向外提供服务时对外公布的外网IP地址。

*[global-address1*]*、global-address2*：外网IP地址范围，所包含的地址数目不能超过256。*global-address1*表示起始地址，*global-address2*表示结束地址。*global-address2*必须大于*global-address1*。

**[global*** global-acl-number*]：指定ACL编号，取值范围为2000～3999。只有与指定的ACL permit规则匹配的报文才可以进行目的地址转换。

**[current-interface**]：使用当前接口的地址作为内部服务器的外网地址，即实现Easy IP方式的内部服务器。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[interface*** interface-type interface-number*]：表示使用指定接口的地址作为内部服务器的外网地址，即实现Easy IP方式的内部服务器。*interface-type**interface-number*表示接口类型和接口编号。目前只支持Loopback接口。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[global-port1*]*、global-port2*：外网端口范围，和内部主机的IP地址范围构成一一对应的关系。*global-port1*表示起始端口，*global-port2*表示结束端口。*global-port2*必须大于*global-port1*，且端口范围中的端口数目不能大于256。外网端口可输入以下形式：

·数字：取值范围为1～65535。起始端口和结束端口均支持此形式。

·协议名称：为1～15个字符的字符串，例如**http**、**telnet**等。仅起始端口支持该形式。

*[local-address1*]、*local-address2*：定义一组连续的内网IP地址范围，和外网端口范围构成一一对应的关系。*local-address1*表示起始地址，*local-address2*表示结束地址。*local-address2*必须大于*local-address1*。该地址范围的数量必须和*global-port1*、*global-port2*定义的端口数量相同。

*[local-port*]：内部服务器的内网端口号，可输入以下形式：

·数字：取值范围为1～65535（FTP数据端口号20除外）。

·协议名称：为1～15个字符的字符串，例如**http**、**telnet**等。

*[global-port*]：外网端口号，缺省值以及取值范围的要求和*local-port*的规定一致。

*[local-address*]：服务器的内网IP地址。

**[vpn-instance ***global-name*]：对外公布的外网地址所属的VPN。*global-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示对外公布的外网地址不属于任何一个VPN。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance ***local-name*]：内部服务器所属的VPN。*local-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示内部服务器不属于任何一个VPN。

**[server-group** *group-number*]：服务器在内网所属的服务器组。若指定了该参数，则表示要配置一个负载分担内部服务器。*group-number*表示内部服务器组编号，不同设备的取值范围不同，请以设备的实际情况为准。

**[acl ***acl-number*]：指定ACL编号，取值范围为2000～3999。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。若指定了该参数，则表示与指定的ACL permit规则匹配的报文才可以使用内部服务器的映射表进行地址转换。

【使用指导】

通过该配置可以利用NAT设备将一些内部网络的服务器提供给外部网络使用，例如内部的Web服务器、FTP服务器、Telnet服务器、POP3服务器、DNS服务器等。这些内部服务器可以位于普通的内网内，也可以位于MPLS VPN实例内。

NAT内部服务器通常配置在NAT设备的外网侧接口上。外网用户可以通过*global-address*定义的外网地址和*global-port*定义的外网端口来访问内网地址和内网端口分别为*local-address*和*local-port*的内部服务器。NAT内部服务器支持以下几种内网和外网的地址、端口映射关系。

表1-18 NAT内部服务器的地址与端口映射关系

外网

内网

一个外网地址

一个内网地址

一个外网地址、一个端口号

一个内网地址、一个内网端口号

一个外网地址，N个连续的外网端口号

一个内网地址，一个内网端口

N个连续的内网地址，一个内网端口号

一个内网地址，N个连续的内网端口号

N个连续的外网地址

一个内网地址

N个连续的内网地址

N个连续的外网地址连续，一个外网端口号

一个内网地址，一个内网端口号

N个连续的内网地址，一个内网端口号

一个内网地址，N个连续的内网端口号

一个外网地址，一个外网端口号

一个内部服务器组

一个外网地址，N个连续的外网端口号

N个连续的外网地址，一个外网端口号

外网地址（通过ACL进行匹配）

一个内网地址

一个内网地址、一个内网端口号

需要注意的是：

·一个接口下允许配置的**nat server**命令个数与设备的型号有关。每个**nat server**命令下可以配置的NAT内部服务器数目为*global-port2*与*global-port1*的差值，即配置多少个外网端口就对应多少个NAT内部服务器。

·设备支持引用接口地址作为NAT内部服务器的外网地址（Easy IP方式）。如果配置关键字**current-interface**，表示外网地址使用的是当前接口的当前主地址；如果指定具体的接口，则只能指定Loopback接口，外网地址使用的是配置的Loopback接口的当前主地址。Easy IP功能的支持情况与设备的型号有关，请以设备的实际情况为准。

·由于Easy IP方式的NAT内部服务器使用了当前接口或其它接口的IP地址作为它的外网地址，因此强烈建议在配置了Easy IP方式的NAT内部服务器之后，其它NAT内部服务器不要再配置该接口的IP地址作为它的外网地址，反之亦然。

·当*pro-type*不是TCP（协议号为6）或UDP（协议号为17）时，用户只能设置内部IP地址与外部IP地址的一一对应的关系，无法设置端口号之间的映射。

·对于同一个接口下配置的NAT服务器，其协议类型、外网地址和外网端口号的组合必须是唯一的，否则认为是配置冲突。本规则同样适用于Easy IP方式的NAT服务器，其外网地址为指定接口的IP地址。

·对于同一个接口下配置的Easy IP方式的NAT服务器，其协议类型、接口名和外网端口的组合必须是唯一的，否则认为是配置冲突。

·对于Easy IP方式的NAT服务器，如果其引用的接口的IP地址发生改变，导致跟现有的其它非Easy IP方式的NAT服务器冲突，则Easy IP方式的NAT服务器配置失效；如果接口地址又修改为不冲突的IP，或者之前与之冲突的NAT服务器被删除，则Easy IP方式的NAT配置重新生效。

【举例】

\# 在接口GigabitEthernet1/0/1上配置NAT内部服务器，指定局域网内部的Web服务器的IP地址是10.110.10.10，希望外部通过http://202.110.10.10:8080可以访问Web服务器。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat server protocol tcp global 202.110.10.10 8080 inside 10.110.10.10 http

Sysname-GigabitEthernet1/0/1 quit

\# 在接口GigabitEthernet1/0/1上配置NAT内部服务器，指定MPLS VPN vrf10内部的FTP服务器的IP地址是10.110.10.11，希望外部通过ftp://202.110.10.10可以访问FTP服务器。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat server protocol tcp global 202.110.10.10 21 inside 10.110.10.11 vpn-instance vrf10

Sysname-GigabitEthernet1/0/1 quit

\# 在接口GigabitEthernet1/0/1上配置NAT内部服务器，指定一个VPN vrf10内部的主机10.110.10.12，希望外部网络的主机可以利用ping 202.110.10.11命令ping通它。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat server protocol icmp global 202.110.10.11 inside 10.110.10.12 vpn-instance vrf10

Sysname-GigabitEthernet1/0/1 quit

\# 在接口GigabitEthernet1/0/1上配置NAT内部服务器，指定一个外部地址202.110.10.10，从端口1001～1100分别映射MPLS VPN vrf10内主机10.110.10.1～10.110.10.100的telnet服务。202.110.10.10:1001访问10.110.10.1，202.110.10:1002访问10.110.10.2，依此类推。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat server protocol tcp global 202.110.10.10 1001 1100 inside 10.110.10.1 10.110.10.100 telnet vpn-instance vrf10

\# 正确的服务器地址为10.0.0.172，用户配置的错误地址为192.168.0.0/24网段的地址，在接口GigabitEthernet1/0/1上配置基于ACL的内部服务器对这部分用户的配置错误进行纠正。

\<Sysname\> system-view

Sysname acl advanced 3000

Sysname-acl-ipv4-adv-3000 rule 5 permit ip destination 192.168.0.0 0.0.0.255

Sysname-acl-ipv4-adv-3000 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat server global 3000 inside 10.0.0.172

【相关命令】

·**display nat all**

·**display nat server**

·**nat server-group**

**NAT命令 \-- NAT配置命令 \-- nat server-group**

------------------------------------------------------------------------

**[nat server-group**]命令用来配置一个内部服务器组。

**[undo nat server-group**]命令用来删除指定的内部服务器组。

【命令】

**[nat server-group** *group-number*]

**[undo nat server-group** *group-number*]

【缺省情况】

不存在内部服务器组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

*[group-number*]：服务器组编号，取值范围与设备的型号有关，请以设备的实际情况为准。{.FigureChar}

【使用指导】

一个内部服务器组中可以包括多个内部服务器组成员（通过**inside ip**命令配置）。

【举例】

\# 配置一个内部服务器组，编号为1。

\<Sysname\> system-view

Sysname nat server-group 1

【相关命令】

·**display nat all**

·**display nat server-group**

·**inside ip**

·**nat server**

**NAT命令 \-- NAT配置命令 \-- nat service**

------------------------------------------------------------------------

![说明](NAT命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[nat service**]命令用来指定提供NAT处理的业务板。

**[undo nat service**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[nat service slot ***slot-number*]

**[undo nat service slot**]

分布式设备－IRF模式：

**[nat service chassis ***chassis-number* **slot** *slot-number*]

**[undo nat service chassis**]

【缺省情况】

未指定提供NAT处理的业务板。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：指定单板所在的槽位号。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：指定设备在IRF中的成员编号。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：指定设备在IRF中的成员编号或者PEX的虚拟槽位号。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：指定单板。*chassis-number*表示设备在IRF中的成员编号PEX对应的虚拟框号，*slot-number*表示单板报在的槽位号PEX所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

【使用指导】

对于支持本命令的设备，必须在配置了NAT业务的接口上指定提供NAT处理的业务板。只有为接口指定了业务板，接口的NAT功能才能生效。

需要注意的是：

·一个接口上的NAT业务只能由一块业务板处理，该业务板可以是设备上的任意可提供NAT处理的业务板。通常，如果接口所在的板具有NAT处理能力，那么建议将接口所在板指定为NAT业务板。

l如果要修改接口下指定的业务板，需要先恢复缺省情况再重新指定。

l多个接口引用了同一个地址组或外网地址时，这些接口必须指定同一块业务板进行NAT处理。否则，可能会出现配置成功但实际不生效的情况，并且在配置恢复（由设备重启、软件升级等原因导致）时可能会造成配置丢失。

【举例】

\# 指定5号单板作为提供NAT处理的业务板。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat service slot 5

\# 指定5号成员设备作为提供NAT处理的业务板。（集中式IRF设备）

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname- GigabitEthernet1/0/1 nat service slot 5

\# 指定2号成员设备的5号单板作为提供NAT处理的业务板。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname interface gigabitethernet 1/3/0/1

Sysname- GigabitEthernet1/3/0/1 nat service chassis 2 slot 5

**NAT命令 \-- NAT配置命令 \-- nat static-load-balance enable**

------------------------------------------------------------------------

![说明](NAT命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[nat static-load-balance enable**]命令用来[使能静态]NAT在多个CPU上进行负载分担的功能。

**[undo nat static-load-balance enable**]命令用来关闭[静态]NAT在多个CPU上进行负载分担的功能。

【命令】

**[nat static-load-balance enable**]

**[undo nat static-load-balance enable**]

【缺省情况】

静态NAT在多个CPU上进行负载分担的功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能本功能后，设备会将静态NAT的处理分担到不同的CPU上，以均衡各个CPU上的负载。如果关闭本功能，则所有静态NAT都由主CPU来处理，可能会导致主CPU负载过重。

【举例】

\# 使能静态NAT在多个CPU上进行负载分担的功能。

\<Sysname\> system-view

Sysname nat static-load-balance enable

**NAT命令 \-- NAT配置命令 \-- nat static enable**

------------------------------------------------------------------------

**[nat static enable**]命令用来开启接口上的NAT静态地址转换功能。

**[undo nat static enable**]命令用来关闭接口上的NAT静态地址转换功能。

【命令】

**[nat static enable**]

**[undo nat static enable**]

【缺省情况】

NAT静态地址转换功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin**

【使用指导】

接口下开启NAT静态地址转换功能后，所有已配置的静态地址转换映射都会在该接口上生效。

【举例】

\# 配置内网IP地址192.168.1.1到外网IP地址2.2.2.2的出方向一对一静态地址转换，并且在接口GigabitEthernet1/0/1上开启静态地址转换功能。

\<Sysname\> system-view

Sysname nat static outbound 192.168.1.1 2.2.2.2

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat static enable

【相关命令】

·**display nat all**

·**display nat static**

·**nat static**

·**nat static net-to-net**

**NAT命令 \-- NAT配置命令 \-- nat static inbound**

------------------------------------------------------------------------

**[nat static inbound**]命令用来配置入方向一对一静态地址转换映射。

**[undo** **nat static**]** inbound**命令用来删除指定的入方向一对一静态地址转换映射。

【命令】

**[nat static inbound*** global-ip * **vpn-instance** *global-name* ] *local-ip*  **vpn-instance** *local-name*   **acl** *acl-number*[ [ **reversible**  ]]

**[undo** **nat static inbound** *global-ip* [ **vpn-instance** *global-name*  ]]

【缺省情况】

不存在任何地址转换映射。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

*[global-ip*]：外网IP地址。

**[vpn-instance ***global-name*]：外网IP地址所属的VPN。*global-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示外网IP地址不属于任何一个VPN。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[local-ip*]：内网IP地址。

**[vpn-instance*** local-name*]：内网IP地址所属的VPN。*local-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示内网IP地址不属于任何一个VPN。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[acl ***acl-number*]：ACL编号，取值范围为3000～3999。本参数用于控制指定源地址的内网主机可以访问外网。

**[reversible**]：表示从内网主动访问外网的报文必须通过ACL反向匹配，才能使用该配置进行目的地址转换。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

对于从外网到内网的报文，将其源地址*global-ip*转换为*local-ip*；对于从内网到外网的报文，将其目的地址*local-ip*转换为*global-ip*。

需要注意的是：

·如果没有指定ACL，则所有从外网到内网的报文都可以使用该配置进行源地址转换；所有从内网到外网的报文都可以使用该配置进行目的地址转换。

·如果仅指定了ACL，没有指定ACL反向匹配（即没有配置**reversible**），对于从外网到内网的报文，只有报文符合ACL permit规则，才能使用该配置进行源地址转换；对于从内网主动访问外网的报文，不能使用该配置进行目的地址转换。

·如果既指定了ACL，又指定了ACL反向匹配（即配置了**reversible**），对于外网到内网的报文，只有报文符合ACL permit规则，才能使用该配置进行源地址转换；对于从内网主动访问外网的报文，需要进行ACL反向匹配（提取报文的源地址/端口和目的地址/端口，并根据配置转换目的地址，然后将源地址/端口和目的地址/端口互换去匹配ACL），只有反向匹配ACL的报文才能使用该配置进行转换，否则不予转换。

·如果接口下既配置了NAT动态地址转换，又使能了NAT静态地址转换，则优先使用静态地址转换。

·设备可支持配置多条入方向静态地址转换映射（包括**nat static inbound**和**nat static inbound net-to-net**）。

【举例】

\# 配置外网IP地址2.2.2.2到内网IP地址192.168.1.1的入方向静态地址转换。

\<Sysname\> system-view

Sysname nat static inbound 2.2.2.2 192.168.1.1

【相关命令】

·**display nat all**

·**display nat static**

·**nat static enable**

**NAT命令 \-- NAT配置命令 \-- nat static inbound net-to-net**

------------------------------------------------------------------------

**[nat static inbound net-to-net**]命令用来配置入方向网段到网段的静态地址转换映射。

**[undo nat static inbound net-to-net**]命令用来删除指定的入方向网段到网段的静态地址转换映射。

【命令】

**[nat static inbound net-to-net ***global-start-address global-end-address *[ **vpn-instance** *global -name*  **local** *local-network* { *mask-length* \| *mask* }  **vpn-instance** *local-name*   **acl** *acl-number*[ [ **reversible**  ]]]]

**[undo nat static inbound net-to-net ***global-start-address global-end-address * **vpn-instance** *global -name* ]

【缺省情况】

不存在任何地址转换映射。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

*[global-start-address global-end-address*]：外网地址范围，所包含的地址数目不能超过255。*global-start-address*表示起始地址，*global-end-address*表示结束地址。*global-end-address*必须大于或等于*global-start-address*，如果二者相同，则表示只有一个地址。

**[vpn-instance ***global-name*]：外网IP地址所属的VPN。*global-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示外网IP地址不属于任何一个VPN。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[local-network*]：内网网段地址。

*[mask-length*]：内网网络地址的掩码长度，取值范围为8～31。

*[mask*]：内网网络地址掩码。

**[vpn-instance*** local-name*]：内网IP地址所属的VPN。*local-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示内网IP地址不属于任何一个VPN。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[acl ***acl-number*]：ACL编号，取值范围为3000～3999。本参数用于控制指定源地址的内网主机可以访问外网。

**[reversible**]：表示从内网主动访问外网的报文必须通过ACL反向匹配，才能使用该配置进行目的地址转换。[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

【使用指导】

外网网段通过起始地址和结束地址来指定，内网网段通过内网地址和掩码来指定。

对于从外网到内网的报文，使用其源地址匹配外网地址，将源地址转换为内网地址；对于从内网到外网的报文，使用其目的地址匹配内网地址，将目的地址转换为外网地址。

需要注意的是：

·外网结束地址不能大于外网起始地址和内网掩码所决定的网段中的最大IP地址。比如：内网地址配置为2.2.2.0，掩码为255.255.255.0，外网起始地址为1.1.1.100，则外网结束地址不应该大于1.1.1.0/24网段中可用的最大IP地址，即1.1.1.255。

·如果没有指定ACL，则所有从外网到内网的报文都可以使用该配置进行源地址转换；所有从内网到外网的报文都可以使用该配置进行目的地址转换。

·如果仅指定了ACL，没有指定ACL反向匹配（即没有配置**reversible**），对于从外网到内网的报文，只有报文符合ACL permit规则，才能使用该配置进行源地址转换；对于从内网到外网的报文，不能使用该配置进行目的地址转换。

·如果既指定了ACL，又指定了ACL反向匹配（即配置了**reversible**），对于外网到内网的报文，只有报文符合ACL permit规则，才能使用该配置进行源地址转换；对于从内网到外网的报文，需要进行ACL反向匹配（提取报文的源地址/端口和目的地址/端口，并根据配置转换目的地址，然后将源地址/端口和目的地址/端口互换去匹配ACL），只有反向匹配ACL的报文才能使用该配置进行转换，否则不予转换。

·如果接口下既配置了NAT动态地址转换，又使能了NAT静态地址转换，则优先使用静态地址转换。

·设备支持配置多条入方向静态地址转换映射（包括**nat static inbound**和**nat static inbound net-to-net**）。

【举例】

\# 配置外网网段202.100.1.0/24到内网网段192.168.1.0/24的入方向静态地址转换。

\<Sysname\> system-view

Sysname nat static inbound net-to-net 202.100.1.1 202.100.1.255 local 192.168.1.0 24

【相关命令】

·**display nat all**

·**display nat static**

·**nat static enable**

**NAT命令 \-- NAT配置命令 \-- nat static outbound**

------------------------------------------------------------------------

**[nat static outbound**]命令用来配置出方向一对一静态地址转换映射。

**[undo** **nat static outbound**]命令用来删除出方向一对一静态地址转换映射。

【命令】

**[nat static outbound ***local-ip***** **vpn-instance** *local-name* ] *global-ip*  **vpn-instance** *global-name*   **acl** *acl-number*[ [ **reversible**  ]]

**[undo** **nat static outbound** *local-ip* [ **vpn-instance** *local-name*  ]]

【缺省情况】

不存在任何地址转换映射。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

*[local-ip*]：内网IP地址。

**[vpn-instance*** local-name*]：内网IP地址所属的VPN。*local-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示内网IP地址不属于任何一个VPN。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[global-ip*]：外网IP地址。

**[vpn-instance ***global-name*]：外网IP地址所属的VPN。*global-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示外网IP地址不属于任何一个VPN。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[acl ***acl-number*]：ACL编号，取值范围为3000～3999。本参数用于控制内网主机可以访问的目的地址。

**[reversible**]：表示从外网主动访问内网的报文必须通过ACL反向匹配，才能使用该配置进行目的地址转换。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

对于从内网到外网的报文，将其源地址*local-ip*转换为*global-ip*；对于从外网到内网的报文，将其目的地址*global-ip*转换为*local-ip*。

需要注意的是：

·如果没有指定ACL，则所有从内网到外网的报文都可以使用该配置进行源地址转换；所有从外网到内网的报文都可以使用该配置进行目的地址转换。

·如果仅指定了ACL，没有指定ACL反向匹配（即没有配置**reversible**），对于从内网到外网的报文，只有报文符合ACL permit规则，才能使用该配置进行源地址转换；对于从外网主动访问内网的报文，不能使用该配置进行目的地址转换。

·如果既指定了ACL，又指定了ACL反向匹配（即配置了**reversible**），对于从内网到外网的报文，只有报文符合ACL permit规则，才能使用该配置进行源地址转换；对于从外网主动访问内网的报文，需要进行ACL反向匹配（提取报文的源地址/端口和目的地址/端口，并根据配置转换目的地址，然后将源地址/端口和目的地址/端口互换去匹配ACL），只有反向匹配ACL的报文才能使用该配置进行转换，否则不予转换。

·如果接口下既配置了NAT动态地址转换，又使能了NAT静态地址转换，则优先使用静态地址转换。

·设备可支持配置多条出方向静态地址转换映射（包括**nat static outbound**和**nat static outbound net-to-net**）。

【举例】

\# 配置内网IP地址192.168.1.1到外网IP地址2.2.2.2的出方向静态地址转换映射。

\<Sysname\> system-view

Sysname nat static outbound 192.168.1.1 2.2.2.2

\# 配置出方向静态地址转换映射，允许内网用户192.168.1.1访问外网网段3.3.3.0/24时，使用外网IP地址2.2.2.2。

\<Sysname\> system-view

Sysname acl advanced 3001

Sysname-acl-ipv4-adv-3001 rule permit ip destination 3.3.3.0 0.0.0.255

Sysname-acl-ipv4-adv-3001 quit

Sysname nat static outbound 192.168.1.1 2.2.2.2 acl 3001

【相关命令】

·**display nat all**

·**display nat static**

·**nat static enable**

**NAT命令 \-- NAT配置命令 \-- nat static outbound net-to-net**

------------------------------------------------------------------------

**[nat static outbound net-to-net**]命令用来配置出方向网段到网段的静态地址转换映射。

**[undo nat static outbound net-to-net**]命令用来删除出方向网段到网段的静态地址转换映射。

【命令】

**[nat static outbound net-to-net** *local-start-address* *local-end-address* [ **vpn-instance** *local-name*  **global** *global-network* { *mask-length* \| *mask* }  **vpn-instance** *global-name*   **acl** *acl-number*  **reversible**  ]]

**[undo nat static outbound net-to-net** *local-start-address* *local-end-address* [ **vpn-instance** *local-name*  ]]

【缺省情况】

不存在任何地址转换映射。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

*[local-start-address local-end-address*]：内网地址范围，所包含的地址数目不能超过255。*local-start-address*表示起始地址，*local-end-address*表示结束地址。*local-end-address*必须大于或等于*local-start-address*，如果二者相同，则表示只有一个地址。

*[global-network*]：外网网段地址。

*[mask-length*]：外网网络地址的掩码长度，取值范围为8～31。

*[mask*]：外网网络地址掩码。

**[acl ***acl-number*]：ACL编号，取值范围为3000～3999。本参数用于控制内网主机可以访问的目的地址

**[reversible**]：表示从外网主动访问内网的报文必须通过ACL反向匹配，才能使用该配置进行目的地址转换。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

内网网段通过起始地址和结束地址来指定，外网网段通过外网地址和掩码来指定。

对于从内网到外网的报文，使用其源地址匹配内网地址，将源地址转换为外网地址；对于从外网到内网的报文，使用其目的地址匹配外网地址，将目的地址转换为内网地址。

需要注意的是：

·内网结束地址不能大于内网起始地址和外网掩码所决定的网段中的最大IP地址。比如：外网地址配置为2.2.2.0，掩码为255.255.255.0，内网起始地址为1.1.1.100，则内网结束地址不应该大于1.1.1.0/24网段中可用的最大IP地址，即1.1.1.255。

·如果没有指定ACL，则所有从内网到外网的报文都可以使用该配置进行源地址转换；所有从外网到内网的报文都可以使用该配置进行目的地址转换。

·如果仅指定了ACL，没有指定ACL反向匹配（即没有配置**reversible**），对于从内网到外网的报文，只有报文符合ACL permit规则，才能使用该配置进行源地址转换；对于从外网主动访问内网的报文，不能使用该配置进行目的地址转换。

·如果既指定了ACL，又指定了ACL反向匹配（即配置了**reversible**），对于从内网到外网的报文，只有报文符合ACL permit规则，才能使用该配置进行源地址转换；对于从外网主动访问内网的报文，需要进行ACL反向匹配（提取报文的源地址/端口和目的地址/端口，并根据配置转换目的地址，然后将源地址/端口和目的地址/端口互换去匹配ACL），只有反向匹配ACL的报文才能使用该配置进行转换，否则不予转换。

·如果接口下既配置了NAT动态地址转换，又使能了NAT静态地址转换，则优先使用静态地址转换。

·设备可支持配置多条出方向静态地址转换映射（包括**nat static outbound**和**nat static outbound net-to-net**）。

【举例】

\# 配置内网网段192.168.1.0/24到外网网段2.2.2.0/24的出方向静态地址转换映射。

\<Sysname\> system-view

Sysname nat static outbound net-to-net 192.168.1.1 192.168.1.255 global 2.2.2.0 24

\# 配置出方向网段到网段的静态地址转换映射，允许内网192.168.1.0/24网段的用户访问外网网段3.3.3.0/24时，使用外网网段2.2.2.0/24中的地址。

\<Sysname\> system-view

Sysname acl advanced 3001

Sysname-acl-ipv4-adv-3001 rule permit ip destination 3.3.3.0 0.0.0.255

Sysname-acl-ipv4-adv-3001 quit

Sysname nat static outbound net-to-net 192.168.1.1 192.168.1.255 global 2.2.2.0 24 acl 3001

【相关命令】

·**display nat all**

·**display nat static**

·**nat static enable**

**NAT命令 \-- NAT配置命令 \-- port-block**

------------------------------------------------------------------------

**[port-block**]命令用来配置NAT地址组的端口块参数。

**[undo port-block**]命令用来删除NAT地址组的端口块参数。

【命令】

**[port-block block-size** *block-size* [ **extended-block-number** *extended-block-number* ]]

**[undo port-block**]

【缺省情况】

NAT地址组未配置端口块参数。

【视图】

NAT地址组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[block-size*** block-size*]：端口块大小，即一个端口块中所包含的端口数，取值范围为1～*max_number*。其中*max_number*的取值与设备的型号有关，请以设备的实际情况为准。同一NAT地址组内，该参数的值不能超过**port-range**参数的值。

**[extended-block-number ***extended-block-number*]：增量端口块数，取值范围为1～5。当分配端口块中的端口资源耗尽（所有端口都被使用）时，如果对应的私网IP地址向公网发起新的连接，则无法从分配端口块中获取端口。此时，如果分配端口块的公网IP地址所属的NAT地址组中配置了增量端口块数，则可以为对应的私网IP地址进行增量端口块分配。一个私网IP地址最多可同时占有1＋*extended-block-number*个端口块。

【使用指导】

端口块动态映射方式下，配置出方向地址转换所引用的NAT地址组中必须配置端口块参数。当某私网IP地址首次向公网发起连接时，从所匹配的NAT地址组中获取一个公网IP地址，从获取的公网IP地址中分配一个动态端口块并创建动态端口块表项（该私网IP地址后续向公网发起连接时，通过私网IP地址查找动态端口块表项），使用公网IP地址进行IP地址转换，并从端口块中动态分配一个端口进行TCP/UDP端口转换。

【举例】

\# 配置NAT地址组2的端口块参数，端口块大小为256，增量端口块数为1。

\<Sysname\> system-view

Sysname nat address-group 2

Sysname-address-group-2 port-block block-size 256 extended-block-number 1

【相关命令】

·**nat address-group**

**NAT命令 \-- NAT配置命令 \-- port-range**

------------------------------------------------------------------------

**[port-range**]命令用来配置公网IP地址的端口范围。

**[undo port-range**]命令用来恢复缺省情况。

【命令】

**[port-range** *start-port-number end-port-number*]

**[undo port-range**]

【缺省情况】

公网IP地址的端口范围为1～65535。

【视图】

NAT地址组视图/NAT端口块组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[start-port-number end-port-number*]：公网IP地址端口的起始端口号和结束端口号。*end-port-number*必须大于或等于*start-port-number*。

【使用指导】

在NAT地址组（或NAT端口块组）视图下配置端口范围后，该NAT地址组（或NAT端口块组）内的所有公网IP地址可用于地址转换的端口都必须位于所指定的端口范围之内。

在NAT端口块组内配置端口范围时，端口范围不能小于端口块大小。在NAT地址组内配置端口范围时，如果地址组配置了端口块参数，则端口范围也不能小于端口块大小。

【举例】

\# 配置NAT地址组1的公网IP地址端口范围为1024～65535。

\<Sysname\> system-view

Sysname nat address-group 1

Sysname-address-group-1 port-range 1024 65535

\# 配置NAT端口块组1的公网IP地址端口范围为30001～65535。

\<Sysname\> system-view

Sysname nat port-block-group 1

Sysname-port-block-group-1 port-range 30001 65535

【相关命令】

·**nat address-group**

·**nat port-block-group**

**NAT命令 \-- NAT配置命令 \-- reset nat session**

------------------------------------------------------------------------

**[reset nat session**]命令用来删除NAT会话。

【命令】

集中式设备：

**[reset nat **]**session**

分布式设备－独立运行模式/集中式IRF设备：

**[reset nat session **] **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[reset nat session **] **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin**

【参数】

**[slot** *slot-number*]：删除指定单板上的NAT会话，*slot-number*表示单板所在的槽位号。如果不指定该参数，则表示删除所有单板上的NAT会话。（分布式设备－独立运行模式）。

**[slot** *slot-number*]：删除指定成员设备上的NAT会话，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，则表示删除所有成员设备上的NAT会话。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：删除指定成员设备/PEX上的NAT会话，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，则表示删除所有成员设备/PEX上的NAT会话。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：删除指定成员设备上指定单板的NAT会话，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，则表示删除所有成员设备的所有单板上的NAT会话。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：删除指定单板上的NAT会话，*chassis-numbe*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定该参数，则表示删除所有单板上的NAT会话。（分布式设备－IRF模式）（不支持IRF3的设备）

**[cpu** *cpu-number*]：删除指定CPU上的NAT会话，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

NAT会话被删除之后，与其相关的NAT EIM表和NO-PAT表也会同时删除。

【举例】

\# 删除NAT会话。（集中式设备）

\<Sysname\> reset nat session

\#删除2号单板的NAT会话。（分布式设备－独立运行模式）

\<Sysname\> reset nat session slot 2

\#删除2号成员设备的NAT会话。（集中式IRF设备）

\<Sysname\> reset nat session slot 2

\# 删除1号成员设备的2号单板上的NAT会话。（分布式设备－IRF模式）

\<Sysname\> reset nat session chassis 1 slot 2

【相关命令】

·**display nat session**

**NAT命令 \-- NAT配置命令 \-- reset nat static-load-balance**

------------------------------------------------------------------------

**[reset nat static-load-balance**]命令用来重新在多个CPU上进行静态NAT（包括静态地址转换、NAT server和静态NAT444）的负载分担。

【命令】

**[reset nat static-load-balance**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行本命令后，设备会综合考虑当前的所有静态NAT配置（包括静态地址转换、NAT server和静态NAT444的配置），重新将静态NAT的处理分担到不同的CPU上，以均衡各个CPU上的负载。

需要注意的是，执行本命令后，会造成流量的暂时中断，请谨慎使用本命令。

【举例】

\# 配置重新在多个CPU上进行静态NAT的负载分担。

\<Sysname\> reset nat static-load-balance

**NAT命令 \-- NAT配置命令 \-- reset nat dynamic-load-balance**

------------------------------------------------------------------------

**[reset nat dynamic-load-balance**]命令用来重新在多个CPU上进行动态NAT（包括动态地址转换和动态NAT444）的负载分担。

【命令】

**[reset nat dynamic-load-balance**** ** address-group**]*****address-group-number *

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[address-group ***address-group-number*]：重新对指定地址池的动态NAT进行负载分担。*address-group-number*为地址池的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果没有指定本参数，则重新对所有动态NAT进行负载分担。

【使用指导】

执行本命令后，设备会综合考虑当前所有的动态NAT配置（包括动态地址转换和动态NAT444的配置）或指定地址池的动态NAT配置，重新将动态NAT的处理分担到不同的CPU上，以均衡各个CPU上的负载。

需要注意的是，执行本命令后，会造成流量的暂时中断，请谨慎使用本命令。

【举例】

\# 配置重新在多个CPU上进行动态NAT的负载分担。

\<Sysname\> reset nat dynamic-load-balance

