
**sFlow \-- sFlow Probe命令 \-- display system internal sflow statistics**

------------------------------------------------------------------------

**[display system internal sflow statistics**]命令用来显示sFlow的统计信息。

【命令】

集中式设备：

**[display system internal sflow statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal sflow statistics ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal sflow statistics** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]*slot-number*：查看指定单板上的sFlow的统计信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）

**[slot**]*slot-number*：查看指定成员设备的sFlow的统计信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示所有设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：查看指定成员设备/PEX的sFlow的统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数时，将显示所有设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：查看指定成员设备上指定单板的sFlow的统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：查看指定单板的sFlow的统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU上的信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**sFlow \-- sFlow Probe命令 \-- reset system internal sflow statistics**

------------------------------------------------------------------------

**[reset system internal sflow statistics**]命令用来清除sFlow的统计信息。

【命令】

集中式设备：

**[reset  system internal sflow statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal sflow statistics ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[reset system internal sflow statistics** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]*slot-number*：清除指定单板上的sFlow的统计信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）

**[slot**]*slot-number*：清除指定成员设备的sFlow的统计信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示所有设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：清除指定成员设备/PEX的sFlow的统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数时，将显示所有设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：清除指定成员设备上指定单板的sFlow的统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板的sFlow的统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：清除指定CPU的信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

