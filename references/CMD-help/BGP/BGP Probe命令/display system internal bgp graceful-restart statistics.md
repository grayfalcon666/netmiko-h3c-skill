
**BGP \-- BGP Probe命令 \-- display system internal bgp graceful-restart statistics**

------------------------------------------------------------------------

**[display system internal bgp graceful-restart statistics**]命令用来显示BGP GR统计信息。

【命令】

**[display system internal bgp graceful-restart** **statistics**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**BGP \-- BGP Probe命令 \-- display system internal bgp instance statistics**

------------------------------------------------------------------------

**[display system internal bgp instance statistics**]命令用来显示BGP实例统计信息。

【命令】

集中式设备：

**[display system internal bgp instance **[{ **ipv4** \| **ipv6** \| **vpnv4** } [ **vpn-instance** *vpn-instance-name*   **rib** \| **send** ] **statistics**]]

**[display system internal bgp instance ****[l2vpn **[\| **vpnv6** } [ **rib** \| **send** ] **statistics**]]

**[display system internal bgp instance ipv4 mdt**[ [ **rib** \| **send** ] **statistics**]]

**[display system internal bgp instance **[{ **ipv4** \| **ipv6** } **multicast**  [ **rib** \| **send** ] **statistics**]]

分布式设备---独立运行模式]/集中式IRF设备：

