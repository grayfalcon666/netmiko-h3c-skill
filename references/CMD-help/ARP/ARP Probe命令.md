<!-- CMD-INDEX
  debugging system internal arp event | Probe视图          | L24
  debugging system internal arp features | Probe视图          | L52
  debugging system internal arp mac-forced-forwarding | Probe视图          | L86
  debugging system internal arp notify | Probe视图          | L122
  debugging system internal arp sync  | Probe视图          | L150
  display system internal arp         | Probe视图          | L178
  display system internal arp ifcb    | Probe视图          | L228
  display system internal arp ip-address | Probe视图          | L274
  display system internal arp mac-forced-forwarding | Probe视图          | L316
  display system internal arp machash | Probe视图          | L362
  display system internal arp probe   | Probe视图          | L410
  display system internal arp rbhash  | Probe视图          | L454
  display system internal arp reload  | Probe视图          | L502
  display system internal arp rule    | Probe视图          | L546
  display system internal arp snooping | Probe视图          | L596
  display system internal arp source-suppression cache | Probe视图          | L652
  display system internal arp statistics | Probe视图          | L696
  display system internal arp suppression xconnect-group verbose | Probe视图          | L740
  display system internal arp vlan    | Probe视图          | L784
  reset system internal arp statistics | Probe视图          | L828
-->

**ARP \-- ARP Probe命令 \-- debugging system internal arp event**

------------------------------------------------------------------------

**[debugging system internal arp event**]命令用来打开ARP事件调试信息开关。

**[undo debugging system internal arp event**]命令用来关闭ARP事件调试信息开关。

【命令】

**[debugging system internal arp** **event**]

**[undo debugging system internal arp** **event** ]

【缺省情况】

ARP事件调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**ARP \-- ARP Probe命令 \-- debugging system internal arp features**

------------------------------------------------------------------------

**[debugging system internal arp features**]命令用来打开ARP子特性的调试信息开关。

**[undo debugging system internal arp features**]命令用来关闭ARP子特性的调试信息开关。

【命令】

**[debugging system internal arp features **[{ **notify** \| **packet** }]]

**[undo debugging system internal arp features **[{ **notify** \| **packet** }]]

【缺省情况】

ARP子特性的调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[notify**]：表示ARP子特性的外部通知调试开关。

**[packet**]:表示ARP子特性报文调试开关。

**ARP \-- ARP Probe命令 \-- debugging system internal arp mac-forced-forwarding**

------------------------------------------------------------------------

**[debugging system internal arp mac-forced-forwarding**]命令用来打开MAC强制转发调试信息开关。

**[undo debugging system internal arp mac-forced-forwarding**]命令用来关闭MAC强制转发调试信息开关。

【命令】

**[debugging system internal arp mac-forced-forwarding **[{ **event** \| **notify** \| **hardware** }]]

**[undo debugging system internal arp mac-forced-forwarding **[{ **event** \| **notify** \| **hardware** }]]

【缺省情况】

MAC强制转发调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：表示MAC强制转发特性事件调试开关。

**[notify**]：表示MAC强制转发特性外部通知调试开关。

**[hardware**]:表示MAC强制转发特性硬件调试开关。

**ARP \-- ARP Probe命令 \-- debugging system internal arp notify**

------------------------------------------------------------------------

**[debugging system internal arp notify**]命令用来打开ARP的外部通知调试信息开关。

**[undo debugging system internal arp notify**]命令用来关闭ARP的外部通知调试信息开关。

【命令】

**[debugging system internal arp** **notify**]

**[undo debugging system internal arp** **notify** ]

【缺省情况】

ARP的外部通知调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**ARP \-- ARP Probe命令 \-- debugging system internal arp sync**

------------------------------------------------------------------------

**[debugging system internal arp sync**]命令用来打开ARP表项的同步调试开关。

**[undo debugging system internal arp sync**]命令用来关闭ARP表项的同步调试开关。

【命令】

**[debugging system internal arp sync**]

**[undo debugging system internal arp sync**]

【缺省情况】

ARP表项的同步调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**ARP \-- ARP Probe命令 \-- display system internal arp**

------------------------------------------------------------------------

**[display system internal arp**]命令用来显示对应设备或单板上学习到的ARP表项信息或表项个数。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal arp **[{ **all** \| **static** \| **dynamic** \| **multiport** } **slot** *slot-number* [ **cpu** *cpu-number* ]  **count** ]]

分布式设备---IRF模式：

**[display system internal arp **[{ **all** \| **static** \| **dynamic** \| **multiport** } **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]  **count** ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all:**]命令用来显示所有ARP表项信息或表项个数。

**[static:**]用来显示静态ARP表项信息或表项个数。

**[dynamic:**]用来显示动态ARP表项信息或表项个数。

**[multiport:**]用来显示多端口ARP表项信息或表项个数。

**[slot ***slot-number*]：显示指定单板的ARP表项信息或表项个数，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ARP表项信息或表项个数，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ARP表项信息或表项个数，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的ARP表项信息或表项个数，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的ARP表项信息或表项个数。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的ARP表项信息或表项个数。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[count**]：用来显示ARP表项个数。

