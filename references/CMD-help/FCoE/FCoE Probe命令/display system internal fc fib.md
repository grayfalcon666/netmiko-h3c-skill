
**FCoE \-- FCoE Probe命令 \-- display system internal fc fib**

------------------------------------------------------------------------

**[display system internal fc fib**]命令用来显示FC FIB相关信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal fc fib ** *fcid*  *mask-length*  ] **vsan** *vsan-id*  **slot** *slot-number*

分布式设备－IRF模式：

**[display system internal fc fib ** *fcid*  *mask-length*  ] **vsan** *vsan-id*  **chassis** *chassis-number* **slot** *slot-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[fcid*]：显示指定目的FC地址的FC FIB表项信息，取值范围为0x000000～0xFFFFFF（十六进制）。

*[mask-length*]：目的FC地址掩码长度，取值范围为0～24。

**[vsan** *vsan-id*]：显示指定VSAN内的FC FIB相关信息。*vsan-id*的取值范围为1～3839。

**[slot ***slot-number*]：显示指定单板上的信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示Master设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示Master设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**FCoE \-- FCoE Probe命令 \-- display system internal fcoe vfcinfo**

------------------------------------------------------------------------

**[display system internal fcoe vfcinfo**]命令用来显示VFC接口相关的内部信息。

【命令】

集中式设备：

**[display system internal fcoe vfcinfo interface vfc*** interface-number*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal fcoe vfcinfo interface vfc*** interface-number * **slot** *slot-number* ]

分布式设备－IRF模式：

**[display system internal fcoe vfcinfo interface vfc*** interface-number * **chassis** *chassis-number* **slot** *slot-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** **vfc** *interface-number*]：显示指定VFC接口的内部信息。

**[slot ***slot-number*]：显示指定单板上的信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示Master设备上的信息。(集中式IRF设备)（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示Master设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。(分布式设备－IRF模式)（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**FCoE \-- FCoE Probe命令 \-- display system internal fcoe vsaninfo**

------------------------------------------------------------------------

**[display system internal fcoe vsaninfo**]命令用来显示VSAN相关的内部信息。

【命令】

集中式设备：

**[display system internal fcoe vsaninfo interface vfc*** interface-number ***vsan ***vsan-id*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal fcoe vsaninfo interface vfc*** interface-number ***vsan ***vsan-id*]

** **slot** *slot-number*

分布式设备－IRF模式：

**[display system internal fcoe vsaninfo interface vfc*** interface-number ***vsan ***vsan-id*]

** **chassis** *chassis-number* **slot** *slot-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface vfc*** interface-number*]：显示指定VFC接口下VSAN相关的内部信息。

**[vsan** *vsan-id*]：显示指定VSAN的内部信息。*vsan-id*的取值范围为1～3839。

**[slot ***slot-number*]：显示指定单板上的信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示Master设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示Master设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**FCoE \-- FCoE Probe命令 \-- display system internal zone acl**

------------------------------------------------------------------------

**[display system internal zone acl**]命令用来显示已经下发的FC Zone ACL相关信息。

【命令】

集中式设备：

**[display system internal zone acl vsan ***vsan-id*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal zone acl vsan ***vsan-id * **slot** *slot-number* ]

分布式设备－IRF模式：

**[display system internal zone acl vsan ***vsan-id * **chassis** *chassis-number* **slot** *slot-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内已经下发的FC Zone ACL信息。*vsan-id*的取值范围为1～3839。

**[slot ***slot-number*]：显示指定单板上的信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示Master设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示Master设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

