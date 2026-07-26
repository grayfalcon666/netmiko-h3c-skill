
**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ip routing-table**

------------------------------------------------------------------------

**[display system internal ip routing-table**]命令用来显示路由表的信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ]  **verbose**  **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ]  **verbose**  **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[topology** *topo-name*]：显示指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[verbose**]：显示全部路由表的详细信息，包括激活路由和未激活路由。如果未指定本参数，将显示激活路由的概要信息。

**[standby slot*** slot-number*]：显示备份的指定单板的路由表信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的路由表信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的路由表信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ip routing-table acl**

------------------------------------------------------------------------

**[display system internal ip routing-table acl**]命令用来显示通过指定ACL过滤的路由信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ip routing-table **[[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] **acl** *acl-number*  **verbose**  **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ip routing-table **[[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] **acl** *acl-number*  **verbose**  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[topology** *topo-name*]：显示指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[acl-number*]：基本ACL的编号，取值范围为2000～2999。

**[verbose**]：显示通过指定ACL过滤的所有路由的详细信息。如果未指定本参数，将只显示通过指定ACL过滤的激活路由的概要信息。

**[standby slot*** slot-number*]：显示备份的指定单板的通过指定ACL过滤的路由信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的通过指定ACL过滤的路由信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上通过指定ACL过滤的路由信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ip routing-table ip-address**

------------------------------------------------------------------------

**[display system internal ip routing-table ***ip-address*]命令用来显示指定目的地址的路由信息。

**[display system internal ip routing-table ***ip-address1 ***to*** ip-address2*]命令用来显示指定目的地址范围内的路由信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] *ip-address* [ *mask* \| *mask-length* ]  **longer-match**   **verbose**  **standby slot** *slot-number*  **cpu** *cpu-number* ]]

**[display system internal ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] *ip-address1* **to** *ip-address2*  **verbose**  **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] *ip-address* [ *mask* \| *mask-length* ]  **longer-match**   **verbose**  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

**[display system internal ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] *ip-address1* **to** *ip-address2*  **verbose**  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[topology** *topo-name*]：显示指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ip-address*]：目的IP地址，点分十进制格式。

*[mask/mask-length*]：IP地址掩码，点分十进制格式或以整数形式表示的长度，当用整数时，取值范围为0～32。

**[longer-match**]：匹配掩码更长的路由。

*[ip-address1* **to** *ip-address2*]：IP地址范围。*ip-address1*和*ip-address2*共同决定一个地址范围，只有地址在此范围内的路由才会被显示。

**[verbose**]：显示全部路由表的详细信息，包括激活路由和未激活路由。如果未指定本参数，将显示激活路由的概要信息。

**[standby slot*** slot-number*]：显示备份的指定单板的指定目的地址的路由信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的指定目的地址的路由信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定目的地址的路由信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ip routing-table prefix-list**

------------------------------------------------------------------------

**[display system internal ip routing-table prefix-list**]命令用来显示通过指定前缀列表过滤的路由信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ip routing-table **[[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] **prefix-list** *prefix-list-name*  **verbose**  **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] **prefix-list** *prefix-list-name*  **verbose**  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[topology** *topo-name*]：显示指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[prefix-list-name*]：前缀列表名称，为1～63个字符的字符串，区分大小写。

**[verbose**]：当使用该参数时，显示通过过滤规则的所有路由的详细信息。如果未指定本参数，将只显示通过过滤规则的激活路由的概要信息。

**[standby slot*** slot-number*]：显示备份的指定单板的指定前缀列表过滤的路由信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的指定前缀列表过滤的路由信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的指定前缀列表过滤的路由信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ip routing-table protocol**

------------------------------------------------------------------------

**[display system internal ip routing-table** **protocol**]命令用来显示指定协议生成或发现的路由信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] **protocol** *protocol* [ **inactive** \| **verbose** ] **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] **protocol** *protocol* [ **inactive** \| **verbose** ] **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[topology** *topo-name*]：显示指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[protocol*]：显示指定路由协议的信息，包括**bgp**、**direct**、**isis**、**ospf**、**rip**和**static**。

