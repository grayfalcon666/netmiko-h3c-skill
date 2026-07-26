
**FDB \-- FDB Probe命令 \-- debugging system internal fdb**

------------------------------------------------------------------------

**[debugging system internal fdb **]命令用来打开流表调试开关。

**[undo debugging system internal fdb**]命令用来关闭流表调试开关。

【命令】

集中式设备：

**[debugging system internal **[{ **ipv4** \| **ipv6** } **fdb** { **all** \| **drv** \| **entry** [ **verbose** ]  **acl** *acl-number*  }]]

**[undo debugging system internal **[{ **ipv4** \| **ipv6** } **fdb** { **all** \| **drv** \| **entry** [ **verbose** ]  **acl** *acl-number*  }]]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging system internal**[ { **ipv4** \| **ipv6** } **fdb** { **all** \| **drv** \| **entry** [ **verbose** ]  **acl** *acl-number*  } **slot** *slot-number*  **cpu** *cpu-number* ]]

**[undo**[ **debugging** **system** **internal** { **ipv4** \| **ipv6** } **fdb** { **all** \| **drv** \| **entry** [ **verbose** ]  **acl** *acl-number*  } **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[debugging**[ **system** **internal** { **ipv4** \| **ipv6** } **fdb** { **all** \| **drv** \| **entry** [ **verbose** ]  **acl** *acl-number*  } **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

**[undo**[ **debugging** **system** **internal** { **ipv4** \| **ipv6** } **fdb** { **all** \| **drv** \| **entry** [ **verbose** ]  **acl** *acl-number*  } **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【缺省情况】

流表调试开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：表示IPv4的流表调试信息。

**[ipv6**]：表示IPv6的流表调试信息。

**[all**]：表示所有的调试信息开关。

**[drv**]：表示下驱动的调试信息开关。

**[entry**]：表示流表的调试信息开关。

**[verbose**]：表示显示详细信息的流表调试信息开关。

**[acl ***acl-number*]：指定ACL的编号。*acl-number*表示ACL的编号，基本ACL取值范围为2000～2999，高级ACL取值范围为3000～3999。

**[slot** *slot-number*]：显示指定单板上的流表调试信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的流表调试信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的流表调试信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的流表调试信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的流表调试信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的流表调试信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**FDB \-- FDB Probe命令 \-- display system internal fdb**

------------------------------------------------------------------------

**[display system internal fdb**]命令用来显示流表的统计信息。

【命令】

集中式设备：

**[display system internal **[{ **ipv4** \| **ipv6** } **fdb statistics**]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal **[{ **ipv4** \| **ipv6** } **fdb statistics slot** *slot-number* [ **[cpu]** *cpu-number* ]]]

分布式设备－IRF模式：

**[display system internal **[{ **ipv4** \| **ipv6** } **fdb statistics chassis** *chassis-number* **slot** *slot-number* [ **[cpu]** *cpu-number* ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：表示IPv4的流表统计信息。

**[ipv6**]：表示IPv6的流表统计信息。

**[slot** *slot-number*]：显示指定单板上流表的统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上流表的统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上流表的统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上流表的统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上流表的统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**] *cpu-number*：显示指定CPU上流表的统计信息。*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**FDB \-- FDB Probe命令 \-- reset system internal fdb**

------------------------------------------------------------------------

**[reset system internal fdb**]命令用来清除流表的统计信息。

【命令】

集中式设备：

**[reset system internal **[{ **ipv4** \| **ipv6** } **fdb statistics**]]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal **[{ **ipv4** \| **ipv6** } **fdb statistics** [ **slot** *slot-number* [ **[cpu]** *cpu-number* ]]]]

分布式设备－IRF模式：

**[reset system internal **[{ **ipv4** \| **ipv6** } **fdb statistics** [ **chassis** *chassis-number* **slot** *slot-number* [ **[cpu]** *cpu-number* ] ] ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：表示清除IPv4的流表统计信息。

**[ipv6**]：表示清除IPv6的流表统计信息。

**[slot** *slot-number*]：清除指定单板上流表的统计信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则清除所有单板上的流表的统计信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：清除指定成员设备上流表的统计信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则清除所有成员设备上的上流表的统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：清除指定成员设备/PEX上流表的统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则清除所有成员设备/PEX上流表的统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备的指定单板上流表的统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则清除所有单板上流表的统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板上流表的统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则清除所有单板上流表的统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**] *cpu-number*：清除指定CPU上流表的统计信息。*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

