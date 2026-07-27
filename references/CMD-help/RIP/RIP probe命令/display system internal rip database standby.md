<!-- CMD-INDEX
  display system internal rip database standby | Probe视图          | L16
  display system internal rip graceful-restart event-log | Probe视图          | L58
  display system internal rip interface | Probe视图          | L94
  display system internal rip interface standby | Probe视图          | L126
  display system internal rip neighbor standby | Probe视图          | L166
  display system internal rip nib     | Probe视图          | L206
  display system internal rip nib log | Probe视图          | L232
  display system internal rip non-stop-routing event-log | Probe视图          | L252
  display system internal rip route standby | Probe视图          | L288
  display system internal rip status  | Probe视图          | L336
  reset system internal rip graceful-restart event-log | Probe视图          | L356
  reset system internal rip non-stop-routing event-log | Probe视图          | L392
-->

**RIP \-- RIP probe命令 \-- display system internal rip database standby**

------------------------------------------------------------------------

**[display system internal rip** **database standby**]命令用来显示备份的RIP数据库的激活路由。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal rip**[ *process-id* **database standby** [ *ip-address* { *mask-length* \| *mask* } ] **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal rip**[ *process-id* **database standby**[ *ip-address* { *mask-length* \| *mask* } ] **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

*[ip-address*]：目的IP地址，点分十进制格式。

*[mask-length/mask*]：IP地址掩码，点分十进制格式或以整数形式表示的长度，当用整数时，取值范围为0～32。

**[standby slot*** slot-number*]：显示备份的指定单板的RIP数据库的激活路由，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIP数据库的激活路由，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的RIP数据库的激活路由，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIP \-- RIP probe命令 \-- display system internal rip graceful-restart event-log**

------------------------------------------------------------------------

**[display system internal rip** **graceful-restart event-log**]命令用来显示RIP GR日志信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal rip** **graceful-restart event-log** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal rip graceful-restart event-log chassis ***chassis-number*** slot ***slot-number *\**[cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：显示指定单板的RIP GR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示指定成员设备的RIP GR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的RIP GR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIP \-- RIP probe命令 \-- display system internal rip interface**

------------------------------------------------------------------------

**[display system internal rip interface**]命令用来显示RIP的接口信息。

【命令】

**[display system internal rip interface **[ **vpn-instance** *vpn-instance-name*  [ *interface-type* *interface-number* \| *ip-address* { *mask* \| *mask-length* } ]]]

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

**RIP \-- RIP probe命令 \-- display system internal rip interface standby**

------------------------------------------------------------------------

**[display system internal rip interface standby**]命令用来显示备份的RIP接口信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal rip ***process-id*** interface standby ** *interface-type interface-number* ] **slot** *slot-number*  **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal rip ***process-id*** interface standby ** *interface-type interface-number* ] **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

*[interface-type interface-number*]：接口类型和编号。如果未指定本参数，将显示RIP的所有接口信息。

**[standby slot*** slot-number*]：显示备份的指定单板的RIP接口信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIP接口信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的RIP接口信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIP \-- RIP probe命令 \-- display system internal rip neighbor standby**

------------------------------------------------------------------------

**[display system internal rip neighbor standby**]命令用来显示备份的RIP邻居信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal rip ***process-id*** neighbor standby ** *interface-type interface-number* ] **slot** *slot-number*  **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal rip ***process-id*** neighbor standby ** *interface-type interface-number* ] **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

*[interface-type interface-number*]：接口类型和编号。如果未指定本参数，将显示RIP的所有邻居信息。

**[standby slot*** slot-number*]：显示备份的指定单板的RIP邻居信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIP邻居信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的RIP邻居信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIP \-- RIP probe命令 \-- display system internal rip nib**

------------------------------------------------------------------------

**[display system internal rip nib**]命令用来显示RIP路由下一跳信息。

【命令】

**[display system internal rip nib** [ *nib-id*   **verbose** ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nib-id*]：下一跳ID，取值范围1～FFFFFFFF。如果不指定，显示所有下一跳信息。

**[verbose**]：显示下一跳详细信息。

**RIP \-- RIP probe命令 \-- display system internal rip nib log**

------------------------------------------------------------------------

**[display system internal rip nib log**]命令用来显示RIP路由下一跳日志信息。

【命令】

**[display system internal rip nib log**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**RIP \-- RIP probe命令 \-- display system internal rip non-stop-routing event-log**

------------------------------------------------------------------------

**[display system internal rip** **non-stop-routing event-log**]命令用来显示RIP NSR日志信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal rip** **non-stop-routing event-log** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal rip non-stop-routing event-log chassis ***chassis-number*** slot ***slot-number *\**[cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：显示指定单板的RIP NSR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示指定成员设备的RIP NSR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的RIP NSR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIP \-- RIP probe命令 \-- display system internal rip route standby**

------------------------------------------------------------------------

**[display system internal rip route standby**]命令用来显示备份的RIP路由信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal rip ***process-id*** route standby **[[ *ip-address* { *mask-length* \| *mask* } [ **verbose** ] \| **peer** *ip-address* \| **statistics** ] **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal rip ***process-id*** route standby **[[ *ip-address* { *mask-length* \| *mask* } [ **verbose** ] \| **peer** *ip-address* \| **statistics** ] **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

*[ip-address*]：目的IP地址，点分十进制格式。

*[mask-length/mask*]：IP地址掩码，点分十进制格式或以整数形式表示的长度，当用整数时，取值范围为0～32。

**[verbose**]：显示当前RIP路由表中指定目的地址和掩码的所有路由信息。如果未指定本参数，则只显示指定目的地址和掩码的最优RIP路由。

**[peer **]*ip-address*：显示从指定邻居学到的所有路由信息。

**[statistics**]：显示路由的统计信息。路由的统计信息包括路由总数目，各个邻居的路由数目。

**[standby slot*** slot-number*]：显示备份的指定单板的RIP路由信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIP路由信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的RIP路由信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIP \-- RIP probe命令 \-- display system internal rip status**

------------------------------------------------------------------------

**[display system internal rip status**]命令用来显示RIP协议全局状态信息。

【命令】

**[display system internal rip status**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**RIP \-- RIP probe命令 \-- reset system internal rip graceful-restart event-log**

------------------------------------------------------------------------

**[reset system internal rip graceful-restart event-log**]命令用来清除RIP GR日志信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal rip graceful-restart event-log** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[reset system internal rip graceful-restart event-log** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：清除指定单板的RIP GR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：清除指定成员设备的RIP GR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的RIP GR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIP \-- RIP probe命令 \-- reset system internal rip non-stop-routing event-log**

------------------------------------------------------------------------

**[reset system internal rip non-stop-routing event-log**]命令用来清除RIP NSR日志信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal rip non-stop-routing event-log** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[reset system internal rip non-stop-routing event-log** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：清除指定单板的RIP NSR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：清除指定成员设备的RIP NSR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的RIP NSR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

