
**MPLS保护倒换 \-- MPLS保护倒换Probe命令 \-- debugging system internal mpls forwarding protection**

------------------------------------------------------------------------

**[debugging system internal mpls forwarding protection**]命令用来打开MPLS转发平面保护倒换的调试信息开关。

**[undo debugging system internal mpls forwarding protection**]命令用来关闭MPLS转发平面保护倒换的调试信息开关。

【命令】

集中式设备：

**[debugging system internal mpls forwarding protection**[ { **all** \| **error** \| **process** }]]

**[undo****debugging system internal mpls forwarding protection**[ { **all** \| **error** \| **process** }]]

分布式设备---独立运行模式/集中式IRF设备：

**[debugging system internal mpls forwarding protection**[ { **all** \| **error** \| **process** } **slot** *slot-number* [ **cpu** *cpu-number* ]]]

**[undo debugging system internal mpls forwarding protection **[{ **all** \| **error** \| **process** } **slot** *slot-number* [ **cpu** *cpu-number* ]]]

分布式设备---IRF模式：

**[debugging system internal mpls forwarding protection**[ { **all** \| **error** \| **process** } **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]]

**[undo****debugging system internal mpls forwarding protection**[ { **all** \| **error** \| **process** } **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]]

【缺省情况】

MPLS转发平面保护倒换的调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示MPLS转发平面保护倒换的所有调试信息开关。

**[error**]：表示MPLS转发平面保护倒换的错误调试信息开关。

**[process**]：表示MPLS转发平面保护倒换的处理过程调试信息开关。

**[slot*** slot-number*]：表示指定单板上的调试信息开关。*slot-number*为单板所在的槽位号。（分布式设备―独立运行模式）

**[slot**]* slot-number*：表示指定成员设备上的调试信息开关。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：表示指定成员设备/PEX上的调试信息开关。*slot-number*为设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number* **slot** *slot-number*：表示指定成员设备指定单板上的调试信息开关。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number* **slot** *slot-number*：表示指定单板上的调试信息开关。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**] *cpu-number*：表示指定CPU的调试信息开关。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS保护倒换 \-- MPLS保护倒换Probe命令 \-- display system internal mpls protection statistics**

------------------------------------------------------------------------

**[display system internal mpls protection statistics**]命令用来显示MPLS保护倒换的统计信息，包括MPLS保护倒换收到的信息、PSC控制报文信息、错误处理信息等。

【命令】

集中式设备：

**[display system internal mpls protection statistics**]

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal mpls protection statistics**]**slot ***slot-number* **cpu** *cpu-number*

分布式设备---IRF模式：

**[display system internal mpls protection statistics**]**chassis ***chassis-number***slot ***slot-number* **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：显示指定单板上的MPLS保护倒换统计信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备上的MPLS保护倒换统计信息。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX上的MPLS保护倒换统计信息。*slot-number*为设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number* **slot** *slot-number*：显示指定成员设备指定单板上的MPLS保护倒换统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number* **slot** *slot-number*：显示指定单板上的MPLS保护倒换统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU上的MPLS保护倒换统计信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

