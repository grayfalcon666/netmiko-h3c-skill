
**IP组播 \-- IP组播Probe命令 \-- debugging system internal igmp-snooping fsm tracing**

------------------------------------------------------------------------

**[debugging** **system** **internal** **igmp-snooping** **fsm** **tracing**]命令用来打开IGMP Snooping状态机的Trace日志调试信息开关。

**[undo** **debugging** **system** **internal** **igmp-snooping** **fsm** **tracing**]命令用来关闭IGMP Snooping状态机的Trace日志调试信息开关。

【命令】

集中式设备：

**[debugging** **system** **internal** **igmp-snooping** **fsm** **tracing** [ **vlan** *vlan-id* [ *group-address* *source-address*  ]  **cpu** *cpu-number* ]]

**[undo** **debugging** **system** **internal** **igmp-snooping** **fsm** **tracing**]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging** **system** **internal** **igmp-snooping** **fsm** **tracing** [ **vlan** *vlan-id* [ *group-address* *source-address*  ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo** **debugging** **system** **internal** **igmp-snooping** **fsm** **tracing**]

分布式设备－IRF模式：

**[debugging** **system** **internal** **igmp-snooping** **fsm** **tracing** [ **vlan** *vlan-id* [ *group-address* *source-address*  ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo** **debugging** **system** **internal** **igmp-snooping** **fsm** **tracing**]

【缺省情况】

IGMP Snooping状态机的Trace日志调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan** *vlan-id*]：输出指定VLAN内的信息，*vlan-id*表示VLAN的编号，取值范围为1～4094。如果未指定本参数，将输出所有VLAN内的信息。

*[group-address*]：输出指定组播组的信息。如果未指定本参数，将输出所有组播组的信息。

*[source-address*]：输出指定组播源的信息。如果未指定本参数，将输出所有组播源的信息。

**[slot** *slot-number*]：输出指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将输出主控板上的信息。（分布式设备－独立运行模式）]

**[slot** *slot-number*]：输出指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将输出主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：输出指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将输出主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：输出指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将输出全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：输出指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将输出全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：输出指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- debugging system internal mld-snooping fsm tracing**

------------------------------------------------------------------------

**[debugging** **system** **internal** **mld-snooping** **fsm** **tracing**]命令用来打开MLD Snooping状态机的Trace日志调试信息开关。

**[undo** **debugging** **system** **internal** **mld-snooping** **fsm** **tracing**]命令用来关闭MLD Snooping状态机的Trace日志调试信息开关。

【命令】

集中式设备：

**[debugging** **system** **internal** **mld-snooping** **fsm** **tracing** [ **vlan** *vlan-id* [ *ipv6-group-address* *ipv6-source-address*  ]  **cpu** *cpu-number* ]]

**[undo** **debugging** **system** **internal** **mld-snooping** **fsm** **tracing**]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging** **system** **internal** **mld-snooping** **fsm** **tracing** [ **vlan** *vlan-id* [ *ipv6-group-address* *ipv6-source-address*  ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo** **debugging** **system** **internal** **mld-snooping** **fsm** **tracing**]

分布式设备－IRF模式：

**[debugging** **system** **internal** **mld-snooping** **fsm** **tracing** [ **vlan** *vlan-id* [ *ipv6-group-address* *ipv6-source-address*  ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo** **debugging** **system** **internal** **mld-snooping** **fsm** **tracing**]

【缺省情况】

MLD Snooping状态机的Trace日志调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan** *vlan-id*]：输出指定VLAN内的信息，*vlan-id*表示VLAN的编号，取值范围为1～4094。如果未指定本参数，将输出所有VLAN内的信息。

**[group** *ipv6-group-address*]：输出指定IPv6组播组的信息。如果未指定本参数，将输出所有IPv6组播组的信息。

**[source** *ipv6-source-address*]：输出指定IPv6组播源的信息。如果未指定本参数，将输出所有IPv6组播源的信息。

**[slot** *slot-number*]：输出指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将输出主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：输出指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将输出主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：输出指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将输出主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：输出指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将输出全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：输出指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将输出全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：输出指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal igmp user-authorization record**

------------------------------------------------------------------------

![说明](IP组播Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **system** **internal** **igmp** **user-authorization** **record**]命令用来显示按用户记录的认证模块通知给IGMP进程的消息数。

【命令】

**[display** **system** **internal** **igmp** **user-authorization** **record**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP组播 \-- IP组播Probe命令 \-- display system internal igmp user-authorization statistics**

------------------------------------------------------------------------

![说明](IP组播Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **system** **internal** **igmp** **user-authorization** **statistics**]命令用来显示按认证类型记录的认证模块通知给IGMP进程的消息数。

【命令】

**[display** **system** **internal** **igmp** **user-authorization** **statistics**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 l2-multicast ip forwarding verbose**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **l2-multicast** **ip** **forwarding** **verbose**]命令用来显示IPv6二层组播的IP转发表详细信息。

【命令】

集中式设备：

**[display**[ **system** **internal** **ipv6** **l2-multicast** **ip** **forwarding** **verbose** [ **group** *ipv6-group-address* \| **source** *ipv6-source-address* ] \*  **vlan** *vlan-id*   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **system** **internal** **ipv6** **l2-multicast** **ip** **forwarding** **verbose** [ **group** *ipv6-group-address* \| **source** *ipv6-source-address* ] \*  **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display**[ **system** **internal** **ipv6** **l2-multicast** **ip** **forwarding** **verbose** [ **group** *ipv6-group-address* \| **source** *ipv6-source-address* ] \*  **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[group** *ipv6-group-address*]：显示指定IPv6组播组的信息。如果未指定本参数，将显示所有IPv6组播组的信息。

**[source*** ipv6-source-address*]：显示指定IPv6组播源的信息。如果未指定本参数，将显示所有IPv6组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 l2-multicast ip verbose**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **l2-multicast** **ip** **verbose**]命令用来显示IPv6二层组播的IP组播组详细信息。

【命令】

集中式设备：

**[display**[ **system** **internal** **ipv6** **l2-multicast** **ip** **verbose** [ **group** *ipv6-group-address* \| **source** *ipv6-source-address*] \*  **vlan** *vlan-id*   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **system** **internal** **ipv6** **l2-multicast** **ip** **verbose** [ **group** *ipv6-group-address* \| **source** *ipv6-source-address*] \*  **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display**[ **system** **internal** **ipv6** **l2-multicast** **ip** **verbose** [ **group** *ipv6-group-address* \| **source** *ipv6-source-address*] \*  **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[group** *ipv6-group-address*]：显示指定IPv6组播组的信息。如果未指定本参数，将显示所有IPv6组播组的信息。

**[source*** ipv6-source-address*]：显示指定IPv6组播源的信息。如果未指定本参数，将显示所有IPv6组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 l2-multicast ipc statistics**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **l2-multicast** **ipc** **statistics**]命令用来显示IPv6二层组播板间消息的统计信息。

【命令】

集中式设备：

**[display** **system** **internal** **ipv6** **l2-multicast** **ipc** **statistics** [ **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **system** **internal** **ipv6** **l2-multicast** **ipc** **statistics** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display** **system** **internal** **ipv6** **l2-multicast** **ipc** **statistics** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果[未指定本参数，将显示主设备上的信息。（集中式]IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 l2-multicast mac forwarding verbose**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **l2-multicast** **mac** **forwarding** **verbose**]命令用来显示IPv6二层组播的MAC转发表详细信息。

【命令】

集中式设备：

**[display** **system** **internal** **ipv6** **l2-multicast** **mac** **forwarding** **verbose** [ *mac-address*   **vlan** *vlan-id*   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **system** **internal** **ipv6** **l2-multicast** **mac** **forwarding** **verbose** [ *mac-address*   **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display** **system** **internal** **ipv6** **l2-multicast** **mac** **forwarding** **verbose** [ *mac-address*   **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：显示指定MAC组播组的信息。如果未指定本参数，将显示所有MAC组播组的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 l2-multicast mac verbose**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **l2-multicast** **mac** **verbose**]命令用来显示IPv6二层组播的MAC组播组详细信息。

【命令】

集中式设备：

**[display** **system** **internal** **ipv6** **l2-multicast** **mac** **verbose** [ *mac-address*   **vlan** *vlan-id*   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **system** **internal** **ipv6** **l2-multicast** **mac** **verbose** [ *mac-address*   **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display** **system** **internal** **ipv6** **l2-multicast** **mac** **verbose** [ *mac-address*   **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：显示指定MAC组播组的信息。如果未指定本参数，将显示所有MAC组播组的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 l2-multicast trill-offload-table**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **l2-multicast** **trill-offload-table**]命令用来显示IPv6二层组播维护的TRILL表项信息。

【命令】

集中式设备：

**[display**[ **system** **internal** **ipv6** **l2-multicast** **trill-offload-table** [ **local** \| **remote** ]  **vlan** *vlan-id* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **system** **internal** **ipv6** **l2-multicast** **trill-offload-table** [ **local** \| **remote** ]  **vlan** *vlan-id*   **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display**[ **system** **internal** **ipv6** **l2-multicast** **trill-offload-table** [ **local** \| **remote** ]  **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：显示入表项信息。

**[remote**]：显示出表项信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 mrib interface statistics**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **mrib** **interface** **statistics**]命令用来显示IPv6MRIB所维护接口的统计信息，这些接口包括配置了IPv6 PIM、MLD等IPv6组播协议的接口以及注册接口、InLoopBack0接口、Null0接口等内部接口。

【命令】

**[display** **system** **internal** **ipv6** **mrib** [ **vpn-instance** *vpn-instance-name*  **interface** **statistics**]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 mrib mbr**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **mrib** **mbr** **interface**]命令用来显示IPv6 MRIB进程中MBR（Multicast Border Router，组播边界路由器）模块维护的组加入信息。

【命令】

**[display** **system** **internal** **ipv6** **mrib** [ **vpn-instance** *vpn-instance-name*  **mbr** **interface** *interface-type* *interface-number*  **source** *ipv6-source-address* **group** *ipv6-group-address* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

**[interface** *interface-type* *interface-number*]：显示指定接口上的信息。

**[source** *ipv6-source-address*]：显示指定组播源的信息。如果未指定本参数，将不显示IPv6 MBR表项信息。

**[group** *ipv6-group-address*]：显示指定组播组的信息，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。如果未指定本参数，将不显示IPv6 MBR表项信息。

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 multicast forwarding vlan reference**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **multicast** **forwarding** **vlan** **reference**]命令用来显示VLAN出接口与IPv6二层组播表项之间的映射关系。

【命令】

集中式设备：

**[display**[ **system** **internal** **ipv6** **multicast** **forwarding** **vlan** **reference** [ **group** *ipv6-group-address* \| **source** *ipv6-source-address* ] \*  **vlan** *vlan-id*   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **system** **internal** **ipv6** **multicast** **forwarding** **vlan** **reference** [ **group** *ipv6-group-address* \| **source** *ipv6-source-address* ] \*  **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display**[ **system** **internal** **ipv6** **multicast** **forwarding** **vlan** **reference** [ **group** *ipv6-group-address* \| **source** *ipv6-source-address* ] \*  **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[group** *ipv6-group-address*]：显示指定IPv6组播组的信息。如果未指定本参数，将显示所有IPv6组播组的信息。

**[source** *ipv6-source-address*]：显示指定IPv6组播源的信息。如果未指定本参数，将显示所有IPv6组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 multicast forwarding-table dummy**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **multicast** **forwarding-table** **dummy**]命令用来显示IPv6组播临时转发表的信息。

【命令】

集中式设备：

**[display** **system** **internal** **ipv6** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **dummy**  *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **cpu** *cpu-number* \| **statistics** ] \*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **system** **internal** **ipv6** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **dummy**  *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **statistics** \| **slot** *slot-number*  **cpu** *cpu-number*  ] \*]]

分布式设备－IRF模式：

**[display** **system** **internal** **ipv6** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **dummy**  *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  \| **statistics** ] \*]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[ipv6-source-address*]：显示指定IPv6组播源的信息。如果未指定本参数，将显示所有IPv6组播源的信息。

*[ipv6-group-address*]：显示指定IPv6组播组的信息，取值范围为FFxy::/16，其中x和y均表示0～F的任意一个十六进制数。如果未指定本参数，将显示所有IPv6组播组的信息。

*[prefix-length*]：指定IPv6组播源或IPv6组播组地址的前缀长度。对于IPv6组播源地址，其取值范围为0～128，缺省值为128；对于IPv6组播组地址，其取值范围为8～128，缺省值为128。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[statistics**]：显示统计信息。

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 multicast forwarding-table verbose**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **multicast** **forwarding-table** **verbose**]命令用来显示IPv6组播转发表的详细信息。

【命令】

集中式设备：

**[display** **system** **internal** **ipv6** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **verbose**  *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **cpu** *cpu-number* \| **incoming-interface** *interface-type* *interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* ] \*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **system** **internal** **ipv6** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **verbose**  *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **incoming-interface** *interface-type* *interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* \| **slot** *slot-number*  **cpu** *cpu-number*  ] \*]]

分布式设备－IRF模式：

**[display** **system** **internal** **ipv6** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **verbose**  *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  \| **incoming-interface** *interface-type* *interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* ] \*]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[ipv6-source-address*]：显示指定IPv6组播源的信息。如果未指定本参数，将显示所有IPv6组播源的信息。

*[ipv6-group-address*]：显示IPv6组播组的信息，取值范围为FFxy::/16，其中x和y均表示0～F的任意一个十六进制数。如果未指定本参数，将显示所有IPv6组播组的信息。

*[prefix-length*]：指定IPv6组播源或IPv6组播组地址的前缀长度。对于IPv6组播源地址，其取值范围为0～128，缺省值为128；对于IPv6组播组地址，其取值范围为8～128，缺省值为128。

**[incoming-interface**]：显示指定入接口的信息。如果未指定本参数，将显示所有入接口的信息。

*[interface-type* *interface-number*]：指定接口类型和接口编号。

**[outgoing-interface**]：显示指定出接口的信息。如果未指定本参数，将显示所有出接口的信息。

**[exclude**]：显示不包含指定接口的信息。

**[include**]：显示包含指定接口的信息。

**[match**]：显示包含且仅包含指定接口的信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 multicast-vlan forwarding-table verbose**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **multicast-vlan** **forwarding-table** **verbose**]命令用来显示IPv6组播VLAN转发表的详细信息。

【命令】

集中式设备：

**[display** **system** **internal** **ipv6** **multicast-vlan** **forwarding-table** **verbose** [ *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **cpu** *cpu-number* \| **subvlan** *vlan-id* \| **vlan** *vlan-id* ] \*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **system** **internal** **ipv6** **multicast-vlan** **forwarding-table** **verbose** [ *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **slot** *slot-number*  **cpu** *cpu-number*  \| **subvlan** *vlan-id* \| **vlan** *vlan-id* ] \*]]

分布式设备－IRF模式：

**[display** **system** **internal** **ipv6** **multicast-vlan** **forwarding-table** **verbose** [ *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  \| **subvlan** *vlan-id* \| **vlan** *vlan-id* ] \*]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-source-address*]：显示指定IPv6组播源的信息。如果未指定本参数，将显示所有IPv6组播源的信息。

*[ipv6-group-address*]：显示指定IPv6组播组的信息，取值范围为FFxy::/16，其中x和y均代表0～F的任意一个十六进制数。如果未指定本参数，将显示所有IPv6组播组的信息。

*[prefix-length*]：指定IPv6组播源或IPv6组播组地址的前缀长度。对于IPv6组播源地址，其取值范[围为]0～128，缺省值为128；对于IPv6组播组地址，其取值范围为8～128，缺省值为128。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[subvlan** *vlan-id*]：显示指定子VLAN的信息。如果未指定本参数，将显示所有子VLAN的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 pim interface**

------------------------------------------------------------------------

**[display**]**system** **internal** **ipv6****pim** **interface**命令用来显示IPv6PIM进程中路由管理LIB所维护的接口信息。

【命令】

**[display**]**system** **internal** **ipv6****pim** **vpn-instance** *vpn-instance-name* **interface**[[ *interface-type* *interface-number* [ **address** \| **gateway** \| **prefix**] ] \| *ipv6-address* *prefix-length* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网实例的信息。

*[interface-type* *interface-number*]：显示指定接口的信息。如果未指定本参数，将显示所有接口的信息。

**[address**]：指定IPv6地址。

**[gateway**]：指定IPv6网关。

**[prefix**]：指定IPv6前缀。

*[ipv6-address*]：显示指定IPv6地址的信息。如果未指定本参数，将显示所有IPv6地址的信息。::为保留地址，用户不感知。

*[prefix-length*]：表示前缀长度，取值范围为0～128。

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 pim rp**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **pim** **rp**]命令用来显示IPv6 PIM的RP统计信息。

【命令】

**[display** **system** **internal** **ipv6** **pim** [ **vpn-instance** *vpn-instance-name*  **rp**]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网实例的信息。

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 pim thread**

------------------------------------------------------------------------

**[display** **system** **internal** **ipv6** **pim** **thread**]命令用来显示IPv6 PIM线程的统计信息。

【命令】

**[display**[ **system** **internal** **ipv6** **pim** **thread** { **event** \| **main** \| **route** }]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：显示IPv6 PIM事件线程的统计信息。

**[main**]：显示IPv6 PIM主线程的统计信息。

**[route**]：显示IPv6 PIM路由线程的统计信息。

**IP组播 \-- IP组播Probe命令 \-- display system internal l2-multicast ip forwarding verbose**

------------------------------------------------------------------------

**[display** **system** **internal** **l2-multicast** **ip** **forwarding** **verbose**]命令用来显示二层组播的IP转发表详细信息。

【命令】

集中式设备：

**[display**[ **system** **internal** **l2-multicast** **ip** **forwarding** **verbose** [ **group** *group-address* \| **source** *source-address* ] \*  **vlan** *vlan-id*   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **system** **internal** **l2-multicast** **ip** **forwarding** **verbose** [ **group** *group-address* \| **source** *source-address* ] \*  **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display**[ **system** **internal** **l2-multicast** **ip** **forwarding** **verbose** [ **group** *group-address* \| **source** *source-address* ] \*  **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[group** *group-address*]：显示指定组播组的信息。如果未指定本参数，将显示所有组播组的信息。

**[source*** source-address*]：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果[未指定本参数，将显示主设备上的信息。（集中式]IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal l2-multicast ip verbose**

------------------------------------------------------------------------

**[display** **system** **internal** **l2-multicast** **ip** **verbose**]命令用来显示二层组播的IP组播组详细信息。

【命令】

集中式设备：

**[display**[ **system** **internal** **l2-multicast** **ip** **verbose** [ **group** *group-address* \| **source** *source-address* ] \*  **vlan** *vlan-id*   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **system** **internal** **l2-multicast** **ip** **verbose** [ **group** *group-address* \| **source** *source-address* ] \*  **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display**[ **system** **internal** **l2-multicast** **ip** **verbose** [ **group** *group-address* \| **source** *source-address* ] \*  **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[group** *group-address*]：显示指定组播组的信息。如果未指定本参数，将显示所有组播组的信息。

**[source*** source-address*]：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal l2-multicast ipc statistics**

------------------------------------------------------------------------

**[display**]**system** **internal** **l2-multicast** **ipc** **statistics**命令用来显示二层组播板间消息的统计信息。

【命令】

集中式设备：

**[display**]**system** **internal** **l2-multicast** **ipc** **statistics** [ **cpu** *cpu-number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display**]**system** **internal** **l2-multicast** **ipc** **statistics** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－IRF模式：

**[display**]**system** **internal** **l2-multicast** **ipc** **statistics** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP组播 \-- IP组播Probe命令 \-- display system internal l2-multicast mac forwarding verbose**

------------------------------------------------------------------------

**[display** **system** **internal** **l2-multicast** **mac** **forwarding** **verbose**]命令用来显示二层组播的MAC转发表详细信息。

【命令】

集中式设备：

**[display** **system** **internal** **l2-multicast** **mac** **forwarding** **verbose** [ *mac-address*   **vlan** *vlan-id*   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **system** **internal** **l2-multicast** **mac** **forwarding** **verbose** [ *mac-address*   **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display** **system** **internal** **l2-multicast** **mac** **forwarding** **verbose** [ *mac-address*   **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：显示指定MAC组播组的信息。如果未指定本参数，将显示所有MAC组播组的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal l2-multicast mac verbose**

------------------------------------------------------------------------

**[display** **system** **internal** **l2-multicast** **mac** **verbose**]命令用来显示二层组播的MAC组播组详细信息。

【命令】

集中式设备：

**[display** **system** **internal** **l2-multicast** **mac** **verbose** [ *mac-address*   **vlan** *vlan-id*   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **system** **internal** **l2-multicast** **mac** **verbose** [ *mac-address*   **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display** **system** **internal** **l2-multicast** **mac** **verbose** [ *mac-address*   **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：显示指定MAC组播组的信息。如果未指定本参数，将显示所有MAC组播组的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal l2-multicast trill-offload-table**

------------------------------------------------------------------------

**[display** **system** **internal** **l2-multicast** **trill-offload-table**]命令用来显示二层组播维护的TRILL表项信息。

【命令】

集中式设备：

**[display**[ **system** **internal** **l2-multicast** **trill-offload-table** [ **local** \| **remote** ]  **vlan** *vlan-id* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **system** **internal** **l2-multicast** **trill-offload-table** [ **local** \| **remote** ]  **vlan** *vlan-id*   **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display**[ **system** **internal** **l2-multicast** **trill-offload-table** [ **local** \| **remote** ]  **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：显示入表项信息。

**[remote**]：显示出表项信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**IP组播 \-- IP组播Probe命令 \-- display system internal mld user-authorization record**

------------------------------------------------------------------------

![说明](IP组播Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **system** **internal** **mld** **user-authorization** **record**]命令用来显示按用户记录的认证模块通知给MLD进程的消息数。

【命令】

**[display** **system** **internal** **mld** **user-authorization** **record**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP组播 \-- IP组播Probe命令 \-- display system internal mld user-authorization statistics**

------------------------------------------------------------------------

![说明](IP组播Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **system** **internal** **mld** **user-authorization** **statistics**]命令用来显示按认证类型记录的认证模块通知给MLD进程的消息数。

【命令】

**[display** **system** **internal** **mld** **user-authorization** **statistics**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP组播 \-- IP组播Probe命令 \-- display system internal mrib interface statistics**

------------------------------------------------------------------------

**[display** **system** **internal** **mrib** **interface** **statistics**]命令用来显示MRIB所维护接口的统计信息，这些接口包括配置了PIM、IGMP等组播协议的接口以及注册接口、InLoopBack0接口、Null0接口等内部接口。

【命令】

**[display** **system** **internal** **mrib** [ **vpn-instance** *vpn-instance-name*  **interface** **statistics**]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

**IP组播 \-- IP组播Probe命令 \-- display system internal mrib mbr**

------------------------------------------------------------------------

**[display** **system** **internal** **mrib** **mbr**]命令用来显示MRIB进程中MBR模块维护的组加入信息。

【命令】

**[display** **system** **internal** **mrib** [ **vpn-instance** *vpn-instance-name*  **mbr** **interface** *interface-type* *interface-number*  **source** *source-address* **group** *group-address* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

**[interface** *interface-type* *interface-number*]：显示指定接口上的信息。

**[source** *source-address*]：显示指定组播源的信息。如果未指定本参数，将不显示MBR表项信息。

**[group** *group-address*]：显示指定组播组的信息，取值范围为224.0.0.0～239.255.255.255。如果未指定本参数，将不显示MBR表项信息。

**IP组播 \-- IP组播Probe命令 \-- display system internal multicast capability**

------------------------------------------------------------------------

**[display** **system** **internal** **multicast** **capability**]命令用来显示组播能力的信息。

【命令】

集中式设备：

**[display** **system** **internal** **multicast** **capability**]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **system** **internal** **multicast** **capability** [ **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display** **system** **internal** **multicast** **capability** [ **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**IP组播 \-- IP组播Probe命令 \-- display system internal multicast forwarding vlan reference**

------------------------------------------------------------------------

**[display** **system** **internal** **multicast** **forwarding** **vlan** **reference**]命令用来显示VLAN出接口与二层组播表项之间的映射关系。

【命令】

集中式设备：

**[display**[ **system** **internal** **multicast** **forwarding** **vlan** **reference** [ **group** *group-address* \| **source** *source-address* ] \*  **vlan** *vlan-id*   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **system** **internal** **multicast** **forwarding** **vlan** **reference** [ **group** *group-address* \| **source** *source-address* ] \*  **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display**[ **system** **internal** **multicast** **forwarding** **vlan** **reference** [ **group** *group-address* \| **source** *source-address* ] \*  **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[group** *group-address*]：显示指定组播组的信息。如果未指定本参数，将显示所有组播组的信息。

**[source** *source-address*]：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal multicast forwarding-table dummy**

------------------------------------------------------------------------

**[display** **system** **internal** **multicast** **forwarding-table** **dummy**]命令用来显示组播临时转发表的信息。

【命令】

集中式设备：

**[display** **system** **internal** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **dummy** [ *group-address* [ **mask** { *mask-length* \| *mask* } ] \| *source-address* [ **mask** { *mask-length* \| *mask* } ] \| **cpu** *cpu-number* \| **statistics** ] \*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **system** **internal** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **dummy** [ *group-address* [ **mask** { *mask-length* \| *mask* } ] \| *source-address* [ **mask** { *mask-length* \| *mask* } ] \| **statistics** \| **slot** *slot-number*  **cpu** *cpu-number*  ] \*]]

分布式设备－IRF模式：

**[display** **system** **internal** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **dummy** [ *group-address* [ **mask** { *mask-length* \| *mask* } ] \| *source-address* [ **mask** { *mask-length* \| *mask* } ] \| **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  \| **statistics** ] \*]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[group-address*]：显示指定组播组的信息，取值范围为224.0.0.0～239.255.255.255。如果未指定本参数，将显示所有组播组的信息。

*[source-address*]：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。

*[mask-length*]：指定组播组或组播源地址的掩码长度。对于组播组地址，其取值范围为4～32，缺省值为32；对于组播源地址，其取值范围为0～32，缺省值为32。

*[mask*]：指定组播组或组播源地址的掩码，缺省值为255.255.255.255。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[statistics**]：显示统计信息。

**IP组播 \-- IP组播Probe命令 \-- display system internal multicast forwarding-table verbose**

------------------------------------------------------------------------

**[display** **system** **internal** **multicast** **forwarding-table** **verbose**]命令用来显示组播转发表的详细信息。

【命令】

集中式设备：

**[display** **system** **internal** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **verbose** [ *group-address* [ **mask** { *mask-length* \| *mask* } ] \| *source-address* [ **mask** { *mask-length* \| *mask* } ] \| **cpu** *cpu-number* \| **incoming-interface** *interface-type* *interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* ] \*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **system** **internal** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **verbose** [ *group-address* [ **mask** { *mask-length* \| *mask* } ] \| *source-address* [ **mask** { *mask-length* \| *mask* } ] \| **incoming-interface** *interface-type* *interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* \| **slot** *slot-number*  **cpu** *cpu-number*  ] \*]]

分布式设备－IRF模式：

**[display** **system** **internal** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **verbose** [ *group-address* [ **mask** { *mask-length* \| *mask* } ] \| *source-address* [ **mask** { *mask-length* \| *mask* } ] \| **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  \| **incoming-interface** *interface-type* *interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* ] \*]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[group-address*]：显示指定组播组的信息，取值范围为224.0.0.0～239.255.255.255。如果未指定本参数，将显示所有组播组的信息。

*[source-address*]：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。

*[mask-length*]：指定组播组或组播源地址的掩码长度。对于组播组地址，其取值范围为4～32，缺省值为32；对于组播源地址，其取值范围为0～32，缺省值为32。

*[mask*]：指定组播组或组播源地址的掩码，缺省值为255.255.255.255。

**[incoming-interface**]：显示指定入接口的信息。如果未指定本参数，将显示所有入接口的信息。

*[interface-type* *interface-number*]：指定接口类型和接口编号。

**[outgoing-interface**]：显示指定出接口的信息。如果未指定本参数，将显示所有出接口的信息。

**[exclude**]：显示不包含指定接口的信息。

**[include**]：显示包含指定接口的信息。

**[match**]：显示包含且仅包含指定接口的信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal multicast record**

------------------------------------------------------------------------

**[display** **system** **internal** **multicast** **record**]命令用来显示组播表项的操作记录。

【命令】

集中式设备：

**[display** **system** **internal** **multicast** **record** [ \| [{ **all** \| **fail** } [ { **group** [ *group-address* \| *ipv6-group-address* ] \| **source** [ *source-address* \| *ipv6-source-address* ] } \* \| **item**]*item-list*[\| **filter** { **exclude** \| **include** } { { **add-l2-ip** \| **add-l2-ip-port** \| **add-l2-ip-slot** \| **add-l2-mac** \| **add-l2-mac-port** \| **add-l2-mac-slot** \| **add-l3-ipm** \| **add-l3-oif** \| **add-l3-port** \| **add-l3-slot** \| **del-l2-ip** \| **del-l2-ip-port** \| **del-l2-ip-slot** \| **del-l2-mac** \| **del-l2-mac-port** \| **del-l2-mac-slot** \| **del-l3-ipm** \| **del-l3-oif** \| **del-l3-port** \| **del-l3-slot** \| **set-l3-iif** } \* \| **ipmc-type-all** } ]  **verbose**  } }  **cpu** *cpu-number* ]

分布式设备－独立运行模式]/集中式IRF设备：

**[display** **system** **internal** **multicast** **record** [ \| [{ **all** \| **fail** } [ { **group** [ *group-address* \| *ipv6-group-address* ] \| **source** [ *source-address* \| *ipv6-source-address* ] } \* \| **item**]*item-list*[\| **filter** { **exclude** \| **include** } { { **add-l2-ip** \| **add-l2-ip-port** \| **add-l2-ip-slot** \| **add-l2-mac** \| **add-l2-mac-port** \| **add-l2-mac-slot** \| **add-l3-ipm** \| **add-l3-oif** \| **add-l3-port** \| **add-l3-slot** \| **del-l2-ip** \| **del-l2-ip-port** \| **del-l2-ip-slot** \| **del-l2-mac** \| **del-l2-mac-port** \| **del-l2-mac-slot** \| **del-l3-ipm** \| **del-l3-oif** \| **del-l3-port** \| **del-l3-slot** \| **set-l3-iif** } \* \| **ipmc-type-all** } ]  **verbose**  } }  **slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－]IRF模式：

**[display** **system** **internal** **multicast** **record** [ \| [{ **all** \| **fail** } [ { **group** [ *group-address* \| *ipv6-group-address* ] \| **source** [ *source-address* \| *ipv6-source-address* ] } \* \| **item**]*item-list*[\| **filter** { **exclude** \| **include** } { { **add-l2-ip** \| **add-l2-ip-port** \| **add-l2-ip-slot** \| **add-l2-mac** \| **add-l2-mac-port** \| **add-l2-mac-slot** \| **add-l3-ipm** \| **add-l3-oif** \| **add-l3-port** \| **add-l3-slot** \| **del-l2-ip** \| **del-l2-ip-port** \| **del-l2-ip-slot** \| **del-l2-mac** \| **del-l2-mac-port** \| **del-l2-mac-slot** \| **del-l3-ipm** \| **del-l3-oif** \| **del-l3-port** \| **del-l3-slot** \| **set-l3-iif** } \* \| **ipmc-type-all** } ]  **verbose**  } }  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】]

Probe]视图

【缺省用户角色】]

network-admin]

mdc-admin

【参数】

**[statistics**]：显示组播表项操作记录的统计信息。

**[all**]：显示组播表项的所有操作记录。

**[fail**]：显示组播表项的失败操作记录。

*[group-address*]：组播组地址，显示指定组播组的记录。

*[ipv6-group-address*]：IPv6组播组地址，显示指定IPv6组播组的记录。

*[source-address*]：组播源地址，显示包含指定组播源的记录。

*[ipv6-source-address*]：IPv6组播源地址，显示包含指定IPv6组播源的记录。

**[item**]*item-list*：记录列表，表示一条或多条记录。表示方式为*item-list =**start-item* [ **to** *end-item* ]。其中，*start-item*和*end-item*的取值范围均为1～500000。

**[filter**]：显示指定模式下的组播表项操作记录。

**[exclude**]：显示排除满足指定条件的组播表项操作记录。

**[include**]：显示包含满足指定条件的组播表项操作记录。

**[add-l2-ip**]：表示添加二层IP表项的操作记录。

**[add-l2-ip-port**]：表示添加二层IP表项端口的操作记录。

**[add-l2-ip-slot**]：表示添加二层IP表项板信息的操作记录。

**[add-l2-mac**]：表示添加二层MAC表项的操作记录。

**[add-l2-mac-port**]：表示添加二层MAC表项端口的操作记录。

**[add-l2-mac-slot**]：表示添加二层MAC表项板信息的操作记录。

**[add-l3-ipm**]：表示添加三层组播表项的操作记录。

**[add-l3-oif**]：表示添加三层表项出接口的操作记录。

**[add-l3-port**]：表示添加三层表项出端口的操作记录。

**[add-l3-slot**]：表示添加三层表项分布式转发的出接口板信息的操作记录。

**[del-l2-ip**]：表示删除二层IP表项的操作记录。

**[del-l2-ip-port**]：表示删除二层IP表项端口的操作记录。

**[del-l2-ip-slot**]：表示删除二层IP表项板信息的操作记录。

**[del-l2-mac**]：表示删除二层MAC表项的操作记录。

**[del-l2-mac-port**]：表示删除二层MAC表项端口的操作记录。

**[del-l2-mac-slot**]：表示删除二层MAC表项板信息的操作记录。

**[del-l3-ipm**]：表示删除三层组播表项的操作记录。

**[del-l3-oif**]：表示删除三层表项出接口的操作记录。

**[del-l3-port**]：表示删除三层表项出端口的操作记录。

**[del-l3-slot**]：表示删除三层表项分布式转发的出接口板信息的操作记录。

**[set-l3-iif**]：表示设置三层表项入接口的操作记录。

**[ipmc-type-all**]：表示全部类型。

**[verbose**]：显示详细信息。如果记录的出接口和出端口显示不全时，需要指定本参数。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数[，将显示主控板上的信息。（分布式设备－独立运行模式）]

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- display system internal multicast-vlan forwarding-table verbose**

------------------------------------------------------------------------

**[display** **system** **internal** **multicast-vlan** **forwarding-table** **verbose**]命令用来显示组播VLAN转发表的详细信息。

【命令】

集中式设备：

**[display**[ **system** **internal** **multicast-vlan** **forwarding-table** **verbose** [ *group-address* [ **mask** { *mask-length* \| *mask* } ] \| *source-address* [ **mask** { *mask-length* \| *mask* } ] \| **cpu** *cpu-number* \| **subvlan** *vlan-id* \| **vlan** *vlan-id* ] \*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **system** **internal** **multicast-vlan** **forwarding-table** **verbose** [ *group-address* [ **mask** { *mask-length* \| *mask* } ] \| *source-address* [ **mask** { *mask-length* \| *mask* } ] \| **slot** *slot-number*  **cpu** *cpu-number*  \| **subvlan** *vlan-id* \| **vlan** *vlan-id* ] \*]]

分布式设备－IRF模式：

**[display**[ **system** **internal** **multicast-vlan** **forwarding-table** **verbose** [ *group-address* [ **mask** { *mask-length* \| *mask* } ] \| *source-address* [ **mask** { *mask-length* \| *mask* } ] \| **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  \| **subvlan** *vlan-id* \| **vlan** *vlan-id* ] \*]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-address*]：显示指定组播组的信息，取值范围为224.0.0.0～239.255.255.255。如果未指定本参数，将显示所有组播组的信息。

**[mask**[ { *mask-length* \| *mask* }]]：指定组播组的掩码长度或掩码。*mask-length*的取值范围为4～32，缺省值为32；*mask*的缺省值为255.255.255.255。

*[source-address*]：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。

**[mask**[ { *mask-length* \| *mask* }]]：指定组播源的掩码长度或掩码。*mask-length*的取值范围为0～32，缺省值为32；*mask*的缺省值为255.255.255.255。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[subvlan** *vlan-id*]：显示指定子VLAN的信息。如果未指定本参数，将显示所有子VLAN的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**IP组播 \-- IP组播Probe命令 \-- display system internal pim interface**

------------------------------------------------------------------------

**[display**]**system** **internal** **pim** **interface**命令用来显示PIM进程中路由管理LIB所维护的接口信息。

【命令】

**[display**]**system** **internal** **pim**  **vpn-instance** *vpn-instance-name* **interface**[[ *interface-type* *interface-number* \| *ip-address* { *mask-length* \| *mask* } ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[interface-type* *interface-number*]：显示指定接口的信息。如果未指定本参数，将显示所有接口的信息。

*[ip-address*]：显示指定IP地址的信息。如果未指定本参数，将显示所有IP地址的信息。0.0.0.0为保留地址，用户不感知。

*[mask-length*]：表示掩码长度，取值范围为0～32。

*[mask*]：表示掩码。

**IP组播 \-- IP组播Probe命令 \-- display system internal pim rp**

------------------------------------------------------------------------

**[display** **system** **internal** **pim** **rp**]命令用来显示PIM的RP统计信息。

【命令】

**[display** **system** **internal** **pim** [ **vpn-instance** *vpn-instance-name*  **rp**]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网实例的信息。

**IP组播 \-- IP组播Probe命令 \-- display system internal pim thread**

------------------------------------------------------------------------

**[display** **system** **internal** **pim** **thread**]命令用来显示PIM线程的统计信息。

【命令】

**[display** **system** **internal** **pim** **thread** [ **event** \| **main** \| **route** ]}

【视图】]

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：显示PIM事件线程的统计信息。

**[main**]：显示PIM主线程的统计信息。

**[route**]：显示PIM路由线程的统计信息。

**IP组播 \-- IP组播Probe命令 \-- igmp user-authorization record limit**

------------------------------------------------------------------------

![说明](IP组播Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[igmp** **user-authorization** **record** **limit**]命令用来配置按用户记录的认证模块通知给IGMP进程消息数的用户上限。

【命令】

**[igmp** **user-authorization** **record** **limit** *limit-value*]

【缺省情况】

按用户记录的认证模块通知给IGMP进程消息数的用户上限为512个。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit-value*]：表示用户上限，取值范围为0～524288。

**IP组播 \-- IP组播Probe命令 \-- mld user-authorization record limit**

------------------------------------------------------------------------

![说明](IP组播Probe命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mld** **user-authorization** **record** **limit**]命令用来配置按用户记录的认证模块通知给MLD进程消息数的用户上限。

【命令】

**[mld** **user-authorization** **record** **limit** *limit-value*]

【缺省情况】

按用户记录的认证模块通知给MLD进程消息数的用户上限为512个。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit-value*]：表示用户上限，取值范围为0～524288。

**IP组播 \-- IP组播Probe命令 \-- multicast record limit**

------------------------------------------------------------------------

**[multicast** **record** **limit**]命令用来配置组播表项操作记录的最大数目。

**[undo** **multicast** **record** **limit**]命令用来恢复缺省情况。

【命令】

**[multicast** **record** [ **fail**  **limit** *limit-value*]]

**[undo** **multicast** **record** [ **fail**  **limit**]]

【缺省情况】

组播表项操作记录的最大数目为0，即不记录组播表项的操作信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[fail**]：表示组播表项的失败操作记录。

*[limit-value*]：表示操作记录的最大数目，取值范围为0～500000。

**IP组播 \-- IP组播Probe命令 \-- reset system internal igmp user-authorization record**

------------------------------------------------------------------------

![说明](IP组播Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset** **system** **internal** **igmp** **user-authorization** **record**]命令用来清除按用户记录的认证模块通知给IGMP进程的消息数。

【命令】

**[reset** **system** **internal** **igmp** **user-authorization** **record**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP组播 \-- IP组播Probe命令 \-- reset system internal igmp user-authorization statistics**

------------------------------------------------------------------------

![说明](IP组播Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset** **system** **internal** **igmp** **user-authorization** **statistics**]命令用来清除按认证类型记录的认证模块通知给IGMP进程的消息数。

【命令】

**[reset** **system** **internal** **igmp** **user-authorization** **statistics**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP组播 \-- IP组播Probe命令 \-- reset system internal ipv6 multicast forwarding-table dummy**

------------------------------------------------------------------------

**[reset****system** **internal ipv6** **multicast** **forwarding-table** **dummy**]命令用来清除IPv6组播临时转发表中的表项。

【命令】

集中式设备：

**[reset****system** **internal ipv6** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **dummy** { { *ipv6-group-address*  *prefix-length*  \| *ipv6-source-address*  *prefix-length*  } \* \| **all** }  **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[reset****system** **internal ipv6** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **dummy** { { *ipv6-group-address*  *prefix-length*  \| *ipv6-source-address*  *prefix-length*  } \* \| **all** }  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[reset****system** **internal ipv6** **multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **dummy** { { *ipv6-group-address*  *prefix-length*  \| *ipv6-source-address*  *prefix-length*  } \* \| **all** }  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的表项，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的表项。

*[ipv6-group-address*]：清除指定IPv6组播组的表项，取值范围为FFxy::/16，其中x和y均表示0～F的任意一个十六进制数。如果未指定本参数，将清除所有IPv6组播组的表项。

*[ipv6-source-address*]：清除指定IPv6组播源的表项。如果未指定本参数，将清除所有IPv6组播源的表项。

*[prefix-length*]：指定IPv6组播组或IPv6组播源地址的前缀长度。对于IPv6组播组地址，其取值范围为8～128，缺省值为128；对于IPv6组播源地址，其取值范围为0～128，缺省值为128。

**[all**]：清除所有表项。

**[slot** *slot-number*]：清除指定单板上的表项，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将清除主控板上的表项。（分布式设备－独立运行模式）]

**[slot** *slot-number*]：清除指定成员设备上的表项，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将清除主设备上的表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：清除指定成员设备/PEX上的表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将清除主设备上的表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除全局主用主控板上的表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板上的表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将清除全局主用主控板上的表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- reset system internal mld user-authorization record**

------------------------------------------------------------------------

![说明](IP组播Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset** **system** **internal** **mld** **user-authorization** **record**]命令用来清除按用户记录的认证模块通知给MLD进程的消息数。

【命令】

**[reset** **system** **internal** **mld** **user-authorization** **record**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP组播 \-- IP组播Probe命令 \-- reset system internal mld user-authorization statistics**

------------------------------------------------------------------------

![说明](IP组播Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset** **system** **internal** **mld** **user-authorization** **statistics**]命令用来清除按认证类型记录的认证模块通知给MLD进程的消息数。

【命令】

**[reset** **system** **internal** **mld** **user-authorization** **statistics**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**IP组播 \-- IP组播Probe命令 \-- reset system internal multicast forwarding-table dummy**

------------------------------------------------------------------------

**[reset****system** **internal multicast** **forwarding-table** **dummy**]命令用来清除组播临时转发表中的表项。

【命令】

集中式设备：

**[reset****system** **internal multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **dummy** { { *source-address* [ **mask** { *mask-length* \| *mask* } ] \| *group-address* [ **mask** { *mask-length* \| *mask* } ] } \* \| **all** }  **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[reset****system** **internal multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **dummy** { { *source-address* [ **mask** { *mask-length* \| *mask* } ] \| *group-address* [ **mask** { *mask-length* \| *mask* } ] } \* \| **all** }  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[reset****system** **internal multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **dummy** { { *source-address* [ **mask** { *mask-length* \| *mask* } ] \| *group-address* [ **mask** { *mask-length* \| *mask* } ] } \* \| **all** }  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的表项，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的表项。

*[source-address*]：清除指定组播源的表项。如果未指定本参数，将清除所有组播源的表项。

*[group-address*]：清除指定组播组的表项，取值范围为224.0.0.0～239.255.255.255。如果未指定本参数，将清除所有组播组的表项。

*[mask-length*]：指定组播源或组播组地址的掩码长度。对于组播源地址，其取值范围为0～32，缺省值为32；对于组播组地址，其取值范围为4～32，缺省值为32。

*[mask*]：指定组播源或组播组地址的掩码，缺省值为255.255.255.255。

**[all**]：清除所有表项。

**[slot** *slot-number*]：清除指定单板上的表项，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除主控板上的表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：清除指定成员设备上的表项，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将清除主设备上的表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：清除指定成员设备/PEX上的表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将清除主设备上的表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将清除全局主用主控板上的表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板上的表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将清除全局主用主控板上的表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**IP组播 \-- IP组播Probe命令 \-- reset system internal multicast record**

------------------------------------------------------------------------

**[reset** **system** **internal multicast** **record**]命令用来清除组播表项的操作记录。

【命令】

**[reset** **system** **internal multicast** **record**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

