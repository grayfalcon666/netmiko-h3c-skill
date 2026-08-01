<!-- CMD-INDEX
  display system internal evi flooding | Probe视图          | L11
  display system internal evi selective-flooding | Probe视图          | L57
  display system internal evi statistics | Probe视图          | L103
  display system internal evi vlan-mapping | Probe视图          | L141
  display system internal evi vlan-status | Probe视图          | L189
  display system internal eviisis status | Probe视图          | L233
  display system internal evi-link data | Probe视图          | L253
-->

**EVI \-- EVI Probe命令 \-- display system internal evi flooding**

------------------------------------------------------------------------

**[display system internal evi flooding**]命令用来显示EVI泛洪功能信息。

【命令】

集中式设备：

**[display system internal evi flooding** **interface** *interface-type interface-number*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal evi flooding interface** *interface-type interface-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal evi flooding interface** *interface-type interface-number* **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的EVI泛洪功能信息。

**[slot*** slot-number*]：显示指定单板的EVI泛洪功能信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的EVI泛洪功能信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的EVI泛洪功能信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的EVI泛洪功能信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的EVI泛洪功能信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的EVI泛洪功能信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**EVI \-- EVI Probe命令 \-- display system internal evi selective-flooding**

------------------------------------------------------------------------

**[display system internal evi selective-flooding**]命令用来显示EVI保存的指定EVI隧道接口下指定泛洪MAC在指定VLAN的下发驱动信息。

【命令】

集中式设备：

**[display system internal evi selective-flooding interface tunnel*** interface-number***mac-address ***mac-address*** vlan ***vlan-id*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal evi selective-flooding interface tunnel*** interface-number***mac-address ***mac-address*** vlan ***vlan-id*** slot**]*****slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal evi selective-flooding interface tunnel*** interface-number***mac-address ***mac-address*** vlan ***vlan-id*** chassis** *chassis-number* **slot**]*****slot-number * **cpu** *cpu-number*

【视图】

Probe视图

【支持的缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface tunnel*** interface-number*]：指定EVI隧道接口。

**[mac-address ***mac-address*]：指定泛洪MAC。

**[vlan ***vlan-id*]：指定VLAN。*vlan-id*表示VLAN编号，取值范围为1～4094。

**[slot** *slot-number*]：显示指定单板的EVI保存的指定EVI隧道接口下指定泛洪MAC在指定VLAN的下发驱动信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的EVI保存的指定EVI隧道接口下指定泛洪MAC在指定VLAN的下发驱动信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的EVI保存的指定EVI隧道接口下指定泛洪MAC在指定VLAN的下发驱动信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上EVI保存的指定EVI隧道接口下指定泛洪MAC在指定VLAN的下发驱动信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**EVI \-- EVI Probe命令 \-- display system internal evi statistics**

------------------------------------------------------------------------

**[display system internal evi statistics**]命令用来显示EVI的统计信息。

【命令】

集中式设备：

**[display system internal evi statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal evi statistics slot**]*****slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal evi statistics chassis** *chassis-number* **slot**]*****slot-number * **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定单板的EVI统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的EVI统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的EVI统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**EVI \-- EVI Probe命令 \-- display system internal evi vlan-mapping**

------------------------------------------------------------------------

**[display system internal evi vlan-mapping**]命令用来显示EVI的VLAN映射信息。

【命令】

集中式设备：

**[display system internal evi vlan-mapping vlan** *vlan-id* **interface** *interface-type interface-number*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal evi vlan-mapping vlan** *vlan-id* **interface** *interface-type interface-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal evi vlan-mapping vlan** *vlan-id* **interface** *interface-type interface-number* **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-id*]：显示指定本地VLAN的VLAN映射信息。v*lan-id*表示VLAN编号，取值范围为1～4094。

**[interface** *interface-type interface-number*]：显示指定接口的VLAN映射信息。

**[slot** *slot-number*]：显示指定单板的VLAN映射信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的VLAN映射信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的VLAN映射信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的VLAN映射信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的VLAN映射信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的VLAN映射信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**EVI \-- EVI Probe命令 \-- display system internal evi vlan-status**

------------------------------------------------------------------------

**[display system internal evi vlan-status**]命令用来显示EVI保存的指定EVI隧道接口下的VLAN下发驱动信息。

【命令】

集中式设备：

**[display system internal evi vlan-status interface tunnel*** interface-number*** vlan ***vlan-id*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal evi vlan-status interface tunnel*** interface-number*** vlan ***vlan-id*** slot**]*****slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal evi vlan-status interface tunnel*** interface-number*** vlan ***vlan-id*** chassis** *chassis-number* **slot**]*****slot-number * **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface tunnel*** interface-number*]：指定EVI隧道接口。

**[vlan ***vlan-id*]：指定VLAN。*vlan-id*表示VLAN编号，取值范围为1～4094。

**[slot** *slot-number*]：显示指定单板的EVI保存的VLAN下发驱动信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的EVI保存的VLAN下发驱动信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的EVI保存的VLAN下发驱动信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上EVI保存的VLAN下发驱动信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**EVI \-- EVI Probe命令 \-- display system internal eviisis status**

------------------------------------------------------------------------

**[display system internal eviisis status**]命令用来显示EVI IS-IS进程的状态信息。

【命令】

**[display system internal eviisis status**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**EVI \-- EVI Probe命令 \-- display system internal evi-link data**

------------------------------------------------------------------------

**[display system internal evi-link data**]命令用来显示EVI-Link接口内核数据信息。

【命令】

集中式设备：

**[display system internal evi-link data interface evi-link** *number* [ **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal evi-link data interface evi-link** *number* [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal evi-link data interface evi-link** *number* [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface evi-link ***number*]：显示指定EVI-Link接口的内核数据信息。*number*表示EVI-Link接口编号，取值为已创建的EVI-Link接口编号。

**[slot** *slot-number*]：显示指定单板的EVI-Link接口内核数据信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示主用主控板的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的EVI-Link接口内核数据信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，则显示主成员设备的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的EVI-Link接口内核数据信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，则显示主成员设备的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的EVI-Link接口内核数据信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示全局主用主控板的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的EVI-Link接口内核数据信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，则显示全局主用主控板的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的EVI-Link接口内核数据信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

