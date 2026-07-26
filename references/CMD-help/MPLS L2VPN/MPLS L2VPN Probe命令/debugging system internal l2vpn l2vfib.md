
**MPLS L2VPN \-- MPLS L2VPN Probe命令 \-- debugging system internal l2vpn l2vfib**

------------------------------------------------------------------------

**[debugging system internal l2vpn l2vfib**]命令用来打开L2VPN L2VFIB模块的调试信息开关。

**[undo debugging system internal l2vpn l2vfib**]命令用来关闭L2VPN L2VFIB模块的调试信息开关。

【命令】

集中式设备：

**[debugging system internal l2vpn l2vfib**[ { **ac** \| **all** \| **config** \| **lpw** \| **sync** }]]

**[undo**[ **debugging system internal l2vpn l2vfib** { **ac** \| **all** \| **config** \| **lpw** \| **sync** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging system internal l2vpn l2vfib**[ { **ac** \| **all** \| **config** \| **lpw** \| **sync** } ]]**slot***slot-number* **cpu** *cpu-number*

**[undo**[ **debugging system internal l2vpn l2vfib** { **ac** \| **all** \| **config** \| **lpw** \| **sync** } **slot** ]]*slot-number* **cpu** *cpu-number*

分布式设备－IRF模式：

**[debugging system internal l2vpn l2vfib**[ { **ac** \| **all** \| **config** \| **lpw** \| **sync** } ]]**chassis***chassis-number***slot***slot-number* **cpu** *cpu-number*

**[undo**[ **debugging system internal l2vpn l2vfib** { **ac** \| **all** \| **config** \| **lpw** \| **sync** } ]]**chassis***chassis-number***slot***slot-number* **cpu** *cpu-number*

【缺省情况】

L2VPN L2VFIB模块的调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ac**]：表示L2VPN L2VFIB AC相关调试信息开关。

**[all**]：表示L2VPN L2VFIB所有调试信息开关。

**[config**]：表示L2VPN L2VFIB配置消息调试信息开关。

**[lpw**]：表示L2VPN L2VFIB LPW相关调试信息开关。

**[sync**]：表示L2VPN L2VFIB同步相关调试信息开关。

**[slot**]* slot-number*：表示指定单板的L2VPN L2VFIB调试信息开关。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式/集中式IRF设备）

**[slot**]* slot-number*：表示指定成员设备的L2VPN L2VFIB调试信息开关。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：表示指定成员设备/PEX的L2VPN L2VFIB调试信息开关。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：表示指定成员设备上指定单板的L2VPN L2VFIB调试信息开关。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：表示指定单板的L2VPN L2VFIB调试信息开关。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示指定CPU的L2VPN L2VFIB调试信息开关。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS L2VPN \-- MPLS L2VPN Probe命令 \-- display system internal l2vpn l2vfib record**

------------------------------------------------------------------------

**[display system internal l2vpn l2vfib record**]命令用来显示L2VPN L2VFIB模块记录的信息，包括L2VFIB模块收到的信息、L2VFIB通知驱动的信息、驱动返回的信息等。

【命令】

集中式设备：

**[display system internal l2vpn l2vfib record** [ **start** ]*start-number *]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal l2vpn l2vfib record** [ **start** ]*start-number * **slot** ]*slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal l2vpn l2vfib record** [ **start** ]*start-number * ]**chassis***chassis-number***slot***slot-number * **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[start**]*start-number*：从指定位置开始显示记录信息。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[slot**]* slot-number*：显示指定单板上的记录信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备上的记录信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX上的记录信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：显示指定成员设备上指定单板的记录信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：显示指定单板的记录信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的记录信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【相关命令】

·**reset system internal l2vpn l2vfib record**

**MPLS L2VPN \-- MPLS L2VPN Probe命令 \-- display system internal l2vpn l2vfib statistics**

------------------------------------------------------------------------

**[display system internal l2vpn l2vfib statistics**]命令用来显示L2VPN L2VFIB模块的统计信息。

【命令】

集中式设备：