**[display system internal bgp instance **[{ **ipv4** \| **ipv6** \| **vpnv4** } [ **vpn-instance** *vpn-instance-name*   **rib** \| **send** ] **statistics**  **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp instance ****[l2vpn **[\| **vpnv6** } [ **rib** \| **send** ] **statistics**  **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp instance **[{ **ipv4** \| **ipv6** } **multicast**  [ **rib** \| **send** ] **statistics**  **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备---]IRF模式：

**[display system internal bgp instance **[{ **ipv4** \| **ipv6** \| **vpnv4** } [ **vpn-instance** *vpn-instance-name*   **rib** \| **send** ] **statistics**  **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp instance ****[l2vpn **[\| **vpnv6** } [ **rib** \| **send** ] **statistics**  **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp instance **[{ **ipv4** \| **ipv6** } **multicast**  [ **rib** \| **send** ] **statistics**  **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】]

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：显示IPv4地址族的BGP实例统计信息。

**[ipv6**]：显示IPv6地址族的BGP实例统计信息。

**[vpnv4**]：显示VPNv4地址族的BGP实例统计信息。

**[l2vpn**]：显示L2VPN地址族的BGP实例统计信息。

**[vpnv6**]：显示VPNv6地址族的BGP实例统计信息。

**[mdt**]：显示MDT地址族的BGP实例统计信息。

**[multicast**]：显示组播地址族的BGP实例统计信息。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的BGP实例统计信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网BGP实例的统计信息。

**[rib**]：显示BGP实例路由模块的统计信息。

**[send**]：显示BGP实例发送模块的统计信息。

**[standby**]：显示指定BGP备进程的信息。如果不指定本参数，则显示BGP主进程的信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

执行本命令时，如果没有指定**rib**和**send**参数，则显示BGP协议的实例统计信息。

开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程。执行本命令时，如果指定了**standby**参数，则显示备份到指定备进程的信息。如果没有开启BGP NSR功能，则指定**standby**参数时，不会显示任何信息。通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp interface**

------------------------------------------------------------------------

**[display system internal bgp interface**]命令用来显示BGP接口信息。

【命令】

**[display system internal bgp interface******ipv4 **[ **vpn-instance** *vpn-instance-name* [ *interface-type* *interface-number* \| *ipv4-address* { *mask* \| *mask-length* } ]]]

**[display system internal bgp interface******ipv6 **[ **vpn-instance** *vpn-instance-name* [ *interface-type* *interface-number* \| *ipv6-address* *prefix-length* ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：显示IPv4地址族的BGP接口信息。

**[ipv6**]：显示IPv6地址族的BGP接口信息。

**[vpn-instance ***vpn-instance-name*]**：**显示指定VPN实例的BGP接口信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网的BGP接口信息。

*[interface-type* *interface-number*]：显示指定BGP接口的信息。*interface-type* *interface-number*为接口类型和接口编号。

*[ipv4-address*[ { *mask* \| *mask-length* }]]：显示IPv4地址为指定值的BGP接口的信息。*ipv4-address*为接口的IPv4地址；*mask*为接口IPv4地址的网络掩码；*mask-length*为接口IPv4地址的网络掩码长度，取值范围为0～32。

*[ipv6-address* *prefix-length*]：显示IPv6地址为指定值的BGP接口的信息。*ipv6-address*为接口的IPv6地址；*prefix-length*为接口IPv6地址的前缀长度，取值范围为0～128。

【使用指导】

执行本命令时，如果没有指定*interface-type* *interface-number*和*ipv4-address*[ { *mask* \| *mask-length* }]、*ipv6-address* *prefix-length*参数，则显示所有BGP接口的信息。

**BGP \-- BGP Probe命令 \-- display system internal bgp l2vpn auto-discovery advertise-info**

------------------------------------------------------------------------

**[display system internal bgp l2vpn auto-discovery advertise-info**]命令用来显示通过BGP协议自动发现的VPLS PE的通告信息。

【命令】

集中式设备：

**[display system internal bgp l2vpn auto-discovery route-distinguisher ***route-distinguisher*** pe-address*** ip-address*** advertise-info**]

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp l2vpn auto-discovery route-distinguisher ***route-distinguisher*** pe-address*** ip-address*** advertise-info ** **standby** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备---IRF模式：

**[display system internal bgp l2vpn auto-discovery route-distinguisher ***route-distinguisher*** pe-address*** ip-address*** advertise-info ** **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[route-distinguisher** *route-distinguisher*]：显示指定路由标识符的信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[pe-address** *ip-address*]：显示通过BGP协议自动发现的指定VPLS PE的信息。*ip-address*为自动发现的PE的IP地址。

**[standby**]：显示指定BGP备进程的信息。如果不指定本参数，则显示BGP主进程的信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程。执行本命令时，如果指定了**standby**参数，则显示备份到指定备进程的信息。如果没有开启BGP NSR功能，则指定**standby**参数时，不会显示任何信息。通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp l2vpn auto-discovery standby**

------------------------------------------------------------------------

**[display system internal bgp l2vpn auto-discovery standby**]命令用来显示BGP备进程上通过BGP协议自动发现的VPLS PE信息。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp l2vpn auto-discovery **[[ **peer** *ip-address* { **advertised** \| **received** } [ **statistics** ] \| **route-distinguisher** *route-distinguisher*  **pe-address** *ip-address*  \| **statistics** ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备---IRF模式：

**[display system internal bgp l2vpn auto-discovery **[[ **peer** *ip-address* { **advertised** \| **received** } [ **statistics** ] \| **route-distinguisher** *route-distinguisher*  **pe-address** *ip-address*  \| **statistics** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[peer** *ip-address*]：显示向指定对等体发布或者从指定对等体收到的BGP协议自动发现VPLS PE信息。*ip-address*表示对等体的地址。

**[advertised**]：显示向指定对等体发布的BGP协议自动发现VPLS PE信息。

**[received**]：显示从指定对等体接收到的BGP协议自动发现VPLS PE信息。

**[statistics**]：显示BGP协议自动发现的VPLS PE的统计信息。

**[route-distinguisher*** route-distinguisher*]：显示通过BGP协议自动发现的指定路由标识符的VPLS PE信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[pe-address ***ip-address*]：显示通过BGP协议自动发现的指定VPLS PE的信息。*ip-address*为自动发现的PE的IP地址。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·执行本命令时，如果没有指定任何参数，则显示指定BGP备进程上所有通过BGP协议自动发现的VPLS PE的简要信息。

·开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启BGP NSR功能，则不会显示任何信息。

·通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp l2vpn auto-discovery verbose**

------------------------------------------------------------------------

**[display system internal bgp l2vpn auto-discovery verbose**]命令用来显示通过BGP协议自动发现的VPLS PE的详细信息。

【命令】

集中式设备：

**[display system internal bgp l2vpn auto-discovery route-distinguisher ***route-distinguisher*** pe-address*** ip-address*** verbose**]

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp l2vpn auto-discovery route-distinguisher ***route-distinguisher*** pe-address*** ip-address*** verbose ** **standby** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备---IRF模式：

**[display system internal bgp l2vpn auto-discovery route-distinguisher ***route-distinguisher*** pe-address*** ip-address*** verbose ** **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[route-distinguisher** *route-distinguisher*]：显示指定路由标识符的信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[pe-address** *ip-address*]：显示通过BGP协议自动发现的指定VPLS PE的详细信息。*ip-address*为自动发现的PE的IP地址。

**[standby**]：显示指定BGP备进程的信息。如果不指定本参数，则显示BGP主进程的信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程。执行本命令时，如果指定了**standby**参数，则显示备份到指定备进程的信息。如果没有开启BGP NSR功能，则指定**standby**参数时，不会显示任何信息。通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp l2vpn signaling advertise-info**

------------------------------------------------------------------------

**[display system internal bgp l2vpn signaling advertise-info**]命令用来显示BGP L2VPN标签块的通告信息。

【命令】

集中式设备：

**[display system internal bgp l2vpn signaling route-distinguisher ***route-distinguisher*** site-id ***site-id ***label-offset ***label-offset*** advertise-info**]

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp l2vpn signaling route-distinguisher ***route-distinguisher*** site-id ***site-id ***label-offset ***label-offset*** advertise-info ** **standby** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备---IRF模式：

**[display system internal bgp l2vpn signaling route-distinguisher ***route-distinguisher*** site-id ***site-id ***label-offset ***label-offset*** advertise-info ** **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[route-distinguisher** *route-distinguisher*]：显示指定路由标识符的信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[site-id*** site-id*]：显示为指定站点分配的BGP L2VPN标签块的通告信息。*site-id*为站点编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[label-offset ***label-offset*]：显示标签块偏移量为指定值的BGP L2VPN标签块的通告信息。*label-offset*为标签块偏移量，取值范围为0～65535。

**[standby**]：显示指定BGP备进程的信息。如果不指定本参数，则显示BGP主进程的信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程。执行本命令时，如果指定了**standby**参数，则显示备份到指定备进程的信息。如果没有开启BGP NSR功能，则指定**standby**参数时，不会显示任何信息。通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp l2vpn signaling standby**

------------------------------------------------------------------------

**[display system internal bgp l2vpn signaling standby**]命令用来显示BGP备进程上的MPLS L2VPN标签块信息。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp l2vpn signaling**[ [ **peer** *ip-address* { **advertised** \| **received** } [ **statistics** ] \| **route-distinguisher** *route-distinguisher*  **site-id** *site-id* [ **label-offset** *label-offset*  ] \| **statistics** ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备---IRF模式：

**[display system internal bgp l2vpn signaling**[ [ **peer** *ip-address* { **advertised** \| **received** } [ **statistics** ] \| **route-distinguisher** *route-distinguisher*  **site-id** *site-id* [ **label-offset** *label-offset*  ] \| **statistics** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[peer ***ip-address*]：显示向指定对等体发布或者从指定对等体收到的MPLS L2VPN标签块信息。*ip-address*表示对等体的IP地址。

**[advertised**]：显示向指定对等体发布的MPLS L2VPN标签块信息。

**[received**]：显示从指定对等体接收到的MPLS L2VPN标签块信息。

**[statistics**]：显示MPLS L2VPN标签块的统计信息。

**[route-distinguisher*** route-distinguisher*]：显示指定路由标识符的MPLS L2VPN标签块信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[site-id*** site-id*]：显示为指定站点分配的MPLS L2VPN标签块信息。*site-id*为站点编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[label-offset ***label-offset*]：显示标签块偏移量为指定值的MPLS L2VPN标签块信息。*label-offset*为标签块偏移量，取值范围为0～65535。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·执行本命令时，如果没有指定任何参数，则显示指定BGP备进程上所有MPLS L2VPN标签块的简要信息。

·开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启BGP NSR功能，则不会显示任何信息。

·通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp l2vpn signaling verbose**

------------------------------------------------------------------------

**[display system internal bgp l2vpn signaling verbose**]命令用来显示BGP L2VPN标签块的详细信息。

【命令】

集中式设备：

**[display system internal bgp l2vpn signaling route-distinguisher ***route-distinguisher*** site-id ***site-id ***label-offset ***label-offset*** verbose**]

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp l2vpn signaling route-distinguisher ***route-distinguisher*** site-id ***site-id ***label-offset ***label-offset*** verbose ** **standby** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备---IRF模式：

**[display system internal bgp l2vpn signaling route-distinguisher ***route-distinguisher*** site-id ***site-id ***label-offset ***label-offset*** verbose ** **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[route-distinguisher** *route-distinguisher*]：显示指定路由标识符的信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[site-id*** site-id*]：显示为指定站点分配的BGP L2VPN标签块的详细信息。*site-id*为站点编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[label-offset ***label-offset*]：显示标签块偏移量为指定值的BGP L2VPN标签块的详细信息。*label-offset*为标签块偏移量，取值范围为0～65535。

**[standby**]：显示指定BGP备进程的信息。如果不指定本参数，则显示BGP主进程的信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程。执行本命令时，如果指定了**standby**参数，则显示备份到指定备进程的信息。如果没有开启BGP NSR功能，则指定**standby**参数时，不会显示任何信息。通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp nib**

------------------------------------------------------------------------

**[display system internal bgp nib**]命令用来显示BGP路由下一跳信息。

【命令】

**[display system internal bgp nib **[{ **ipv4** \| **ipv6** } [ *nib-id* ]  **verbose** ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：显示IPv4地址族的BGP路由下一跳信息。

**[ipv6**]：显示IPv6地址族的BGP路由下一跳信息。

*[nib-id*]：下一跳ID，取值范围为1～FFFFFFFF。如果不指定本参数，则显示所有下一跳信息。

**[verbose**]：显示下一跳的详细信息。如果不指定本参数，则显示下一跳的简要信息。

**BGP \-- BGP Probe命令 \-- display system internal bgp nib log**

------------------------------------------------------------------------

**[display system internal bgp nib log**]命令用来显示BGP路由下一跳的日志信息。

【命令】

**[display system internal bgp nib log**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**BGP \-- BGP Probe命令 \-- display system internal bgp peer standby**

------------------------------------------------------------------------

**[display system internal bgp peer standby**]命令用来显示BGP备进程上BGP对等体的信息。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp peer ipv4 ****[multicast **[\| [ **unicast** ]  **vpn-instance** *vpn-instance-name * } ]  *ip-address*  **verbose** ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]

**[display system internal bgp peer ipv6 ****[multicast**[ \| [ **unicast** ] \**vpn-instance ***vpn-instance-name*  }  [ *ipv6-address*  **verbose** ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

**[display system internal bgp peer ipv6 ** **unicast** ]   *ip-address*  **verbose** ] **standby** **slot** *slot-number*  **cpu** *cpu-number*

**[display system internal bgp peer vpnv4** [ **vpn-instance** *vpn-instance-name *  [ *ip-address*  **verbose** ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

**[display system internal bgp peer **[[ \| **vpnv6** } [ [ *ip-address* ] **verbose** ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备---]IRF模式：

**[display system internal bgp peer ipv4 ****[multicast **[\| [ **unicast** ]  **vpn-instance** *vpn-instance-name * } ]  *ip-address*  **verbose** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]

**[display system internal bgp peer ipv6 ****[multicast**[ \| [ **unicast** ] \**vpn-instance ***vpn-instance-name*  }  [ *ipv6-address*  **verbose** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

**[display system internal bgp peer ipv6 ** **unicast** ]   *ip-address*  **verbose** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*

**[display system internal bgp peer vpnv4** [ **vpn-instance** *vpn-instance-name *  [ *ip-address*  **verbose** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

**[display system internal bgp peer **[[ \| **vpnv6** } [ [ *ip-address* ] **verbose** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】]

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：显示BGP IPv4对等体的信息。

**[ipv6**]：显示BGP IPv6对等体的信息。

**[vpnv4**]：显示BGP VPNv4对等体的信息。

**[l2vpn**]：显示BGP L2VPN对等体的信息。

**[vpnv6**]：显示BGP VPNv6对等体的信息。

**[multicast**]：显示BGP组播对等体的信息。

**[unicast**]：显示BGP单播对等体的信息。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN实例的BGP对等体的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网BGP对等体的信息。

*[ip-address*]：显示指定对等体的信息。*ip-address*为对等体的IP地址。如果不指定本参数，则显示所有BGP对等体的信息。

*[ipv6-address*]：显示指定对等体的信息。*ipv6-address*为对等体的IPv6地址。如果不指定本参数，则显示所有BGP对等体的信息。

**[verbose**]：显示对等体的详细信息。如果不指定本参数，则显示BGP对等体的简要信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

执行本命令时，如果没有指定**unicast**和**multicast**参数，则缺省为**unicast**。

开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启BGP NSR功能，则不会显示任何信息。

通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp peer statistics**

------------------------------------------------------------------------

**[display system internal bgp peer statistics**]命令用来显示BGP对等体的统计信息。

【命令】

集中式设备：

**[display system internal bgp peer **[{ **ipv4** \| **vpnv4** } [ **vpn-instance** *vpn-instance-name* ] *ipv4-address* [ **rib** \| **send** \| **session** ] **statistics**]]

**[display system internal bgp peer ipv6 **[[ \| [ **vpn-instance** *vpn-instance-name* ] *ipv6-address* } [ **rib** \| **send** \| **session** ] **statistics**]]

**[display system internal bgp peer vpnv6 ***ipv6-address*[[ **rib** \| **send** \| **session** ] **statistics**]]

**[display system internal bgp peer l2vpn ***ipv4-address*[[ **rib** \| **send** \| **session** ] **statistics**]]

**[display system internal bgp peer ipv4 mdt ***ipv4-address*[[ **rib** \| **send** \| **session** ] **statistics**]]

**[display system internal bgp peer ipv4 multicast ***ipv4-address*****[[ **rib** \| **send** \| **session** ] **statistics**]]

**[display system internal bgp peer ipv6 multicast ***ipv6-address*****[[ **rib** \| **send** \| **session** ] **statistics**]]

分布式设备---独立运行模式]/集中式IRF设备：

**[display system internal bgp peer **[{ **ipv4** \| **vpnv4** } [ **vpn-instance** *vpn-instance-name* ] *ipv4-address* [ **rib** \| **send** \| **session** ] **statistics**  **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp peer ipv6 **[[ \| [ **vpn-instance** *vpn-instance-name* ] *ipv6-address* } [ **rib** \| **send** \| **session** ] **statistics**  **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp peer vpnv6 ***ipv6-address*[[ **rib** \| **send** \| **session** ] **statistics**  **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp peer l2vpn ***ipv4-address*[[ **rib** \| **send** \| **session** ] **statistics**  **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp peer ipv4 multicast ***ipv4-address*****[[ **rib** \| **send** \| **session** ] **statistics**  **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp peer ipv6 multicast ***ipv6-address*****[[ **rib** \| **send** \| **session** ] **statistics**  **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备---]IRF模式：

**[display system internal bgp peer **[{ **ipv4** \| **vpnv4** } [ **vpn-instance** *vpn-instance-name* ] *ipv4-address* [ **rib** \| **send** \| **session** ] **statistics**  **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp peer ipv6 **[[ \| [ **vpn-instance** *vpn-instance-name* ] *ipv6-address* } [ **rib** \| **send** \| **session** ] **statistics**  **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp peer vpnv6 ***ipv6-address*[[ **rib** \| **send** \| **session** ] **statistics**  **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp peer l2vpn ***ipv4-address*[[ **rib** \| **send** \| **session** ] **statistics**  **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp peer ipv4 multicast ***ipv4-address*****[[ **rib** \| **send** \| **session** ] **statistics**  **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp peer ipv6 multicast ***ipv6-address*****[[ **rib** \| **send** \| **session** ] **statistics**  **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】]

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：显示IPv4地址族的BGP对等体统计信息。

**[ipv6**]：显示IPv6地址族的BGP对等体统计信息。

**[vpnv4**]：显示VPNv4地址族的BGP对等体统计信息。

**[vpnv6**]：显示VPNv6地址族的BGP对等体统计信息。

**[l2vpn**]：显示L2VPN地址族的BGP对等体统计信息。

**[mdt**]：显示MDT地址族的BGP对等体统计信息。

**[multicast**]：显示组播地址族的BGP对等体统计信息。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN实例的BGP对等体统计信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网的BGP对等体统计信息。

*[ipv4-address*]：显示指定对等体的信息。*ipv4-address*为对等体的IPv4地址。

*[ipv6-address*]：显示指定对等体的信息。*ipv6-address*为对等体的IPv6地址。

**[rib**]：显示BGP路由模块相关信息。

**[send**]：显示BGP发送模块相关信息。

**[session**]：显示BGP会话模块相关信息。

**[standby**]：显示指定BGP备进程的信息。如果不指定本参数，则显示BGP主进程的信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

指定本命令时，如果不指定**rib**、**send**和**session**参数，则显示BGP协议的对等体统计信息。

开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程。执行本命令时，如果指定了**standby**参数，则显示备份到指定备进程的信息。如果没有开启BGP NSR功能，则指定**standby**参数时，不会显示任何信息。通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp protocol statistics**

------------------------------------------------------------------------

**[display system internal bgp protocol statistics**]命令用来显示BGP协议的统计信息。

【命令】

集中式设备：

**[display system internal bgp protocol **[[ **calc** \| **rib** \| **send** \| **session** ] **statistics**]]

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp protocol **[[ **calc** \| **rib** \| **send** \| **session** ] **statistics** ] **standby** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备---IRF模式：

**[display system internal bgp protocol **[[ **calc** \| **rib** \| **send** \| **session** ] **statistics** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[calc**]：显示BGP路由优选模块的统计信息。

**[rib**]：显示BGP路由模块的统计信息。

**[send**]：显示BGP发送模块的统计信息。

**[session**]：显示BGP会话模块的统计信息。

**[standby**]：显示指定BGP备进程的信息。如果不指定本参数，则显示BGP主进程的信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

执行本命令时，如果没有指定任何参数，则显示BGP协议的统计信息。

开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程。执行本命令时，如果指定了**standby**参数，则显示备份到指定备进程的信息。如果没有开启BGP NSR功能，则指定**standby**参数时，不会显示任何信息。通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp routing-table advertise-info**

------------------------------------------------------------------------

**[display system internal bgp routing-table advertise-info**]命令用来显示BGP路由的通告信息。

【命令】

集中式设备：

**[display system internal bgp routing-table ipv4 **[ **vpn-instance** *vpn-instance-name*  *network-address* { *mask* \| *mask-length* } **advertise-info**]]

**[display system internal bgp routing-table ipv6 ** **vpn-instance** *vpn-instance-name* ] *network-address* *prefix-length* **advertise-info**

**[display system internal bgp routing-table vpnv4 ***network-address *[{ *mask* \| *mask-length* } **advertise-info**]]

**[display system internal bgp routing-table vpnv6 ***network-address prefix-length* **advertise-info**]

**[display system internal bgp routing-table ipv4 multicast ***network-address *[{ *mask* \| *mask-length* } **advertise-info**]]

**[display system internal bgp routing-table ipv6 multicast ***network-address prefix-length* **advertise-info**]

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp routing-table ipv4 **[ **vpn-instance** *vpn-instance-name*  *network-address* { *mask* \| *mask-length* } **advertise-info**  **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp routing-table ipv6 ** **vpn-instance** *vpn-instance-name* ] *network-address* *prefix-length* **advertise-info**  **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]

**[display system internal bgp routing-table vpnv4 ***network-address *[{ *mask* \| *mask-length* } **advertise-info** [ **standby** **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

**[display system internal bgp routing-table vpnv6 ***network-address prefix-length* **advertise-info** [ **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp routing-table ipv4 multicast ***network-address *[{ *mask* \| *mask-length* } **advertise-info** [ **standby** **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

**[display system internal bgp routing-table ipv6 multicast ***network-address prefix-length* **advertise-info** [ **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备---IRF模式：

**[display system internal bgp routing-table ipv4 **[ **vpn-instance** *vpn-instance-name*  *network-address* { *mask* \| *mask-length* } **advertise-info**  **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp routing-table ipv6 ** **vpn-instance** *vpn-instance-name* ] *network-address* *prefix-length* **advertise-info**  **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

**[display system internal bgp routing-table vpnv4 ***network-address *[{ *mask* \| *mask-length* } **advertise-info** [ **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

**[display system internal bgp routing-table vpnv6 ***network-address prefix-length* **advertise-info** [ **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp routing-table ipv4 multicast ***network-address *[{ *mask* \| *mask-length* } **advertise-info** [ **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

**[display system internal bgp routing-table ipv6 multicast ***network-address prefix-length* **advertise-info** [ **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：显示IPv4地址族的BGP路由通告信息。

**[ipv6**]：显示IPv6地址族的BGP路由通告信息。

**[vpnv4**]：显示VPNv4地址族的BGP路由通告信息。

**[vpnv6**]：显示VPNv6地址族的BGP路由通告信息。

**[multicast**]：显示组播地址族的BGP路由通告信息。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN实例的BGP路由通告信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网的BGP路由通告信息。

*[network-address*]：目的网络的地址。

*[mask*]：目的网络的掩码，点分十进制格式。

*[mask-length*]：目的网络的掩码长度，取值范围为0～32。

*[prefix-length*]：目的网络的前缀长度，取值范围为0～128。

**[standby**]：显示指定BGP备进程的信息。如果不指定本参数，则显示BGP主进程的信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程。执行本命令时，如果指定了**standby**参数，则显示备份到指定备进程的信息。如果没有开启BGP NSR功能，则指定**standby**参数时，不会显示任何信息。通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp routing-table ipv4 multicast standby**

------------------------------------------------------------------------

**[display system internal bgp routing-table ipv4 multicast standby**]命令用来显示BGP备进程上BGP IPv4组播路由信息。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp routing-table ipv4 multicast **[[ *network-address* [ { *mask* \| *mask-length* } [ **longest-match** ] ] \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* }  **whole-match**  \| *adv-community-list-number* } \| **peer** *ip-address* { **advertised-routes** \| **received-routes** } [ *network-address* [ *mask* \| *mask-length* ] \| **statistics** ] \| **statistics** ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备---IRF模式：

**[display system internal bgp routing-table ipv4 multicast **[[ *network-address* [ { *mask* \| *mask-length* } [ **longest-match** ] ] \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* }  **whole-match**  \| *adv-community-list-number* } \| **peer** *ip-address* { **advertised-routes** \| **received-routes** } [ *network-address* [ *mask* \| *mask-length* ] \| **statistics** ] \| **statistics** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[network-address*]：目的网络的IP地址。

*[mask*]：网络掩码，点分十进制格式。

*[mask-length*]：网络掩码长度，取值范围为0～32。

**[longest-match**]：指定根据如下方法判断显示哪条BGP IPv4组播路由信息：

(1)将用户输入的网络地址和路由的掩码进行与操作；

(2)计算结果与路由的网段地址相同，且掩码小于等于用户输入子网掩码的路由中，子网掩码最长的路由将被显示出来。

**[as-path-acl*** as-path-acl-number*]：显示匹配指定AS路径过滤列表的BGP IPv4组播路由信息。*as-path-acl-number*为AS路径过滤列表号，取值范围为1～256。

**[community-list**]：显示匹配指定BGP团体列表的BGP IPv4组播路由信息。

*[basic-community-list-number*]：基本团体列表号，取值范围为1～99。

*[comm-list-name*]：团体属性列表名，为1～63个字符的字符串，区分大小写。

**[whole-match**]：精确匹配。如果指定了本参数，则只有路由的团体属性列表与指定的团体属性列表完全相同时，才显示该路由的信息；如果未指定本参数，则只要路由的团体属性列表中包含指定的团体属性列表，就显示该路由的信息。

*[adv-community-list-number*]：高级团体列表号，取值范围为100～199。

**[peer*** ip-address*]：显示向指定对等体发布或者从指定对等体收到的BGP IPv4组播路由信息。*ip-address*为对等体的地址。

**[advertised-routes**]：显示向指定的对等体发布的路由信息。

**[received-routes**]：显示从指定的对等体接收到的路由信息。

**[statistics**]：显示路由的统计信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*

表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·如果没有指定任何参数，则显示指定BGP备进程上所有BGP IPv4组播路由的简要信息。

·如果只指定了*network-address*参数，则将指定的网络地址和路由的掩码进行与操作，若计算结果与路由的网段地址相同，则显示该路由的详细信息。

·如果指定了*network-address mask*或*network-address mask-length*参数，没有指定**longest-match**参数，则显示与指定目的网络IP地址和网络掩码（或掩码长度）精确匹配的BGP IPv4组播路由的详细信息。

·开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启BGP NSR功能，则不会显示任何信息。

·通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp routing-table ipv4 unicast outlabel standby**

------------------------------------------------------------------------

**[display system internal bgp routing-table ipv4 unicast outlabel standby**]命令用来显示BGP备进程上BGP IPv4单播路由的出标签信息。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp** **routing-table ipv4** [ **unicast**   **vpn-instance** *vpn-instance-name*  **outlabel standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备---IRF模式：

**[display system internal bgp** **routing-table ipv4** [ **unicast**   **vpn-instance** *vpn-instance-name*  **outlabel standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：显示指定VPN实例内BGP IPv4单播路由的出标签信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网BGP IPv4单播路由的出标签信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启BGP NSR功能，则不会显示任何信息。

·通过**standby**参数指定的单板不能是BGP主进程所在的单板。

·执行本命令时指定**unicast**参数和不指定**unicast**参数的效果相同。

**BGP \-- BGP Probe命令 \-- display system internal bgp routing-table ipv4 unicast standby**

------------------------------------------------------------------------

**[display system internal bgp routing-table ipv4 unicast standby**]命令用来显示BGP备进程上BGP IPv4单播路由信息。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp routing-table ipv4 ** **unicast** ]** **vpn-instance** *vpn-instance-name *[[ *network-address* [ { *mask* \| *mask-length* } [ **longest-match** ] ] \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* }  **whole-match**  \| *adv-community-list-number* } \| **peer** *ip-address* { **advertised-routes** \| **received-routes** } [ *network-address* [ *mask* \| *mask-length* ] \| **statistics** ] \| **statistics** ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]

分布式设备---IRF模式：

**[display system internal bgp routing-table ipv4 ** **unicast** ]** **vpn-instance** *vpn-instance-name *[[ *network-address* [ { *mask* \| *mask-length* } [ **longest-match** ] ] \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* }  **whole-match**  \| *adv-community-list-number* } \| **peer** *ip-address* { **advertised-routes** \| **received-routes** } [ *network-address* [ *mask* \| *mask-length* ] \| **statistics** ] \| **statistics** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：显示指定VPN实例的BGP IPv4单播路由信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网BGP IPv4单播路由信息。

*[network-address*]：目的网络的IP地址。

*[mask*]：网络掩码，点分十进制格式。

*[mask-length*]：网络掩码长度，取值范围为0～32。

**[longest-match**]：指定根据如下方法判断显示哪条BGP IPv4单播路由信息：

(1)将用户输入的网络地址和路由的掩码进行与操作；

(2)计算结果与路由的网段地址相同，且掩码小于等于用户输入子网掩码的路由中，子网掩码最长的路由将被显示出来。

**[as-path-acl*** as-path-acl-number*]：显示匹配指定AS路径过滤列表的BGP IPv4单播路由信息。*as-path-acl-number*为AS路径过滤列表号，取值范围为1～256。

**[community-list**]：显示匹配指定BGP团体列表的BGP IPv4单播路由信息。

*[basic-community-list-number*]：基本团体列表号，取值范围为1～99。

*[comm-list-name*]：团体属性列表名，为1～63个字符的字符串，区分大小写。

**[whole-match**]：精确匹配。如果指定了本参数，则只有路由的团体属性列表与指定的团体属性列表完全相同时，才显示该路由的信息；如果未指定本参数，则只要路由的团体属性列表中包含指定的团体属性列表，就显示该路由的信息。

*[adv-community-list-number*]：高级团体列表号，取值范围为100～199。

**[peer*** ip-address*]：显示向指定对等体发布或者从指定对等体收到的BGP IPv4单播路由信息。*ip-address*为对等体的地址。

**[advertised-routes**]：显示向指定的对等体发布的路由信息。

**[received-routes**]：显示从指定的对等体接收到的路由信息。

**[statistics**]：显示路由的统计信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*

表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·如果没有指定任何参数，则显示指定BGP备进程上所有BGP IPv4单播路由的简要信息。

·如果只指定了*network-address*参数，则将指定的网络地址和路由的掩码进行与操作，若计算结果与路由的网段地址相同，则显示该路由的信息。

·如果指定了*network-address mask*或*network-address mask-length*参数，没有指定**longest-match**参数，则显示与指定目的网络IP地址和网络掩码（或掩码长度）精确匹配的BGP IPv4单播路由的信息。

·开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启BGP NSR功能，则不会显示任何信息。

·通过**standby**参数指定的单板不能是BGP主进程所在的单板。

·执行本命令时指定**unicast**参数和不指定**unicast**参数的效果相同。

**BGP \-- BGP Probe命令 \-- display system internal bgp routing-table ipv6 multicast standby**

------------------------------------------------------------------------

**[display system internal bgp routing-table ipv6 multicast standby**]命令用来显示BGP备进程上BGP IPv6 组播路由信息。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp routing-table ipv6******multicast **[[ *network-address prefix-length* \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* } [ **whole-match** ] \| *adv-community-list-number* } \| **peer** *ipv6-address* { **advertised-routes** \| **received-routes** } [ *network-address prefix-length* \| **statistics** ] \| **statistics** ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备---IRF模式：

**[display system internal bgp routing-table ipv6******multicast **[[ *network-address prefix-length* \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* } [ **whole-match** ] \| *adv-community-list-number* } \| **peer** *ipv6-address* { **advertised-routes** \| **received-routes** } [ *network-address prefix-length* \| **statistics** ] \| **statistics** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[network-address prefix-length*]：显示与指定的目的网络地址和前缀长度精确匹配的BGP IPv6组播路由信息。*prefix-length*为目的网络地址的前缀长度，取值范围为0～128。如果没有指定本参数，则显示所有BGP IPv6组播路由的简要信息。

**[as-path-acl ***as-path-acl-number*]：显示匹配指定AS路径过滤列表的BGP IPv6组播路由信息。*as-path-acl-number*为AS路径过滤列表号，取值范围为1～256。

**[community-list**]：显示匹配指定BGP团体列表的BGP IPv6组播路由信息。

*[basic-community-list-number*]：基本团体列表号，取值范围为1～99。

*[comm-list-name*]：团体属性列表名，为1～63个字符的字符串，区分大小写。

**[whole-match**]：精确匹配。如果指定了本参数，则只有路由的团体属性列表与指定的团体属性列表完全相同时，才显示该路由的信息；如果未指定本参数，则只要路由的团体属性列表中包含指定的团体属性列表，就显示该路由的信息。

*[adv-community-list-number*]：高级团体列表号，取值范围为100～199。

**[peer**]：显示向指定的对等体发布或者从指定的对等体收到的BGP IPv6组播路由信息。

*[ipv6-address*]：对等体的IPv6地址。

**[advertised-routes**]：显示向指定的对等体发布的路由信息。

**[received-routes**]：显示从指定的对等体接收到的路由信息。

**[statistics**]：显示路由的统计信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启BGP NSR功能，则不会显示任何信息。

·通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp routing-table ipv6 unicast outlabel standby**

------------------------------------------------------------------------

**[display system internal bgp routing-table ipv6 unicast outlabel standby**]命令用来显示BGP备进程上BGP IPv6单播路由的出标签信息。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp** **routing-table ipv6** [ **unicast**  **outlabel standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备---IRF模式：

**[display system internal bgp** **routing-table ipv6** [ **unicast**  **outlabel standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启BGP NSR功能，则不会显示任何信息。

·通过**standby**参数指定的单板不能是BGP主进程所在的单板。

·执行本命令时指定**unicast**参数和不指定**unicast**参数的效果相同。

**BGP \-- BGP Probe命令 \-- display system internal bgp routing-table ipv6 unicast standby**

------------------------------------------------------------------------

**[display system internal bgp routing-table ipv6 unicast standby**]命令用来显示BGP备进程上BGP IPv6单播路由信息。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp routing-table ipv6**** **unicast** ] \**[vpn-instance ***vpn-instance-name * [ *network-address prefix-length* \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* } [ **whole-match** ] \| *adv-community-list-number* } \| **peer** *ipv6-address* { **advertised-routes** \| **received-routes** } [ *network-address prefix-length* \| **statistics** ] \| **statistics** ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]

**[display system internal bgp routing-table ipv6 ** **unicast** ] **peer** *ip-address *[{ **advertised-routes** \| **received-routes** } [ *network-address prefix-length* \| **statistics** ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]

分布式设备---IRF模式：

**[display system internal bgp routing-table ipv6**** **unicast** ] \**[vpn-instance ***vpn-instance-name * [ *network-address prefix-length* \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* } [ **whole-match** ] \| *adv-community-list-number* } \| **peer** *ipv6-address* { **advertised-routes** \| **received-routes** } [ *network-address prefix-length* \| **statistics** ] \| **statistics** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]

**[display system internal bgp routing-table ipv6 ** **unicast** ] **peer** *ip-address *[{ **advertised-routes** \| **received-routes** } [ *network-address prefix-length* \| **statistics** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：显示指定VPN实例的BGP IPv6单播路由信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网BGP IPv6单播路由信息。

*[network-address prefix-length*]：显示与指定的目的网络地址和前缀长度精确匹配的BGP IPv6单播路由信息。*prefix-length*为目的网络地址的前缀长度，取值范围为0～128。如果没有指定本参数，则显示所有BGP IPv6单播路由的简要信息。

**[as-path-acl ***as-path-acl-number*]：显示匹配指定AS路径过滤列表的BGP IPv6单播路由信息。*as-path-acl-number*为AS路径过滤列表号，取值范围为1～256。

**[community-list**]：显示匹配指定BGP团体列表的BGP IPv6单播路由信息。

*[basic-community-list-number*]：基本团体列表号，取值范围为1～99。

*[comm-list-name*]：团体属性列表名，为1～63个字符的字符串，区分大小写。

**[whole-match**]：精确匹配。如果指定了本参数，则只有路由的团体属性列表与指定的团体属性列表完全相同时，才显示该路由的信息；如果未指定本参数，则只要路由的团体属性列表中包含指定的团体属性列表，就显示该路由的信息。

*[adv-community-list-number*]：高级团体列表号，取值范围为100～199。

**[peer**]：显示向指定的对等体发布或者从指定的对等体收到的BGP IPv6单播路由信息。

*[ip-address*]：对等体的IPv4地址。

*[ipv6-address*]：对等体的IPv6地址。

**[advertised-routes**]：显示向指定的对等体发布的路由信息。

**[received-routes**]：显示从指定的对等体接收到的路由信息。

**[statistics**]：显示路由的统计信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启BGP NSR功能，则不会显示任何信息。

·通过**standby**参数指定的单板不能是BGP主进程所在的单板。

·执行本命令时指定**unicast**参数和不指定**unicast**参数的效果相同。

**BGP \-- BGP Probe命令 \-- display system internal bgp routing-table verbose**

------------------------------------------------------------------------

**[display system internal bgp routing-table verbose**]命令用来显示BGP路由的详细信息。

【命令】

集中式设备：

**[display system internal bgp routing-table ipv4 **[ **vpn-instance** *vpn-instance-name*  *network-address* { *mask* \| *mask-length* } **verbose**]]

**[display system internal bgp routing-table ipv6 ** **vpn-instance** *vpn-instance-name* ] *network-address* *prefix-length* **verbose**

**[display system internal bgp routing-table vpnv4 ***network-address *[{ *mask* \| *mask-length* } **verbose**]]

**[display system internal bgp routing-table vpnv6 ***network-address prefix-length* **verbose**]

**[display system internal bgp routing-table ipv4 mdt ***network-address*** verbose**]

**[display system internal bgp routing-table ipv4 multicast ***network-address *[{ *mask* \| *mask-length* } **verbose**]]

**[display system internal bgp routing-table ipv6 multicast ***network-address prefix-length* **verbose**]

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp routing-table ipv4 **[ **vpn-instance** *vpn-instance-name*  *network-address* { *mask* \| *mask-length* } **verbose**  **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp routing-table ipv6 ** **vpn-instance** *vpn-instance-name* ] *network-address* *prefix-length* **verbose**  **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]

**[display system internal bgp routing-table vpnv4 ***network-address *[{ *mask* \| *mask-length* } **verbose** [ **standby** **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

**[display system internal bgp routing-table vpnv6 ***network-address prefix-length* **verbose** [ **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp routing-table ipv4 multicast ***network-address *[{ *mask* \| *mask-length* } **verbose** [ **standby** **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

**[display system internal bgp routing-table ipv6 multicast ***network-address prefix-length* **verbose** [ **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备---IRF模式：

**[display system internal bgp routing-table ipv4 **[ **vpn-instance** *vpn-instance-name*  *network-address* { *mask* \| *mask-length* } **verbose**  **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp routing-table ipv6 ** **vpn-instance** *vpn-instance-name* ] *network-address* *prefix-length* **verbose**  **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

**[display system internal bgp routing-table vpnv4 ***network-address *[{ *mask* \| *mask-length* } **verbose** [ **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

**[display system internal bgp routing-table vpnv6 ***network-address prefix-length* **verbose** [ **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal bgp routing-table ipv4 multicast ***network-address *[{ *mask* \| *mask-length* } **verbose** [ **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

**[display system internal bgp routing-table ipv6 multicast ***network-address prefix-length* **verbose** [ **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：显示IPv4地址族的BGP路由详细信息。

**[ipv6**]：显示IPv6地址族的BGP路由详细信息。

**[vpnv4**]：显示VPNv4地址族的BGP路由详细信息。

**[vpnv6**]：显示VPNv6地址族的BGP路由详细信息。

**[mdt**]：显示MDT地址族的BGP MDT详细信息。

**[multicast**]：显示组播地址族的BGP路由详细信息。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN实例的BGP路由详细信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网的BGP路由详细信息。

*[network-address*]：目的网络的地址。

*[mask*]：目的网络的掩码，点分十进制格式。

*[mask-length*]：目的网络的掩码长度，取值范围为0～32。

*[prefix-length*]：目的网络的前缀长度，取值范围为0～128。

**[standby**]：显示指定BGP备进程的信息。如果不指定本参数，则显示BGP主进程的信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程。执行本命令时，如果指定了**standby**参数，则显示备份到指定备进程的信息。如果没有开启BGP NSR功能，则指定**standby**参数时，不会显示任何信息。通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp routing-table vpnv4 outlabel standby**

------------------------------------------------------------------------

**[display system internal bgp routing-table vpnv4 outlabel standby**]命令用来显示BGP备进程上所有BGP VPNv4路由的出标签信息。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp** **routing-table vpnv4** **outlabel** **standby** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备---IRF模式：

**[display system internal bgp** **routing-table vpnv4** **outlabel standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启BGP NSR功能，则不会显示任何信息。

·通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp routing-table vpnv4 standby**

------------------------------------------------------------------------

**[display system internal bgp routing-table vpnv4 standby**]命令用来显示BGP备进程上BGP VPNv4路由信息。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp routing-table vpnv4 **[ [ **route-distinguisher** *route-distinguisher*  [ *network-address* [ { *mask* \| *mask-length* } [ **longest-match** ] ] \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* }  **whole-match**  \| *adv-community-list-number* } ] \|  **vpn-instance** *vpn-instance-name*  **peer** *ip-address* { **advertised-routes** \| **received-routes** } [ *network-address* [ *mask* \| *mask-length* ] \| **statistics** ] \| **statistics** ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备---IRF模式：

**[display system internal bgp routing-table vpnv4 **[ [ **route-distinguisher** *route-distinguisher*  [ *network-address* [ { *mask* \| *mask-length* } [ **longest-match** ] ] \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* }  **whole-match**  \| *adv-community-list-number* } ] \|  **vpn-instance** *vpn-instance-name*  **peer** *ip-address* { **advertised-routes** \| **received-routes** } [ *network-address* [ *mask* \| *mask-length* ] \| **statistics** ] \| **statistics** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[route-distinguisher** *route-distinguisher*]：显示指定路由标识符的BGP VPNv4路由信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号：16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

*[network-address*]：目的网段的IP地址。

*[mask*]：网络掩码，为点分十进制格式。

*[mask-l*]*ength*：掩码长度，取值范围为0～32。

**[longest-match**]：指定根据如下方法判断显示哪条BGP VPNv4路由信息：

(1)将用户输入的网络地址和路由的掩码进行与操作；

(2)计算结果与路由的网段地址相同，且掩码小于等于用户输入子网掩码的路由中，子网掩码最长的路由将被显示出来。

**[as-path-acl*** as-path-acl-number*]：显示匹配指定AS路径过滤列表的BGP VPNv4路由信息。*as-path-acl-number*为AS路径过滤列表号，取值范围为1～256。

**[community-list**]：显示匹配指定BGP团体列表的BGP VPNv4路由信息。

*[basic-community-list-number*]：基本团体列表号，取值范围为1～99。

*[comm-list-name*]：团体属性列表名，为1～63个字符的字符串，区分大小写。

**[whole-match**]：精确匹配。如果指定了本参数，则只有路由的团体属性列表与指定的团体属性列表完全相同时，才显示该路由的信息；如果未指定本参数，则只要路由的团体属性列表中包含指定的团体属性列表，就显示该路由的信息。

*[adv-community-list-number*]：高级团体列表号，取值范围为100～199。

**[vpn-instance ***vpn-instance-name*]：显示向指定对等体发布或者从指定对等体收到的指定VPN实例内BGP VPNv4路由信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示向指定对等体发布或者从指定对等体收到的公网内BGP VPNv4路由信息。

**[peer**]：显示向指定对等体发布或者从指定对等体收到的BGP VPNv4路由信息。

*[ip-address*]：对等体的地址。

**[advertised-routes**]：显示向指定的对等体发布的路由信息。

**[received-routes**]：显示从指定的对等体接收到的路由信息。

**[statistics**]：显示BGP VPNv4路由的统计信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·如果没有指定任何参数，则显示指定BGP备进程上所有BGP VPNv4路由的信息。

·如果指定了*network-address mask*或*network-address mask-length*参数，则显示与指定目的网段IP地址和网络掩码（或掩码长度）精确匹配的BGP VPNv4路由的信息。

·如果只指定了*network-address*参数，没有指定*mask*和*mask-length*参数，则将指定的网络地址和路由的掩码进行与操作，若计算结果与路由的网段地址相同，则显示该路由的信息。

·开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启BGP NSR功能，则不会显示任何信息。

·通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp routing-table vpnv6 outlabel standby**

------------------------------------------------------------------------

**[display system internal bgp routing-table vpnv6 outlabel standby**]命令用来显示BGP备进程上所有BGP VPNv6路由的出标签信息。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp** **routing-table vpnv6** **outlabel standby** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备---IRF模式：

**[display system internal bgp** **routing-table vpnv6** **outlabel standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启BGP NSR功能，则不会显示任何信息。

·通过**standby**参数指定的单板不能是BGP主进程所在的单板。

**BGP \-- BGP Probe命令 \-- display system internal bgp routing-table vpnv6 standby**

------------------------------------------------------------------------

**[display system internal bgp routing-table vpnv6 standby**]命令用来显示BGP备进程上BGP VPNv6路由信息。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal bgp routing-table vpnv6 **[ [ **route-distinguisher** *route-distinguisher*  [ *network-address prefix-length* \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* } [ **whole-match** ] \| *adv-community-list-number* } ] \| **peer** *ip-address* { **advertised-routes** \| **received-routes** } [ *network-address* *prefix-length* \| **statistics** ] \| **statistics** ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备---IRF模式：

**[display system internal bgp routing-table vpnv6 **[ [ **route-distinguisher** *route-distinguisher*  [ *network-address prefix-length* \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* } [ **whole-match** ] \| *adv-community-list-number* } ] \| **peer** *ip-address* { **advertised-routes** \| **received-routes** } [ *network-address* *prefix-length* \| **statistics** ] \| **statistics** ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[route-distinguisher** *route-distinguisher*]：显示指定路由标识符的BGP VPNv6路由信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号：16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

*[network-address prefix-l*]*ength*：显示与指定目的网段地址及前缀长度精确匹配的BGP VPNv6路由信息。*network-address*为目的网段的IPv6地址；*prefix-length*为目的网段地址的前缀长度，取值范围为0～128。如果没有指定本参数，则显示所有BGP VPNv6路由信息。

**[as-path-acl*** as-path-acl-number*]：显示匹配指定AS路径过滤列表的BGP VPNv6路由信息。*as-path-acl-number*为AS路径过滤列表号，取值范围为1～256。

**[community-list**]：显示匹配指定BGP团体列表的BGP VPNv6路由信息。

*[basic-community-list-number*]：基本团体列表号，取值范围为1～99。

*[comm-list-name*]：团体属性列表名，为1～63个字符的字符串，区分大小写。

**[whole-match**]：精确匹配。如果指定了本参数，则只有路由的团体属性列表与指定的团体属性列表完全相同时，才显示该路由的信息；如果未指定本参数，则只要路由的团体属性列表中包含指定的团体属性列表，就显示该路由的信息。

*[adv-community-list-number*]：高级团体列表号，取值范围为100～199。

**[peer**]：显示向指定对等体发布或者从指定对等体收到的BGP VPNv6路由信息。

*[ip-address*]：对等体的IPv4地址。

**[advertised-routes**]：显示向指定的对等体发布的路由信息。

**[received-routes**]：显示从指定的对等体接收到的路由信息。

**[statistics**]：显示BGP VPNv6路由的统计信息。

**[slot**]* slot-number*：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·开启BGP NSR功能后，BGP主进程将BGP邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启BGP NSR功能，则不会显示任何信息。

·通过**standby**参数指定的单板不能是BGP主进程所在的单板。

