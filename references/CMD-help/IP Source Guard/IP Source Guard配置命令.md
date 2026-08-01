<!-- CMD-INDEX
  display ip source binding           | 任意视图             | L12
  display ipv6 source binding         | 任意视图             | L146
  ip source binding(interface view)   | 二层以太网端口/三层以太网接口/VLAN接口 | L270
  ip source binding(system view)      | 系统视图             | L330
  ip verify source                    | 二层以太网端口/三层以太网接口/VLAN接口/三层聚合接口 | L386
  ipv6 source binding(interface view) | 二层以太网端口/三层以太网接口/VLAN接口 | L470
  ipv6 source binding(system view)    | 系统视图             | L530
  ipv6 verify source                  | 二层以太网端口/三层以太网接口/VLAN接口/三层聚合接口 | L586
-->

**IP Source Guard \-- IP Source Guard配置命令 \-- display ip source binding**

------------------------------------------------------------------------

**[display ip source binding**]命令用来显示IPv4绑定表项信息。

【命令】

集中式设备：

**[display ip source binding **[[ **static** \| [ **vpn-instance** *vpn-instance-name*   **dhcp-relay** \| **dhcp-server** \| **dhcp-snooping** \| **dot1x** ] ]  **ip-address** *ip-address*   **mac-address** *mac-address*   **vlan** *vlan-id*   **interface** *interface-type interface-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ip source binding **[[ **static** \| [ **vpn-instance** *vpn-instance-name*   **dhcp-relay** \| **dhcp-server** \| **dhcp-snooping** \| **dot1x** ] ]  **ip-address** *ip-address*   **mac-address** *mac-address*   **vlan** *vlan-id*   **interface** *interface-type interface-number*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ip source binding **[[ **static** \| [ **vpn-instance** *vpn-instance-name*   **dhcp-relay** \| **dhcp-server** \| **dhcp-snooping** \| **dot1x** ] ]  **ip-address** *ip-address*   **mac-address** *mac-address*   **vlan** *vlan-id*   **interface** *interface-type interface-number*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[static**]：显示配置的静态绑定表项。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的动态绑定表项，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示显示公网的动态绑定表项。

**[dhcp-relay**]：显示DHCP中继模块生成的动态绑定表项。

**[dhcp-server**]：显示DHCP服务器模块生成的动态绑定表项。

**[dhcp-snooping**]：显示DHCP Snooping模块生成的动态绑定表项。

**[dot1x**]：显示802.1X模块生成的动态绑定表项。

**[ip-address*** ip-address*]：显示指定IPv4地址的绑定表项，*ip-address*表示绑定的IPv4地址。

**[mac-address*** mac-address*]：显示指定MAC地址的绑定表项，*mac-address*表示绑定的MAC地址，格式为H-H-H。

**[vlan** *vlan-id*]：显示指定VLAN的绑定表项，*vlan-id*表示绑定的VLAN ID，取值范围为1～4094。

**[interface ***interface-type interface-number*]：显示指定接口的绑定表项，*interface-type interface-number*表示绑定的接口类型和接口编号。

**[slot ***slot-number*]：显示指定单板上的绑定表项，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的绑定表项。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的绑定表项，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上的绑定表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的绑定表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的绑定表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的绑定表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的绑定表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的绑定表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示公网所有接口的IPv4绑定表项和全局的IPv4静态绑定表项。

\<Sysname\> display ip source binding

Total entries found: 5

IP Address      MAC Address    Interface                VLAN Type

10.1.0.5        040a-0000-4000 GE1/0/1                  1    DHCP snooping

10.1.0.6        040a-0000-3000 GE1/0/1                  1    DHCP snooping

10.1.0.7        040a-0000-2000 GE1/0/1                  1    DHCP snooping

10.1.0.8        040a-0000-1000 GE1/0/2                  N/A  DHCP relay

10.1.0.9        040a-0000-2000 GE1/0/2                  N/A  Static

表1-1 display ip source-binding命令显示信息描述表

字段

描述

Total entries found

查询到的绑定表项总数

IP Address

绑定表项的IPv4地址（N/A表示该表项不绑定IP地址）

MAC Address

绑定表项的MAC地址（N/A表示该表项不绑定MAC地址）

Interface

绑定表项所属的接口（N/A表示该表项为全局绑定）

VLAN

绑定表项所属的VLAN（N/A表示该表项中没有VLAN信息）

Type

绑定表项类型：

·Static表示配置的静态绑定表项

·802.1X表示来源于802.1X模块的动态绑定表项

·DHCP relay表示DHCP中继模块生成的动态绑定表项

·DHCP server表示DHCP服务器模块生成的动态绑定表项

·DHCP snooping表示DHCP Snooping模块生成的动态绑定表项

【相关命令】

·**ip**** source binding**

·**ip verify** **source**

**IP Source Guard \-- IP Source Guard配置命令 \-- display ipv6 source binding**

------------------------------------------------------------------------

**[display ipv6 source binding**]命令用来显示IPv6绑定表项信息。

【命令】

集中式设备：

**[display ipv6 source binding **[[ **static** \|   **vpn-instance** *vpn-instance-name*   **dhcpv6-snooping**  ]  **ip-address** *ipv6-address*   **mac-address** *mac-address*   **vlan** *vlan-id*   **interface** *interface-type interface-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 source binding **[[ **static** \|  **vpn-instance** *vpn-instance-name*   **dhcpv6-snooping**  ]  **ip-address** *ipv6-address*   **mac-address** *mac-address*   **vlan** *vlan-id*   **interface** *interface-type interface-number*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 source binding **[[ **static** \|   **vpn-instance** *vpn-instance-name*   **dhcpv6-snooping**  ]  **ip-address** *ipv6-address*   **mac-address** *mac-address*   **vlan** *vlan-id*   **interface** *interface-type interface-number*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[static**]：显示配置的静态绑定表项。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的动态绑定表项，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示显示公网的动态绑定表项。

**[dhcpv6-snooping**]：显示DHCPv6 Snooping模块生成的动态绑定表项。

**[ip-address*** ipv6-address*]：显示指定IPv6地址的绑定表项，*ipv6-address*表示绑定的IPv6地址。

**[mac-address*** mac-address*]：显示指定MAC地址的绑定表项，*mac-address*表示绑定的MAC地址，格式为H-H-H。

**[vlan** *vlan-id*]：显示指定VLAN的绑定表项，*vlan-id*表示绑定的VLAN ID，取值范围为1～4094。

**[interface ***interface-type interface-number*]：显示指定接口的绑定表项，*interface-type interface-number*表示绑定的接口类型和接口编号。

**[slot ***slot-number*]：显示指定单板上的绑定表项，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的绑定表项。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的绑定表项，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上的绑定表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的绑定表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的绑定表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的绑定表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的绑定表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的绑定表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示公网所有接口的IPv6绑定表项和全局的IPv6静态绑定表项。

\<Sysname\> display ipv6 source binding

Total entries found: 2

IPv6 Address         MAC Address    Interface               VLAN Type

2012:1222:2012:1222: 000f-2202-0435 GE1/0/1                 1    DHCPv6 snooping

2012:1222:2012:1222

2012:1222:2012:1222: 000f-2202-0436 GE1/0/1                 N/A  Static

2012:1222:2012:1223

表1-2 display ipv6 source-binding命令显示信息描述表

字段

描述

Total entries found

查询到的绑定表项总数

IPv6 Address

绑定表项的IPv6地址（N/A表示该表项不绑定IPv6地址）

MAC Address

绑定表项的MAC地址（N/A表示该表项不绑定MAC地址）

Interface

绑定表项所属的接口（N/A表示该表项为全局绑定）

VLAN

绑定表项所属的VLAN（N/A表示该表项没有VLAN信息）

Interface

绑定表项所属的接口

Type

绑定表项类型：

·Static表示配置的静态绑定表项

·DHCPv6 snooping表示DHCPv6 Snooping模块生成的动态绑定表项

【相关命令】

·**ipv6**** source binding**

·**ipv6 verify source**

**IP Source Guard \-- IP Source Guard配置命令 \-- ip source binding(interface view)**

------------------------------------------------------------------------

**[ip**] **source** **binding**命令用来配置接口的IPv4静态绑定表项。

**[undo ip**] **source** **binding**命令用来删除当前接口的IPv4静态绑定表项。

【命令】

**[ip**[ **source** **binding** { **ip-address** *ip-address* \| **ip-address** *ip-address* **mac-address** *mac-address \|* **mac-address** *mac-address* } [ **vlan** *vlan-id* ]]]

**[undo**[ **ip** **source** **binding** { **all** \| **ip-address** *ip-address* \| **ip-address** *ip-address* **mac-address** *mac-address* \| **mac-address** *mac-address* } [ **vlan** *vlan-id* ]]]

【缺省情况】

接口上无IPv4静态绑定表项。

【视图】

二层以太网端口/三层以太网接口/VLAN接口

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：当前接口所有的IPv4静态绑定表项，本参数只在**undo** **ip** **source** **binding**命令中生效。

**[ip-address*** ip-address*]：指定接口的IPv4静态绑定表项的IPv4地址。其中*ip-address*表示绑定的IPv4地址，必须为A、B、C三类地址之一，不能为127.x.x.x和0.0.0.0。

**[mac-address*** mac-address*]：指定接口的IPv4静态绑定表项的MAC地址。其中*mac-address*表示绑定的MAC地址，格式为H-H-H，取值不能为全0、全F（广播MAC）和组播MAC。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vlan ***vlan-id*]：指定接口的IPv4静态绑定表项的VLAN。其中*vlan-id*表示绑定的VLAN ID，取值范围为1～4094。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。本参数仅在二层以太网接口视图下支持。

【使用指导】

接口的IPv4静态绑定表项用于过滤接口收到的IPv4报文，或者与ARP Detection功能配合使用检查接入用户的合法性。

加入业务环回组的接口上不能配置IPv4静态绑定表项。

【举例】

\# 在接口GigabitEthernet1/0/1上配置一条IPv4静态绑定表项，仅允许源IP地址为192.168.0.1且源MAC地址为0001-0001-0001的报文通过。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip source binding ip-address 192.168.0.1 mac-address 0001-0001-0001

【相关命令】

·**display ip source****binding**

·**ip source binding**(system view)

**IP Source Guard \-- IP Source Guard配置命令 \-- ip source binding(system view)**

------------------------------------------------------------------------

**[ip**] **source** **binding**命令用来配置全局的IPv4静态绑定表项。

**[undo ip**] **source** **binding**命令用来删除已配置的全局IPv4静态绑定表项。

【命令】

**[ip** **source** **binding** **ip-address** *ip-address* **mac-address** *mac-address*]

**[undo**[ **ip** **source** **binding** { **all** \| **ip-address** *ip-address* **mac-address** *mac-address* }]]

【缺省情况】

设备上无全局的IPv4静态绑定表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip-address*** ip-address*]：指定全局的IPv4静态绑定表项的IPv4地址。其中*ip-address*表示绑定的IPv4地址，必须为A、B、C三类地址之一，不能为127.x.x.x和0.0.0.0。

**[mac-address*** mac-address*]：指定全局的IPv4静态绑定表项的MAC地址。其中*mac-address*表示绑定的MAC地址，格式为H-H-H，取值不能为全0、全F（广播MAC）和组播MAC。

**[all**]：设备上所有全局的IPv4静态绑定表项。

【使用指导】

全局的IPv4静态绑定表项对设备的所有接口都生效。

设备最多允许配置的全局的IPv4静态绑定表项数量与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 在设备上配置一条全局的IPv4静态绑定表项，允许源IP地址为192.168.0.1且源MAC地址为0001-0001-0001的报文通过。

\<Sysname\> system-view

Sysname ip source binding ip-address 192.168.0.1 mac-address 0001-0001-0001

【相关命令】

·**display ip source****binding**

·**ip source binding**(interface view)

**IP Source Guard \-- IP Source Guard配置命令 \-- ip verify source**

------------------------------------------------------------------------

**[ip verify source**]命令用来配置IPv4接口绑定功能。

**[undo ip verify source**]命令用来恢复缺省情况。

【命令】

**[ip verify source **[**[\| **ip-address mac-address** \| **mac-address** }]]

**[undo ip verify source**]

【缺省情况】]

接口的IPv4接口绑定功能处于关闭状态。

【视图】

二层以太网端口/三层以太网接口/VLAN接口/三层聚合接口

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip-address**]：表示绑定源IPv4地址，即根据接口收到的报文的源IPv4地址对报文进行过滤。

**[ip-address mac-address**]：表示绑定源IP地址和MAC地址,即接口上收到的报文的源IPv4地址和源MAC地址都与某动态绑定表项匹配，该报文才能被正常转发，否则将被丢弃。

**[mac-address**]：表示绑定源MAC地址，即根据接口收到的报文的源MAC地址对报文进行过滤。

【使用指导】

配置该功能后，IP Source Guard模块会通过配置的静态绑定表项或通过获取其它模块表项信息生成的动态绑定表项过滤接口收到的用户IP报文，符合绑定表项的用户报文被正常转发，不符合绑定表项的用户报文将被丢弃。目前，可为IP Source Guard提供动态绑定表项信息的模块包括802.1X、DHCP relay、DHCP Snooping、DHCP服务器。其中，DHCP中继、DHCP Snooping模块生成的动态绑定表项可被IP Source Guard模块用于过滤报文，802.1X模块和DHCP服务器模块生成的动态绑定表项不被直接用于过滤报文，用于配合其它模块提供相应的安全服务，比如ARP Detection可利用802.1X模块生成的动态绑定表项进行用户ARP合法性检查。

需要注意的是：

·加入业务环回组的接口上不能配置动态绑定功能。

·本命令中指定的绑定参数，仅对动态生成的绑定表项有效，是接口使用动态绑定表项过滤报文时关心的报文特征项。如果仅使用静态绑定表项来过滤接口的报文，则本命令仅用于控制是否开启接口的报文过滤功能，接口依据配置的静态绑定表项参数来过滤报文，而不关心本命令中指定的参数。

【举例】

\# 在二层以太网接口GigabitEthernet1/0/1上配置IPv4接口绑定功能，根据报文的源IP地址和源MAC地址对接口收到的报文进行过滤。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip verify source ip-address mac-address

\# 在Vlan-interface100上配置对报文的源IP和MAC地址的IPv4接口绑定功能，根据报文的源IP地址和源MAC地址对接口收到的报文进行过滤。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ip verify source ip-address mac-address

\# 在三层以太网接口GigabitEthernet1/0/2上配置对报文的源IP和MAC地址的IPv4接口绑定功能，根据报文的源IP地址和源MAC地址对接口收到的报文进行过滤。该配置的支持情况与设备的型号有关，请以设备的实际情况为准。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 ip verify source ip-address mac-address

\# 在三层以太网接口GigabitEthernet1/0/2上配置对报文的源MAC地址的IPv4接口绑定功能，根据报文的源MAC地址对接口收到的报文进行过滤。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 ip verify source mac-address

【相关命令】

·**display ip source****binding**

**IP Source Guard \-- IP Source Guard配置命令 \-- ipv6 source binding(interface view)**

------------------------------------------------------------------------

**[ipv6** **source** **binding**]命令用来配置接口的IPv6静态绑定表项。

**[undo ipv6** **source** **binding**]命令用来删除当前接口配置的IPv6静态绑定表项。

【命令】

**[ipv6**[ **source** **binding** { **ip-address** *ipv6-address* \| **ip-address** *ipv6-address* **mac-address** *mac-address \|* **mac-address** *mac-address* } [ **vlan** *vlan-id* ]]]

**[undo ipv6**[ **source** **binding** { **all** \| **ip-address** *ipv6-address* \| **ip-address** *ipv6-address* **mac-address** *mac-address \|* **mac-address** *mac-address* } [ **vlan** *vlan-id* ]]]

【缺省情况】

接口上无IPv6静态绑定表项。

【视图】

二层以太网端口/三层以太网接口/VLAN接口

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：当前接口所有的IPv6静态绑定表项，本参数只在**undo** **ipv6** **source** **binding**命令中生效。

**[ip-address*** ipv6-address*]：指定接口的IPv6静态绑定表项的IPv6地址。其中*ipv6-address*表示绑定的IPv6地址，不能为全0地址、组播地址、环回地址。

**[mac-address*** mac-address*]：指定接口的IPv6静态绑定表项的MAC地址。其中*mac-address*表示绑定的MAC地址，格式为H-H-H，取值不能为全0、全F（广播MAC）和组播MAC。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vlan ***vlan-id*]：指定接口的IPv6静态绑定表项的VLAN。其中*vlan-id*表示绑定的VLAN ID，取值范围为1～4094。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。本参数仅在二层以太网接口视图下支持。

【使用指导】

接口的IPv6静态绑定表项用于过滤接口收到的IPv6报文，或者与ND Detection功能配合使用检查接入用户的合法性。

加入业务环回组的接口上不能配置IPv6静态绑定表项。

【举例】

\# 在接口GigabitEthernet1/0/1上配置一条IPv6静态绑定表项，仅允许源IPv6地址为2001::1且源MAC地址为0002-0002-0002的报文通过。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 source binding ip-address 2001::1 mac-address 0002-0002-0002

【相关命令】

·**display ipv6 source****binding**

·**ipv6 source binding**(system view)

**IP Source Guard \-- IP Source Guard配置命令 \-- ipv6 source binding(system view)**

------------------------------------------------------------------------

**[ipv6**] **source** **binding**命令用来配置全局的IPv6静态绑定表项。

**[undo ipv6**] **source** **binding**命令用来删除已配置的全局IPv6静态绑定表项。

【命令】

**[ipv6** **source** **binding** **ip-address** *ipv6-address* **mac-address** *mac-address*]

**[undo**[ **ipv6** **source** **binding** { **all** \| **ip-address** *ipv6-address* **mac-address** *mac-address* }]]

【缺省情况】

设备上无全局的IPv6静态绑定表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip-address*** ipv6-address*]：指定全局的IPv6静态绑定表项的IPv6地址。其中*ipv6-address*表示绑定的IPv6地址，不能为全0地址、组播地址、环回地址。

**[mac-address*** mac-address*]：指定全局的IPv6静态绑定表项的MAC地址。其中*mac-address*表示绑定的MAC地址，格式为H-H-H，取值不能为全0、全F（广播MAC）和组播MAC。

**[all**]：设备上所有全局的IPv6静态绑定表项。

【使用指导】

全局的IPv6静态绑定表项对设备的所有接口都生效。

设备最多允许配置的全局的IPv6静态绑定表项数量与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 在设备上配置一条全局的IPv6静态绑定表项，允许源IPv6地址为2001::1且源MAC地址为0002-0002-0002的报文通过。

\<Sysname\> system-view

Sysname ipv6 source binding ip-address 2001::1 mac-address 0002-0002-0002

【相关命令】

·**display ip****v6 sourcebinding**

·**ipv6 source binding**(interface view)

**IP Source Guard \-- IP Source Guard配置命令 \-- ipv6 verify source**

------------------------------------------------------------------------

**[ipv6 verify source**]命令用来配置IPv6接口绑定功能。

**[undo ipv6 verify source**]命令用来恢复缺省情况。

【命令】

**[ipv6 verify source **[**[\| **ip-address** **mac-address** \| **mac-address** }]]

**[undo ipv6 verify source**]

【缺省情况】]

接口的IPv6接口绑定功能处于关闭状态。

【视图】

二层以太网端口/三层以太网接口/VLAN接口/三层聚合接口

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip-address**]：表示绑定源IPv6地址，即根据接口收到的报文的源IPv6地址对报文进行过滤。

