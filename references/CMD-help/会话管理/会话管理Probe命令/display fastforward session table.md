<!-- CMD-INDEX
  display fastforward session table   | Probe视图          | L5
-->

**会话管理 \-- 会话管理Probe命令 \-- display fastforward session table**

------------------------------------------------------------------------

**[display fastforward session table**]命令用来显示未经过安全业务处理的会话表项。目前，设备上的安全业务包括NAT、ASPF、连接数限制、APR。

【命令】

集中式设备：

**[display fastforward session table**[ { **ipv4** \| **ipv6** } [ **source-ip** *source-ip* ]  **destination-ip** *destination-ip*   **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display fastforward session table**[ { **ipv4** \| **ipv6** } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]  **source-ip** *source-ip*   **destination-ip** *destination-ip*   **verbose** ]]

分布式设备－IRF模式：

**[display fastforward session table**[ { **ipv4** \| **ipv6** } ]**chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]  **source-ip** *source-ip*   **destination-ip** *destination-ip*   **verbose** ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：显示IPv4会话表项。

**[ipv6**]：显示IPv6会话表项。

**[slot** *slot-num*]：显示指定单板上的会话表项，*slot-number*表示单板所在槽位号。若不指定该参数，则显示所有单板上的会话表项。（分布式设备－独立运行模式）

**[slot** *slot-num*]：显示指定成员设备上的会话表项，*slot-number*表示设备在IRF中的成员编号。若不指定该参数，则显示所有成员设备上的会话表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的会话表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则显示所有成员设备/PEX上的会话表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的会话表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。若不指定该参数，则显示所有成员设备的所有单板上的会话表项。（分布式IRF设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的会话表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若不指定该参数，则显示所有单板上的会话表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的会话表项，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[source-ip** *source-ip*]：显示指定源IP地址的会话表项。其中，*source-ip*表示发起方到响应方会话的源IP地址。

**[destination-ip** *destination-ip*]：显示指定目的IP地址的会话表项。其中，*destination-ip*表示发起方到响应方会话的目的IP地址。

**[verbose**]：显示详细的会话表项。不指定该参数表示显示会话表项的概要信息。

【使用指导】

如果除**ipv4**、**ipv6**外不指定任何参数，则显示所有未经过安全业务处理的IPv4或IPv6会话表项。