**ARP \-- ARP Probe命令 \-- display system internal arp ifcb**

------------------------------------------------------------------------

**[display system internal arp ifcb**]命令用来查看指定板上二层或三层接口ARP控制块信息

【命令】

集中式设备

**[display system internal arp ifcb interface ***interface-type interface-number *]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal arp ifcb interface*** interface-type interface-number ***slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal arp ifcb interface ***interface-type interface-number ***chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface ***interface-type interface-number *]：显示指定二层或三层接口上的ARP控制块信息，*interface-type interface-number*为接口类型和接口编号。

**[slot ***slot-number*]：显示指定单板的ARP控制块信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ARP控制块信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ARP控制块信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的ARP控制块信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的ARP控制块信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的ARP控制块信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**ARP \-- ARP Probe命令 \-- display system internal arp ip-address**

------------------------------------------------------------------------

**[display system internal arp ***ip-address*]命令用来显示指定板上指定IP的ARP表项信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal arp ***ip-address* **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal arp ***ip-address* **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address***:**]用来显示指定IP的ARP表项信息。

**[slot ***slot-number*]：显示指定单板指定IP的ARP表项信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备指定IP的ARP表项信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX指定IP的ARP表项信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：表示指定成员设备上指定单板指定IP的ARP表项信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板指定IP的ARP表项信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU指定IP的ARP表项信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**ARP \-- ARP Probe命令 \-- display system internal arp mac-forced-forwarding**

------------------------------------------------------------------------

**[display system internal arp mac-forced-forwarding**]命令用来显示指定板上MAC强制转发配置信息。

【命令】

集中式设备：

**[display system internal arp mac-forced-forwarding vlan ***vlan-id*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal arp mac-forced-forwarding vlan ***vlan-id ***slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal arp mac-forced-forwarding vlan ***vlan-id ***chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-id*]:显示指定VLAN上mac强制转发配置信息。*vlan-id*表示指定VLAN的编号。

**[slot ***slot-number*]：显示指定单板的MFF配置信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的MFF配置信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的MFF配置信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的MFF配置信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的MFF配置信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的MFF配置信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**ARP \-- ARP Probe命令 \-- display system internal arp machash**

------------------------------------------------------------------------

**[display system internal arp machash**]命令用来显示指定板上machash表项信息。

【命令】

集中式设备：

**[display system internal arp machash vlan ***vlan-id ***ip*** ip-address*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal arp machash vlan ***vlan-id ***ip*** ip-address* **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal arp machash vlan ***vlan-id ***ip*** ip-address* **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-id*]: 显示指定VLAN上machash表项信息。*vlan-id*表示指定VLAN的id。

**[ip*** ip-address*]：显示指定IP上machash表项信息。*ip-address*表示指定IP的IP地址

**[slot ***slot-number*]：显示指定单板的machash表项信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的machash表项信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的machash表项信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的machash表项信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的machash表项信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的machash表项信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**ARP \-- ARP Probe命令 \-- display system internal arp probe**

------------------------------------------------------------------------

**[display system internal arp probe**]命令用来显示指定板上ARP探测链表项。

【命令】

集中式设备：

**[display system internal arp probe**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal arp probe** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal arp probe** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的ARP探测链表项，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ARP探测链表项，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ARP探测链表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的ARP探测链表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的ARP探测链表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的ARP探测链表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**ARP \-- ARP Probe命令 \-- display system internal arp rbhash**

------------------------------------------------------------------------

**[display system internal arp rbhash**]命令用来显示指定板上rbhash表项信息。

【命令】

集中式设备：

**[display system internal arp rbhash vlan ***vlan-id ***ip*** ip-address*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal arp rbhash vlan ***vlan-id ***ip*** ip-address* **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal arp rbhash vlan ***vlan-id ***ip*** ip-address* **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-id*]: 显示指定VLAN上rbhash表项信息。*vlan-id*表示指定VLAN的编号。

**[ip*** ip-address*]：显示指定IP上rbhash表项信息。

**[slot ***slot-number*]：显示指定单板的rbhash表项信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的rbhash表项信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的rbhash表项信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：表示指定成员设备上指定单板的rbhash表项信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的rbhash表项信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的rbhash表项信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**ARP \-- ARP Probe命令 \-- display system internal arp reload**

------------------------------------------------------------------------

**[display system internal arp reload**]命令用来显示指定板上ARP重刷链表项。

【命令】

集中式设备：

**[display system internal arp reload**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal arp reload** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal arp reload** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的ARP重刷链表项，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ARP重刷链表项，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ARP重刷链表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的ARP重刷链表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的ARP重刷链表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的ARP重刷链表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**ARP \-- ARP Probe命令 \-- display system internal arp rule**

------------------------------------------------------------------------

**[display system internal arp rule**]命令用来显示ARP规则信息。

【命令】

集中式设备：

**[display system internal arp rule ***address* }]

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal arp rule ***address* } **slot**]* slot-number * **cpu** *cpu-number*