**[ip-address mac-address**]：表示绑定源IPv6地址和MAC地址,即接口上收到的报文的源IPv6地址和源MAC地址都与某动态绑定表项匹配，该报文才能被正常转发，否则将被丢弃。

**[mac-address**]：表示绑定源MAC地址，即根据接口收到的报文的源MAC地址对报文进行过滤。

【使用指导】

配置该功能后，IP Source Guard模块会通过配置的静态绑定表项或通过获取DHCPv6 Snooping表项生成的动态绑定表项来过滤接口收到的用户IPv6报文，符合绑定表项的用户报文被正常转发，不符合绑定表项的用户报文将被丢弃。

需要注意的是：

·加入业务环回组的接口上不能配置动态绑定功能。

·本命令中指定的绑定参数，仅对动态生成的绑定表项有效，是接口使用动态绑定表项过滤报文时关心的报文特征项。如果仅使用静态绑定表项来过滤接口的报文，则本命令仅用于控制是否开启接口的报文过滤功能，接口依据配置的静态绑定表项参数来过滤报文，而不关心本命令中指定的参数。

【举例】

\# 在二层以太网接口GigabitEthernet1/0/1上配置IPv6接口绑定功能，根据报文的源IPv6地址和源MAC地址对接口收到的报文进行过滤。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 verify source ip-address mac-address

【相关命令】

·**display ipv6 source binding**