**[inactive**]：显示未激活路由的信息。如果未指定本参数，则显示激活路由和未激活路由的信息。

**[verbose**]：当使用该参数时，显示路由的详细信息。如果未指定本参数，将显示路由的概要信息。

**[standby slot*** slot-number*]：显示备份的指定单板的指定路由协议的信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的路由表中的指定路由协议的信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的路由表中的指定路由协议的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ip routing-table statistics**

------------------------------------------------------------------------

**[display system internal ip routing-table statistics**]命令用来显示路由表中的综合路由统计信息。综合路由统计信息包括路由总数目、路由协议添加/删除路由数目、激活路由数目。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] **statistics** **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] **statistics** **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[topology** *topo-name*]：显示指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[standby slot*** slot-number*]：显示备份的指定单板的路由表中的综合路由统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的路由表中的综合路由统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的路由表中的综合路由统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib attribute**

------------------------------------------------------------------------

**[display system internal ipv6 rib attribute**]命令用来显示IPv6 RIB的路由属性信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 rib attribute** [ *attribute-id*  **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ipv6 rib attribute** [ *attribute-id*  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[attribute-id*]：路由属性ID值，取值范围0～FFFFFFFF。

**[standby slot*** slot-number*]：显示备份的指定单板的IPv6 RIB路由属性信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的IPv6 RIB路由属性信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的IPv6 RIB路由属性信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib event attribute**

------------------------------------------------------------------------

**[display system internal ipv6 rib event attribute **]命令用来显示IPv6 RIB的路由属性事件信息。

【命令】

**[display system internal ipv6 rib event attribute**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib event policy**

------------------------------------------------------------------------

**[display system internal ipv6 rib event policy**]命令用来显示IPv6 RIB的路由策略事件信息。

【命令】

**[display system internal ipv6 rib event policy**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib event prefix**

------------------------------------------------------------------------

**[display system internal ipv6 rib event prefix**]命令用来显示IPv6 RIB的路由前缀事件信息。

【命令】

**[display system internal ipv6 rib event prefix**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib event protocol**

------------------------------------------------------------------------

**[display system internal ipv6 rib event protocol**]命令用来显示IPv6 RIB的协议事件信息。

【命令】

**[display system internal ipv6 rib event protocol ** **vpn-instance** *vpn-instance-name* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib event statistics**

------------------------------------------------------------------------

**[display system internal ipv6 rib event statistics**]用来显示IPv6 RIB的统计事件信息。

【命令】

**[display system internal ipv6 rib event statistics** [ **vpn-instance** *vpn-instance-name* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib log**

------------------------------------------------------------------------

**[display system internal ipv6 rib log**]命令用来显示IPv6 RIB的日志信息。

【命令】

集中式设备：

**[display system internal ipv6 rib log** [ **reverse** ]]

**[display system internal ipv6 rib event log**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 rib log** [ **reverse**   **standby slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal ipv6 rib event log**** **standby slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal ipv6 rib log** [ **reverse**   **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal ipv6 rib event log** [ **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rib**]：显示IPv6 RIB的日志信息。

**[event**]：显示IPv6 RIB路由变化通知的日志信息。

**[reverse**]：按时间新旧显示日志信息。

**[standby slot*** slot-number*]：显示备份的指定单板RIB的日志信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示RIB的日志信息。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIB的日志信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示RIB的日志信息。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上RIB的日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示RIB的日志信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib memory**

------------------------------------------------------------------------

**[display system internal** **ipv6 rib memory**]命令用来显示IPv6 RIB的内存信息。

【命令】

**[display system internal ipv6 rib memory**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib nib**

------------------------------------------------------------------------

**[display system internal ipv6 rib nib**]命令用来显示IPv6 RIB的下一跳信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 rib nib ** **self-originated** ]  *nib-id*   **verbose**  **standby slot** *slot-number*  **cpu** *cpu-number*

**[display system internal ipv6 rib nib protocol ***protocol-name* [ **verbose**  **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ipv6 rib nib** [ **self-originated**   *nib-id*   **verbose**   **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

**[display system internal ipv6 rib nib protocol ***protocol-name* [ **verbose**  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[self-originated**]：路由管理自己生成的下一跳。

*[nib-id*]：路由下一跳ID值，取值范围1～FFFFFFFF。

**[verbose**]：显示详细信息。如果未指定本参数，则显示概要信息。

**[protocol ***protocol-name*]：显示指定路由协议的下一跳信息，包括**bgp4+**、**direct6**、**isisv6**、**ospfv3**、**ripng**和**static6**。

**[standby slot*** slot-number*]：显示备份的指定单板的IPv6 RIB下一跳信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的IPv6 RIB下一跳信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的IPv6 RIB下一跳信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib nib log**

------------------------------------------------------------------------

**[display system internal ipv6 rib nib log**]命令用来显示系统内部IPv6 NIB子模块运行状态的日志信息。

【命令】

集中式设备：

**[display system internal ipv6 rib nib log** [ **reverse** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 rib nib log** [ **reverse**   **standby slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal ipv6 rib nib log** [ **reverse**   **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[nib**]：显示IPv6 NIB子模块的运行状态。

**[reverse**]：按时间新旧显示日志信息。

**[standby slot*** slot-number*]：显示备份的指定单板NIB子模块的运行状态日志，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示NIB子模块的运行状态日志。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的NIB子模块的运行状态日志，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示NIB子模块的运行状态日志。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上NIB子模块的运行状态日志，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示NIB子模块的运行状态日志。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib prefix**

------------------------------------------------------------------------

**[display system internal ipv6 rib prefix**]命令用来显示IPv6路由表前缀信息。

【命令】

集中式设备：

**[display system internal ipv6 rib prefix ***ipv6-address******prefix-length* [ **vpn-instance** *vpn-instance-name* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 rib prefix ***ipv6-address******prefix-length* [ **vpn-instance** *vpn-instance-name*   **standby slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal ipv6 rib prefix ***ipv6-address******prefix-length* [ **vpn-instance** *vpn-instance-name*   **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：指定IPv6目的地址。

*[prefix-length*]：前缀长度，取值范围为0～128。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[standby slot*** slot-number*]：显示备份的指定单板IPv6路由表前缀信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IPv6路由表前缀信息。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的IPv6路由表前缀信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示IPv6路由表前缀信息。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上IPv6路由表前缀信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IPv6路由表前缀信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib summary**

------------------------------------------------------------------------

**[display system internal ipv6 rib summary**]命令用来显示IPv6 RIB的统计信息。

【命令】

集中式设备：

**[display system internal ipv6 rib summary**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 rib summary ** **standby slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal ipv6 rib summary ** **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：显示备份的指定单板的RIB统计信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示RIB统计信息。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIB统计信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示RIB统计信息。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的RIB统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示RIB统计信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 route-direct interface**

------------------------------------------------------------------------

**[display system internal ipv6 route-direct interface**]命令用来显示IPv6地址接口的信息。

【命令】

**[display system internal ipv6 route-direct interface** [ **vpn-instance** *vpn-instance-name*  [ *interface-type* *interface-number* \| *ipv6-address* *prefix-length* ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[interface-type* *interface-number*]：接口类型和接口编号。

*[ipv6-address*]：IPv6地址。

*[prefix-length*]：前缀长度，取值范围为0～128。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 route-direct log**

------------------------------------------------------------------------

**[display system internal ipv6 route-direct log**]命令用来显示IPv6直连路由日志信息。

【命令】

**[display system internal ipv6 route-direct **[{ **event** \| **notify** \| **nib** } **log** [ **reverse** ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：接口事件相关日志。

**[notify**]：接口事件通知相关日志。

**[nib**]：IPv6直连路由NIB子模块相关日志。

**[reverse**]：按时间新旧显示日志信息。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 routing-table**

------------------------------------------------------------------------

**[display system internal ipv6 routing-table**]命令用来显示IPv6路由表的信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 routing-table ** **vpn-instance** *vpn-instance-name* ]  **verbose**  **standby** **slot** *slot-number*  **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal ipv6 routing-table ** **vpn-instance** *vpn-instance-name* ]  **verbose**  **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[verbose**]：显示IPv6路由表的详细信息，包括激活路由和未激活路由。如果未指定本参数，将显示激活路由的概要信息。

**[slot*** slot-number*]：显示备份的指定单板的IPv6路由表信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示备份的指定成员设备的IPv6路由表信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的IPv6路由表信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 routing-table acl**

------------------------------------------------------------------------

**[display system internal ipv6 routing-table acl**]命令用来显示通过指定IPv6 ACL过滤的IPv6路由信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 routing-table ** **vpn-instance** *vpn-instance-name* ] **acl** *acl-number*  **verbose**  **standby slot** *slot-number*  **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal ipv6 routing-table ** **vpn-instance** *vpn-instance-name* ] **acl** *acl-number*  **verbose**  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[acl6-number*]：基本IPv6 ACL编号，取值范围为2000～2999。

**[verbose**]：显示通过指定IPv6 ACL过滤的所有路由的详细信息。如果未指定本参数，只显示通过IPv6 ACL过滤的激活路由的概要信息。

**[standby slot*** slot-number*]：显示备份的指定单板的通过指定ACL过滤的IPv6路由信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的通过指定ACL过滤的IPv6路由信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上通过指定ACL过滤的IPv6路由信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 routing-table ipv6-address**

------------------------------------------------------------------------

**[display system internal ipv6 routing-table ***ipv6-address*]命令用来显示指定目的地址的IPv6路由信息。

**[display system internal ipv6 routing-table ***ipv6-address1 ***to*** ipv6-address2*]命令用来显示指定目的地址范围内的IPv6路由信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 routing-table** [ **vpn-instance** *vpn-instance-name*  *ip-address* [ *mask* \| *mask-length* ]  **longer-match**   **verbose**  **standby slot** *slot-number*  **cpu** *cpu-number* ]]

**[display system internal ipv6 routing-table ** **vpn-instance** *vpn-instance-name* ] *ipv6-address1* **to** *ipv6-address2*  **verbose**  **standby slot** *slot-number*  **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal ipv6 routing-table** [ **vpn-instance** *vpn-instance-name*  *ip-address* [ *mask* \| *mask-length* ]  **longer-match**   **verbose**  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

**[display system internal ipv6 routing-table ** **vpn-instance** *vpn-instance-name* ] *ipv6-address1* **to** *ipv6-address2*  **verbose**  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ipv6-address*]：IPv6目的地址。

*[prefix-length*]：前缀长度，取值范围为0～128。

**[longer-match**]：匹配并显示前缀最长的路由条目。

*[ipv6-address1* **to** *ipv6-address2*]：IPv6地址范围。*ipv6-address1*和*ipv6-address2*共同决定一个地址范围，只有地址在此范围内的路由才会被显示。

**[verbose**]：显示激活和未激活路由的详细信息。如果未指定本参数，将显示激活路由的概要信息。

**[standby slot*** slot-number*]：显示备份的指定单板的指定目的地址的IPv6路由信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的指定目的地址的IPv6路由信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定目的地址的IPv6路由信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 routing-table prefix-list**

------------------------------------------------------------------------

**[display system internal ipv6 routing-table prefix-list**]命令用来显示通过指定前缀列表过滤的IPv6路由信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 routing-table ** **vpn-instance** *vpn-instance-name* ] **prefix-list** *prefix-list-name*  **verbose**  **standby slot** *slot-number*  **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal ipv6 routing-table** [ **vpn-instance** *vpn-instance-name*  **prefix-list** *prefix-list-name*  **verbose**  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[prefix-list-name*]：IPv6前缀列表的名称，为1～63个字符的字符串，区分大小写。

**[verbose**]：显示所有路由的详细信息。如果未指定本参数，只显示激活路由的概要信息。

**[standby slot*** slot-number*]：显示备份的指定单板的指定前缀列表过滤的IPv6路由信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的指定前缀列表过滤的IPv6路由信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的指定前缀列表过滤的IPv6路由信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 routing-table protocol**

------------------------------------------------------------------------

**[display system internal ipv6 routing-table protocol**]命令用来显示指定协议生成或发现的IPv6路由信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 routing-table** [ **vpn-instance** *vpn-instance-name*  **protocol** *protocol* [ **inactive** \| **verbose** ] **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ipv6 routing-table** [ **vpn-instance** *vpn-instance-name*  **protocol** *protocol* [ **inactive** \| **verbose** ] **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[protocol*]：显示指定路由协议的信息，包括**bgp4+**、**direct**、**isisv6**、**ospfv3**、**ripng**和**static**。

**[inactive**]：如果配置了该参数，此命令只显示未激活路由信息。如果未指定本参数，将显示所有激活和未激活路由信息。

**[verbose**]：显示激活和未激活路由的详细信息。如果未指定本参数，将显示路由的概要信息。

**[standby slot*** slot-number*]：显示备份的指定单板的指定IPv6路由协议的信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的指定IPv6路由协议的信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的指定IPv6路由协议的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 routing-table statistics**

------------------------------------------------------------------------

**[display system internal ipv6 routing-table statistics**]命令用来显示IPv6路由表中的综合路由统计信息。综合路由统计信息包括路由总数、增加的路由数、删除的路由数等。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 routing-table** [ **vpn-instance** *vpn-instance-name*  **statistics** **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ipv6 routing-table** [ **vpn-instance** *vpn-instance-name*  **statistics** **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[standby slot*** slot-number*]：显示备份的指定单板的IPv6路由表中的综合路由统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的IPv6路由表中的综合路由统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的IPv6路由表中的综合路由统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib attribute**

------------------------------------------------------------------------

**[display system internal rib attribute**]命令用来显示RIB的路由属性信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal rib attribute** [ *attribute-id*  **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal rib attribute ** *attribute-id* ] **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[attribute-id*]：路由属性ID值，取值范围0～FFFFFFFF。

**[standby slot*** slot-number*]：显示备份的指定单板的RIB路由属性信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIB路由属性信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的RIB路由属性信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib event attribute**

------------------------------------------------------------------------

**[display system internal rib event attribute**]命令用来显示IPv4 RIB的路由属性事件信息。

【命令】

**[display system internal rib event attribute**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib event policy**

------------------------------------------------------------------------

**[display system internal rib event policy**]命令用来显示IPv4 RIB的路由策略事件信息。

【命令】

**[display system internal rib event policy**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib event prefix**

------------------------------------------------------------------------

**[display system internal rib notificaion prefix**]命令用来显示IPv4 RIB的路由前缀事件信息。

【命令】

**[display system internal rib event prefix**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib event protocol**

------------------------------------------------------------------------

**[display system internal rib event protocol**]命令用来显示IPv4 RIB的协议事件信息。

【命令】

**[display system internal rib event protocol ** **vpn-instance** *vpn-instance-name* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib event statistics**

------------------------------------------------------------------------

**[display system internal rib event statistics**]用来显示IPv4 RIB的统计事件信息。

【命令】

**[display system internal rib event statistics** [ **vpn-instance** *vpn-instance-name* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib ftn**

------------------------------------------------------------------------

**[display system internal rib ftn**]命令用来显示FTN表项和统计计数信息。

【命令】

**[display system internal rib ftn** [ *index*   **statistics** ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[index*]：显示指定FTN索引的FTN信息。*index*为FTN索引值，为十六进制数，最高位统一设置为1。如果未指定本参数，将显示所有FTN索引的FTN信息。

**[statistics**]：显示FTN统计计数信息。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib ftn summary**

------------------------------------------------------------------------

**[display system internal rib ftn summary**]命令用来显示FTN的运行信息。

【命令】

**[display system internal rib ftn summary**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib log**

------------------------------------------------------------------------

**[display system internal rib log**]命令用来显示RIB的日志信息。

【命令】

集中式设备：

**[display system internal rib log** [ **reverse** ]]

**[display system internal rib event log**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal rib log** [ **reverse**   **standby slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal rib event log**** **standby slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal rib log** [ **reverse**   **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[display system internal rib event log** [ **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rib**]：显示RIB的日志信息。

**[event**]：显示RIB路由变化通知的日志信息。

**[reverse**]：按时间新旧显示日志信息。

**[standby slot*** slot-number*]：显示备份的指定单板RIB的日志信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示RIB的日志信息。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIB的日志信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示RIB的日志信息。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上RIB的日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示RIB的日志信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib memory**

------------------------------------------------------------------------

**[display system internal rib memory**]命令用来显示RIB的内存信息。

【命令】

**[display system internal rib memory**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib nib**

------------------------------------------------------------------------

**[display system internal rib nib**]命令用来显示RIB的下一跳信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal rib nib ** **self-originated** ]  *nib-id*   **verbose**  **standby slot** *slot-number*  **cpu** *cpu-number*

**[display system internal rib nib protocol ***protocol-name* [ **verbose**  **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal rib nib ** **self-originated** ]  *nib-id*   **verbose**  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*

**[display system internal rib nib protocol ***protocol-name* [ **verbose**  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[self-originated**]：路由管理自己生成的下一跳信息。

*[nib-id*]：路由下一跳信息的ID值，取值范围1～FFFFFFFF。

**[verbose**]：显示详细信息。如果未指定本参数，则显示概要信息。

**[protocol ***protocol-name*]：显示指定路由协议生成的下一跳信息，包括**bgp**、**direct**、**isis**、**ospf**、**rip**和**static**。

**[standby slot*** slot-number*]：显示备份的指定单板的RIB下一跳信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIB下一跳信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的RIB下一跳信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib nib log**

------------------------------------------------------------------------

**[display system internal rib nib log**]命令用来显示系统内部NIB子模块运行状态的日志记录。

【命令】

集中式设备：

**[display system internal rib nib log** [ **reverse** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal rib nib log** [ **reverse**   **standby slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal rib nib log** [ **reverse**   **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[nib**]：显示NIB子模块的运行状态。

**[reverse**]：按时间新旧显示日志信息。

**[standby slot*** slot-number*]：显示备份的指定单板NIB子模块的运行状态日志，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示NIB子模块的运行状态日志。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的NIB子模块的运行状态日志，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示NIB子模块的运行状态日志。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上NIB子模块的运行状态日志，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示NIB子模块的运行状态日志。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib prefix**

------------------------------------------------------------------------

**[display system internal rib prefix**]命令用来显示IPv4路由表前缀信息。

【命令】

集中式设备：

**[display system internal rib prefix ***ip-address mask-length* [ **vpn-instance** *vpn-instance-name* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal rib prefix ***ip-address mask-length* [ **vpn-instance** *vpn-instance-name*   **standby slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal rib prefix ***ip-address mask-length* [ **vpn-instance** *vpn-instance-name*   **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：指定IPv4目的地址。

*[mask-length*]：IP地址掩码，取值范围为0～32。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[standby slot*** slot-number*]：显示备份的指定单板IPv4路由表前缀信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IPv4路由表前缀信息。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的IPv4路由表前缀信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示IPv4路由表前缀信息。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上IPv4路由表前缀信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IPv4路由表前缀信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib summary**

------------------------------------------------------------------------

**[display system internal rib summary**]命令用来显示IPv4 RIB的统计信息。

【命令】

集中式设备：

**[display system internal rib summary**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal rib summary** [ **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal rib summary** [ **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：显示备份的指定单板的RIB统计信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示RIB统计信息。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIB统计信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示RIB统计信息。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的RIB统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示RIB统计信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal route-direct interface**

------------------------------------------------------------------------

**[display system internal route-direct interface**]命令用来显示IPv4地址接口的信息。

【命令】

**[display system internal route-direct interface** [ **vpn-instance** *vpn-instance-name*  [ *interface-type* *interface-number* \| *ip-address* { *mask* \| *mask-length* } ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[interface-type* *interface-number*]：接口类型和接口编号。

*[ip-address*]：接口IP地址，点分十进制，显示指定IP地址和掩码/掩码长度接口的信息。

*[mask*]：IP地址的掩码，点分十进制格式。

*[mask-length*]：掩码长度，取值范围为0～32。

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal route-direct log**

------------------------------------------------------------------------

**[display system internal route-direct log**]命令用来显示直连路由日志信息。

【命令】

**[display system internal route-direct **[{ **event** \| **notify** \| **nib** } **log** [ **reverse** ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：接口事件相关日志。

**[notify**]：接口事件通知相关日志。

**[nib**]：直连路由NIB子模块相关日志。

**[reverse**]：按时间新旧显示日志信息。

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal ip routing-table statistics protocol**

------------------------------------------------------------------------

**[reset system internal ip routing-table statistics protocol**]命令用来清除路由表中的路由统计信息。

【命令】

**[reset ip routing-table statistics protocol **[ **vpn-instance** *vpn-instance-name*  { *protocol* \| **all** } **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

**[reset ip routing-table statistics protocol **[ **vpn-instance** *vpn-instance-name*  { *protocol* \| **all** } **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：清除指定VPN的路由统计信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则清除公网的路由统计信息。

*[protocol*]：清除IPv4路由表中指定路由协议的统计信息。目前可选择**bgp**、**direct**、**isis**、**ospf**、**rip**和**static**。

**[all**]：清除IPv4路由表中所有路由协议的统计信息。

**[standby slot*** slot-number*]：清除备份的指定单板的路由统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：清除备份的指定成员设备的路由统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：清除备份的指定成员设备的路由统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal ipv6 rib log**

------------------------------------------------------------------------

**[reset system internal ipv6 rib log**]命令用来清除IPv6 RIB相关的日志内容。

【命令】

集中式设备：

**[reset system internal ipv6 rib** [ **event**  **log**]]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal ipv6 rib** [ **event**  **log**  **standby slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[reset system internal ipv6 rib** [ **event**  **log**  **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：IPv6 RIB路由变化相关的日志。

**[standby slot*** slot-number*]：清除备份的指定单板RIB相关的日志内容，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除RIB相关的日志内容。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：清除备份的指定成员设备的RIB相关的日志内容，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将清除RIB相关的日志内容。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：清除备份的指定成员设备上RIB相关的日志内容，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除RIB相关的日志内容。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：清除指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal ipv6 rib nib log**

------------------------------------------------------------------------

**[reset system internal ipv6 rib nib log**]命令用来清除IPv6 NIB子模块日志。

【命令】

集中式设备：

**[reset system internal ipv6 rib nib log**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal ipv6 rib nib log**** **standby slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[reset system internal ipv6 rib nib log ** **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：清除备份的指定单板NIB子模块日志，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除NIB子模块日志。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：清除备份的指定成员设备的NIB子模块日志，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将清除NIB子模块日志。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：清除备份的指定成员设备上NIB子模块日志，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除NIB子模块日志。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：清除指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal ipv6 rib summary**

------------------------------------------------------------------------

**[reset system internal ipv6 rib summary**]命令用来清除IPv6 RIB的统计摘要信息。

【命令】

集中式设备：

**[reset system internal ipv6 rib summary**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal ipv6 rib summary**** **standby slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[reset system internal ipv6 rib summary** [ **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：清除备份的指定单板RIB的统计摘要信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除RIB的统计摘要信息。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：清除备份的指定成员设备RIB的统计摘要信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将清除RIB的统计摘要信息。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：清除备份的指定成员设备上RIB的统计摘要信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除RIB的统计摘要信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：清除指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal ipv6 route-direct log**

------------------------------------------------------------------------

**[reset system internal ipv6 route-direct log**]命令用来清除直连路由日志。

【命令】

**[reset system internal ipv6 route-direct **[{ **event** \| **notify** \| **nib** } **log**]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：接口事件相关日志。

**[notify**]：接口事件通知相关日志。

**[nib**]：ipv6直连路由NIB子模块相关日志。

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal ipv6 routing-table statistics protocol**

------------------------------------------------------------------------

**[reset system internal ipv6 routing-table statistics protocol**]命令用来清除IPv6路由表中的综合路由统计信息。

【命令】

**[reset system internal ipv6 routing-table statistics protocol** [ **vpn-instance** *vpn-instance-name*  { *protocol* \| **all** } **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

**[reset system internal ipv6 routing-table statistics protocol** [ **vpn-instance** *vpn-instance-name*  { *protocol* \| **all** } **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：清除指定VPN的路由统计信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则清除公网的路由统计信息。

*[protocol*]：清除IPv6路由表中指定路由协议的统计信息。目前可选择**bgp4+**、**direct**、**isisv6**、**ospfv3**、**ripng**和**static**。

**[all**]：清除IPv6路由表中所有路由协议的统计信息。

**[standby slot*** slot-number*]：清除备份的指定单板的路由统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：清除备份的指定成员设备的路由统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：清除备份的指定成员设备的路由统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal rib log**

------------------------------------------------------------------------

**[reset system internal rib log**]命令用来清除RIB相关的日志内容。

【命令】

集中式设备：

**[reset system internal rib** [ **event**  **log**]]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal rib** [ **event**  **log**  **standby slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[reset system internal rib** [ **event**  **log**  **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：RIB路由变化相关的日志。

**[standby slot*** slot-number*]：清除备份的指定单板RIB相关的日志内容，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除RIB相关的日志内容。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：清除备份的指定成员设备的RIB相关的日志内容，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将清除RIB相关的日志内容。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：清除备份的指定成员设备上RIB相关的日志内容，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除RIB相关的日志内容。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：清除指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal rib nib log**

------------------------------------------------------------------------

**[reset system internal rib nib log**]命令用来清除NIB子模块日志。

【命令】

集中式设备：

**[reset system internal rib nib log**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal rib nib log ** **standby slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[reset system internal rib** **nib log** [ **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：清除备份的指定单板NIB子模块日志，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除NIB子模块日志。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：清除备份的指定成员设备的NIB子模块日志，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将清除NIB子模块日志。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：清除备份的指定成员设备上NIB子模块日志，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除NIB子模块日志。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：清除指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal rib summary**

------------------------------------------------------------------------

**[reset system internal rib summary**]命令用来清除IPv4 RIB的统计摘要信息。

【命令】

集中式设备：

**[reset system internal rib summary**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal rib summary ** **standby slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[reset system internal rib summary** [ **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：清除备份的指定单板RIB的统计摘要信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除RIB的统计摘要信息。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：清除备份的指定成员设备RIB的统计摘要信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将清除RIB的统计摘要信息。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：清除备份的指定成员设备上RIB的统计摘要信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除RIB的统计摘要信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：清除指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal route-direct log**

------------------------------------------------------------------------

**[reset system internal route-direct log**]命令用来清除直连路由日志。

【命令】

**[reset system internal route-direct**[ { **event** \| **notify** \| **nib** } **log**]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：接口事件相关日志。

**[notify**]：接口事件通知相关日志。

**[nib**]：直连路由NIB子模块相关日志。

