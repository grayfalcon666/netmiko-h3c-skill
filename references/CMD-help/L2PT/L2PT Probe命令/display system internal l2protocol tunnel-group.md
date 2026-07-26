
**L2PT \-- L2PT Probe命令 \-- display system internal l2protocol tunnel-group**

------------------------------------------------------------------------

**[display system internal l2protocol tunnel-group**]命令用来显示L2PT组播组信息。

【命令】

集中式设备：

**[display system internal l2protocol tunnel-group**]

分布式设备/集中式IRF设备：

**[display system internal l2protocol tunnel-group **]**slot ***slot-number*

分布式IRF设备：

**[display system internal l2protocol tunnel-group **]**chassis ***chassis-number ***slot ***slot-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot **]*slot-number*：显示指定单板的L2PT组播组信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的L2PT组播组信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的L2PT组播组信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）
