<!-- CMD-INDEX
  display system internal ripng database standby | Probe视图          | L16
  display system internal ripng graceful-restart event-log | Probe视图          | L56
  display system internal ripng interface | Probe视图          | L92
  display system internal ripng interface standby | Probe视图          | L122
  display system internal ripng neighbor standby | Probe视图          | L162
  display system internal ripng nib   | Probe视图          | L202
  display system internal ripng nib log | Probe视图          | L228
  display system internal ripng non-stop-routing event-log | Probe视图          | L248
  display system internal ripng route standby | Probe视图          | L284
  display system internal ripng status | Probe视图          | L322
  reset system internal ripng graceful-restart event-log | Probe视图          | L342
  reset system internal ripng non-stop-routing event-log | Probe视图          | L378
-->

**RIPng \-- RIPng probe命令 \-- display system internal ripng database standby**

------------------------------------------------------------------------

**[display system internal ripng** **database standby**]命令用来显示备份的RIPng数据库的激活路由。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ripng** *process-id* **database standby**[ *ipv6-address* *prefix-length*  **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ripng** *process-id* **database standby**[ *ipv6-address* *prefix-length*  **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

*[ipv6-address*]*****prefix-length*：显示指定IPv6地址的激活路由信息。*ipv6-address*表示IPv6地址；*prefix-length*表示IPv6地址前缀长度，取值范围为0～128。

**[standby slot*** slot-number*]：显示备份的指定单板的RIPng数据库的激活路由，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIPng数据库的激活路由，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的RIPng数据库的激活路由，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu**] *cpu-number*：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIPng \-- RIPng probe命令 \-- display system internal ripng graceful-restart event-log**

------------------------------------------------------------------------

**[display system internal ripng** **graceful-restart event-log**]命令用来显示RIPng GR日志信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ripng** **graceful-restart event-log** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ripng graceful-restart event-log chassis ***chassis-number*** slot ***slot-number *\**[cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：显示指定单板的RIPng GR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示指定成员设备的RIPng GR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的RIPng GR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu**] *cpu-number*：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIPng \-- RIPng probe命令 \-- display system internal ripng interface**

------------------------------------------------------------------------

**[display system internal ripng interface**]命令用来显示RIPng的接口信息。

【命令】

**[display system internal ripng interface **[ **vpn-instance** *vpn-instance-name*  [ *interface-type* *interface-number* \| *ipv6-address* *prefix-length* ]]]

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

**RIPng \-- RIPng probe命令 \-- display system internal ripng interface standby**

------------------------------------------------------------------------

**[display system internal ripng interface standby**]命令用来显示备份的RIPng接口信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ripng ***process-id ***interface standby ** *interface-type interface-number* ] **slot** *slot-number*  **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal ripng ***process-id*** interface standby ** *interface-type interface-number* ] **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

*[interface-type interface-number*]：接口类型和编号。如果未指定本参数，将显示RIPng指定进程的所有接口信息。

**[standby slot*** slot-number*]：显示备份的指定单板的RIPng接口信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIPng接口信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的RIPng接口信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu**] *cpu-number*：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIPng \-- RIPng probe命令 \-- display system internal ripng neighbor standby**

------------------------------------------------------------------------

**[display system internal ripng neighbor standby**]命令用来显示备份的RIPng邻居信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ripng ***process-id*** neighbor standby ** *interface-type interface-number* ] **slot** *slot-number*  **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal ripng ***process-id*** neighbor standby ** *interface-type interface-number* ] **chassis** *chassis-number* ** slot** *slot-number*  **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

*[interface-type interface-number*]：接口类型和编号。如果未指定本参数，将显示RIPng的所有接口信息。

**[standby slot*** slot-number*]：显示备份的指定单板的RIPng邻居信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIPng邻居信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的RIPng邻居信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu**] *cpu-number*：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIPng \-- RIPng probe命令 \-- display system internal ripng nib**

------------------------------------------------------------------------

**[display  system internal ripng nib**]命令用来RIPng路由下一跳信息。

【命令】

**[display system internal ripng nib** [ *nib-id*   **verbose** ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nib-id*]：下一跳ID，取值范围1～FFFFFFFF。如果不指定，显示所有下一跳信息。

**[verbose**]：显示下一跳详细信息。

**RIPng \-- RIPng probe命令 \-- display system internal ripng nib log**

------------------------------------------------------------------------

**[display  system internal ripng nib log**]命令用来RIPng路由下一跳日志信息。

【命令】

**[display system internal ripng nib** **log**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**RIPng \-- RIPng probe命令 \-- display system internal ripng non-stop-routing event-log**

------------------------------------------------------------------------

**[display system internal ripng** **non-stop-routing event-log**]命令用来显示RIPng NSR日志信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ripng** **non-stop-routing event-log** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ripng non-stop-routing event-log chassis ***chassis-number*** slot ***slot-number *\**[cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：显示指定单板的RIPng NSR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示指定成员设备的RIPng NSR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的RIPng NSR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu**] *cpu-number*：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIPng \-- RIPng probe命令 \-- display system internal ripng route standby**

------------------------------------------------------------------------

**[display system internal ripng route standby**]命令用来显示备份的RIPng路由信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ripng ***process-id*** route standby **[ *ipv6-address prefix-length* [ **verbose**  \| **peer** *ipv6-address* \| **statistics** ]  **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ripng ***process-id*** route standby **[ *ipv6-address prefix-length* [ **verbose**  \| **peer** *ipv6-address* \| **statistics** ]  **chassis** *chassis-number*   **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535

**[standby slot*** slot-number*]：显示备份的指定单板的RIPng路由信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：显示备份的指定成员设备的RIPng路由信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的RIPng路由信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu**] *cpu-number*：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIPng \-- RIPng probe命令 \-- display system internal ripng status**

------------------------------------------------------------------------

**[display system internal ripng status**]命令用来显示RIPng协议全局状态信息。

【命令】

**[display system internal ripng status**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**RIPng \-- RIPng probe命令 \-- reset system internal ripng graceful-restart event-log**

------------------------------------------------------------------------

**[reset system internal ripng graceful-restart event-log**]命令用来清除RIPng GR日志信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal ripng graceful-restart event-log** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[reset system internal ripng graceful-restart event-log** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：清除指定单板的RIPng GR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：清除指定成员设备的RIPng GR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的RIPng GR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu**] *cpu-number*：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**RIPng \-- RIPng probe命令 \-- reset system internal ripng non-stop-routing event-log**

------------------------------------------------------------------------

**[reset system internal ripng non-stop-routing event-log**]命令用来清除RIPng NSR日志信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal ripng non-stop-routing event-log slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[reset system internal ripng non-stop-routing event-log chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby slot*** slot-number*]：清除指定单板的RIPng备进程的NSR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[standby slot*** slot-number*]：清除指定成员设备的RIPng备进程的NSR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的RIPng备进程的NSR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu**] *cpu-number*：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

