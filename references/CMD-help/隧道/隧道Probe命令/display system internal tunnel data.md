
**隧道 \-- 隧道Probe命令 \-- display system internal tunnel data**

------------------------------------------------------------------------

**[display system internal tunnel data**]命令用来显示Tunnel接口内核数据信息。

【命令】

集中式设备：

**[display system internal tunnel data interface tunnel** *number* [ **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal tunnel data interface tunnel** *number* [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal tunnel data interface tunnel** *number* [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface tunnel ***number*]：显示指定Tunnel接口的内核数据信息。*number*表示Tunnel接口编号，取值为已创建的Tunnel接口的编号。

**[slot** *slot-number*]：显示指定单板的Tunnel接口内核数据信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示主用主控板的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的Tunnel接口内核数据信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，则显示命令所在主成员设备的信息。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的Tunnel接口内核数据信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示全局主用主控板的信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU上的Tunnel接口内核数据信息。*cpu-number*表示CPU的编号。本参数的支持情况与设备的具体型号有关，请以设备的实际情况为准。