**[display system internal l2vpn l2vfib **]**statistics**

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal l2vpn l2vfib statistics slot**]*slot-number* **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal l2vpn l2vfib statistics** **chassis** ]*chassis-number* **slot** *slot-number* **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：显示指定单板上的L2VPN L2VFIB模块统计信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备上的L2VPN L2VFIB模块统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX上的L2VPN L2VFIB模块统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number* **slot*** slot-number*：显示指定成员设备上指定单板的L2VPN L2VFIB模块统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number* **slot*** slot-number*：显示指定单板的L2VPN L2VFIB模块统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的L2VPN L2VFIB模块统计信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS L2VPN \-- MPLS L2VPN Probe命令 \-- display system internal l2vpn ldp**

------------------------------------------------------------------------

**[display system internal l2vpn ldp**]命令用来显示LDP协议备进程的PW标签相关信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal l2vpn ldp ** **peer** *ip-address*  **pw-id** *pw-id*  ]  **verbose**  **standby slot** *slot-number  *[ **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display system internal l2vpn ldp ** **peer** *ip-address*  **pw-id** *pw-id*  ]  **verbose** ****standby chassis** *chassis-number* **slot** *slot-number*** **cpu** *cpu-number*

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[peer*** ip-address*]：显示指定远端PE通过LDP通告的PW标签相关信息。*ip-address*为远端PE的LSR ID。如果没有指定本参数，则显示所有远端PE通过LDP通告的PW标签相关信息。

**[pw-id ***pw-id*]：显示指定PW的PW标签相关信息。*pw-id*为PW的PW ID，取值范围为1～4294967295。如果指定了**peer*** ip-address*参数，没有指定本参数，则显示指定远端PE通过LDP通告的所有PW标签相关信息。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

**[standby**]**：**显示指定LDP备进程的信息。

**[slot**]* slot-number*：指定备进程所在的主控板。*slot-number*为主控板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和主控板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

执行本命令时，本设备接收到的LDP PW标签映射信息都会显示；而本设备通告的PW标签映射只有成功通告给远端PE后才会显示。

**MPLS L2VPN \-- MPLS L2VPN Probe命令 \-- l2vpn l2vfib record size**

------------------------------------------------------------------------

**[l2vpn l2vfib record size**]命令用来设置L2VPN L2VFIB模块记录信息的最大数目。

【命令】

集中式设备：

**[l2vpn l2vfib record size**]*size*

分布式设备－独立运行模式/集中式IRF设备：

**[l2vpn l2vfib record size**]*size* **slot** *slot-number* **cpu** *cpu-number*

分布式设备－IRF模式：

**[l2vpn l2vfib record size**]*size* **chassis** *chassis-number* **slot** *slot-number* **cpu** *cpu-number*

【缺省情况】

L2VPN L2VFIB模块记录信息的最大数目为4096条。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：记录信息的最大数目。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[slot**]* slot-number*：指定单板上的记录信息的最大数目。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定成员设备上的记录信息的最大数目。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：指定成员设备/PEX上的记录信息的最大数目。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：指定成员设备上指定单板的记录信息的最大数目。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：指定单板的记录信息的最大数目。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：指定CPU上的记录信息的最大数目。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS L2VPN \-- MPLS L2VPN Probe命令 \-- reset system internal l2vpn l2vfib record**

------------------------------------------------------------------------

**[reset system internal l2vpn l2vfib record**]命令用来清除L2VPN L2VFIB模块记录的信息。

【命令】

集中式设备：

**[reset system internal l2vpn l2vfib record**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal l2vpn l2vfib record** **slot** ]*slot-number* **cpu** *cpu-number*

分布式设备－IRF模式：

**[reset system internal l2vpn l2vfib record chassis**]*chassis-number* **slot** *slot-number* **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：清除指定单板上的记录信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：清除指定成员设备上的记录信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：清除指定成员设备/PEX上的记录信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：清除指定成员设备上指定单板的记录信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：清除指定单板的记录信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：清除指定CPU上的记录信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【相关命令】

·**display system internal l2vpn l2vfib record**
