
**IP地址管理 \-- IP地址管理 Probe命令 \-- display system internal ip address**

------------------------------------------------------------------------

**[display system internal ip address**]命令用来显示地址详细信息

【命令】

集中式设备：

**[display system internal ip address** [ **vpn-instance** *vpn-instance-name*   **interface** *interface-type interface-number*   *ip-address*  ]]

分布式设备/集中式IRF设备：

**[display system internal ip address** [ **vpn-instance** *vpn-instance-name*   **interface** *interface-type interface-number*   *ip-address*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式IRF设备：

**[display system internal ip address** [ **vpn-instance** *vpn-instance-name*   **interface** *interface-type interface-number*   *ip-address*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip-address**]* ip-address*：显示指定IP地址。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN的IP地址。

**[interface ***interface-type interface-number*]：显示指定接口的IP地址，*interface-type interface-number*表示接口类型和接口编号。

**[slot** *slot-number*]：显示指定单板上的IP地址，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的IP地址。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的IP地址，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上的IP地址。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的IP地址，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的IP地址。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IP地址，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的IP地址。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IP地址。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上的IP地址。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU的IP地址。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）
