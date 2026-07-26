::: {#1557977849 .myid}
[]{#_Toc404793778}[]{#struct_0_x1956_11086_457361217}

**IP Source Guard \-- IP Source Guard配置命令 \-- display ip source binding**

------------------------------------------------------------------------

[**[display ip source binding]{lang="EN-US"}**]{#struct_0_x1956_11086_x841691635}[命令用来显示]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[绑定表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x1755609560}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1956_11086_2045724625}

[**[display ip source binding ]{lang="EN-US"}**[\[ **static** \| \[ **vpn-instance** *vpn-instance-name* \] \[ **dhcp-relay** \| **dhcp-server** \| **dhcp-snooping** \| **dot1x** \] \] \[ **ip-address** *ip-address* \] \[ **mac-address** *mac-address* \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1956_11086_x973249332}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1956_11086_x268834713}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip source binding ]{lang="EN-US"}**[\[ **static** \| \[ **vpn-instance** *vpn-instance-name* \] \[ **dhcp-relay** \| **dhcp-server** \| **dhcp-snooping** \| **dot1x** \] \] \[ **ip-address** *ip-address* \] \[ **mac-address** *mac-address* \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1956_11086_x908987341}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1956_11086_x1582936172}[模式：]{style="font-family:宋体"}

[**[display ip source binding ]{lang="EN-US"}**[\[ **static** \| \[ **vpn-instance** *vpn-instance-name* \] \[ **dhcp-relay** \| **dhcp-server** \| **dhcp-snooping** \| **dot1x** \] \] \[ **ip-address** *ip-address* \] \[ **mac-address** *mac-address* \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1956_11086_139323792}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x1431712376}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1956_11086_x841363955}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x2143773609}

[[network-admin]{lang="EN-US"}]{#struct_0_x1956_11086_724305355}

[[network-operator]{lang="EN-US"}]{#struct_0_x1956_11086_x218581576}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1956_11086_845372902}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1956_11086_x1419940142}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x28080721}

[**[static]{lang="EN-US"}**]{#struct_0_x1956_11086_1077257022}[：显示配置的静态绑定表项。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1956_11086_x2047116210}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的动态绑定表项，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示公网的动态绑定表项。]{style="font-family:宋体"}

[**[dhcp-relay]{lang="EN-US"}**]{#struct_0_x1956_11086_x1676358285}[：显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继模块生成的动态绑定表项。]{style="font-family:宋体"}

[**[dhcp-server]{lang="EN-US"}**]{#struct_0_x1956_11086_x841298419}[：显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器模块生成的动态绑定表项。]{style="font-family:宋体"}

[**[dhcp-snooping]{lang="EN-US"}**]{#struct_0_x1956_11086_x215894653}[：显示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[模块生成的动态绑定表项。]{style="font-family:宋体"}

[**[dot1x]{lang="EN-US"}**]{#struct_0_x1956_11086_1093576072}[：显示]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[模块生成的动态绑定表项。]{style="font-family:宋体"}

[**[ip-address]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_x1956_11086_1217216827}[：显示指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的绑定表项，]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x1956_11086_598470299}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的绑定表项，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1956_11086_x1815314984}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的绑定表项，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1956_11086_1897540596}[：显示指定接口的绑定表项，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示绑定的接口类型和接口编号。]{style="font-family:
宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1956_11086_x2009704429}[：显示指定单板上的绑定表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的绑定表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1956_11086_2137706289}[：显示指定成员设备上的绑定表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的绑定表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1956_11086_2146280616}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的绑定表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的绑定表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1956_11086_x841495027}[：显示指定成员设备上指定单板的绑定表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1956_11086_613299988}[：显示指定单板的绑定表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1956_11086_580196675}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的绑定表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x1961468595}

[[\# ]{lang="EN-US"}]{#struct_0_x1956_11086_491680850}[显示公网所有接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[绑定表项和全局的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态绑定表项。]{style="font-family:宋体"}

[[\<Sysname\> display ip source binding]{lang="EN-US"}]{#struct_0_x1956_11086_x841429491}

[Total entries found: 5]{lang="EN-US"}

[IP Address      MAC Address    Interface                VLAN Type]{lang="EN-US"}

[10.1.0.5        040a-0000-4000 GE1/0/1                  1    DHCP snooping]{lang="EN-US"}

[10.1.0.6        040a-0000-3000 GE1/0/1                  1    DHCP snooping]{lang="EN-US"}

[10.1.0.7        040a-0000-2000 GE1/0/1                  1    DHCP snooping]{lang="EN-US"}

[10.1.0.8        040a-0000-1000 GE1/0/2                  N/A  DHCP relay]{lang="EN-US"}

[10.1.0.9        040a-0000-2000 GE1/0/2                  N/A  Static]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ip source-binding]{lang="EN-US"}]{#struct_0_x1956_11086_x1809569080}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1109648184}[[字段]{style="font-family:黑体"}]{#struct_0_x1956_11086_x1370804842}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1956_11086_x68611383}

[[Total entries found]{lang="EN-US"}]{#struct_0_x1956_11086_x1875324980}

[[查询到的绑定表项总数]{style="font-family:宋体"}]{#struct_0_x1956_11086_x1919122998}

[[IP Address]{lang="EN-US"}]{#struct_0_x1956_11086_2118611318}

[[绑定表项的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1956_11086_x841101811}[地址（]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示该表项不绑定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址）]{style="font-family:宋体"}

[[MAC Address]{lang="EN-US"}]{#struct_0_x1956_11086_1368819047}

[[绑定表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1956_11086_2022318731}[地址（]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示该表项不绑定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址）]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1956_11086_1750584213}

[[绑定表项所属的接口（]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_x1956_11086_1160401408}[表示该表项为全局绑定）]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_x1956_11086_361482211}

[[绑定表项所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1956_11086_x841036275}[（]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示该表项中没有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[信息）]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1956_11086_1360614597}

[[绑定表项类型：]{style="font-family:宋体"}]{#struct_0_x1956_11086_x2147146243}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_x1956_11086_992629412}[表示配置的静态绑定表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.1X]{lang="EN-US"}]{#struct_0_x1956_11086_292585276}[表示来源于]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[模块的动态绑定表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP relay]{lang="EN-US"}]{#struct_0_x1956_11086_740954003}[表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继模块生成的动态绑定表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP server]{lang="EN-US"}]{#struct_0_x1956_11086_724457845}[表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器模块生成的动态绑定表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP snooping]{lang="EN-US"}]{#struct_0_x1956_11086_398315146}[表示]{lang="EN-US" style="font-family:宋体"}[DHCP ]{lang="EN-US"}[S]{lang="EN-US"}[nooping]{lang="EN-US"}[模块生成的动态绑定表项]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x1757813902}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**]{#struct_0_x1956_11086_552292370}**[ source binding]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip verify]{lang="EN-US"}**[ **source**]{lang="EN-US"}]{#struct_0_x1956_11086_498958245}

::: {#-2119884469 .myid}
[]{#_Toc404793779}[]{#struct_0_x1956_11086_x1722123937}

**IP Source Guard \-- IP Source Guard配置命令 \-- display ipv6 source binding**

------------------------------------------------------------------------

[**[display ipv6 source binding]{lang="EN-US"}**]{#struct_0_x1956_11086_611687316}[命令用来显示]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[绑定表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_724523381}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1956_11086_106804594}

[**[display ipv6 source binding ]{lang="EN-US"}**[\[ **static** \| ]{lang="EN-US"}[\[ **vpn-instance** *vpn-instance-name* \] \[ **dhcpv6-snooping** \] \] \[ **ip-address** *ipv6-address* \] \[ **mac-address** *mac-address* \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1956_11086_329751255}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1956_11086_490235735}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display ipv6 source binding ]{lang="EN-US"}**[\[ **static** \|]{lang="EN-US"}[ \[ **vpn-instance** *vpn-instance-name* \] \[ **dhcpv6-snooping** \] \] \[ **ip-address** *ipv6-address* \] \[ **mac-address** *mac-address* \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1956_11086_x1976931180}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1956_11086_x674014207}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display ipv6 source binding ]{lang="EN-US"}**[\[ **static** \| ]{lang="EN-US"}[\[ **vpn-instance** *vpn-instance-name* \] \[ **dhcpv6-snooping** \] \] \[ **ip-address** *ipv6-address* \] \[ **mac-address** *mac-address* \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1956_11086_1959777286}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1956_11086_1124398187}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1956_11086_x2125408045}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1956_11086_1479428414}

[[network-admin]{lang="EN-US"}]{#struct_0_x1956_11086_724326773}

[[network-operator]{lang="EN-US"}]{#struct_0_x1956_11086_1370612488}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1956_11086_x48685565}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1956_11086_145853552}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1956_11086_2118966629}

[**[static]{lang="EN-US"}**]{#struct_0_x1956_11086_1961156751}[：显示配置的静态绑定表项。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1956_11086_440078164}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的动态绑定表项，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示公网的动态绑定表项。]{style="font-family:宋体"}

[**[dhcpv6-snooping]{lang="EN-US"}**]{#struct_0_x1956_11086_730498027}[：显示]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[模块生成的动态绑定表项。]{style="font-family:宋体"}

[**[ip-address]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_x1956_11086_x765195444}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的绑定表项，]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x1956_11086_724392309}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的绑定表项，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1956_11086_1366210199}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的绑定表项，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1956_11086_1391154181}[：显示指定接口的绑定表项，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示绑定的接口类型和接口编号。]{style="font-family:
宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1956_11086_x561566990}[：显示指定单板上的绑定表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的绑定表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1956_11086_x1470309171}[：显示指定成员设备上的绑定表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的绑定表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1956_11086_1965664081}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的绑定表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的绑定表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1956_11086_x768105392}[：显示指定成员设备上指定单板的绑定表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1956_11086_x1760811522}[：显示指定单板的绑定表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上的绑定表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1956_11086_696536829}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的绑定表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1956_11086_288014375}

[[\# ]{lang="EN-US"}]{#struct_0_x1956_11086_961476080}[显示公网所有接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[绑定表项和全局的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态绑定表项。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 source binding]{lang="EN-US"}]{#struct_0_x1956_11086_x653647125}

[Total entries found: 2]{lang="EN-US"}

[IPv6 Address         MAC Address    Interface               VLAN Type]{lang="EN-US"}

[2012:1222:2012:1222: 000f-2202-0435 GE1/0/1                 1    DHCPv6 snooping]{lang="EN-US"}

[2012:1222:2012:1222]{lang="EN-US"}

[2012:1222:2012:1222: 000f-2202-0436 GE1/0/1                 N/A  Static]{lang="EN-US"}

[2012:1222:2012:1223]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ipv6 source-binding]{lang="EN-US"}]{#struct_0_x1956_11086_860275339}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1136674488}[[字段]{style="font-family:黑体"}]{#struct_0_x1956_11086_x706098995}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1956_11086_724785525}

[[Total entries found]{lang="EN-US"}]{#struct_0_x1956_11086_345820554}

[[查询到的绑定表项总数]{style="font-family:宋体"}]{#struct_0_x1956_11086_2121127234}

[[IPv6 Address]{lang="EN-US"}]{#struct_0_x1956_11086_1698935392}

[[绑定表项的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1956_11086_1546433885}[地址（]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示该表项不绑定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址）]{style="font-family:宋体"}

[[MAC Address]{lang="EN-US"}]{#struct_0_x1956_11086_x767635778}

[[绑定表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1956_11086_1115580559}[地址（]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示该表项不绑定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址）]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1956_11086_724588917}

[[绑定表项所属的接口（]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_x1956_11086_792741068}[表示该表项为全局绑定）]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_x1956_11086_x100787858}

[[绑定表项所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1956_11086_1590316883}[（]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示该表项没有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[信息）]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1956_11086_x1850326531}

[[绑定表项所属的接口]{style="font-family:宋体"}]{#struct_0_x1956_11086_x775621230}

[[Type]{lang="EN-US"}]{#struct_0_x1956_11086_724654453}

[[绑定表项类型：]{style="font-family:宋体"}]{#struct_0_x1956_11086_316430148}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_x1956_11086_x1871200372}[表示配置的静态绑定表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCPv6 snooping]{lang="EN-US"}]{#struct_0_x1956_11086_401975324}[表示]{lang="EN-US" style="font-family:
  宋体"}[DHCPv6 ]{lang="EN-US"}[S]{lang="EN-US"}[nooping]{lang="EN-US"}[模块生成的动态绑定表项]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x575040838}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6]{lang="EN-US"}**]{#struct_0_x1956_11086_x785383011}**[ source binding]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 verify source]{lang="EN-US"}**]{#struct_0_x1956_11086_x21180404}

::: {#625414302 .myid}
[]{#_Toc404793780}[]{#struct_0_x1956_11086_724982133}[]{#_Toc320538913}[]{#_Toc320538927}[]{#_Toc320538965}[]{#_Toc320539072}[]{#_Toc320539087}[]{#_Toc320539200}

**IP Source Guard \-- IP Source Guard配置命令 \-- ip source binding(interface view)**

------------------------------------------------------------------------

[**[ip]{lang="DA"}**]{#struct_0_x1956_11086_1706336240}[ **source** **binding**]{lang="DA"}[命令用来配置接口的]{style="font-family:宋体"}[IPv4]{lang="DA"}[静态绑定表项。]{style="font-family:宋体"}

[**[undo ip]{lang="DA"}**]{#struct_0_x1956_11086_1154354502}[ **source** **binding**]{lang="DA"}[命令用来删除当前接口的]{style="font-family:宋体"}[IPv4]{lang="DA"}[静态绑定表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_1282495176}

[**[ip]{lang="EN-US"}**[ **source** **binding** { **ip-address** *ip-address* \| **ip-address** *ip-address* **mac-address** *mac-address \|* **mac-address** *mac-address* } \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x1956_11086_917814770}

[**[undo]{lang="EN-US"}**[ **ip** **source** **binding** { **all** \| **ip-address** *ip-address* \| **ip-address** *ip-address* **mac-address** *mac-address* \| **mac-address** *mac-address* } \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x1956_11086_x1252419081}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x901129374}

[[接口上无]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1956_11086_1657080397}[静态绑定表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x1391778551}

[[二层以太网端口]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1956_11086_725047669}[三层以太网接口]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x294629636}

[[network-admin]{lang="EN-US"}]{#struct_0_x1956_11086_1007226097}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1956_11086_x2094264999}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1956_11086_970055373}

[**[all]{lang="EN-US"}**]{#struct_0_x1956_11086_1560333524}[：当前接口所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态绑定表项，本参数只在]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **ip** **source** **binding**]{lang="EN-US"}[命令中生效。]{style="font-family:宋体"}

[**[ip-address]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_x1956_11086_x719277635}[：指定接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态绑定表项的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。其中]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，必须为]{style="font-family:宋体"}[A]{lang="EN-US"}[、]{style="font-family:宋体"}[B]{lang="EN-US"}[、]{style="font-family:
宋体"}[C]{lang="EN-US"}[三类地址之一，不能为]{style="font-family:宋体"}[127.x.x.x]{lang="EN-US"}[和]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x1956_11086_339953300}[：指定接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态绑定表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。其中]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[，取值不能为全]{style="font-family:宋体"}[0]{lang="EN-US"}[、全]{style="font-family:宋体"}[F]{lang="EN-US"}[（广播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[）和组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1956_11086_724457846}[：指定接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态绑定表项的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。本参数仅在二层以太网接口视图下支持。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1956_11086_398315147}

[[接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1956_11086_x1757813901}[静态绑定表项用于过滤接口收到的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文，或者与]{style="font-family:宋体"}[ARP Detection]{lang="EN-US"}[功能配合使用检查接入用户的合法性。]{style="font-family:宋体"}

[[加入业务环回组的接口上不能配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1956_11086_2118376311}[静态绑定表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1956_11086_763552054}

[[\# ]{lang="EN-US"}]{#struct_0_x1956_11086_x205260019}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置一条]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态绑定表项，仅允许源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.1]{lang="EN-US"}[且源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0001-0001-0001]{lang="EN-US"}[的报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1956_11086_627503295}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip source binding ip-address 192.168.0.1 mac-address 0001-0001-0001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x1613496139}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip source]{lang="EN-US"}**]{#struct_0_x1956_11086_724523382}**[ ]{lang="EN-US"}[binding]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip source binding]{lang="EN-US"}**]{#struct_0_x1956_11086_106804597}[(system view)]{lang="EN-US"}
:::

::: {#684161950 .myid}
[]{#_Toc404793781}[]{#struct_0_x1956_11086_329751256}

**IP Source Guard \-- IP Source Guard配置命令 \-- ip source binding(system view)**

------------------------------------------------------------------------

[**[ip]{lang="DA"}**]{#struct_0_x1956_11086_490235736}[ **source** **binding**]{lang="DA"}[命令用来配置全局的]{style="font-family:宋体"}[IPv4]{lang="DA"}[静态绑定表项。]{style="font-family:宋体"}

[**[undo ip]{lang="DA"}**]{#struct_0_x1956_11086_x1976931181}[ **source** **binding**]{lang="DA"}[命令用来删除已配置的全局]{style="font-family:宋体"}[IPv4]{lang="DA"}[静态绑定表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_2054869148}

[**[ip]{lang="EN-US"}**[ **source** **binding** **ip-address** *ip-address* **mac-address** *mac-address*]{lang="EN-US"}]{#struct_0_x1956_11086_682969033}

[**[undo]{lang="EN-US"}**[ **ip** **source** **binding** { **all** \| **ip-address** *ip-address* **mac-address** *mac-address* }]{lang="EN-US"}]{#struct_0_x1956_11086_x80603852}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x81095336}

[[设备上无全局的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1956_11086_724326774}[静态绑定表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1956_11086_1370612491}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1956_11086_x49275390}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1956_11086_220317815}

[[network-admin]{lang="EN-US"}]{#struct_0_x1956_11086_x1624130597}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1956_11086_x654654878}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1956_11086_747315297}

[**[ip-address]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_x1956_11086_x2019687273}[：指定全局的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态绑定表项的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。其中]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，必须为]{style="font-family:宋体"}[A]{lang="EN-US"}[、]{style="font-family:宋体"}[B]{lang="EN-US"}[、]{style="font-family:
宋体"}[C]{lang="EN-US"}[三类地址之一，不能为]{style="font-family:宋体"}[127.x.x.x]{lang="EN-US"}[和]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x1956_11086_1784959849}[：指定全局的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态绑定表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。其中]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[，取值不能为全]{style="font-family:宋体"}[0]{lang="EN-US"}[、全]{style="font-family:宋体"}[F]{lang="EN-US"}[（广播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[）和组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1956_11086_x1558821359}[：设备上所有全局的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态绑定表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1956_11086_724392310}

[[全局的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1956_11086_x972441954}[静态绑定表项对设备的所有接口都生效。]{style="font-family:宋体"}

[[设备最多允许配置的全局的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1956_11086_x1461416473}[静态绑定表项数量与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x360578819}

[[\# ]{lang="EN-US"}]{#struct_0_x1956_11086_661814350}[在设备上配置一条全局的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态绑定表项，允许源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.1]{lang="EN-US"}[且源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0001-0001-0001]{lang="EN-US"}[的报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1956_11086_x580482707}

[\[Sysname\] ip source binding ip-address 192.168.0.1 mac-address 0001-0001-0001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_1518427059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip source]{lang="EN-US"}**]{#struct_0_x1956_11086_102463800}**[ ]{lang="EN-US"}[binding]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip source binding]{lang="EN-US"}**]{#struct_0_x1956_11086_724719990}[(interface view)]{lang="EN-US"}
:::

::: {#971233793 .myid}
[]{#_Toc404793782}[]{#struct_0_x1956_11086_x1702935644}

**IP Source Guard \-- IP Source Guard配置命令 \-- ip verify source**

------------------------------------------------------------------------

[**[ip verify source]{lang="EN-US"}**]{#struct_0_x1956_11086_x1718931721}[命令用来配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[接口绑定功能。]{style="font-family:宋体"}

[**[undo ip verify source]{lang="EN-US"}**]{#struct_0_x1956_11086_2007272945}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x945410579}

[**[ip ]{lang="EN-US"}[verify source ]{lang="EN-US"}**[{ **ip-address**]{lang="EN-US"}*[ ]{lang="EN-US"}*[\| **ip-address mac-address** \| **mac-address** }]{lang="EN-US"}]{#struct_0_x1956_11086_x1076358829}

[**[undo ip ]{lang="EN-US"}[verify source]{lang="EN-US"}**]{#struct_0_x1956_11086_1176389804}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1956_11086_168565687}

[[接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1956_11086_x1753718688}[接口绑定功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1956_11086_245416317}

[[二层以太网端口]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1956_11086_724785526}[三层以太网接口]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1956_11086_345820553}

[[network-admin]{lang="EN-US"}]{#struct_0_x1956_11086_2121127239}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1956_11086_1698738784}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1956_11086_828945275}

[**[ip-address]{lang="EN-US"}**]{#struct_0_x1956_11086_158050142}[：表示绑定源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，即根据接口收到的报文的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址对报文进行过滤。]{style="font-family:宋体"}

[**[ip-address mac-address]{lang="EN-US"}**]{#struct_0_x1956_11086_x820384917}[：表示绑定源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[,]{lang="EN-US"}[即接口上收到的报文的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址和源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址都与某动态绑定表项匹配，该报文才能被正常转发，否则将被丢弃。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}**]{#struct_0_x1956_11086_x1831260532}[：表示绑定源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，即根据接口收到的报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对报文进行过滤。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1956_11086_1192379253}

[[配置该功能后，]{style="font-family:宋体"}[IP Source Guard]{lang="EN-US"}]{#struct_0_x1956_11086_724588918}[模块会通过配置的静态绑定表项或通过获取其它模块表项信息生成的动态绑定表项过滤接口收到的用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文，符合绑定表项的用户报文被正常转发，不符合绑定表项的用户报文将被丢弃。目前，可为]{style="font-family:宋体"}[IP Source Guard]{lang="EN-US"}[提供动态绑定表项信息的模块包括]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[、]{style="font-family:宋体"}[DHCP relay]{lang="EN-US"}[、]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[、]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器。其中，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继、]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[模块生成的动态绑定表项可被]{style="font-family:宋体"}[IP Source Guard]{lang="EN-US"}[模块用于过滤报文，]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[模块和]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器模块生成的动态绑定表项不被直接用于过滤报文，用于配合其它模块提供相应的安全服务，比如]{style="font-family:宋体"}[ARP Detection]{lang="EN-US"}[可利用]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[模块生成的动态绑定表项进行用户]{style="font-family:宋体"}[ARP]{lang="EN-US"}[合法性检查。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1956_11086_792741059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[加入业务环回组的接口上不能配置动态绑定功能。]{style="font-family:宋体"}]{#struct_0_x1956_11086_x2057102995}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令中指定的绑定参数，仅对动态生成的绑定表项有效，是接口使用动态绑定表项过滤报文时关心的报文特征项。如果仅使用静态绑定表项来过滤接口的报文，则本命令仅用于控制是否开启接口的报文过滤功能，接口依据配置的静态绑定表项参数来过滤报文，而不关心本命令中指定的参数。]{style="font-family:宋体"}]{#struct_0_x1956_11086_x1150962295}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1956_11086_2048428206}

[[\# ]{lang="EN-US"}]{#struct_0_x1956_11086_261282993}[在二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[接口绑定功能，根据报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对接口收到的报文进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1956_11086_x964089995}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip verify source ip-address mac-address]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1956_11086_x1666584550}[在]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置对报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[和]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[接口绑定功能，根据报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对接口收到的报文进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1956_11086_724654454}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ip verify source ip-address mac-address]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1956_11086_316430149}[在三层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上配置对报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[和]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[接口绑定功能，根据报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对接口收到的报文进行过滤。该配置的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1956_11086_x1871200371}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] ip verify source ip-address mac-address]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1956_11086_x1309203}[在三层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上配置对报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[接口绑定功能，根据报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对接口收到的报文进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1956_11086_2023818203}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] ip verify source mac-address]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_196070191}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip source]{lang="EN-US"}**]{#struct_0_x1956_11086_x1860384761}**[ ]{lang="EN-US"}[binding]{lang="EN-US"}**
:::

::: {#-1536581422 .myid}
[]{#_Toc404793783}[]{#struct_0_x1956_11086_483837362}

**IP Source Guard \-- IP Source Guard配置命令 \-- ipv6 source binding(interface view)**

------------------------------------------------------------------------

[**[ipv6]{lang="EN-US"}**[ **source** **binding**]{lang="EN-US"}]{#struct_0_x1956_11086_724982134}[命令用来配置接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态绑定表项。]{style="font-family:宋体"}

[**[undo ipv6]{lang="EN-US"}**[ **source** **binding**]{lang="EN-US"}]{#struct_0_x1956_11086_1706336247}[命令用来删除当前接口配置的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态绑定表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_1154682182}

[**[ipv6]{lang="EN-US"}**[ **source** **binding** { **ip-address** *ipv6-address* \| **ip-address** *ipv6-address* **mac-address** *mac-address \|* **mac-address** *mac-address* } \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x1956_11086_1678064545}

[**[undo ipv6]{lang="EN-US"}**[ **source** **binding** { **all** \| **ip-address** *ipv6-address* \| **ip-address** *ipv6-address* **mac-address** *mac-address \|* **mac-address** *mac-address* } \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x1956_11086_502531958}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1956_11086_2001943658}

[[接口上无]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1956_11086_1414177152}[静态绑定表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1956_11086_1783331238}

[[二层以太网端口]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1956_11086_463989804}[三层以太网接口]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x1723620477}

[[network-admin]{lang="EN-US"}]{#struct_0_x1956_11086_725047670}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1956_11086_2044022533}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1956_11086_1361727010}

[**[all]{lang="EN-US"}**]{#struct_0_x1956_11086_957055913}[：当前接口所有的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态绑定表项，本参数只在]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **ipv6** **source** **binding**]{lang="EN-US"}[命令中生效。]{style="font-family:宋体"}

[**[ip-address]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_x1956_11086_x1326827239}[：指定接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态绑定表项的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。其中]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，不能为全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址、组播地址、环回地址。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x1956_11086_1426953693}[：指定接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态绑定表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。其中]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[，取值不能为全]{style="font-family:宋体"}[0]{lang="EN-US"}[、全]{style="font-family:宋体"}[F]{lang="EN-US"}[（广播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[）和组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1956_11086_440635539}[：指定接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态绑定表项的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。本参数仅在二层以太网接口视图下支持。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x834382378}

[[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1956_11086_724457843}[静态绑定表项用于过滤接口收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文，或者与]{style="font-family:宋体"}[ND Detection]{lang="EN-US"}[功能配合使用检查接入用户的合法性。]{style="font-family:宋体"}

[[加入业务环回组的接口上不能配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1956_11086_398315144}[静态绑定表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x1757813904}

[[\# ]{lang="EN-US"}]{#struct_0_x1956_11086_1358861424}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置一条]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态绑定表项，仅允许源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[且源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0002-0002-0002]{lang="EN-US"}[的报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1956_11086_2048765808}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 source binding ip-address 2001::1 mac-address 0002-0002-0002]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x2083464859}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 source]{lang="EN-US"}**]{#struct_0_x1956_11086_854908525}**[ ]{lang="EN-US"}[binding]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 source binding]{lang="EN-US"}**]{#struct_0_x1956_11086_1345257360}[(system view)]{lang="EN-US"}
:::

::: {#-790296085 .myid}
[]{#_Toc404793784}[]{#struct_0_x1956_11086_724523379}

**IP Source Guard \-- IP Source Guard配置命令 \-- ipv6 source binding(system view)**

------------------------------------------------------------------------

[**[ipv6]{lang="DA"}**]{#struct_0_x1956_11086_444511610}[ **source** **binding**]{lang="DA"}[命令用来配置全局的]{style="font-family:宋体"}[IPv6]{lang="DA"}[静态绑定表项。]{style="font-family:宋体"}

[**[undo ipv6]{lang="DA"}**]{#struct_0_x1956_11086_x1609076016}[ **source** **binding**]{lang="DA"}[命令用来删除已配置的全局]{style="font-family:宋体"}[IPv6]{lang="DA"}[静态绑定表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x158367859}

[**[i]{lang="DA"}[pv6]{lang="EN-US"}**[ **source** **binding** **ip-address** *ipv6-address* **mac-address** *mac-address*]{lang="EN-US"}]{#struct_0_x1956_11086_987742704}

[**[undo]{lang="EN-US"}**[ **ipv6** **source** **binding** { **all** \| **ip-address** *ipv6-address* **mac-address** *mac-address* }]{lang="EN-US"}]{#struct_0_x1956_11086_x1542285010}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1956_11086_1220525552}

[[设备上无全局的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1956_11086_1010947433}[静态绑定表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x1581090664}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1956_11086_11297210}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1956_11086_724326771}

[[network-admin]{lang="EN-US"}]{#struct_0_x1956_11086_1370612486}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1956_11086_x49603069}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1956_11086_677324088}

[**[ip-address]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_x1956_11086_x1215817913}[：指定全局的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态绑定表项的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。其中]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，不能为全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址、组播地址、环回地址。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x1956_11086_1684486591}[：指定全局的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态绑定表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。其中]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[表示绑定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[，取值不能为全]{style="font-family:宋体"}[0]{lang="EN-US"}[、全]{style="font-family:宋体"}[F]{lang="EN-US"}[（广播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[）和组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1956_11086_2063622188}[：设备上所有全局的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态绑定表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x1521340229}

[[全局的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1956_11086_2140913052}[静态绑定表项对设备的所有接口都生效。]{style="font-family:宋体"}

[[设备最多允许配置的全局的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1956_11086_724392307}[静态绑定表项数量与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1956_11086_1366210205}

[[\# ]{lang="EN-US"}]{#struct_0_x1956_11086_x565947378}[在设备上配置一条全局的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态绑定表项，允许源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[且源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0002-0002-0002]{lang="EN-US"}[的报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1956_11086_x593997342}

[\[Sysname\] ipv6 source binding ip-address 2001::1 mac-address 0002-0002-0002]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x439248096}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip]{lang="EN-US"}**]{#struct_0_x1956_11086_x1553824064}**[v6]{lang="EN-US"}[ source]{lang="EN-US"}[ ]{lang="EN-US"}[binding]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 source binding]{lang="EN-US"}**]{#struct_0_x1956_11086_x668337334}[(interface view)]{lang="EN-US"}
:::

::: {#166980183 .myid}
[]{#_Toc404793785}[]{#struct_0_x1956_11086_x833007300}[]{#_Toc320538917}[]{#_Toc320538931}[]{#_Toc320538969}[]{#_Toc320539076}[]{#_Toc320539091}[]{#_Toc320539204}

**IP Source Guard \-- IP Source Guard配置命令 \-- ipv6 verify source**

------------------------------------------------------------------------

[**[ipv6 ve]{lang="EN-US"}[rify source]{lang="EN-US"}**]{#struct_0_x1956_11086_x294288418}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[接口绑定功能。]{style="font-family:宋体"}

[**[undo ipv6 verify source]{lang="EN-US"}**]{#struct_0_x1956_11086_724719987}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_635716515}

[**[ipv6 ]{lang="EN-US"}[verify source ]{lang="EN-US"}**[{ **ip-address**]{lang="EN-US"}*[ ]{lang="EN-US"}*[\| **ip-address** **mac-address** \| **mac-address** }]{lang="EN-US"}]{#struct_0_x1956_11086_x1668300761}

[**[undo ipv6 ]{lang="EN-US"}[verify source]{lang="EN-US"}**]{#struct_0_x1956_11086_x660032404}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x1419966059}

[[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1956_11086_1281473727}[接口绑定功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1956_11086_1489240661}

[[二层以太网端口]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1956_11086_x759990346}[三层以太网接口]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x203951383}

[[network-admin]{lang="EN-US"}]{#struct_0_x1956_11086_724785523}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1956_11086_345820548}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x217524914}

[**[ip-address]{lang="EN-US"}**]{#struct_0_x1956_11086_x570972949}[：表示绑定源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，即根据接口收到的报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对报文进行过滤。]{style="font-family:宋体"}

[**[ip-address mac-address]{lang="EN-US"}**]{#struct_0_x1956_11086_1394404373}[：表示绑定源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[,]{lang="EN-US"}[即接口上收到的报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址都与某动态绑定表项匹配，该报文才能被正常转发，否则将被丢弃。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}**]{#struct_0_x1956_11086_x812045678}[：表示绑定源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，即根据接口收到的报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对报文进行过滤。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1956_11086_729034631}

[[配置该功能后，]{style="font-family:宋体"}[IP Source Guard]{lang="EN-US"}]{#struct_0_x1956_11086_1982343165}[模块会通过配置的静态绑定表项或通过获取]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项生成的动态绑定表项来过滤接口收到的用户]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文，符合绑定表项的用户报文被正常转发，不符合绑定表项的用户报文将被丢弃。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1956_11086_x2129722632}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[加入业务环回组的接口上不能配置动态绑定功能。]{style="font-family:宋体"}]{#struct_0_x1956_11086_1185120461}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令中指定的绑定参数，仅对动态生成的绑定表项有效，是接口使用动态绑定表项过滤报文时关心的报文特征项。如果仅使用静态绑定表项来过滤接口的报文，则本命令仅用于控制是否开启接口的报文过滤功能，接口依据配置的静态绑定表项参数来过滤报文，而不关心本命令中指定的参数。]{style="font-family:宋体"}]{#struct_0_x1956_11086_724588915}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1956_11086_792741070}

[[\# ]{lang="EN-US"}]{#struct_0_x1956_11086_1855527286}[在二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[接口绑定功能，根据报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对接口收到的报文进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1956_11086_464974905}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 verify source ip-address mac-address]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1956_11086_x557234001}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 source binding]{lang="EN-US"}**]{#struct_0_x1956_11086_x1041752198}[]{#_Toc320538919}[]{#_Toc320538933}[]{#_Toc320538971}[]{#_Toc320539078}[]{#_Toc320539093}[]{#_Toc320539207}
:::
