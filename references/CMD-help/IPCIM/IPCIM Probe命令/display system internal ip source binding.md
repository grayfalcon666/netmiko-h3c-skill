
**IPCIM \-- IPCIM Probe命令 \-- display system internal ip source binding**

------------------------------------------------------------------------

**[display system internal ip source binding**]命令用来显示详细的IPv4绑定表项信息。

【命令】

集中式设备：

**[display system internal ip source binding**[ [ **static** \| [ **vpn-instance** *vpn-instance-name*   **dot1x** \| **dhcp-relay** \| **dhcp-server** \| **dhcp-snooping** ] ]  **ip-address** *ip-address*   **mac-address** *mac-address*   **vlan** *vlan-id*   **interface** *interface-type interface-number*  ]]

分布式设备-独立运行模式/集中式IRF设备

**[display system internal ip source binding**[ [ **static** \| [ **vpn-instance** *vpn-instance-name*   **dot1x** \| **dhcp-relay** \| **dhcp-server** \| **dhcp-snooping** ] ]  **ip-address** *ip-address*   **mac-address** *mac-address*   **vlan** *vlan-id*   **interface** *interface-type interface-number*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备-IRF模式

**[display system internal ip source binding**[ [ **static** \| [ **vpn-instance** *vpn-instance-name*   **dot1x** \| **dhcp-relay** \| **dhcp-server** \| **dhcp-snooping** ] ]  **ip-address** *ip-address*   **mac-address** *mac-address*   **vlan** *vlan-id*   **interface** *interface-type interface-number*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

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

**[interface ***interface-type* *interface-number*]：显示指定接口的绑定表项，*interface-type interface-number*表示绑定的接口类型和接口编号。

**[slot ***slot-number*]：显示存储在指定单板上的绑定表项，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的绑定表项。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示存储在指定成员设备上的绑定表项，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上的绑定表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示存储在指定成员设备/PEX上的绑定表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的绑定表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示存储在指定成员设备上指定单板的绑定表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示存储在指定单板的绑定表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示存储在指定CPU的绑定表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPCIM \-- IPCIM Probe命令 \-- display system internal ipv6 source binding**

------------------------------------------------------------------------

**[display system internal ipv6 source binding**]命令用来显示详细的IPv6绑定表项信息。

【命令】

集中式设备：

**[display system internal ipv6 source binding**[ [ **static** \| [ **vpn-instance** *vpn-instance-name* ] **dhcpv6-snooping**  ]  **ip-address** *ipv6-address*   **mac-address** *mac-address*   **vlan** *vlan-id*   **interface** *interface-type interface-number*  ]]

分布式设备-独立运行模式/集中式IRF设备

**[display system internal ipv6 source binding**[ [ **static** \| [ **vpn-instance** *vpn-instance-name* ] **dhcpv6-snooping**  ]  **ip-address** *ipv6-address*   **mac-address** *mac-address*   **vlan** *vlan-id*   **interface** *interface-type interface-number*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备-IRF模式

**[display system internal ipv6 source binding**[ [ **static** \| [ **vpn-instance** *vpn-instance-name* ] **dhcpv6-snooping**  ]  **ip-address** *ipv6-address*   **mac-address** *mac-address*   **vlan** *vlan-id*   **interface** *interface-type interface-number*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[static**]：显示配置的静态绑定表项。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的动态绑定表项，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示显示公网的动态绑定表项。

**[dhcpv6-snooping**]：显示DHCPv6 Snooping模块生成的动态绑定表项。

**[ip-address*** ipv6-address*]：显示指定IPv6地址的绑定表项，*ipv6-address*表示绑定的IPv6地址。

**[mac-address*** mac-address*]：显示指定MAC地址的绑定表项，*mac-address*表示绑定的MAC地址，格式为H-H-H。

**[vlan** *vlan-id*]：显示指定VLAN的绑定表项，*vlan-id*表示绑定的VLAN ID，取值范围为1～4094。

**[interface ***interface-type interface-number*]：显示指定接口的绑定表项，*interface-type interface-number*表示绑定的接口类型和接口编号。

**[slot ***slot-number*]：显示存储在指定单板上的绑定表项，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的绑定表项。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示存储在指定成员设备上的绑定表项，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上的绑定表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示存储在指定成员设备/PEX上的绑定表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的绑定表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示存储在指定成员设备上指定单板的绑定表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示存储在指定单板的绑定表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示存储在指定CPU的绑定表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

