<!-- CMD-INDEX
  debugging system internal vlan      | Probe视图          | L6
  display system internal vlan        | Probe视图          | L46
-->

**VLAN \-- VLAN Probe命令 \-- debugging system internal vlan**

------------------------------------------------------------------------

**[debugging system internal vlan**]命令用来打开VLAN的调试开关。

**[undo debugging system internal vlan**]命令用来关闭VLAN的调试开关。

【命令】

**[debugging system internal vlan **[{ **all** \| **error** \| **event** \| **execution** \| **hardware** }]]

**[undo debugging system internal vlan **[{ **all** \| **error** \| **event** \| **execution** \| **hardware** }]]

【缺省情况】

VLAN的调试开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示VLAN的所有调试信息开关。

**[error**]：表示VLAN的错误调试信息开关。

**[event**]：表示VLAN的事件调试信息开关。

**[execution**]：表示VLAN的执行调试信息开关。

**[hardware**]：表示VLAN的硬件调试信息开关。

**VLAN \-- VLAN Probe命令 \-- display system internal vlan**

------------------------------------------------------------------------

**[display system internal vlan**]命令用来查看VLAN模块相关的内部信息。

【命令】

集中式设备：

**[display system internal vlan**[ { **instance** *vlan-id* \| **interface** *interface-type interface-number* \| **summary** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal vlan**[ { **instance** *vlan-id* \| **interface** *interface-type interface-number* \| **summary** } **slot** *slot-number* [ **cpu** *cpu-number* ]]]

分布式设备－IRF模式：

**[display system internal vlan**[ { **instance** *vlan-id* \| **interface** *interface-type interface-number* \| **summary** } **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[instance*** vlan-id*]：显示指定VLAN的VLAN模块信息。*vlan-id*为指定VLAN的编号，取值范围为1～4094。

**[interface ***interface-type interface-number*]：显示指定端口的VLAN模块信息。*interface-type interface-number*为端口类型和端口编号。

**[summary**]：显示VLAN模块的摘要信息。

**[slot** *slot-number*]：查看指定单板上的VLAN模块信息。其中，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：查看指定成员设备上的VLAN模块信息。其中，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis ***chassis-number ***slot** *slot-number*]：查看指定成员设备上指定单板的VLAN模块信息。其中，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu**] *cpu-number*：查看指定CPU上的VLAN模块信息。*cpu-number*表示CPU的编号。不指定该参数时，表示默认CPU。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。
