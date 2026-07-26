
**MPLS L3VPN \-- MPLS L3VPN Probe命令 \-- debugging system internal ip vpn-instance**

------------------------------------------------------------------------

**[debugging system internal ip vpn-instance**]命令用来打开VPN实例调试信息开关。

**[undo debugging system internal ip vpn-instance**]命令用来关闭VPN实例调试信息开关。

【命令】

集中式设备：

**[debugging system internal ip vpn-instance**]

**[undo debugging system internal ip vpn-instance**]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging system internal ip vpn-instance slot**]* slot-number* **cpu** *cpu-number*

**[undo debugging system internal ip vpn-instance slot**]* slot-number* **cpu** *cpu-number*

分布式设备－IRF模式：

**[debugging system internal ip vpn-instance chassis**]* chassis-number ***slot***slot-number* **cpu** *cpu-number*

**[undo** **debugging system internal ip vpn-instance chassis**]* chassis-number ***slot*** slot-number* **cpu** *cpu-number*

【缺省情况】

VPN实例的调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：表示指定单板上的VPN实例调试信息开关。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：表示指定成员设备上的VPN实例调试信息开关。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：表示指定成员设备/PEX上的VPN实例调试信息开关。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：表示指定成员设备上指定单板的VPN实例调试信息开关。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：表示指定单板的VPN实例调试信息开关。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：表示指定CPU上的VPN实例调试信息开关。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS L3VPN \-- MPLS L3VPN Probe命令 \-- display system internal ip vpn-binding**

------------------------------------------------------------------------

**[display system internal ip vpn-binding**]命令用来显示内核的VPN实例绑定信息。

【命令】

集中式设备：

**[display system internal ip vpn-binding**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ip vpn-binding slot**]*slot-number* **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal ip vpn-binding chassis**]* chassis-number ***slot***slot-number* **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：显示指定单板上的内核VPN实例绑定信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备上的内核VPN实例绑定信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX上的内核VPN实例绑定信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：显示指定成员设备上指定单板的内核VPN实例绑定信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：显示指定单板的内核VPN实例绑定信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的内核VPN实例绑定信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS L3VPN \-- MPLS L3VPN Probe命令 \-- display system internal ip vpn-instance**

------------------------------------------------------------------------

**[display system internal ip vpn-instance**]命令用来显示内核的VPN实例信息。

【命令】

集中式设备：

**[display system internal ip vpn-instance** [ **instance-name** ]*vpn-instance-name* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ip vpn-instance** [ **instance-name** ]*vpn-instance-name*  **slot** ]*slot-number* **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal ip vpn-instance** [ **instance-name** ]*vpn-instance-name * **chassis** ]*chassis-number ***slot*** slot-number * **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[instance-name **]*vpn-instance-name*：显示指定VPN实例的内核信息。*vpn-instance-name*表示VPN实例的名称，为1～31个字符的字符串，区分大小写。

**[slot**]* slot-number*：显示指定单板上的内核VPN实例信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备上的内核VPN实例信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX上的内核VPN实例信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：显示指定成员设备上指定单板的内核VPN实例信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：显示指定单板的内核VPN实例信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的内核VPN实例信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS L3VPN \-- MPLS L3VPN Probe命令 \-- display system internal ip vpn-instance inactive**

------------------------------------------------------------------------

**[display system internal ip vpn-instance inactive**]命令用来显示正在删除中的VPN实例的信息。

【命令】

**[display system internal ip vpn-instance inactive**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**MPLS L3VPN \-- MPLS L3VPN Probe命令 \-- display system internal ip vpn-instance statistics**

------------------------------------------------------------------------

**[display system internal ip vpn-instance statistics**]命令用来显示内核VPN实例的统计信息。

【命令】

集中式设备：

**[display system internal ip vpn-instance statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ip vpn-instance statistics slot**]*slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal ip vpn-instance statistics chassis**]*chassis-number ***slot***slot-number* **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：显示指定单板上的内核VPN实例统计信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备上的内核VPN实例统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX上的内核VPN实例统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：显示指定成员设备上指定单板的内核VPN实例统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：显示指定单板的内核VPN实例统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的内核VPN实例统计信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS L3VPN \-- MPLS L3VPN Probe命令 \-- display system internal ospf sham-link standby**

------------------------------------------------------------------------

**[display system internal ospf sham-link standby**]命令用来显示OSPF备进程上OSPF伪连接的信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ospf ** *process-id* ] **sham-link**  **area** *area-id*  **standby** **slot** *slot-number*  **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal ospf ** *process-id* ] **sham-link**  **area** *area-id*  **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：显示指定OSPF进程内的伪连接信息。*process-id*为OSPF进程号，取值范围为1～65535。如果不指定本参数，则显示所有OSPF进程的伪连接信息。

**[area** *area-id*]：显示指定OSPF区域内的伪连接信息。*area-id*为OSPF区域号，可以是整数形式，也可以是IPv4地址形式。当是整数形式时，取值范围为0～4294967295。如果不指定本参数，则显示所有OSPF区域的伪连接信息。

**[slot** *slot-number*]：指定备进程所在的单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定备进程所在的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

执行本命令时，如果不指定进程号和区域号，则显示所有的OSPF伪连接信息。

开启OSPF NSR功能后，OSPF主进程将OSPF邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启OSPF NSR功能，则不会显示任何信息。

