<!-- CMD-INDEX
  display system internal mac-address configuration | Probe视图          | L9
  display system internal mac-address learned | Probe视图          | L63
  display system internal mac-address protocol | Probe视图          | L121
  display system internal mac-address statistics | Probe视图          | L179
  reset system internal mac-address statistics | Probe视图          | L223
-->

**MAC地址表 \-- MAC地址Probe命令 \-- display system internal mac-address configuration**

------------------------------------------------------------------------

**[display system internal mac-address configuration**]命令用来显示MAC地址表的配置信息。

【命令】

集中式设备：

**[display system internal mac-address configuration **[{ **blackhole \| multiport \| multicast \| static** } [ **count** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mac-address configuration **[{ **blackhole \| multiport \| multicast \| static** } [ **count** ] **slot** ]*slot-number * **cpu**]* cpu-number*****

分布式设备－IRF模式：

**[display system internal mac-address configuration **[{ **blackhole \| multiport \| multicast \| static** } [ **count** ] **chassis** *chassis-number* ]**slot**]*****slot-number * **cpu*** cpu-number*****

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[blackhole**]：显示黑洞MAC地址表项。

**[multiport**]：显示多端口单播MAC地址表项。本参数的支持情况与设备的型号有关，请以设备的实际情况为准

**[multicast**]：显示组播MAC地址表项。本参数的支持情况与设备的型号有关，请以设备的实际情况为准

**[static**]：显示静态MAC地址表项。

**[count**]：显示MAC地址表项的数量。如果配置本参数，将仅显示符合条件的（由**count**前面的参数决定）MAC地址表项的数量，而不显示MAC地址表项的具体内容。如果不指定本参数，则显示符合条件的MAC地址表的具体内容。

**[slot** *slot-number*]：显示指定单板的MAC地址信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的MAC地址信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的MAC地址信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的MAC地址信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的MAC地址信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的MAC地址信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MAC地址表 \-- MAC地址Probe命令 \-- display system internal mac-address learned**

------------------------------------------------------------------------

![说明](MAC地址表Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal mac-address learned**]命令用来显示动态MAC地址表项。

【命令】

集中式设备：

**[display system internal mac-address learned **[ *mac-address* [ **vlan** *vlan-id*  \|  **interface** *interface-type interface-number*   **vlan** *vlan-id*   **count**  ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mac-address learned** [ *mac*-*address* [ **vlan** *vlan-id*  \|  **interface** *interface-type interface-number*   **vlan** *vlan-id*   **count**  ] **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal mac-address learned** [ *mac*-*address* [ **vlan** *vlan-id*  \|  **interface** *interface-type interface-number*   **vlan** *vlan-id*   **count**  ] **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac*-*address*]：显示指定MAC地址的动态MAC地址表项，*mac*-*address*的格式为H-H-H。在配置时，用户可以省去MAC地址中每段开头的"0"，例如输入"f-e2-1"即表示输入的MAC地址为"000f-00e2-0001"。

**[vlan ***vlan*-*id*]：显示指定VLAN的动态MAC地址表项。*vlan*-*id*的取值范围为1～4094。

**[interface** *interface-type interface-number*]：显示指定接口的动态MAC地址表项。*interface-type interface-number*为接口类型和接口编号。

**[count**]：显示动态MAC地址表项的数量。如果配置本参数，将仅显示符合条件的（由**count**前面的参数决定）动态MAC地址表项的数量，而不显示动态MAC地址表项的具体内容。如果不指定本参数，则显示符合条件的动态MAC地址表项的具体内容。

**[slot** *slot-number*]：显示指定单板的动态MAC地址表项。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的动态MAC地址表项。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的动态MAC地址表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的动态MAC地址表项*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的动态MAC地址表项*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的动态MAC地址表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MAC地址表 \-- MAC地址Probe命令 \-- display system internal mac-address protocol**

------------------------------------------------------------------------

**[display system internal mac-address protocol**]命令用来显示指定协议或特性生成的MAC地址或VLAN接口的MAC地址。

【命令】

集中式设备：

**[display system internal mac-address protocol **[[ **auth** \| **dot1x** \| **ead** \| **evb** \| **security** \| **vlan-interface** \| **voice-vlan** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mac-address protocol **[[ **auth** \| **dot1x** \| **ead** \| **evb** \| **security** \| **vlan-interface** \| **voice-vlan** ] **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal mac-address protocol**[ [ **auth** \| **dot1x** \| **ead** \| **evb** \| **security** \| **vlan-interface** \| **voice-vlan** ] **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auth**]：显示MAC地址认证特性的MAC地址表项。

**[dot1x**]：显示802.1X特性的MAC地址表项。

**[ead**]：显示EAD特性的MAC地址表项。

**[evb**]：显示EVB特性的MAC地址表项。

**[security**]：显示端口安全特性中学习到的MAC地址表项。

**[vlan-interface**]：显示VLAN接口的MAC地址表项。

**[voice-vlan**]：显示Voice VLAN特性的MAC地址表项。

**[slot** *slot-number*]：显示指定单板的MAC地址表项。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的MAC地址表项。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的MAC地址表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的MAC地址表项*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的MAC地址表项*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的MAC地址表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MAC地址表 \-- MAC地址Probe命令 \-- display system internal mac-address statistics**

------------------------------------------------------------------------

**[display system internal mac-address statistics**]命令用来显示MAC地址表的统计信息。

【命令】

集中式设备：

**[display system internal mac-address statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mac-address statistics slot ***slot-number * **cpu**]* cpu-number*****

分布式设备－IRF模式：

**[display system internal mac-address statistics chassis*** chassis-number***slot**]*****slot-number * **cpu*** cpu-number*****

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定单板的MAC地址表统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的MAC地址表统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的MAC地址表统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的MAC地址表统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的MAC地址表统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的MAC地址表的统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**MAC地址表 \-- MAC地址Probe命令 \-- reset system internal mac-address statistics**

------------------------------------------------------------------------

**[reset system internal mac-address statistics**]命令用来清除MAC地址表的统计信息

【命令】

集中式设备：

**[reset system internal mac-address statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal mac-address statistics slot**]*****slot-number * **cpu*** cpu-number*****

分布式设备－IRF模式：

**[reset system internal mac-address statistics chassis** *chassis-number* **slot**]*****slot-number * **cpu*** cpu-number*****

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：清除指定单板的MAC地址表统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：清除指定成员设备的MAC地址表统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：清除指定成员设备/PEX的MAC地址表统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的MAC地址表统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板的MAC地址表统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU的MAC地址表统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。
