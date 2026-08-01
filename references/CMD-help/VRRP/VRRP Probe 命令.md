<!-- CMD-INDEX
  display system internal vrrp kernel | Probe视图          | L6
  display system internal vrrp ipv6 kernel | Probe视图          | L58
-->

**VRRP \-- VRRP Probe 命令 \-- display system internal vrrp kernel**

------------------------------------------------------------------------

**[display system internal vrrp kernel**]命令用来显示IPv4 VRRP内核信息。

【命令】

集中式设备：

**[display system internal vrrp kernel **[{ **virtual-ip** \| **virtual-router** } [ **interface** *interface-type interface number* [ **vrid** *virtual-router-id* ] ]]]

分布式设备-独立运行模式/集中式IRF设备：

**[display system internal vrrp kernel **[{ **virtual-ip** \| **virtual-router** } [ **interface** *interface-type interface number* [ **vrid** *virtual-router-id* ] ] **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备-IRF模式：

**[display system internal vrrp kernel **[{ **virtual-ip** \| **virtual-router** } [ **interface** *interface-type interface number* [ **vrid** *virtual-router-id* ] ] **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[virtual-ip**]：显示IPv4 VRRP内核的虚拟地址信息。

**[virtual-router**]：显示IPv4 VRRP内核的虚拟路由器信息。

**[interface** *interface-type interface-number*]：显示指定接口的IPv4 VRRP备份组内核信息。interface-type interface-number表示接口类型和接口编号。

**[vrid** *virtual-router-id*]：显示指定VRRP备份组号的备份组内核信息。

**[slot** *slot-number*]：显示指定单板的IPv4 VRRP备份组内核信息。slot-number表示单板所在的槽位号。（分布式设备-独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的IPv4 VRRP备份组内核信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的IPv4 VRRP备份组内核信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定成员设备上的指定单板的VRRP备份组内核信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备-IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定单板的VRRP备份组内核信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备-IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的VRRP备份组内核信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**VRRP \-- VRRP Probe 命令 \-- display system internal vrrp ipv6 kernel**

------------------------------------------------------------------------

**[display system internal vrrp ipv6 kernel**]命令用来显示IPv6 VRRP内核信息。

【命令】

集中式设备：

**[display system internal vrrp ipv6 kernel **[{ **virtual-ip** \| **virtual-router** } [ **interface** *interface-type interface number* [ **vrid** *virtual-router-id* ] ]]]

分布式设备-独立运行模式/集中式IRF设备：

**[display system internal vrrp ipv6 kernel **[{ **virtual-ip** \| **virtual-router** } [ **interface** *interface-type interface number* [ **vrid** *virtual-router-id* ] ] **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备-IRF模式：

**[display system internal vrrp ipv6 kernel **[{ **virtual-ip** \| **virtual-router** } [ **interface** *interface-type interface number* [ **vrid** *virtual-router-id* ] ] **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[virtual-ip**]：显示IPv6 VRRP内核的虚拟地址信息。

**[virtual-router**]：显示IPv6 VRRP内核的虚拟路由器信息。

**[interface** *interface-type interface-number*]：显示指定接口的IPv6 VRRP备份组内核信息。*interface-type interface-number*表示接口类型和接口编号。

**[vrid** *virtual-router-id*]：显示指定IPv6 VRRP备份组号的备份组内核信息。

**[slot** *slot-number*]：显示指定单板的IPv6 VRRP备份组内核信息。*slot-number*表示单板所在的槽位号。（分布式设备-独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的IPv6 VRRP备份组内核信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的IPv6 VRRP备份组内核信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定成员设备上的指定单板的IPv6 VRRP备份组内核信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备-IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定单板的IPv6 VRRP备份组内核信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备-IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的IPv6 VRRP备份组内核信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）
