<!-- CMD-INDEX
  display system internal isis import-route | Probe视图          | L14
  display system internal isis interface | Probe视图          | L60
  display system internal isis interface standby | Probe视图          | L94
  display system internal isis lsdb standby | Probe视图          | L136
  display system internal isis nib    | Probe视图          | L186
  display system internal isis nib log | Probe视图          | L214
  display system internal isis peer standby | Probe视图          | L234
  display system internal isis prefix | Probe视图          | L276
  display system internal isis standby | Probe视图          | L328
  display system internal isis status | Probe视图          | L366
-->

**IS-IS \-- IS-IS probe命令 \-- display system internal isis import-route**

------------------------------------------------------------------------

**[display system internal isis import-route**]命令用来显示IS-IS的IPv4引入路由表。

【命令】

集中式设备：

**[display system internal isis import-route** [ **ipv4** [ **topology** *topo-name*  ]  *process-id* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal isis import-route** [ **ipv4** [ **topology** *topo-name*  ]  *process-id*   **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal isis import-route** [ **ipv4** [ **topology** *topo-name*  ]  *process-id*   **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：显示IS-IS的IPv4引入路由表。如果不指定该参数，显示IPv4引入路由表。

**[topology** *topo-name*]：显示指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程引入路由表。 如果未指定IS-IS进程号，将显示所有IS-IS进程引入路由表。

**[standby**]**slot*** slot-number*：显示备份的指定成员设备的IS-IS引入路由表信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示IS-IS引入路由表信息。（集中式IRF设备）

**[standby**]**slot*** slot-number*：显示备份的指定单板的IS-IS引入路由表信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IS-IS的引入路由表。（分布式设备－独立运行模式）

**[standby**]**chassis** *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的IS-IS引入路由表，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IS-IS的引入路由表。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IS-IS \-- IS-IS probe命令 \-- display system internal isis interface**

------------------------------------------------------------------------

**[display system internal isis interface**]命令用来显示接口的IPv4信息。

【命令】

**[display system internal isis interface **[ **ipv4**   **vpn-instance** *vpn-instance-name*  [ *interface-type* *interface-number* \| *ip-address* { *mask* \| *mask-length* } ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：显示接口的IPv4信息。如果未指定该参数，显示接口的IPv4信息。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[interface-type* *interface-number*]：接口类型和接口编号。

*[ip-address*]：接口IP地址，点分十进制，显示指定IP地址和掩码/掩码长度接口的信息。

*[mask*]：IP地址的掩码，点分十进制格式。

*[mask-length*]：掩码长度，取值范围为0～32。

**IS-IS \-- IS-IS probe命令 \-- display system internal isis interface standby**

------------------------------------------------------------------------

**[display system internal isis interface standby**]命令用来显示接口的备份信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal isis interface ** *interface-type interface-number* ]  **verbose**   *process-id*  **standby slot** *slot-number*  **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal isis interface ** *interface-type interface-number* ]  **verbose**   *process-id*  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：显示指定接口的信息。如果未指定本参数，将显示所有接口的信息。

**[verbose**]：显示接口的详细信息。如果未指定该参数，将显示接口的概要信息。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示与指定IS-IS进程相关联接口的信息。如果未指定本参数，将显示所有IS-IS进程的接口信息。

**[standby **]**slot*** slot-number*：显示备份的指定单板的IS-IS接口信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IS-IS的接口信息。（分布式设备－独立运行模式）

**[standby **]**slot*** slot-number*：显示备份的指定成员设备的IS-IS接口信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示IS-IS的接口信息。（集中式IRF设备）

**[standby **]**chassis** *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的IS-IS接口信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IS-IS的接口信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IS-IS \-- IS-IS probe命令 \-- display system internal isis lsdb standby**

------------------------------------------------------------------------

**[display system internal isis lsdb standby**]命令用来显示IS-IS的备份链路状态数据库信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal isis lsdb**[ [ [ **level-1** \| **level-2** ] \| **local** \| [ **lsp-id** *lspid* \| **lsp-name** *lspname* ] \| **verbose** ] \*  *process-id*  **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal isis lsdb**[ [ [ **level-1** \| **level-2** ] \| **local** \| [ **lsp-id** *lspid* \| **lsp-name** *lspname* ] \| **verbose** ] \*  *process-id*  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[level-1**]：显示Level-1链路状态数据库。

**[level-2**]：显示Level-2链路状态数据库。

**[local**]：显示当前路由器产生的LSP的信息。

**[lsp-id*** lspid*]：LSP标识，形式为SYSID*.*Pseudonode ID-fragment num，其中，SYSID是产生该LSP的节点或伪节点的SystemID，Pseudonode ID是伪节点ID，fragment num是该LSP的分片号。

**[lsp-name*** lspname*]：LSP名称，形式为Symbolic name.[Pseudo ID-fragment num]。

**[verbose**]：显示链路状态数据库中的LSP的详细信息。如果未指定该参数，将显示链路状态数据库中的LSP的概要信息。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的链路状态数据库信息。如果未指定本参数，将显示所有IS-IS进程的链路状态数据库信息。

**[standby **]**slot*** slot-number*：显示备份的指定单板的IS-IS链路状态数据库信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IS-IS的链路状态数据库信息。（分布式设备－独立运行模式）

**[standby **]**slot*** slot-number*：显示备份的指定成员设备的IS-IS链路状态数据库信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示IS-IS的链路状态数据库信息。（集中式IRF设备）

**[standby **]**chassis** *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的IS-IS链路状态数据库信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IS-IS的链路状态数据库信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IS-IS \-- IS-IS probe命令 \-- display system internal isis nib**

------------------------------------------------------------------------

**[display system internal isis nib**]命令用来显示IS-IS的IPv4路由下一跳信息。

【命令】

**[display system internal isis nib** [ **ipv4**   *nib-id*   **verbose** ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：显示IS-IS的IPv4下一跳信息。如果不指定该参数，显示IPv4下一跳信息。

*[nib-id*]：下一跳ID，取值范围1～FFFFFFFF。如果不指定，显示所有下一跳信息。

**[verbose**]：显示下一跳详细信息。

**IS-IS \-- IS-IS probe命令 \-- display system internal isis nib log**

------------------------------------------------------------------------

**[display system internal isis nib log**]命令用来显示IS-IS路由下一跳日志信息。

【命令】

**[display system internal isis nib log**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IS-IS \-- IS-IS probe命令 \-- display system internal isis peer standby**

------------------------------------------------------------------------

**[display system internal isis peer standby**]命令用来显示IS-IS的备份邻居信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **system internal isis** **peer** [ **statistics** \| **verbose** ]  *process-id*  **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display**[ **system internal** **isis** **peer** [ **statistics** \| **verbose** ]  *process-id*  **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[statistics**]：显示IS-IS邻居的统计信息。

**[verbose**]：显示IS-IS邻居的详细信息。如果未指定该参数，将显示IS-IS邻居的概要信息。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的邻居信息。如果未指定本参数，将显示所有IS-IS进程的邻居信息。

**[standby**]**slot*** slot-number*：显示备份的指定单板的IS-IS邻居信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IS-IS的邻居信息。（分布式设备－独立运行模式）

**[standby**]**slot*** slot-number*：显示备份的指定成员设备的IS-IS邻居信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示IS-IS的邻居信息。（集中式IRF设备）

**[standby**]**chassis** *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的IS-IS邻居信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IS-IS的邻居信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IS-IS \-- IS-IS probe命令 \-- display system internal isis prefix**

------------------------------------------------------------------------

**[display system internal isis prefix**]命令用来显示IS-IS的IPv4前缀信息。

【命令】

集中式设备：

**[display system internal isis prefix **[ **ipv4** [ **topology** *topo-name*    [ **level-1** \| **level-2** ] \|  *prefix mask-length*  ] \*  *process-id* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal isis prefix **[ **ipv4** [ **topology** *toponame*    [ **level-1** \| **level-2** ] \|  *prefix mask-length*  ] \*  *process-id*   **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal isis prefix **[ **ipv4** [ **topology** *toponame*    [ **level-1** \| **level-2** ] \|  *prefix mask-length*  ] \*  *process-id*   **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：显示IS-IS的IPv4前缀信息。如果不指定该参数，显示IPv4前缀信息。

**[topology** *topo-name*]：显示指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[level-1**]：显示IS-IS的Level-1前缀信息。如果未指定级别，将同时显示Level-1和Level-2的前缀信息。

**[level-2**]：显示IS-IS的Level-2前缀信息。如果未指定级别，将同时显示Level-1和Level-2的前缀信息。

*[prefix mask-length*]：显示指定前缀和掩码长度的前缀信息。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的前缀信息。如果未指定IS-IS进程号，将显示所有IS-IS进程的前缀信息。

**[standby**]**slot*** slot-number*：显示备份的指定成员设备的IPv4前缀信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示IPv4前缀信息。（集中式IRF设备）

**[standby**]**slot*** slot-number*：显示备份的指定单板的IPv4前缀信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IPv4前缀信息。（分布式设备－独立运行模式）

**[standby**]**chassis** *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的IS-IS IPv4前缀信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IPv4前缀信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IS-IS \-- IS-IS probe命令 \-- display system internal isis standby**

------------------------------------------------------------------------

**[display system internal isis** **standby**]命令用来显示IS-IS的进程备份信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal isis ** *process-id* ] **standby slot** *slot-number*  **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal isis ** *process-id* ] **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的进程信息。如果未指定本参数，将显示所有IS-IS进程的进程信息。

**[standby **]**slot*** slot-number*：显示备份的指定单板的IS-IS进程信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IS-IS的进程信息。（分布式设备－独立运行模式）

**[standby **]**slot*** slot-number*：显示备份的指定成员设备的IS-IS进程信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示IS-IS的进程信息。（集中式IRF设备）

**[standby **]**chassis** *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的IS-IS进程信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IS-IS的进程信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IS-IS \-- IS-IS probe命令 \-- display system internal isis status**

------------------------------------------------------------------------

**[display system internal isis status**]命令用来显示IS-IS的协议全局状态信息。

【命令】

**[display system internal isis status**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

