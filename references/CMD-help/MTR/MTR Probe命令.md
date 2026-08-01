<!-- CMD-INDEX
  debugging system internal ip topology |                  | L7
  display system internal ip topology | Probe视图          | L59
  display system internal ip topology inactive | Probe视图          | L103
-->

**MTR \-- MTR Probe命令 \-- debugging system internal ip topology**

------------------------------------------------------------------------

**[debugging system internal ip topology**]命令用来打开拓扑调试信息的开关。

**[undo debugging system internal ip topology**]命令用来关闭拓扑调试信息的开关。

【命令】

集中式设备：

**[debugging system internal ip topology**]

**[undo debugging system internal ip topology**]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging system internal ip topology** [ **s**]**lot** *slot-number*  **cpu** *cpu-number* ]

**[undo debugging system internal ip topology** [ **s**]**lot** *slot-number*  **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[debugging system internal ip topology** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]

**[undo debugging system internal ip topology** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]

【缺省情况】

拓扑的调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：指定单板，*slot-number*表示单板所在的槽位号。如果未指定本参数，将打开主用主控板的拓扑调试信息开关。（分布式设备－独立运行模式）

**[slot*** slot-number*]：指定成员设备，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将打开主用设备的拓扑调试信息开关。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定成员设备上指定单板，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将打开全局主用主控板的拓扑调试信息开关。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：指定CPU，*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MTR \-- MTR Probe命令 \-- display system internal ip topology**

------------------------------------------------------------------------

**[display system internal ip topology**]命令用来显示拓扑信息。

【命令】

集中式设备：

**[display system internal ip topology **[[ *topology-name* \| **statistics** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ip topology**[ [ *topology-name* \| **statistics** ]  **s**]**lot** *slot-number*  **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display system internal ip topology**[ [ *topology-name* \| **statistics** ] ]**chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[topology-name*]：配置的拓扑名字，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有拓扑的信息。

**[statistics**]：显示统计信息。

**[slot*** slot-number*]：指定单板，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主用主控板的拓扑信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：指定成员设备，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主用设备的拓扑信息。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定成员设备上指定单板，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板的拓扑信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：指定CPU，*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MTR \-- MTR Probe命令 \-- display system internal ip topology inactive**

------------------------------------------------------------------------

**[display system internal ip topology inactive**]命令用来显示处于非活动状态的多拓扑实例信息。

【命令】

**[display system internal ip topology inactive**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令可以显示处于删除状态，但是还没有完全删除完毕的多拓扑实例信息。

