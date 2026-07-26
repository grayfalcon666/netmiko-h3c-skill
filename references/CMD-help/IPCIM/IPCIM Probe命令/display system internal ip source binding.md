::: {#1390132968 .myid}
[]{#_Toc404798933}[]{#struct_0_12801_72881_x503961059}

**IPCIM \-- IPCIM Probe命令 \-- display system internal ip source binding**

------------------------------------------------------------------------

[**[display system internal ip source binding]{lang="EN-US"}**]{#struct_0_12801_72881_x1542494628}[命令用来显示详细的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[绑定表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12801_72881_x1011207161}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12801_72881_1693395318}

[**[display system internal ip source binding]{lang="EN-US"}**[ \[ **static** \| \[ **vpn-instance** *vpn-instance-name* \] \[ **dot1x** \| **dhcp-relay** \| **dhcp-server** \| **dhcp-snooping** \] \] \[ **ip-address** *ip-address* \] \[ **mac-address** *mac-address* \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \] ]{lang="EN-US"}]{#struct_0_12801_72881_794277535}

[[分布式设备]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_12801_72881_x1730688073}[独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}

[**[display system internal ip source binding]{lang="EN-US"}**[ \[ **static** \| \[ **vpn-instance** *vpn-instance-name* \] \[ **dot1x** \| **dhcp-relay** \| **dhcp-server** \| **dhcp-snooping** \] \] \[ **ip-address** *ip-address* \] \[ **mac-address** *mac-address* \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12801_72881_x337776539}

[[分布式设备]{style="font-family:宋体"}[-IRF]{lang="EN-US"}]{#struct_0_12801_72881_x55462077}[模式]{style="font-family:宋体"}

[**[display system internal ip source binding]{lang="EN-US"}**[ \[ **static** \| \[ **vpn-instance** *vpn-instance-name* \] \[ **dot1x** \| **dhcp-relay** \| **dhcp-server** \| **dhcp-snooping** \] \] \[ **ip-address** *ip-address* \] \[ **mac-address** *mac-address* \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12801_72881_x1338641715}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12801_72881_420100264}

[[Probe]{lang="EN-US"}]{#struct_0_12801_72881_x1452464723}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12801_72881_1389714912}

[[network-admin]{lang="EN-US"}]{#struct_0_12801_72881_1056524670}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12801_72881_x185708035}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12801_72881_x1532321736}

[**[static]{lang="EN-US"}**]{#struct_0_12801_72881_x1796837475}[：显示配置的静态绑定表项。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_12801_72881_x1041843382}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的动态绑定表项，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示公网的动态绑定表项。]{style="font-family:宋体"}

[**[dhcp-relay]{lang="EN-US"}**]{#struct_0_12801_72881_827893553}[：显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继模块生成的动态绑定表项。]{style="font-family:宋体"}

[**[dhcp-server]{lang="EN-US"}**]{#struct_0_12801_72881_x55527613}[：显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器模块生成的动态绑定表项。]{style="font-family:宋体"}

[**[dhcp-snooping]{lang="EN-US"}**]{#struct_0_12801_72881_x506251709}[：显示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[模块生成的动态绑定表项。]{style="font-family:宋体"}

[**[dot1x]{lang="EN-US"}**]{#struct_0_12801_72881_1683907930}[：显示]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[模块生成的动态绑定表项。]{style="font-family:宋体"}

[**[ip-address]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_12801_72881_x1638935524}[：显示指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的绑定表项，]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_12801_72881_1758410617}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的绑定表项，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_12801_72881_x196008819}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的绑定表项，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_12801_72881_2020245608}[：显示指定接口的绑定表项，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示绑定的接口类型和接口编号。]{style="font-family:
宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12801_72881_x1579628212}[：显示存储在指定单板上的绑定表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的绑定表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12801_72881_x2106977576}[：显示存储在指定成员设备上的绑定表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的绑定表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12801_72881_627923192}[：显示存储在指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的绑定表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的绑定表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12801_72881_x362276212}[：显示存储在指定成员设备上指定单板的绑定表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12801_72881_x1580621149}[：显示存储在指定单板的绑定表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_12801_72881_x1077167908}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示存储在指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的绑定表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-241285459 .myid}
[]{#_Toc404798934}[]{#struct_0_12801_72881_1510490795}

**IPCIM \-- IPCIM Probe命令 \-- display system internal ipv6 source binding**

------------------------------------------------------------------------

[**[display system internal ipv6 source binding]{lang="EN-US"}**]{#struct_0_12801_72881_1433011369}[命令用来显示详细的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[绑定表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12801_72881_85106822}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12801_72881_x1204613895}

[**[display system internal ipv6 source binding]{lang="EN-US"}**[ \[ **static** \| \[ **vpn-instance** *vpn-instance-name* \] \[**dhcpv6-snooping** \] \] \[ **ip-address** *ipv6-address* \] \[ **mac-address** *mac-address* \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \] ]{lang="EN-US"}]{#struct_0_12801_72881_x1805442285}

[[分布式设备]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_12801_72881_150538103}[独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}

[**[display system internal ipv6 source binding]{lang="EN-US"}**[ \[ **static** \| \[ **vpn-instance** *vpn-instance-name* \] \[**dhcpv6-snooping** \] \] \[ **ip-address** *ipv6-address* \] \[ **mac-address** *mac-address* \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12801_72881_x1307666268}

[[分布式设备]{style="font-family:宋体"}[-IRF]{lang="EN-US"}]{#struct_0_12801_72881_411257579}[模式]{style="font-family:宋体"}

[**[display system internal ipv6 source binding]{lang="EN-US"}**[ \[ **static** \| \[ **vpn-instance** *vpn-instance-name* \] \[**dhcpv6-snooping** \] \] \[ **ip-address** *ipv6-address* \] \[ **mac-address** *mac-address* \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12801_72881_x1935061491}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12801_72881_x425847060}

[[Probe]{lang="EN-US"}]{#struct_0_12801_72881_1781042495}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12801_72881_1510425259}

[[network-admin]{lang="EN-US"}]{#struct_0_12801_72881_x518495634}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12801_72881_92549232}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12801_72881_343718004}

[**[static]{lang="EN-US"}**]{#struct_0_12801_72881_1757613182}[：显示配置的静态绑定表项。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_12801_72881_x798636283}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的动态绑定表项，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示公网的动态绑定表项。]{style="font-family:宋体"}

[**[dhcpv6-snooping]{lang="EN-US"}**]{#struct_0_12801_72881_551030692}[：显示]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[模块生成的动态绑定表项。]{style="font-family:宋体"}

[**[ip-address]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_12801_72881_x2062754441}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的绑定表项，]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_12801_72881_2028858516}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的绑定表项，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_12801_72881_x1801401552}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的绑定表项，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_12801_72881_1510621867}[：显示指定接口的绑定表项，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示绑定的接口类型和接口编号。]{style="font-family:
宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12801_72881_304779329}[：显示存储在指定单板上的绑定表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的绑定表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12801_72881_1642710741}[：显示存储在指定成员设备上的绑定表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的绑定表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12801_72881_x1294325573}[：显示存储在指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的绑定表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的绑定表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12801_72881_683819888}[：显示存储在指定成员设备上指定单板的绑定表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12801_72881_1110979037}[：显示存储在指定单板的绑定表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_12801_72881_x1076905765}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示存储在指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的绑定表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
