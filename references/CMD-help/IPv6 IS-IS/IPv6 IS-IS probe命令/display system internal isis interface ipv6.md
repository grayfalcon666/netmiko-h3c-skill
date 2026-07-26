
**IPv6 IS-IS \-- IPv6 IS-IS probe命令 \-- display system internal isis interface ipv6**

------------------------------------------------------------------------

**[display system internal isis interface ipv6**]命令用来显示接口的IPv6信息。

【命令】

**[display system internal isis interface ipv6 **[ **vpn-instance** *vpn-instance-name*  [ *interface-type* *interface-number* \| *ipv6-address* *prefix-length* ]]]

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

**IPv6 IS-IS \-- IPv6 IS-IS probe命令 \-- display system internal isis import-route ipv6**

------------------------------------------------------------------------

**[display system internal isis import-route ipv6**]命令用来显示IS-IS的IPv6引入路由表。

【命令】

集中式设备：

**[display system internal isis import-route** **ipv6** [ *process-id* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal isis import-route** **ipv6** [ *process-id*   **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal isis import-route** **ipv6** [ *process-id*   **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程引入路由表。如果未指定IS-IS进程号，将显示所有IS-IS进程引入路由表。

**[standby**]**slot*** slot-number*：显示备份的指定单板的IS-IS引入路由表信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IS-IS的引入路由表。（分布式设备－独立运行模式）

**[standby**]**slot*** slot-number*：显示备份的指定成员设备的IS-IS引入路由表信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示IS-IS引入路由表信息。（集中式IRF设备）

**[standby**]**chassis** *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的IS-IS引入路由表信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示IS-IS的引入路由表信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IPv6 IS-IS \-- IPv6 IS-IS probe命令 \-- display system internal isis nib ipv6**

------------------------------------------------------------------------

**[display system internal isis nib ipv6**]命令用来显示IS-IS的IPv6路由下一跳信息。

【命令】

**[display system internal isis nib** **ipv6** [ *nib-id*   **verbose** ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nib-id*]：下一跳ID，取值范围1～FFFFFFFF。如果未指定本参数，则显示所有下一跳信息。

**[verbose**]：显示下一跳详细信息。如果未指定本参数，则显示概要信息。

**IPv6 IS-IS \-- IPv6 IS-IS probe命令 \-- display system internal isis prefix ipv6**

------------------------------------------------------------------------

**[display system internal isis prefix ipv6**]命令用来显示IS-IS的IPv6前缀信息。

【命令】

集中式设备：

**[display system internal isis prefix ipv6**[ [ [ **level-1** \| **level-2** ] \|  *prefix mask-length*  ] \*  *process-id* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal isis prefix ipv6**[ [ [ **level-1** \| **level-2** ] \|  *prefix mask-length*  ] \*  *process-id*   **standby** **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal isis prefix ipv6**[ [ [ **level-1** \| **level-2** ] \|  *prefix mask-length*  ] \*  *process-id*   **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[level-1**]：显示IS-IS的Level-1前缀信息。如果未指定级别，将同时显示Level-1和Level-2的前缀信息。

**[level-2**]：显示IS-IS的Level-2前缀信息。如果未指定级别，将同时显示Level-1和Level-2的前缀信息。

*[prefix mask-length*]：显示指定前缀和掩码长度的前缀信息。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的前缀信息。如果未指定IS-IS进程号，将显示所有IS-IS进程的前缀信息。

**[standby**]**slot*** slot-number*：显示备份的指定单板的IS-IS前缀信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主进程的IS-IS前缀信息。（分布式设备－独立运行模式）

**[standby**]**slot*** slot-number*：显示备份的指定成员设备的IS-IS前缀信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示IS-IS前缀信息。（集中式IRF设备）

**[standby**]**chassis** *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的IS-IS 前缀信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主进程的IS-IS前缀信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

