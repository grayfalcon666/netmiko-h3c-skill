
**VXLAN \-- VXLAN Probe命令 \-- debugging system internal overlay mac-address**

------------------------------------------------------------------------

**[debugging system internal overlay mac-address**]命令用来打开Overlay MAC地址的调试信息开关。

**[undo debugging system internal overlay mac-address**]命令用来关闭Overlay MAC地址的调试信息开关。

【命令】

**[debugging system internal overlay mac-address **[{ **all** \| **event** \| **hardware** \| **isis** }]]

**[undo debugging system internal overlay mac-address **[{ **all** \| **event** \| **hardware** \| **isis** }]]

【缺省情况】

Overlay MAC地址的调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示Overlay MAC地址的所有调试信息开关。

**[event**]：表示Overlay MAC地址的事件调试信息开关。

**[hardware**]：表示Overlay MAC地址的下驱动调试信息开关。

**[isis**]：表示Overlay MAC地址的ISIS相关调试信息开关。

**VXLAN \-- VXLAN Probe命令 \-- display system internal multicast tunnel nexthop**

------------------------------------------------------------------------

**[display system internel multicast tunnel nexthop**]命令用来显示VXLAN组播隧道的下一跳表项信息。

【命令】

集中式设备：

**[display system internal multicast**[ **tunnel nexthop** [ *source-address* [ **mask** { *mask-length* \| *mask* } ] \| *group-address* [ **mask** { *mask-length* \| *mask* } ] \| **mtunnel** *tunnel-number* \| **outgoing-interface** *interface-type interface-number* ] \*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal multicast**[ **tunnel nexthop** [ *source-address* [ **mask** { *mask-length* \| *mask* } ] \| *group-address* [ **mask** { *mask-length* \| *mask* } ] \| **mtunnel** *tunnel-number* \| **outgoing-interface** *interface-type interface-number* \| **slot** *slot-number*  **cpu** *cpu-number*  ] \*]]

分布式设备－IRF模式：

**[display system internal multicast**[ **tunnel nexthop** [ *source-address* [ **mask** { *mask-length* \| *mask* } ] \| *group-address* [ **mask** { *mask-length* \| *mask* } ] \| **mtunnel** *tunnel-number* \| **outgoing-interface** *interface-type interface-number* \| **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ] \*]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[source-address*]：源地址，这里指到达下一跳的出接口地址。

*[group-address*]：组播组地址，取值范围为224.0.0.0～239.255.255.255。

*[mask-length*]：指定组播组地址或下一跳出接口地址的掩码长度。对于组播组地址，取值范围为4～32，缺省值为32；对于下一跳出接口地址，取值范围为0～32，缺省值为32。

*[mask*]：指定组播组地址或下一跳出接口地址的掩码，缺省值为255.255.255.255。

**[mtunnel ***tunnel-number*]：显示指定组播隧道的下一跳表项。*tunnel-number*为组播隧道的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[outgoing-interface** *interface-type interface-number*]：显示指定出接口的下一跳表项。*interface-type interface-number*为出接口的接口类型和接口编号。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**VXLAN \-- VXLAN Probe命令 \-- display system internal overlay arp suppression**

------------------------------------------------------------------------

**[display system internal overlay arp suppression**]命令用来显示ARP泛洪抑制信息。

【命令】

集中式设备：

**[display system internal overlay arp suppression vsi ***vsi-name*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal overlay arp suppression vsi ***vsi-name***** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal overlay arp suppression vsi ***vsi-name***** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsi*** vsi-name*]：显示指定VSI内的ARP泛洪抑制信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。

**[slot**]*slot-number*：显示指定单板上的ARP泛洪抑制信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的ARP泛洪抑制信息。（分布式设备－独立运行模式）

**[slot**]*slot-number*：显示指定成员设备上的ARP泛洪抑制信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示主设备上的ARP泛洪抑制信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的ARP泛洪抑制信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示主设备上的ARP泛洪抑制信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备指定单板上的ARP泛洪抑制信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的ARP泛洪抑制信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ARP泛洪抑制信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示全局主用主控板上的ARP泛洪抑制信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**VXLAN \-- VXLAN Probe命令 \-- display system internal overlay flooding**

------------------------------------------------------------------------

**[display system internal overlay flooding**]命令用来显示泛洪模式状态。

【命令】

集中式设备：

**[display system internal overlay flooding vsi ***vsi-name*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal overlay flooding vsi ***vsi-name***** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal overlay flooding vsi ***vsi-name***** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsi*** vsi-name*]：显示指定VSI内的泛洪模式状态。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。

**[slot**]*slot-number*：显示指定单板上的泛洪模式状态。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的泛洪模式状态。（分布式设备－独立运行模式）

**[slot**]*slot-number*：显示指定成员设备上的泛洪模式状态。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示主设备上的泛洪模式状态。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的泛洪模式状态。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示主设备上的泛洪模式状态。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备指定单板上的泛洪模式状态。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的泛洪模式状态。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的泛洪模式状态。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示全局主用主控板上的泛洪模式状态。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**VXLAN \-- VXLAN Probe命令 \-- display system internal overlay mac-address**

------------------------------------------------------------------------

**[display system internal overlay mac-address**]命令用来显示远端MAC地址表项。

【命令】

集中式设备：

**[display system internal overlay mac-address **[[ **isis-learned** \| **static** \| **openflow** ]  **interface tunnel** *tunnel-number*   **vsi** *vsi-name*   **count** ]]

**[display system internal overlay mac-address ***mac-address***** **vsi** *vsi-name* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal overlay mac-address **[[ **isis-learned** \| **static** \| **openflow** ]  **interface tunnel** *tunnel-number*   **vsi** *vsi-name*   **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

**[display system internal overlay mac-address ***mac-address***** **vsi** *vsi-name* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal overlay mac-address **[[ **isis-learned** \| **static** \| **openflow** ]  **interface tunnel** *tunnel-number*   **vsi** *vsi-name*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

**[display system internal overlay mac-address ***mac-address***** **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[isis-learned**]：显示通过IS-IS协议学习的远端MAC地址表项。

**[static**]：显示远端静态MAC地址表项。

**[openflow**]：显示通过OpenFlow下发的远端MAC地址表项。

**[interface tunnel*** tunnel-number*]：显示与指定VXLAN隧道接口对应的远端MAC地址表项。*tunnel-number*为VXLAN隧道接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[vsi*** vsi-name*]：显示指定VSI内的远端MAC地址表项。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。

**[count**]：显示远端MAC地址表项的数量。如果指定本参数，则仅显示符合条件的（由**count**前面的参数决定）远端MAC地址表项的数量，而不显示远端MAC地址表项的具体内容。如果不指定本参数，则显示符合条件的远端MAC地址表项的具体内容。

*[mac*-]*address*：显示指定MAC地址的远端MAC地址表项。*mac*-*address*的格式为H-H-H。在配置时，用户可以省去MAC地址中每段开头的"0"，例如输入"f-e2-1"即表示输入的MAC地址为"000f-00e2-0001"。

**[slot**]*slot-number*：显示指定单板上的远端MAC地址表项。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的远端MAC地址表项。（分布式设备－独立运行模式）

**[slot**]*slot-number*：显示指定成员设备上的远端MAC地址表项。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示主设备上的远端MAC地址表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的远端MAC地址表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示主设备上的远端MAC地址表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备上指定单板的远端MAC地址表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的远端MAC地址表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的远端MAC地址表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示全局主用主控板上的远端MAC地址表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**VXLAN \-- VXLAN Probe命令 \-- display system internal overlay selective-flooding mac-address**

------------------------------------------------------------------------

**[display system internal overlay selective-flooding mac-address**]命令用来显示泛洪MAC地址表项。

【命令】

集中式设备：

**[display system internal overlay selective-flooding mac-address ** *mac-address* ]  **vsi** *vsi-name*

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal overlay selective-flooding mac-address ** *mac-address* ]  **vsi** *vsi-name*   **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal overlay selective-flooding mac-address ** *mac-address* ]  **vsi** *vsi-name*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac*-*address*]：显示指定MAC地址的泛洪MAC地址表项。*mac*-*address*的格式为H-H-H。在配置时，用户可以省去MAC地址中每段开头的"0"，例如输入"f-e2-1"即表示输入的MAC地址为"000f-00e2-0001"。

**[vsi*** vsi-name*]：显示指定VSI下的泛洪MAC地址表项。

**[slot** *slot-number*]：显示指定单板的泛洪MAC地址表项。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示主控板的泛洪MAC地址表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的泛洪MAC地址表项。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示主设备上的泛洪MAC地址表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的泛洪MAC地址表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示主设备上的泛洪MAC地址表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的泛洪MAC地址表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的泛洪MAC地址表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的泛洪MAC地址表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示全局主用主控板上的泛洪MAC地址表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**VXLAN \-- VXLAN Probe命令 \-- display system internal overlaymac statistics**

------------------------------------------------------------------------

**[display system internal overlaymac statistics**]命令用来显示OverlayMAC模块的统计信息。

【命令】

集中式设备：

**[display system internal overlaymac statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal overlaymac statistics** * *[ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal overlaymac statistics**** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定单板的OverlayMAC模块的统计信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示主控板的OverlayMAC模块的统计信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的OverlayMAC模块的统计信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示主设备上的OverlayMAC模块的统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的OverlayMAC模块的统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示主设备上的OverlayMAC模块的统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的OverlayMAC模块的统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的OverlayMAC模块的统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的OverlayMAC模块的统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示全局主用主控板上的OverlayMAC模块的统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**VXLAN \-- VXLAN Probe命令 \-- display system internal vxlan forwarding tunnel**

------------------------------------------------------------------------

**[display system internal vxlan forwarding tunnel**]命令用来显示VXLAN隧道的转发信息。

【命令】

集中式设备：

**[display system internal vxlan forwarding tunnel** [ **vxlan-id** *vxlan-id* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal vxlan forwarding tunnel** [ **vxlan-id** *vxlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal vxlan forwarding tunnel** [ **vxlan-id** *vxlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vxlan-id*** vxlan-id*]：显示指定VXLAN的隧道转发信息。*vxlan-id*为VXLAN的编号，取值范围为0～16777215。不指定此参数，则显示所有VXLAN的隧道转发信息。

**[slot**]*slot-number*：显示指定单板上的VXLAN隧道转发信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的VXLAN隧道转发信息。（分布式设备－独立运行模式）

**[slot**]*slot-number*：显示指定成员设备上的VXLAN隧道转发信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示主设备上的VXLAN隧道转发信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的VXLAN隧道转发信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示主设备上的VXLAN隧道转发信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备指定单板上的VXLAN隧道转发信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的VXLAN隧道转发信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的VXLAN隧道转发信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示全局主用主控板上的VXLAN隧道转发信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的VXLAN隧道转发信息。只有指定的**slot**支持多CPU时，才能配置该参数。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**VXLAN \-- VXLAN Probe命令 \-- display system internal vxlan isis status**

------------------------------------------------------------------------

**[display system internal vxlan isis status**]命令用来显示VXLAN IS-IS进程的状态。

【命令】

**[display system internal vxlan isis status**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**VXLAN \-- VXLAN Probe命令 \-- reset system internal overlaymac statistics**

------------------------------------------------------------------------

**[reset system internal overlaymac statistics**]命令用来清除OverlayMAC模块的统计信息。

【命令】

**[reset system internal overlaymac statistics**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

