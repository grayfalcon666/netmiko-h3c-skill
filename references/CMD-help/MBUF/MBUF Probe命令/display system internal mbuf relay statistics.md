
**MBUF \-- MBUF Probe命令 \-- display system internal mbuf relay statistics**

------------------------------------------------------------------------

![说明](MBUF%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal mbuf relay statistics**]命令用来显示MBUF中继模块的统计信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mbuf relay statistics** **slot** *slot-number* [ **cpu** *cpu-numbe*   **vcpu** *vcpu-number* [ **rcv** *receiver-id*  ]]]

分布式设备－IRF模式：

**[display system internal mbuf relay statistics** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-numbe*   **vcpu** *vcpu-number* [ **rcv** *receiver-id*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的MBUF中继模块的统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的MBUF中继模块的统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的MBUF中继模块的统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的MBUF中继模块的统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板/PEX的MBUF中继模块的统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：MBUF中继使用的CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vcpu**] v*cpu-**number*：MBUF中继使用的VCPU的编号。不指定该参数时，表示当前单板上的所有VCPU。

**[rcv ***received-id*]：MBUF中继接收者的编号。不指定该参数时，表示当前CPU上的所有接收者。

**MBUF \-- MBUF Probe命令 \-- reset system internal mbuf relay statistics**

------------------------------------------------------------------------

![说明](MBUF%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset system internal mbuf relay statistics**]命令用来清除MBUF中继模块的统计信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal mbuf relay statistics** **slot** *slot-number* [ **cpu** *cpu-numbe*   **vcpu** *vcpu-number* [ **rcv** *receiver-id*  ]]]

分布式设备－IRF模式：

**[reset system internal mbuf relay statistics** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-numbe*   **vcpu** *vcpu-number* [ **rcv** *receiver-id*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：清除指定单板的MBUF中继模块的统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：清除指定成员设备的MBUF中继模块的统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：清除指定成员设备/PEX的MBUF中继模块的统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的MBUF中继模块的统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板/PEX的MBUF中继模块的统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：MBUF中继使用的CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vcpu**] v*cpu-** number*：MBUF中继使用的VCPU的编号。不指定该参数时，表示当前单板上的所有VCPU。

**[rcv ***received-id*]：MBUF中继接收者的编号。不指定该参数时，表示当前CPU上的所有接收者。

