<!-- CMD-INDEX
  debugging system internal mpls lfib |                  | L15
  display system internal mpls forwarding temporary-ilm | Probe视图          | L83
  display system internal mpls lfib ilm | Probe视图          | L129
  display system internal mpls lfib nhlfe | Probe视图          | L175
  display system internal mpls lfib nhlfe reflist | Probe视图          | L221
  display system internal mpls lfib record | Probe视图          | L267
  display system internal mpls lfib statistics | Probe视图          | L317
  display system internal mpls lsp-pending | Probe视图          | L361
  display system internal mpls statistics | Probe视图          | L381
  mpls lfib record size               | Probe视图          | L401
  reset system internal mpls lfib record | Probe视图          | L451
-->

**MPLS基础 \-- MPLS基础Probe命令 \-- debugging system internal mpls lfib**

------------------------------------------------------------------------

**[debugging system internal mpls lfib**]命令用来打开MPLS LFIB模块的调试信息开关。

**[undo debugging system internal mpls lfib**]命令用来关闭MPLS LFIB模块的调试信息开关。

【命令】

集中式设备：

**[debugging system internal mpls lfib**[ { **all** \| **config** \| **ilm** \| **message** \| **nhlfe** \| **sync** }]]

**[undo**[ **debugging system internal mpls lfib** { **all** \| **config** \| **ilm** \| **message** \| **nhlfe** \| **sync** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging system internal mpls lfib**[ { **all** \| **config** \| **ilm** \| **message** \| **nhlfe** \| **sync** } ]]**slot***slot-number * **cpu** *cpu-number*

**[undo**[ **debugging system internal mpls lfib** { **all** \| **config** \| **ilm** \| **message** \| **nhlfe** \| **sync** } **slot** ]]*slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[debugging system internal mpls lfib**[ { **all** \| **config** \| **ilm** \| **message** \| **nhlfe** \| **sync** } ]]**chassis***chassis-number***slot***slot-number * **cpu** *cpu-number*

**[undo**[ **debugging system internal mpls lfib** { **all** \| **config** \| **ilm** \| **message** \| **nhlfe** \| **sync** } ]]**chassis***chassis-number***slot***slot-number * **cpu** *cpu-number*

【缺省情况】

MPLS LFIB模块的调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示MPLS LFIB所有调试信息开关。

**[config**]：表示MPLS LFIB配置消息调试信息开关。

**[ilm**]：表示MPLS LFIB ILM相关调试信息开关。

**[message**]：表示MPLS LFIB消息相关调试信息开关。

**[nhlfe**]：表示MPLS LFIB NHLFE相关调试信息开关。

**[sync**]：表示MPLS LFIB同步相关调试信息开关。

**[slot**]* slot-number*：表示指定单板的MPLS LFIB调试信息开关。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：表示指定成员设备的MPLS LFIB调试信息开关。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：表示指定成员设备/PEX的MPLS LFIB调试信息开关。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：表示指定成员设备上指定单板的MPLS LFIB调试信息开关。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：表示指定单板的MPLS LFIB调试信息开关。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：指定单板CPU的调试信息开关。*cpu-number*表示单板上CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls forwarding temporary-ilm**

------------------------------------------------------------------------

**[display system internal mpls forwarding temporary-ilm**]命令用来显示临时保存的ILM表项信息。

【命令】

集中式设备：

**[display system internal mpls forwarding temporary-ilm **\*****label *]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mpls forwarding temporary-ilm **\*****label *] **slot** *slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal mpls forwarding temporary-ilm** *label*  **chassis** ]*chassis-number* **slot** *slot-number * **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[label*]：显示指定入标签的临时ILM表项，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果不指定本参数，则显示所有的临时ILM表项信息。

**[slot**]* slot-number*：显示指定单板上的临时ILM表项。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备上的临时ILM表项。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX上的临时ILM表项。*slot-number*为设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number* **slot*** slot-number*：显示指定成员设备上指定单板的临时ILM表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number* **slot*** slot-number*：显示指定单板的临时ILM表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的临时ILM表项。*cpu-number*表示单板上CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls lfib ilm**

------------------------------------------------------------------------

**[display system internal mpls lfib ilm**]命令用来显示MPLS ILM表项的详细信息。

【命令】

集中式设备：

**[display system internal mpls lfib ilm**]*label*

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mpls lfib ilm**]*label* **slot** *slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal mpls lfib ilm **]*label* **chassis** *chassis-number* **slot** *slot-number * **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[label*]：显示指定入标签的ILM表项详细信息。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[slot**]* slot-number*：显示指定单板上的ILM表项详细信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备上的ILM表项详细信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX上的ILM表项详细信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：显示指定成员设备上指定单板的ILM表项详细信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：显示指定单板的ILM表项详细信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的ILM表项详细信息。*cpu-number*表示单板上CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls lfib nhlfe**

------------------------------------------------------------------------

**[display system internal mpls lfib nhlfe**]命令用来显示MPLS NHLFE表项详细信息。

【命令】

集中式设备：

