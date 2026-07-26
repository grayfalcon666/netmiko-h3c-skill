
**NVGRE \-- NVGRE Probe命令 \-- display system internal nvgre forwarding tunnel**

------------------------------------------------------------------------

**[display system internal nvgre forwarding tunnel**]命令用来显示NVGRE隧道转发信息。

【命令】

集中式设备：

**[display system internal nvgre forwarding tunnel** [ **vsid** *vsid* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal nvgre forwarding tunnel** [ **vsid** *vsid*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal nvgre forwarding tunnel** [ **vsid** *vsid*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsid*]：显示指定NVGRE网络的NVGRE隧道转发信息。*vsid*为NVGRE虚拟子网编号，取值范围为4096～16777214。不指定此参数，则显示所有NVGRE网络的NVGRE隧道转发信息。

**[slot**]*slot-number*：显示指定单板上的NVGRE隧道转发信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的NVGRE隧道转发信息。（分布式设备－独立运行模式）

**[slot**]*slot-number*：显示指定成员设备上的NVGRE隧道转发信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示主设备上的NVGRE隧道转发信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的NVGRE隧道转发信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示主设备上的NVGRE隧道转发信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备指定单板上的NVGRE隧道转发信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的NVGRE隧道转发信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的NVGRE隧道转发信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示全局主用主控板上的NVGRE隧道转发信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的NVGRE隧道转发信息。只有指定的**slot**支持多CPU时，才能配置该参数。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

