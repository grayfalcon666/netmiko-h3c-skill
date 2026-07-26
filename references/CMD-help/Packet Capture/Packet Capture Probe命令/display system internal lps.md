
**Packet Capture \-- Packet Capture Probe命令 \-- display system internal lps**

------------------------------------------------------------------------

**[display system internal lps**]命令用来显示LPS（Linux Packet Socket）信息。

【命令】

集中式设备：

**[display system internal lps**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal lps** [ **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display system internal lps** [ **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lps**]：显示LPS信息。

**[slot** *slot-number*]：显示指定单板的LPS信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板的连接信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的LPS信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备的连接信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的LPS信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX的连接信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的LPS信息。*chassis-numbe*r表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板的连接信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的LPS信息。*chassis-numbe*r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板的连接信息。（分布式设备－IRF模式）（支持IRF3的设备）