**[display system internal mpls lfib nhlfe**]*nid*

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mpls lfib nhlfe**]*nid* **slot** *slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal mpls lfib nhlfe**]*nid* **chassis** *chassis-number* **slot** *slot-number * **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nid*]：显示指定NHLFE表项的详细信息。*nid*为NHLFE表项索引，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[slot**]* slot-number*：显示指定单板上的NHLFE表项详细信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备上的NHLFE表项详细信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX上的NHLFE表项详细信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number* **slot*** slot-number*：显示指定成员设备上指定单板的NHLFE表项详细信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number* **slot*** slot-number*：显示指定单板的NHLFE表项详细信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的NHLFE表项详细信息。*cpu-number*表示单板上CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls lfib nhlfe reflist**

------------------------------------------------------------------------

**[display system internal mpls lfib nhlfe reflist**]命令用来显示MPLS NHLFE反向关联信息。

【命令】

集中式设备：

**[display system internal mpls lfib nhlfe**]*nid ***reflist**

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mpls lfib nhlfe**]*nid* **reflist** **slot** *slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal mpls lfib nhlfe**]*nid* **reflist** **chassis** *chassis-number* **slot** *slot-number * **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nid*]：显示指定NHLFE表项的反向关联信息。*nid*为NHLFE表项索引，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[slot**]* slot-number*：显示指定单板上的NHLFE表项的反向关联信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备上的NHLFE表项的反向关联信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX上的NHLFE表项的反向关联信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number* **slot*** slot-number*：显示指定成员设备上指定单板的NHLFE表项的反向关联信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number* **slot*** slot-number*：显示指定单板的NHLFE表项的反向关联信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的NHLFE表项的反向关联信息。*cpu-number*表示单板上CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls lfib record**

------------------------------------------------------------------------

**[display system internal mpls lfib record**]命令用来显示MPLS LFIB模块记录的信息，包括LFIB模块收到的信息、LFIB通知驱动的信息、驱动返回的信息等。

【命令】

集中式设备：

**[display system internal mpls lfib record** [ **start** ]*start-number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mpls lfib record** [ **start** ]*start-number*  **slot** ]*slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal mpls lfib record** [ **start** ]*start-number*  ]**chassis***chassis-number***slot***slot-number * **cpu** *cpu-number*

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

**[cpu** *cpu-number*]：显示指定单板CPU的记录信息。*cpu-number*表示单板上CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【相关命令】

·**reset system internal****mpls lfib record**

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls lfib statistics**

------------------------------------------------------------------------

**[display system internal mpls **]**lfib statistics**命令用来显示MPLS LFIB的统计信息。

【命令】

集中式设备：

**[display system internal **]**mpls lfib statistics**

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mpls lfib statistics slot**]*slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal mpls lfib statistics** **chassis** ]*chassis-number* **slot** *slot-number * **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：显示指定单板上的MPLS LFIB统计信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备上的MPLS LFIB统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX上的MPLS LFIB统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number* **slot*** slot-number*：显示指定成员设备上指定单板的MPLS LFIB统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number* **slot*** slot-number*：显示指定单板的MPLS LFIB统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定单板CPU的MPLS LFIB模块统计信息。*cpu-number*表示单板上CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls lsp-pending**

------------------------------------------------------------------------

**[display system internal mpls lsp-pending**]命令用来显示LDP、BGP、RSVP协议GR过程中，尚未下发到转发平面的LSP信息。

【命令】

**[display system internal mpls lsp-pending**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls statistics**

------------------------------------------------------------------------

**[display system internal mpls statistics**]命令用来显示MPLS的内部状态统计信息。

【命令】

**[display system internal mpls statistics**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**MPLS基础 \-- MPLS基础Probe命令 \-- mpls lfib record size**

------------------------------------------------------------------------

**[mpls lfib record size**]命令用来设置MPLS LFIB模块记录信息的最大数目。

【命令】

集中式设备：

**[mpls lfib record size**]*size*

分布式设备－独立运行模式/集中式IRF设备：

**[mpls lfib record size**]*size* **slot** *slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[mpls lfib record size **]*size* **chassis** *chassis-number* **slot** *slot-number * **cpu** *cpu-number*

【缺省情况】

MPLS LFIB模块记录信息的最大数目为4096条。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：指定记录信息的最大数目。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[slot**]* slot-number*：指定单板上的记录信息的最大数目。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定成员设备上的记录信息的最大数目。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：指定成员设备/PEX上的记录信息的最大数目。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：指定成员设备上指定单板的记录信息的最大数目。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***slot*** slot-number*：指定单板的记录信息的最大数目。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：指定单板CPU记录信息的最大数目。*cpu-number*表示单板上CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MPLS基础 \-- MPLS基础Probe命令 \-- reset system internal mpls lfib record**

------------------------------------------------------------------------

**[reset system internal mpls lfib record**]命令用来清除MPLS LFIB模块记录的信息。

【命令】

集中式设备：

**[reset system internal mpls lfib record**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal mpls lfib record slot**]*slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[reset system internal mpls lfib record chassis**]*chassis-number* **slot** *slot-number * **cpu** *cpu-number*

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

**[cpu** *cpu-number*]：清除指定单板CPU的记录信息。*cpu-number*表示单板上CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【相关命令】

·**display system internal mpls lfib record**
