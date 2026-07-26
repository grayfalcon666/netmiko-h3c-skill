
**CFD \-- CFD Probe命令 \-- debugging system internal cfd**

------------------------------------------------------------------------

**[debugging** **system** **internal** **cfd**]命令用来打开CFD调试信息开关。

**[undo** **debugging** **system** **internal** **cfd**]命令用来关闭CFD调试信息开关。

【命令】

**[debugging**[ **system** **internal** **cfd** { **error** \| **hardware** }]]

**[undo**[ **debugging** **system** **internal** **cfd** { **error** \| **hardware** }]]

【缺省情况】

CFD调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[error**]：表示CFD错误调试信息开关。

**[hardware**]：表示CFD硬件调试信息开关。

**CFD \-- CFD Probe命令 \-- display system internal cfd hardware**

------------------------------------------------------------------------

**[display** **system** **internal** **cfd** **hardware**]命令用来显示CFD硬件表项的信息。

【命令】

集中式设备：

**[display** **system** **internal** **cfd** **hardware** **level** *level-value* [ **vlan** *vlan-id* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **system** **internal** **cfd** **hardware** **slot** *slot-number* **level** *level-value* [ **vlan** *vlan-id* ]]

分布式设备－IRF模式：

**[display** **system** **internal** **cfd** **hardware** **chassis** *chassis-number* **slot** *slot-number* **level** *level-value* [ **vlan** *vlan-id* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[level** *level-value*]：显示指定MD级别的信息，*level-value*的取值范围为0～7。

**[vlan** *vlan-id*]：显示指定VLAN的信息，*vlan-id*的取值范围为1～4094。如果未指定本参数，将显示无VLAN属性的CFD硬件表项信息。

**CFD \-- CFD Probe命令 \-- display system internal cfd mep**

------------------------------------------------------------------------

**[display** **system** **internal** **cfd** **mep**]命令用来显示CFD的MEP节点信息。

【命令】

集中式设备：

**[display** **system** **internal** **cfd** **mep** *mep-id* **service-instance** *instance-id*]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **system** **internal** **cfd** **mep** *mep-id* **service-instance** *instance-id* **slot** *slot-number*]

分布式设备－IRF模式：

**[display** **system** **internal** **cfd** **mep** *mep-id* **service-instance** *instance-id* **chassis** *chassis-number* **slot** *slot-number*]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mep-id*]：显示指定MEP上的信息。其中，*mep-id*表示MEP的编号，取值范围为1～8191。

**[service-instance** *instance-id*]：显示指定服务实例中的信息。其中，*instance-id*表示服务实例的编号，取值范围为1～32767。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