分布式设备---IRF模式：

**[display system internal arp rule ***address* } **chassis**] *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：显示所有ARP规则信息。

**[interface **]*interface-type interface-number*：显示指定接口的ARP规则信息，*interface-type interface-number*表示接口类型和接口编号。

*[ip-*]*address*：显示指定IP地址的ARP规则信息。

**[slot**] *slot-number*：显示指定单板的ARP规则信息。*slot-number*表示单板所在的槽位号。（分布式设备---独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的ARP规则信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的ARP规则信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ARP规则信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备---IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的ARP规则信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备---IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的ARP规则信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**ARP \-- ARP Probe命令 \-- display system internal arp snooping**

------------------------------------------------------------------------

**[display system internal arp snooping**]命令用来在Probe视图显示ARP Snooping表项。

【命令】

集中式设备：

**[display system internal arp snooping ** **vlan** *vlan-id* ]  **count**

**[display system internal arp snooping ip ***ip-address*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal arp snooping **] **vlan** *vlan-id*  **slot** *slot-number*  **cpu** *cpu-number*   **count**

**[display system internal arp snooping ip** *ip-address* **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal arp snooping** [ **vlan** *vlan-id*  **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*   **count** ]]

**[display system internal arp snooping ip ***ip-address ***chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan** *vlan-id*]：显示指定VLAN内的ARP Snooping表项。*vlan-id*的取值范围为1～4094。

**[count**]：显示当前ARP Snooping表项的数量。

**[ip ***ip-address*]：显示指定IP地址对应的ARP Snooping表项。

**[slot ***slot-number*]：显示指定单板的ARP Snooping表项，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ARP Snooping表项，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ARP Snooping表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的ARP Snooping表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的ARP Snooping表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的ARP Snooping表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**ARP \-- ARP Probe命令 \-- display system internal arp source-suppression cache**

------------------------------------------------------------------------

**[display system internal arp source-suppression cache**]命令用来显示指定板源抑制表项。

【命令】

集中式设备：

**[display system internal arp source-suppression cache**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal arp source-suppression cache slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal arp source-suppression cache******chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的源抑制表项，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的源抑制表项，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的源抑制表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的源抑制表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的源抑制表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的源抑制表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**ARP \-- ARP Probe命令 \-- display system internal arp statistics**

------------------------------------------------------------------------

**[display system internal arp statistics**]命令用来显示指定板ARP统计信息。

【命令】

集中式设备：

**[display system internal arp statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal arp statistics** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal arp statistics** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的ARP统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ARP统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ARP统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的ARP统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的ARP统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的ARP统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**ARP \-- ARP Probe命令 \-- display system internal arp suppression xconnect-group verbose**

------------------------------------------------------------------------

**[display system internal arp suppression xconnect-group verbose**]命令用来显示ARP泛洪抑制表项的详细信息。

【命令】

集中式设备：

**[display system internal arp suppression xconnect-group verbose**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal arp suppression xconnect-group verbose ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal arp suppression** **xconnect-group verbose** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的ARP泛洪抑制表项的详细信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的ARP泛洪抑制表项的详细信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ARP泛洪抑制表项的详细信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上的ARP泛洪抑制表项的详细信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ARP泛洪抑制表项的详细信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的ARP泛洪抑制表项的详细信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的ARP泛洪抑制表项的详细信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的ARP泛洪抑制表项的详细信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的ARP泛洪抑制表项的详细信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上的ARP泛洪抑制表项的详细信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的ARP泛洪抑制表项的详细信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**ARP \-- ARP Probe命令 \-- display system internal arp vlan**

------------------------------------------------------------------------

**[display system internal arp vlan**]命令用来显示指定VLAN的ARP表项信息或表项个数。

【命令】

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal arp vlan*** vlan-id*** slot ***slot-number***** **cpu** *cpu-number* ]  **count**

分布式设备---IRF模式：

**[display system internal arp vlan ***vlan-id*** chassis ***chassis-number*** slot ***slot-number***** **cpu** *cpu-number* ]  **count**

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-id***:**]用来显示指定VLAN的ARP表项信息或表项个数。

**[slot ***slot-number*]：显示指定单板指定VLAN的ARP表项信息或表项个数，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备指定VLAN的ARP表项信息或表项个数，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX指定VLAN的ARP表项信息或表项个数，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板指定VLAN的ARP表项信息或表项个数，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板指定VLAN的ARP表项信息或表项个数。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU指定VLAN的ARP表项信息或表项个数。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[count**]：用来显示ARP表项个数。

**ARP \-- ARP Probe命令 \-- reset system internal arp statistics**

------------------------------------------------------------------------

**[reset system internal arp statistics**]命令用来清除指定板上的ARP统计信息。

【命令】

集中式设备：

**[reset system internal arp statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal arp statistics slot ***slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[reset system internal arp statistics** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：清除指定单板的ARP统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：清除指定成员设备的ARP统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：清除指定成员设备/PEX的ARP统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：清除指定成员设备上指定单板的ARP统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：清除指定单板的ARP统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU的ARP统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）
